import re
from BopSource import BopLayouts, BopSource
from FileMgr import FileMgr


class BopValidator:
    issue_types = ['broken-links', 'missing-proof', "malformed-tables"]

    allowed_layout_combis = {
        BopLayouts.root: [BopLayouts.branch, BopLayouts.index, BopLayouts.epoch],
        BopLayouts.index: [BopLayouts.index],
        BopLayouts.branch: [BopLayouts.part, BopLayouts.axiom, BopLayouts.definition, BopLayouts.theorem,
                            BopLayouts.proposition, BopLayouts.lemma, BopLayouts.example, BopLayouts.explanation,
                            BopLayouts.motivation, BopLayouts.application, BopLayouts.problem, BopLayouts.algorithm],
        BopLayouts.part: [BopLayouts.chapter, BopLayouts.axiom, BopLayouts.definition, BopLayouts.theorem,
                          BopLayouts.proposition, BopLayouts.lemma, BopLayouts.example, BopLayouts.explanation,
                          BopLayouts.motivation, BopLayouts.application, BopLayouts.problem, BopLayouts.algorithm],
        BopLayouts.chapter: [BopLayouts.section, BopLayouts.axiom, BopLayouts.definition, BopLayouts.theorem,
                             BopLayouts.proposition,
                             BopLayouts.lemma, BopLayouts.example, BopLayouts.explanation,
                             BopLayouts.motivation, BopLayouts.application, BopLayouts.problem, BopLayouts.algorithm],
        BopLayouts.section: [BopLayouts.subsection, BopLayouts.axiom, BopLayouts.definition, BopLayouts.theorem,
                             BopLayouts.proposition,
                             BopLayouts.lemma, BopLayouts.example, BopLayouts.explanation,
                             BopLayouts.motivation, BopLayouts.application, BopLayouts.problem, BopLayouts.algorithm],
        BopLayouts.subsection: [BopLayouts.axiom, BopLayouts.definition, BopLayouts.theorem, BopLayouts.proposition,
                                BopLayouts.lemma, BopLayouts.example, BopLayouts.explanation,
                                BopLayouts.motivation, BopLayouts.application, BopLayouts.problem,
                                BopLayouts.algorithm],
        BopLayouts.theorem: [BopLayouts.proof, BopLayouts.corollary, BopLayouts.example, BopLayouts.explanation,
                             BopLayouts.motivation, BopLayouts.application,
                             BopLayouts.problem],
        BopLayouts.lemma: [BopLayouts.proof, BopLayouts.corollary, BopLayouts.example, BopLayouts.explanation,
                           BopLayouts.motivation, BopLayouts.application,
                           BopLayouts.problem],
        BopLayouts.proposition: [BopLayouts.proof, BopLayouts.corollary, BopLayouts.example, BopLayouts.explanation,
                                 BopLayouts.motivation, BopLayouts.application,
                                 BopLayouts.problem],
        BopLayouts.corollary: [BopLayouts.proof, BopLayouts.corollary, BopLayouts.example, BopLayouts.explanation,
                               BopLayouts.motivation, BopLayouts.application, BopLayouts.problem],
        BopLayouts.definition: [BopLayouts.example, BopLayouts.explanation, BopLayouts.motivation,
                                BopLayouts.application, BopLayouts.problem],
        BopLayouts.axiom: [BopLayouts.explanation],
        BopLayouts.algorithm: [BopLayouts.proof, BopLayouts.example, BopLayouts.explanation, BopLayouts.motivation,
                               BopLayouts.application, BopLayouts.problem],
        BopLayouts.problem: [BopLayouts.solution],
        BopLayouts.example: [],
        BopLayouts.motivation: [],
        BopLayouts.explanation: [],
        BopLayouts.solution: [],
        BopLayouts.epoch: [BopLayouts.epoch],
    }

    def __init__(self, sources: dict):
        self.sources = sources
        self._unique_nodeids = dict()
        self._parent_child_graph = dict()
        self._unique_file_names = dict()
        self._category_graph = dict()
        self._all_categories = dict()
        self._validate_nodeids()
        self._validate_names()
        self._validate_orderids()
        self._validate_parentids()
        self._validate_tree()
        self._validate_hyperlinks()
        self._validate_scripts()
        self._validate_categories()
        self._validate_issues()
        self._validate_layouts()

    def _validate_nodeids(self):
        """
        Check for duplicate or missing nodeids, also check if nodeid is provided if and only if layout!=default
        :return: None, or raises an Error
        """
        print("   Validating nodeid")
        for source_id in self.sources:
            bop_source = self.sources[source_id]
            if bop_source.layout == "":
                raise AssertionError("Missing layout detected in " + bop_source.get_file_name())
            if bop_source.layout == BopLayouts.default and bop_source.nodeid != "":
                raise AssertionError("Nodeid not allowed for nodes with layout:default " + bop_source.get_file_name())
            elif bop_source.layout != BopLayouts.default and bop_source.nodeid == "":
                raise AssertionError("Missing nodeid when layout: (other than default) " + bop_source.get_file_name())
            if bop_source.nodeid != "" and bop_source.nodeid not in self._unique_nodeids:
                self._unique_nodeids[bop_source.nodeid] = bop_source
            elif bop_source.nodeid == "" and bop_source.nodeid not in self._unique_nodeids:
                pass
            else:
                raise AssertionError(
                    "Duplicate nodeid {0} detected in ".format(bop_source.nodeid) + bop_source.get_file_name())

    def _validate_names(self):
        """
        Check if each file name is unique, regardless where it resides in the folder structure of _sources.
        :return: None, or raises an error
        """
        print("   Validating names")
        for nodeid in self._unique_nodeids:
            bop_source = self._unique_nodeids[nodeid]
            base_name = FileMgr.get_base_name(bop_source.get_file_name())
            base_name_without_ext = base_name.split(".")[0]
            if base_name_without_ext not in self._unique_file_names:
                self._unique_file_names[base_name_without_ext] = bop_source
            else:
                duplicate = self._unique_file_names[base_name_without_ext]
                raise AssertionError(
                    "Duplicate filename detected in {0} and {1}".format(duplicate.get_file_name(),
                                                                        bop_source.get_file_name()))

    def _validate_orderids(self):
        """
        Check for positive integer order ids
        :return: None, or raises an Error
        """
        print("   Validating orderid")
        for source_id in self._unique_nodeids:
            bop_source = self._unique_nodeids[source_id]
            if bop_source.orderid.isdigit():
                bop_source.orderid = int(bop_source.orderid)
            else:
                raise AssertionError(
                    "Only positive integer orderid allowed for {0} detected in {1}".format(bop_source.nodeid,
                                                                                           bop_source.get_file_name()))

    def _validate_parentids(self):
        """
        Check for missing parentids
        :return: None, or raises an Error
        """
        print("   Validating parentid")
        for source_id in self._unique_nodeids:
            bop_source = self._unique_nodeids[source_id]
            if bop_source.parentid == "" and bop_source.nodeid in BopSource.root_nodes:
                pass  # only the single node bookofproofs$0 may have no parentid (since it is the root)
            elif bop_source.parentid == "" and bop_source.nodeid not in BopSource.root_nodes:
                raise AssertionError(
                    "Missing parentid only allowed for the root nodes {0}; ".format(str(BopSource.root_nodes)) +
                    "detected in " + bop_source.get_file_name())
            elif bop_source.parentid not in self._unique_nodeids:
                raise AssertionError(
                    "Unknown parentid {0} detected in ".format(bop_source.parentid) + bop_source.get_file_name())
            if bop_source.parentid != "":
                if bop_source.parentid not in self._parent_child_graph:
                    self._parent_child_graph[bop_source.parentid] = list()
                self._parent_child_graph[bop_source.parentid].append(bop_source.nodeid)
                bop_source.set_parent(self._unique_nodeids[bop_source.parentid])

    def _validate_tree(self):
        """
        Check if the parent-child relationship between parentid and nodeid produces any cycles
        and if the graph is disconnected
        :return:
        """
        print("   Validating tree graph")
        visited = list()
        for root_node in BopSource.root_nodes:
            if root_node not in self._parent_child_graph.keys():
                raise AssertionError("No root '{0}' in any of _sources/*".format(root_node))
            self._visit_rec(root_node, visited)
        li1 = list(self._parent_child_graph.keys())
        li2 = visited
        unvisited = list()
        for i in li1:
            if i not in li2:
                unvisited.append(i)
        if len(unvisited) > 0:
            raise AssertionError("{0} disconnected nodes detected {1}".format(len(unvisited), str(unvisited)))

    def _visit_rec(self, node, visited):
        if node in visited:
            raise AssertionError(
                "Cycle detected in {0} after visiting {1}".format(self._unique_nodeids[node].get_file_name(),
                                                                  str(visited + [node])))
        visited += [node]
        if node not in self._parent_child_graph:
            # leaf node detected
            pass
        else:
            for child in self._parent_child_graph[node]:
                self._visit_rec(child, visited)

    def _visit_cat_rec(self, category: str, visited: list, affected_nodes: dict):
        if category in visited:
            raise AssertionError(
                "Cycle {0} detected within categories {1} in {2}".format(category,
                                                                         visited,
                                                                         affected_nodes[category][0].get_file_name()))
        visited += [category]
        if category not in self._category_graph:
            # leaf node detected
            pass
        else:
            for child in self._category_graph[category]:
                self._visit_cat_rec(child, visited, affected_nodes)

    def get_order_id(self, element):
        return self._unique_nodeids[element].orderid

    def _validate_hyperlinks(self):
        """
        Check if all hyperlinks exist; create for each source a hyperlink reference list
        :return: None, or raises an Error
        """
        print("   Validating hyperlinks")
        pattern = re.compile(r'\[(.*?)\]\[([a-zA-Z0-9\-]+\$[a-zA-Z0-9\-]+)\]')
        for source_id in self.sources:
            bop_source = self.sources[source_id]
            if bop_source.layout != BopLayouts.default:
                content_with_possible_hyperlinks = bop_source.get_pre_body() + "\n\n" + bop_source.get_body()
                for match in pattern.finditer(content_with_possible_hyperlinks):
                    search_key = match.group(2)
                    if "[" + search_key + "]:http" not in content_with_possible_hyperlinks:
                        if search_key not in self._unique_nodeids:
                            raise AssertionError(
                                "Cannot resolve hyperlink reference [{0}] detected in ".format(
                                    search_key) + bop_source.get_file_name())
                        elif search_key not in bop_source.links:
                            bop_source.links[search_key] = self._unique_nodeids[search_key].url()

    def _validate_scripts(self):
        """
        Check if all scripts exist; create a dictionary for scripts (if any available) for each source
        :return: None, or raises an Error
        """
        print("   Validating scripts")
        pattern = re.compile(r'^(§§§\d+)$', flags=re.M)
        for source_id in self.sources:
            bop_source = self.sources[source_id]
            script_source = bop_source.get_script_source().strip()
            if script_source != "":
                split_script_source = re.split(pattern, script_source)
                keys = list()
                values = list()
                for match in split_script_source:
                    match = match.strip()
                    if match != "":
                        if re.match(r'§§§\d+', match):
                            keys.append(match)
                        else:
                            values.append(match)
                if len(keys) != len(values):
                    raise AssertionError(
                        "Script keys {0} and corresponding scripts do not match in {1}".format(str(keys),
                                                                                               bop_source.get_file_name()))
                if len(set(keys)) != len(keys):
                    raise AssertionError(
                        "Script Keys {0} are not unique in {1}".format(str(keys), bop_source.get_file_name()))
                # create the script dictionary for this bop_source
                counter = 0
                while counter < len(keys):
                    bop_source.scripts[keys[counter]] = values[counter]
                    counter += 1

    def _validate_categories(self):
        """
        Check if all nodes have categories, and if there are no cycles in the categories.
        Make sure there is a source named after the category to avoid missing links when users navigate through them.
        :return: None, or raises an Error
        """
        print("   Validating categories")
        for nodeid in self._unique_nodeids:
            bop_source = self._unique_nodeids[nodeid]
            if len(bop_source.categories) == 0:
                raise AssertionError(
                    "Missing categories in {0}".format(bop_source.get_file_name()))
            pattern = re.compile(r'[a-z0-9\-]+')
            for cat in bop_source.categories:
                if cat not in self._all_categories:
                    self._all_categories[cat] = list()
                if not re.match(pattern, cat):
                    raise AssertionError(
                        "Malformed category '{0}' found in {1} (must match '[a-z0-0\-]+')".format(
                            bop_source.get_file_name()))
                if cat not in self._category_graph:
                    self._category_graph[cat] = list()
                if cat not in self._unique_file_names:
                    raise AssertionError(
                        "No markdown file found for the category '{0}'".format(cat))

            # chain the categories
            for i in range(0, len(bop_source.categories) - 1):
                if bop_source.categories[i + 1] not in self._category_graph[bop_source.categories[i]]:
                    self._category_graph[bop_source.categories[i]].append(bop_source.categories[i + 1])
            # add the node to its last category
            self._all_categories[bop_source.categories[-1]].append(bop_source)
        # sort the nodes within each category
        for cat in self._all_categories:
            self._all_categories[cat].sort(key=lambda x: x.title)
        # check if the categories have cycles
        for cat in self._all_categories:
            visited = list()
            self._visit_cat_rec(cat, visited, self._all_categories)

    def _validate_issues(self):
        """
        Check if the issues listed in the nodes (if any) belong to known categories.
        :return: None, or raises an Error
        """
        print("   Validating issues")
        for bop_source in self._unique_nodeids.values():
            if bop_source.layout in [BopLayouts.theorem, BopLayouts.corollary, BopLayouts.proposition,
                                     BopLayouts.lemma]:
                if not self._has_proof(bop_source):
                    if "missing-proof" not in bop_source.issues:
                        bop_source.issues.append("missing-proof")
            if len(bop_source.issues) > 0:
                for issue in bop_source.issues:
                    if issue not in BopValidator.issue_types:
                        raise AssertionError(
                            "Unknown issue type '{0}' found in {0}".format(issue, bop_source.get_file_name()))

    def _has_proof(self, bop_source):
        for possible_proof in self._unique_nodeids.values():
            if possible_proof.parentid == bop_source.nodeid:
                if possible_proof.layout == BopLayouts.proof:
                    return True
        return False

    def _validate_layouts(self):
        """
        Check if the the layout of each node is is allowed inside the layout of its parent
        :return: None, or raises an Error
        """
        print("   Validating layout nesting")
        errors_found = list()
        erroneous_layouts = list()
        for bop_source in self._unique_nodeids.values():
            if bop_source.nodeid == "bookofproofs$6308":
                pass
            if bop_source.parentid != "":
                parent_node = self._unique_nodeids[bop_source.parentid]
                if parent_node.layout not in BopValidator.allowed_layout_combis:
                    raise AssertionError("Unspecified layout '{0}' in "
                                         "BopValidator.allowed_layout_combis found in {1}".format(
                        parent_node.layout,
                        parent_node.get_file_name()
                    ))
                elif bop_source.layout not in BopValidator.allowed_layout_combis[parent_node.layout]:
                    if "bad-layout-nesting" not in bop_source.issues:
                        bop_source.issues.append("bad-layout-nesting")
                    errors_found.append(bop_source.nodeid)
                    combi = parent_node.layout + "->" + bop_source.layout
                    if combi not in erroneous_layouts:
                        erroneous_layouts.append(combi)
        if errors_found:
            print("      Issues with {0}".format(str(erroneous_layouts)))
            print("      (were added to {0})".format(str(errors_found)))

    def get_parent_child_graph(self):
        return self._parent_child_graph

    def get_nodes(self):
        return self._unique_nodeids

    def get_category_graph(self):
        return self._category_graph

    def get_all_categories(self):
        return self._all_categories
