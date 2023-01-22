from BopSource import BopSource, BopLayouts
from BopValidator import BopValidator


class BopIndexCompiler:
    def __init__(self, validator):
        self._validator = validator

    def get_tree_index(self):
        index = "<ul id='myUL'>\n"
        level = 0
        pre_order = list()
        for root_node in BopSource.root_nodes:
            index += self._get_tree_index_rec(level, root_node, pre_order)
        index += "</ul>\n"
        # as a by-product, we know the pre-order of the tree
        # now we can calculate the predecessors and successors of the tree
        for i in range(1, len(pre_order) - 1):
            node = pre_order[i]
            node.set_predecessor(pre_order[i - 1])
            node.set_successor(pre_order[i + 1])
        pre_order[0].set_successor(pre_order[1])
        return index

    def _get_tree_index_rec(self, level: int, nodeid: str, pre_order: list):
        index = ""
        unique_nodes = self._validator.get_nodes()
        node = unique_nodes[nodeid]
        pre_order.append(node)
        if node.layout in [BopLayouts.default, BopLayouts.index]:
            pass  # exclude specific nodes from the index
        else:
            level += 1
            parent_child_graph = self._validator.get_parent_child_graph()
            if nodeid in parent_child_graph:
                if nodeid in BopSource.root_nodes:
                    index += " " * level + "<li><span class='caret'></span><a href='{0}'>{1}</a>\n".format(
                        node.url(),
                        node.get_long_title())
                else:
                    index += " " * level + "<li><span class='caret'>{0}:</span> <a href='{1}'>{2}</a>\n".format(
                        BopSource.get_layout_title(node.layout), node.url(),
                        node.get_long_title())
                # if a node has a subtree, continue with a nested ul element
                level += 1
                index += " " * level + "<ul class='nested'>\n"
                # order the children by order id
                parent_child_graph[nodeid].sort(key=self._validator.get_order_id)
                for childid in parent_child_graph[nodeid]:
                    index += self._get_tree_index_rec(level, childid, pre_order)
                index += " " * level + "</ul>\n"
                level -= 1
            else:
                index += " " * level + "<li><span>{0}:</span> <a href='{1}'>{2}</a>\n".format(
                    BopSource.get_layout_title(node.layout), node.url(), node.get_long_title())

            index += " " * level + "</li>\n"
        return index

    def get_building_block_index(self):
        index = "<ul id='myUL'>\n"
        index += self._get_bb_index_specific(BopLayouts.axiom)
        index += self._get_bb_index_specific(BopLayouts.definition)
        index += self._get_bb_index_specific(BopLayouts.theorem)
        index += self._get_bb_index_specific(BopLayouts.lemma)
        index += self._get_bb_index_specific(BopLayouts.proposition)
        index += self._get_bb_index_specific(BopLayouts.corollary)
        index += self._get_bb_index_specific(BopLayouts.proof)
        index += "</ul>\n"
        return index

    def get_issue_index(self):
        index = "<ul id='myUL'>\n"
        for issue_type in BopValidator.issue_types:
            nodes = self._collect_nodes_with_issue(issue_type)
            if len(nodes) > 0:
                title = issue_type.replace("-", " ").title()
                index += " <li><span class='caret'>{0}:</span>\n".format(title)
                index += "  <ul class='nested'>\n"
                for node in nodes:
                    index += "   <li><span>{0}:</span> <a href='{1}'>{2}</a></li>\n".format(
                        BopSource.get_layout_title(node.layout),
                        node.url(),
                        node.get_long_title())
                index += "  </ul>\n"
                index += " </li>\n"
        index += "</ul>\n"
        return index

    def _collect_nodes_with_issue(self, issue_type: str):
        ret = list()
        for bop_source in self._validator.get_nodes().values():
            found = False
            for issue in bop_source.issues:
                if issue == issue_type:
                    found = True
                    break
            if found:
                ret.append(bop_source)
        ret.sort(key=lambda x: x.get_sort_title())
        return ret

    def get_other_building_block_index(self):
        index = "<ul id='myUL'>\n"
        index += self._get_bb_index_specific(BopLayouts.algorithm)
        index += self._get_bb_index_specific(BopLayouts.motivation)
        index += self._get_bb_index_specific(BopLayouts.application)
        index += self._get_bb_index_specific(BopLayouts.explanation)
        index += self._get_bb_index_specific(BopLayouts.example)
        index += self._get_bb_index_specific(BopLayouts.problem)
        index += self._get_bb_index_specific(BopLayouts.solution)
        index += "</ul>\n"
        return index

    def get_history_building_block_index(self):
        index = "<ul id='myUL'>\n"
        index += self._get_bb_index_specific(BopLayouts.epoch)
        index += self._get_bb_index_specific(BopLayouts.topic)
        index += "</ul>\n"
        return index

    def get_search_autocomplete_index(self):
        value_label_pairs = list()
        unique_nodes = self._validator.get_nodes()
        for bop_source in unique_nodes.values():
            link = "{value:\"" + bop_source.get_file_destination() + "/" + bop_source.name + ".html\""
            title = ",label:\"" + bop_source.get_plane_long_title().replace("\"", "") + "\"}"
            value_label_pairs.append(link + title)
        return ",".join(value_label_pairs)

    def _get_bb_index_specific(self, layout: str):
        index = ""
        relevant_nodes = list()
        relevant_node_ids = list()
        unique_nodes = self._validator.get_nodes()
        for nodeid in unique_nodes:
            bop_source = unique_nodes[nodeid]
            if bop_source.layout == layout:
                relevant_nodes.append(bop_source)
                relevant_node_ids.append(bop_source.nodeid)
        if len(relevant_nodes) == 0:
            index += " <li><span>{0}:</span> (None)\n".format(BopSource.get_plural_layout_title(layout))
            index += " </li>\n"
        else:
            index += " <li><span class='caret'>{0}:</span>\n".format(BopSource.get_plural_layout_title(layout))
            index += "  <ul class='nested'>\n"
            relevant_nodes.sort(key=lambda x: ", ".join(x.categories) + x.get_sort_title())
            # gather all different paths to categories
            groups_of_categories = dict()
            for bop_source in relevant_nodes:
                cat_key = str(bop_source.categories)
                if cat_key not in groups_of_categories:
                    groups_of_categories[cat_key] = bop_source.categories.copy()
            # remove standard paths to make the building block index more readable
            for cat_key in groups_of_categories:
                if cat_key.startswith("['branches'"):
                    groups_of_categories[cat_key].pop(0)
                if cat_key.startswith("['history'"):
                    groups_of_categories[cat_key].pop(0)
            to_be_processed_cats = list()
            for cat_key in groups_of_categories:
                for cat in groups_of_categories[cat_key]:
                    if cat not in to_be_processed_cats:
                        to_be_processed_cats.append(cat)

            # make the index nesting the categories
            if len(to_be_processed_cats) > 0:
                while len(to_be_processed_cats) > 0:
                    level = 3
                    cat = to_be_processed_cats[0]
                    index += self.__get_recursive_categories(level, cat, relevant_node_ids, to_be_processed_cats,
                                                             layout)
            else:
                level = 3
                cat = ""
                index += self.__get_recursive_categories(level, cat, relevant_node_ids, to_be_processed_cats, layout)

            index += "  </ul>\n"
            index += " </li>\n"
        return index

    def __get_recursive_categories(self, level: int, cat: str, relevant_node_ids: list, relevant_cats: list,
                                   layout: str):
        index = ""
        if cat != "":
            cat_title = cat.replace("-", " ").title()
            category_graph = self._validator.get_category_graph()
            if len(category_graph[cat]) > 0:
                level += 1
                index += " " * level + "<li><span class='caret'>{0}</span>\n".format(cat_title)
                level += 1
                index += " " * level + "<ul class='nested'>\n"
                for childcat in category_graph[cat]:
                    if childcat in relevant_cats:
                        level += 1
                        index += self.__get_recursive_categories(level, childcat, relevant_node_ids, relevant_cats,
                                                                 layout)
                        level -= 1
                index += " " * level + "</ul>\n"
                level -= 1
                index += " " * level + "</li>\n"
            else:
                level += 1
                index += " " * level + "<li><span class='caret'>{0}</span>\n".format(cat_title)
                level += 1
                index += " " * level + "<ul class='nested'>\n"
                all_categories = self._validator.get_all_categories()
                for node in all_categories[cat]:
                    if node.nodeid in relevant_node_ids:
                        index += " " * level + \
                                 "<li><span>{0}:</span> <a href='{1}'>{2}</a></li>\n".format(
                                     BopSource.get_layout_title(node.layout),
                                     node.url(),
                                     node.get_long_title())
                level -= 1
                index += " " * level + "</ul>\n"
                level -= 1
                index += " " * level + "</li>\n"
            if len(relevant_cats) > 0:
                relevant_cats.pop(0)
        else:
            all_nodes = self._validator.get_nodes()
            for nodeid in relevant_node_ids:
                node = all_nodes[nodeid]
                if node.layout == layout:
                    index += " " * level + \
                             "<li><span>{0}:</span> <a href='{1}'>{2}</a></li>\n".format(
                                 BopSource.get_layout_title(node.layout),
                                 node.url(),
                                 node.get_long_title())
        return index
