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
                index += node.bop_source.get_titled_anchor(node.count, level)
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
                index += node.bop_source.get_titled_anchor(0, level)
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
        self._filter_nodes_by_layout(BopLayouts.person)
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

    def get_github_contributors_index(self):
        BopIndexNode.clear(self._index_tree)
        distinct_contributors = list()
        for bop_source in self._all_nodes.values():
            for contributor in bop_source.contributors:
                if contributor not in distinct_contributors and not contributor.startswith("@"):
                    distinct_contributors.append(contributor)
        distinct_contributors.sort()
        for contributor in distinct_contributors:
            contributor_node = BopIndexNode()
            contributor_node.label = contributor
            contributor_node.parent = self._index_tree
            relevant_bop_sources = self._filter_nodes_by_lambda(lambda x: contributor in x.contributors)
            relevant_bop_sources.sort(key=lambda x: x.get_plane_title())
            self._add_to_index_tree(contributor_node, relevant_bop_sources)

        self._calculate_counts(self._index_tree)
        if len(distinct_contributors) > 0:
            ret = self._get_index_to_html()
        else:
            ret = "(no Github contributors found)"
        return ret

    def get_non_github_contributors_index(self):
        BopIndexNode.clear(self._index_tree)
        distinct_contributors = dict()
        sortable_contributors = list()
        for bop_source in self._all_nodes.values():
            for contributor in bop_source.contributors:
                if contributor not in distinct_contributors and contributor.startswith("@"):
                    # remove any html tags from contributor
                    sortable_contributor = re.sub(r'<[^<]+?>', '', contributor, flags=re.M)
                    distinct_contributors[sortable_contributor] = contributor
                    sortable_contributors.append(sortable_contributor)

        sortable_contributors.sort()
        for contributor in sortable_contributors:
            contributor_node = BopIndexNode()
            contributor_node.label = distinct_contributors[contributor]
            contributor_node.parent = self._index_tree
            relevant_bop_sources = self._filter_nodes_by_lambda(
                lambda x: distinct_contributors[contributor] in x.contributors)
            relevant_bop_sources.sort(key=lambda x: x.get_plane_title())
            self._add_to_index_tree(contributor_node, relevant_bop_sources)

        self._calculate_counts(self._index_tree)
        if len(distinct_contributors) > 0:
            ret = self._get_index_to_html()
        else:
            ret = "(no non-Github contributors found)"
        return ret

    def get_widgets_index(self):
        BopIndexNode.clear(self._index_tree)
        sage_cell_node = BopIndexNode()
        sage_cell_node.label = "SageCell"
        sage_cell_node.parent = self._index_tree
        sage_cell_sources = self._filter_nodes_by_lambda(lambda x: "<div class='sage'>" in str(x.scripts))
        self._add_to_index_tree(sage_cell_node, sage_cell_sources)
        jsx_graph_node = BopIndexNode()
        jsx_graph_node.label = "JsxGraph"
        jsx_graph_node.parent = self._index_tree
        jsx_graph_sources = self._filter_nodes_by_lambda(lambda x: "JXG.JSXGraph" in str(x.scripts))
        self._add_to_index_tree(jsx_graph_node, jsx_graph_sources)
        self._calculate_counts(self._index_tree)
        return self._get_index_to_html()

    def get_sourcecode_index(self):
        BopIndexNode.clear(self._index_tree)
        sourcecode_node = BopIndexNode()
        sourcecode_node.label = "Sourcecode"
        sourcecode_node.parent = self._index_tree
        sourcecode_sources = self._filter_nodes_by_lambda(lambda x: x.script_has_python(str(x.scripts)))
        self._add_to_index_tree(sourcecode_node, sourcecode_sources)
        self._calculate_counts(self._index_tree)
        return self._get_index_to_html()

    def get_person_index_by_name(self):
        BopIndexNode.clear(self._index_tree)
        persons_remaining_set = self._calculate_remaining_persons_set()
        labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                  "T", "U", "V", "W", "X", "Y", "Z"]
        for label in labels:
            sub_node = BopIndexNode()
            sub_node.label = label
            sub_node.parent = self._index_tree
            sources = self._filter_nodes_by_lambda(
                lambda x: x.title.startswith(label) and x.layout == BopLayouts.person)
            sources.sort(key=lambda x: x.get_plane_title().split("-")[0])
            self._add_to_index_tree(sub_node, sources)
            for bop_source in sources:
                persons_remaining_set.remove(bop_source.nodeid)
        self._add_unknown_node(persons_remaining_set, label="Other")
        self._calculate_counts(self._index_tree)
        return self._get_index_to_html()

    def _calculate_remaining_persons_set(self):
        all_persons = self._validator.get_all_persons()
        persons_remaining_set = set()
        for bop_person in all_persons.values():
            if bop_person.nodeid not in persons_remaining_set:
                persons_remaining_set.add(bop_person.nodeid)
        return persons_remaining_set

    def get_person_index_by_birth_year(self):
        BopIndexNode.clear(self._index_tree)
        persons_remaining_set = self._calculate_remaining_persons_set()
        labels = ["Ancient World", "Late Ancient World", "Early Middle Ages",
                  "1000 - 1099", "1100 - 1199", "1200 - 1299", "1300 - 1399", "1400 - 1499",
                  "1500 - 1599", "1600 - 1699", "1700 - 1799", "1800 - 1899", "1900 - 1999"]
        pattern = re.compile(r"(\d{4})\s*\-\s*(\d{4})")
        for label in labels:
            sub_node = BopIndexNode()
            sub_node.label = label
            sub_node.parent = self._index_tree
            if label == "Ancient World":
                for year in range(-4000, 0):
                    sources = self._filter_nodes_by_lambda(
                        lambda x: x.layout == BopLayouts.person and x.born == year)
                    self._get_subnode_person_index(sources, year, sub_node, persons_remaining_set)
            elif label == "Late Ancient World":
                for year in range(1, 500):
                    sources = self._filter_nodes_by_lambda(
                        lambda x: x.layout == BopLayouts.person and x.born == year)
                    self._get_subnode_person_index(sources, year, sub_node, persons_remaining_set)
            elif label == "Early Middle Ages":
                for year in range(500, 999):
                    sources = self._filter_nodes_by_lambda(
                        lambda x: x.layout == BopLayouts.person and x.born == year)
                    self._get_subnode_person_index(sources, year, sub_node, persons_remaining_set)
            elif re.match(pattern, label):
                year_lower_bound = 0
                year_upper_bound = 0
                for match in pattern.finditer(label):
                    year_lower_bound = int(match.group(1))
                    year_upper_bound = int(match.group(2))
                    break
                for year in range(year_lower_bound, year_upper_bound + 1):
                    sources = self._filter_nodes_by_lambda(
                        lambda x: x.layout == BopLayouts.person and x.born == year)
                    self._get_subnode_person_index(sources, year, sub_node, persons_remaining_set)
        self._add_unknown_node(persons_remaining_set)
        self._calculate_counts(self._index_tree)
        return self._get_index_to_html()

    def _add_unknown_node(self, persons_remaining_set: set, label="Unknown"):
        if len(persons_remaining_set) > 0:
            sources = list()
            for nodeid in persons_remaining_set:
                sources.append(self._validator.get_nodes()[nodeid])
            sub_sub_node = BopIndexNode()
            sub_sub_node.label = label
            sub_sub_node.parent = self._index_tree
            sources.sort(key=lambda x: x.get_plane_title().split("-")[0])
            self._add_to_index_tree(sub_sub_node, sources)

    def _get_subnode_person_index(self, sources: list, year: int, sub_node: BopIndexNode,
                                  persons_remaining_set: set):
        if len(sources) > 0:
            sub_sub_node = BopIndexNode()
            sub_sub_node.label = str(abs(year))
            sub_sub_node.parent = sub_node
            if year < 0:
                sub_sub_node.label += " BC"
            sources.sort(key=lambda x: x.get_plane_title().split("-")[0])
            self._add_to_index_tree(sub_sub_node, sources)
            for bop_source in sources:
                persons_remaining_set.remove(bop_source.nodeid)

    def get_person_index_by_tag(self):
        BopIndexNode.clear(self._index_tree)
        distinct_tags = list()
        all_persons = self._validator.get_all_persons()
        for person in all_persons.values():
            for tag in person.tags:
                if tag not in distinct_tags:
                    distinct_tags.append(tag)
        distinct_tags.sort()
        first_in_between_node = {"origin": None, "prize": None, "ancient": None}
        for tag in distinct_tags:
            in_between_tag_found = False
            for ibt in first_in_between_node:
                if tag.startswith(ibt + "-"):
                    in_between_tag_found = True
                    if first_in_between_node[ibt] is None:
                        sub_node = BopIndexNode()
                        sub_node.parent = self._index_tree
                        sub_node.label = ibt.title()
                        first_in_between_node[ibt] = sub_node
                    sub_node = BopIndexNode()
                    sub_node.parent = first_in_between_node[ibt]
                    sub_node.label = tag[len(ibt) + 1:].replace("-", " ").title()
            if not in_between_tag_found:
                sub_node = BopIndexNode()
                sub_node.parent = self._index_tree
                sub_node.label = tag.replace("-", " ").title()
            sources = self._filter_nodes_by_lambda(lambda x: x.layout == BopLayouts.person and tag in x.tags)
            sources.sort(key=lambda x: x.get_plane_title().split("-")[0])
            self._add_to_index_tree(sub_node, sources)
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
        # calculate keyword-referencing and keyword-containing nodes
        keyword_referencing_nodes = dict()
        keyword_containing_nodes = dict()

        for keyword in keyword_defining_nodes:
            if keyword not in keyword_referencing_nodes:
                keyword_referencing_nodes[keyword] = list()
            if keyword not in keyword_containing_nodes:
                keyword_containing_nodes[keyword] = list()
            for bop_source in self._all_nodes.values():
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
                if link_counter <= 100:
                    index += "<a href='{0}' title='{1}'>[{2}]</a> ".format(bop_source.url(),
                                                                           bop_source.get_title_for_anchor(),
                                                                           link_counter)
            for bop_source in keyword_referencing_nodes[keyword]:
                link_counter += 1
                if link_counter <= 100:
                    index += "<a href='{0}' title='{1}'>({2})</a> ".format(bop_source.url(),
                                                                           bop_source.get_title_for_anchor(),
                                                                           link_counter)
            for bop_source in keyword_containing_nodes[keyword]:
                link_counter += 1
                if link_counter <= 100:
                    index += "<a href='{0}' title='{1}'>{2}</a> ".format(bop_source.url(),
                                                                         bop_source.get_title_for_anchor(),
                                                                         link_counter)
            if link_counter > 100:
                index += "... (" + str(link_counter - 100) + " more)"
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
        relevant_bop_sources.sort(key=lambda x: x.get_plane_title())
        self._add_to_index_tree(issue_node, relevant_bop_sources)

    def _filter_nodes_by_layout(self, layout: str):
        layout_node = BopIndexNode()
        layout_node.label = BopSource.get_plural_layout_title(layout)
        layout_node.parent = self._index_tree
        relevant_bop_sources = self._filter_nodes_by_lambda(lambda x: x.layout == layout)
        self._add_to_index_tree_by_category(layout_node, relevant_bop_sources)

    def _add_to_index_tree(self, root_node: BopIndexNode, relevant_bop_sources: list):
        for bop_source in relevant_bop_sources:
            node = BopIndexNode()
            node.bop_source = bop_source
            node.parent = root_node

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
