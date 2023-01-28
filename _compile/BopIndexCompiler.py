import re

from BopSource import BopSource, BopLayouts
from BopIndexNode import BopIndexNode


class BopIndexCompiler:
    def __init__(self, validator):
        self._validator = validator
        self._index_tree = BopIndexNode()
        self._all_nodes = self._validator.get_nodes()
        self._pc = self._validator.get_parent_child_graph()

    def _get_index_to_html(self):
        index = "<ul id='myUL'>\n"
        level = 0
        for node in self._index_tree.children:
            index += self._get_index_to_html_rec(level, node)
        index += "</ul>\n"
        # as a by-product, we know the pre-order of the tree
        return index

    def _get_index_to_html_rec(self, level: int, node: BopIndexNode):
        index = ""
        level += 1
        if len(node.children) > 0:
            index += " " * level + "<li>"
            if node.bop_source is not None:
                outline = BopSource.get_layout_title(node.bop_source.layout)
                if outline == ".":
                    outline = ""
                else:
                    outline += ": "
                index += "<span class='caret'>{0}</span><a href='{1}'>{2}</a> ({3}) \n".format(
                    outline,
                    node.bop_source.url(),
                    node.bop_source.get_long_title(),
                    node.count
                )
            else:
                index += "<span class='caret'></span> {0} ({1}) \n".format(node.label, node.count)
            level += 1
            index += " " * level + "<ul class='nested'>\n"
            for child in node.children:
                index += self._get_index_to_html_rec(level, child)
            index += " " * level + "</ul>\n"
            level -= 1
            index += " " * level + "</li>\n"
        else:
            if node.bop_source is not None:
                outline = BopSource.get_layout_title(node.bop_source.layout)
                if outline == ".":
                    outline = ""
                else:
                    outline += ": "
                index += " " * level + "<li><span>{0}</span><a href='{1}'>{2}</a></li>\n".format(
                    outline,
                    node.bop_source.url(),
                    node.bop_source.get_long_title()
                )
            else:
                index += " " * level + "<li>{0}</li>\n".format(node.label)
        level -= 1
        return index

    def _calculate_counts(self, node: BopIndexNode):
        if len(node.children) == 0:
            node.count = 0
            return 1
        else:
            ret = 0
            for child in node.children:
                ret += self._calculate_counts(child)
            node.count = ret
            return ret

    def get_tree_index(self):
        # use the main parent child graph of the validator as the input parent-child graph for the index html
        BopIndexNode.clear(self._index_tree)
        for nodeid in BopSource.root_nodes:
            node = BopIndexNode()
            node.bop_source = self._all_nodes[nodeid]
            node.parent = self._index_tree
            self._copy_tree_rek(node)
            # mark predecessors / successors for navigation
            pre_order = BopIndexNode.get_bop_sources_in_pre_order(node)
            for i in range(1, len(pre_order) - 1):
                pre_order[i].predecessor = pre_order[i - 1]
                pre_order[i].successor = pre_order[i + 1]
            if len(pre_order) > 2:
                pre_order[0].successor = pre_order[1]
                pre_order[-1].predecessor = pre_order[-2]

        self._calculate_counts(self._index_tree)
        return self._get_index_to_html()

    def _copy_tree_rek(self, node: BopIndexNode):
        if node.bop_source is not None:
            if node.bop_source.nodeid in self._pc:
                for childid in self._pc[node.bop_source.nodeid]:
                    child_node = BopIndexNode()
                    child_node.bop_source = self._all_nodes[childid]
                    child_node.parent = node
                    self._copy_tree_rek(child_node)

    def get_building_block_index(self):
        # create an own parent child graph for building blocks of mathematics
        BopIndexNode.clear(self._index_tree)
        self._filter_nodes_by_layout(BopLayouts.axiom)
        self._filter_nodes_by_layout(BopLayouts.definition)
        self._filter_nodes_by_layout(BopLayouts.theorem)
        self._filter_nodes_by_layout(BopLayouts.lemma)
        self._filter_nodes_by_layout(BopLayouts.proposition)
        self._filter_nodes_by_layout(BopLayouts.corollary)
        self._filter_nodes_by_layout(BopLayouts.proof)
        self._calculate_counts(self._index_tree)
        return self._get_index_to_html()

    def get_other_building_block_index(self):
        # create an own parent child graph for other building blocks
        BopIndexNode.clear(self._index_tree)
        self._filter_nodes_by_layout(BopLayouts.algorithm)
        self._filter_nodes_by_layout(BopLayouts.motivation)
        self._filter_nodes_by_layout(BopLayouts.application)
        self._filter_nodes_by_layout(BopLayouts.explanation)
        self._filter_nodes_by_layout(BopLayouts.example)
        self._filter_nodes_by_layout(BopLayouts.problem)
        self._filter_nodes_by_layout(BopLayouts.solution)
        self._calculate_counts(self._index_tree)
        return self._get_index_to_html()

    def get_history_building_block_index(self):
        # create an own parent child graph for history building blocks
        BopIndexNode.clear(self._index_tree)
        self._filter_nodes_by_layout(BopLayouts.epoch)
        self._filter_nodes_by_layout(BopLayouts.topic)
        self._calculate_counts(self._index_tree)
        return self._get_index_to_html()

    def get_issue_index(self):
        BopIndexNode.clear(self._index_tree)
        collected_issue_types = set()
        for bop_source in self._all_nodes.values():
            for issue in bop_source.issues:
                if issue not in collected_issue_types:
                    collected_issue_types.add(issue)
        list_issue_types = list(collected_issue_types)
        list_issue_types.sort()
        for issue in list_issue_types:
            self._filter_nodes_by_issue(issue)
        self._calculate_counts(self._index_tree)
        return self._get_index_to_html()

    def get_contributors_index(self):
        BopIndexNode.clear(self._index_tree)
        distinct_contributors = list()
        for bop_source in self._all_nodes.values():
            for contributor in bop_source.contributors:
                if contributor not in distinct_contributors:
                    distinct_contributors.append(contributor)
        distinct_contributors.sort()
        for contributor in distinct_contributors:
            contributor_node = BopIndexNode()
            contributor_node.label = contributor
            contributor_node.parent = self._index_tree
            relevant_bop_sources = self._filter_nodes_by_lambda(lambda x: contributor in x.contributors)
            self._add_to_index_tree_by_category(contributor_node, relevant_bop_sources)

        self._calculate_counts(self._index_tree)
        return self._get_index_to_html()

    def get_keywords_index(self):
        # gather all keyword-defining nodes
        keyword_defining_nodes = dict()
        keyword_defining_nodesids = set()
        pattern = re.compile(r"\*\*(.+?)\*\*")
        for bop_source in self._all_nodes.values():
            content = bop_source.get_pre_body() + "\n" + bop_source.get_body()
            distinct_keywords = set()
            for match in pattern.finditer(content):
                keyword = match.group(1)
                if keyword not in distinct_keywords:
                    distinct_keywords.add(keyword)
            for keyword in distinct_keywords:
                if keyword not in keyword_defining_nodes:
                    keyword_defining_nodes[keyword] = list()
                keyword_defining_nodes[keyword].append(bop_source)
                keyword_defining_nodesids.add(bop_source.nodeid)
        # create keyword-referencing and keyword-containing nodes
        keyword_referencing_nodes = dict()
        keyword_containing_nodes = dict()

        for keyword in keyword_defining_nodes:
            if keyword not in keyword_referencing_nodes:
                keyword_referencing_nodes[keyword] = list()
            if keyword not in keyword_containing_nodes:
                keyword_containing_nodes[keyword] = list()
            for bop_source in keyword_defining_nodes[keyword]:
                content = bop_source.get_pre_body() + "\n" + bop_source.get_body()
                if "][" + bop_source.nodeid + "]" in content:
                    keyword_referencing_nodes[keyword].append(bop_source)
                if keyword in content and bop_source.nodeid not in keyword_defining_nodesids:
                    keyword_containing_nodes[keyword].append(bop_source)
        sorted_keywords = list(keyword_defining_nodes.keys())
        sorted_keywords.sort()
        # create the actual html index
        index = "<dl>"
        for keyword in sorted_keywords:
            link_counter = 0
            keyword_term = keyword
            if keyword_term == "":
                keyword_term = "&lt;missing&gt;"
            index += "<dt>" + keyword_term + "</dt><dd>"
            for bop_source in keyword_defining_nodes[keyword]:
                link_counter += 1
                index += "<a href='{0}'>[{1}]</a> ".format(bop_source.url(), link_counter)
            for bop_source in keyword_referencing_nodes[keyword]:
                link_counter += 1
                index += "<a href='{0}'>({1})</a> ".format(bop_source.url(), link_counter)
            for bop_source in keyword_containing_nodes[keyword]:
                link_counter += 1
                index += "<a href='{0}'>{1}</a> ".format(bop_source.url(), link_counter)
            index += "</dd>\n"
        index += "</dl>\n"
        return index

    def get_seo_keywords_index(self):
        # gather all keyword-defining nodes
        keyword_defining_nodes = dict()
        for bop_source in self._all_nodes.values():
            distinct_keywords = set()
            for keyword in bop_source.keywords.split(","):
                if keyword not in distinct_keywords:
                    distinct_keywords.add(keyword)
            for keyword in distinct_keywords:
                if keyword not in keyword_defining_nodes:
                    keyword_defining_nodes[keyword] = list()
                keyword_defining_nodes[keyword].append(bop_source)
        # create keyword-containing nodes
        keyword_containing_nodes = dict()
        for keyword in keyword_defining_nodes:
            if keyword not in keyword_containing_nodes:
                keyword_containing_nodes[keyword] = list()
            for bop_source in keyword_defining_nodes[keyword]:
                content = bop_source.get_pre_body() + "\n" + bop_source.get_body()
                if keyword in content:
                    keyword_containing_nodes[keyword].append(bop_source)
        sorted_keywords = list(keyword_defining_nodes.keys())
        sorted_keywords.sort()

        # create the actual html index
        index = "<dl>"
        for keyword in sorted_keywords:
            link_counter = 0
            keyword_term = keyword
            if keyword_term == "":
                keyword_term = "&lt;missing&gt;"
            index += "<dt>" + keyword_term + "</dt><dd>"
            for bop_source in keyword_defining_nodes[keyword]:
                link_counter += 1
                index += "<a href='{0}'>[{1}]</a> ".format(bop_source.url(), link_counter)
            for bop_source in keyword_containing_nodes[keyword]:
                link_counter += 1
                index += "<a href='{0}'>{1}</a> ".format(bop_source.url(), link_counter)
            index += "</dd>\n"
        index += "</dl>\n"
        return index

    def _collect_nodes_with_issue(self, issue_type: str):
        ret = list()
        for bop_source in self._all_nodes.values():
            found = False
            for issue in bop_source.issues:
                if issue == issue_type:
                    found = True
                    break
            if found:
                ret.append(bop_source)
        ret.sort(key=lambda x: x.get_sort_title())
        return ret

    def get_search_autocomplete_index(self):
        value_label_pairs = list()
        for bop_source in self._all_nodes.values():
            link = "{value:\"" + bop_source.get_file_destination() + "/" + bop_source.name + ".html\""
            title = ",label:\"" + bop_source.get_plane_long_title().replace("\"", "") + "\"}"
            value_label_pairs.append(link + title)
        return ",".join(value_label_pairs)

    def _filter_nodes_by_lambda(self, filter_expr):
        filtered_nodes = list(filter(filter_expr, self._all_nodes.values()))
        # sort alphabetically
        filtered_nodes.sort(key=lambda x: ", ".join(x.categories) + ", " + x.get_sort_title())
        return filtered_nodes

    def _filter_nodes_by_issue(self, issue: str):
        issue_node = BopIndexNode()
        issue_node.label = issue.replace("-", " ").title()
        issue_node.parent = self._index_tree
        relevant_bop_sources = self._filter_nodes_by_lambda(lambda x: issue in x.issues)
        self._add_to_index_tree_by_category(issue_node, relevant_bop_sources)

    def _filter_nodes_by_layout(self, layout: str):
        layout_node = BopIndexNode()
        layout_node.label = BopSource.get_plural_layout_title(layout)
        layout_node.parent = self._index_tree
        relevant_bop_sources = self._filter_nodes_by_lambda(lambda x: x.layout == layout)
        self._add_to_index_tree_by_category(layout_node, relevant_bop_sources)

    def _add_to_index_tree_by_category(self, root_node: BopIndexNode, relevant_bop_sources: list):
        processed_categories = dict()
        last_parent = root_node
        for bop_source in relevant_bop_sources:
            for i in range(1, len(bop_source.categories)):
                cat_id = ",".join(bop_source.categories[1:i + 1])
                found_parent = None
                for ci in processed_categories:
                    if cat_id.startswith(ci):
                        found_parent = processed_categories[ci]
                if found_parent is None:
                    if cat_id not in processed_categories:
                        processed_categories[cat_id] = root_node
                    last_parent = root_node
                    cat_node = BopIndexNode()
                    cat_node.label = bop_source.categories[i].replace("-", " ").title()
                    cat_node.parent = last_parent
                    last_parent = cat_node
                    processed_categories[cat_id] = cat_node
                else:
                    if cat_id not in processed_categories:
                        cat_node = BopIndexNode()
                        cat_node.label = bop_source.categories[i].replace("-", " ").title()
                        cat_node.parent = found_parent
                        last_parent = cat_node
                        processed_categories[cat_id] = cat_node

            node = BopIndexNode()
            node.bop_source = bop_source
            node.parent = last_parent
