import html
import re
from BopSource import BopLayouts, BopSource
from FileMgr import FileMgr
from BopValidationError import BopValidationError


class BopValidator:
    allowed_layout_combis = {
        BopLayouts.root: [BopLayouts.branch, BopLayouts.index, BopLayouts.epoch, BopLayouts.topic],
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
        BopLayouts.epoch: [BopLayouts.epoch, BopLayouts.topic],
        BopLayouts.topic: [BopLayouts.topic]
    }

    def __init__(self, sources: dict):
        self.sources = sources
        self._unique_nodeids = dict()
        self._parent_child_graph = dict()
        self._unique_file_names = dict()
        self._category_graph = dict()
        self._all_categories = dict()
        self._validate_nodeids("IDENTIFIER")
        self._validate_names("NAMING")
        self._validate_orderids("ORDER")
        self._validate_parentids("PARENT")
        self._validate_tree("STRUCTURE")
        self._validate_notation("NOTATION")
        self._validate_hyperlinks("LINK")
        self._validate_scripts("SCRIPT")
        self._validate_categories("CATEGORY")
        self._validate_issues("ISSUE")
        self._validate_layouts("LAYOUT")
        self._validate_persons("PERSON")

    def _validate_nodeids(self, err_type: str):
        """
        Check for duplicate or missing nodeids, also check if nodeid is provided if and only if layout!=default
        :param err_type: error domain
        :return: None, or raises an Error
        """
        print("   Validating " + err_type)
        for bop_source in self.sources.values():
            if bop_source.layout == "":
                raise BopValidationError(err_type, "01", "Missing layout detected in " + bop_source.get_file_name())
            if bop_source.layout == BopLayouts.default and bop_source.nodeid != "":
                raise BopValidationError(err_type, "02",
                                         "nodeid not allowed for nodes with layout:default " +
                                         bop_source.get_file_name())
            elif bop_source.layout not in [BopLayouts.default, BopLayouts.hidden] and bop_source.nodeid == "":
                raise BopValidationError(err_type, "03",
                                         "Missing nodeid when layout: (other than default) " +
                                         bop_source.get_file_name())
            if bop_source.nodeid != "" and bop_source.nodeid not in self._unique_nodeids:
                self._unique_nodeids[bop_source.nodeid] = bop_source
            elif bop_source.nodeid == "" and bop_source.nodeid not in self._unique_nodeids:
                pass
            else:
                raise BopValidationError(err_type, "04",
                                         "Duplicate nodeid {0} detected in ".format(
                                             bop_source.nodeid) + bop_source.get_file_name())

    def _validate_names(self, err_type: str):
        """
        Check if each file name is unique, regardless where it resides in the folder structure of _sources.
        :param err_type: error domain
        :return: None, or raises an Error
        """
        print("   Validating " + err_type)
        pattern = re.compile(r"^[a-z0-9\-]+$")
        for nodeid in self._unique_nodeids:
            bop_source = self._unique_nodeids[nodeid]
            base_name = FileMgr.get_base_name(bop_source.get_file_name())
            base_name_without_ext = base_name.split(".")[0]
            if base_name_without_ext not in self._unique_file_names:
                if not re.match(pattern, base_name_without_ext):
                    msg = "Illegal characters found in filename {0}".format(bop_source.get_file_name())
                    raise BopValidationError(err_type, "01", msg)
                self._unique_file_names[base_name_without_ext] = bop_source
            else:
                duplicate = self._unique_file_names[base_name_without_ext]
                raise BopValidationError(err_type, "02",
                                         "Duplicate filename in\n{0} and\n{1}".format(duplicate.get_file_name(),
                                                                                      bop_source.get_file_name()))

    def _validate_orderids(self, err_type: str):
        """
        Check for positive integer order ids; Create an issue if there are multiple nodes with the same order id
        inside the same parent
        :param err_type: error domain
        :return: None, or raises an Error if negative or non-numeric
        """
        print("   Validating " + err_type)
        for source_id in self._unique_nodeids:
            bop_source = self._unique_nodeids[source_id]
            if bop_source.orderid.isdigit():
                bop_source.orderid = int(bop_source.orderid)
            else:
                raise BopValidationError(err_type, "01",
                                         "Only positive integer orderid " +
                                         "allowed for {0} detected in {1}".format(bop_source.nodeid,
                                                                                  bop_source.get_file_name()))

            filter_expr = lambda x: x.parentid == bop_source.nodeid
            children_nodes = list(filter(filter_expr, self._unique_nodeids.values()))
            clashing_orderids = set()
            for child in children_nodes:
                if child.orderid not in clashing_orderids:
                    clashing_orderids.add(child.orderid)
                else:
                    bop_source.issues.append("conflicting-order-of-children")
                    break

    def _validate_parentids(self, err_type: str):
        """
        Check for missing parentids
        :param err_type: error domain
        :return: None, or raises an Error
        """
        print("   Validating " + err_type)
        for source_id in self._unique_nodeids:
            bop_source = self._unique_nodeids[source_id]
            if bop_source.parentid == "" and bop_source.nodeid in BopSource.root_nodes:
                pass  # only the single node bookofproofs$0 may have no parentid (since it is the root)
            elif bop_source.parentid == "" and bop_source.nodeid not in BopSource.root_nodes and \
                    bop_source.layout != BopLayouts.hidden:
                raise BopValidationError(err_type, "01",
                                         "Missing parentid only allowed for hidden and the root nodes {0}; ".format(
                                             str(BopSource.root_nodes)) +
                                         "detected in " + bop_source.get_file_name())
            elif bop_source.parentid not in self._unique_nodeids and bop_source.layout != BopLayouts.hidden:
                raise BopValidationError(err_type, "02",
                                         "Unknown parentid {0} detected in ".format(
                                             bop_source.parentid) + bop_source.get_file_name())
            if bop_source.parentid != "":
                if bop_source.parentid not in self._parent_child_graph:
                    self._parent_child_graph[bop_source.parentid] = list()
                self._parent_child_graph[bop_source.parentid].append(bop_source.nodeid)
                bop_source.parent = self._unique_nodeids[bop_source.parentid]
        print("   Sorting parent-child graph")
        for nodeid in self._unique_nodeids:
            if nodeid in self._parent_child_graph:
                self._parent_child_graph[nodeid].sort(key=self.get_order_id)

    def _validate_tree(self, err_type: str):
        """
        Check if the parent-child relationship between parentid and nodeid produces any cycles
        and if the graph is disconnected
        :param err_type: error domain
        :return: None, or raises an Error
        """
        print("   Validating " + err_type)
        visited = list()
        for root_node in BopSource.root_nodes:
            if root_node not in self._parent_child_graph.keys():
                raise BopValidationError(err_type, "01", "No root '{0}' in any of _sources/*".format(root_node))
            self._visit_rec(err_type, root_node, visited)
        li1 = list(self._parent_child_graph.keys())
        li2 = visited
        unvisited = list()
        for i in li1:
            if i not in li2:
                unvisited.append(i)
        if len(unvisited) > 0:
            raise BopValidationError(err_type, "02",
                                     "{0} disconnected nodes detected {1}".format(len(unvisited), str(unvisited)))

    def _visit_rec(self, err_type: str, node, visited):
        if node in visited:
            raise BopValidationError(err_type, "03",
                                     "Cycle detected in {0} after visiting {1}".format(
                                         self._unique_nodeids[node].get_file_name(),
                                         str(visited + [node])))
        visited += [node]
        if node not in self._parent_child_graph:
            # leaf node detected
            pass
        else:
            for child in self._parent_child_graph[node]:
                self._visit_rec(err_type, child, visited)

    def get_order_id(self, element):
        return self._unique_nodeids[element].orderid

    def _validate_hyperlinks(self, err_type: str):
        """
        Check if all hyperlinks exist; create for each source a hyperlink reference list
        :param err_type: error domain
        :return: None, or raises an Error
        """
        print("   Validating " + err_type)
        pattern = re.compile(r'\[(.*?)\]\[([a-zA-Z0-9\-]+\$[a-zA-Z0-9\-]+)\]')
        for source_id in self.sources:
            bop_source = self.sources[source_id]
            if bop_source.layout != BopLayouts.default:
                content_with_possible_hyperlinks = bop_source.get_pre_body() + "\n\n" + bop_source.get_body()
                for match in pattern.finditer(content_with_possible_hyperlinks):
                    search_key = match.group(2)
                    if "[" + search_key + "]:http" not in content_with_possible_hyperlinks:
                        if search_key not in self._unique_nodeids:
                            raise BopValidationError(err_type, "01",
                                                     "Cannot resolve hyperlink reference [{0}] detected in ".format(
                                                         search_key) + bop_source.get_file_name())
                        elif search_key not in bop_source.links:
                            other_node = self._unique_nodeids[search_key]
                            bop_source.links[
                                search_key] = other_node.url() + " \"" + other_node.get_title_for_anchor() + "\""

    def _validate_scripts(self, err_type: str):
        """
        Check if all scripts exist; create a dictionary for scripts (if any available) for each source
        :param err_type: error domain
        :return: None, or raises an Error
        """
        print("   Validating " + err_type)
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
                    raise BopValidationError(err_type, "01",
                                             "Script keys {0} and corresponding scripts do not match in {1}".format(
                                                 str(keys),
                                                 bop_source.get_file_name()))
                if len(set(keys)) != len(keys):
                    raise BopValidationError(err_type, "02",
                                             "Script Keys {0} are not unique in {1}".format(str(keys),
                                                                                            bop_source.get_file_name()))
                # create the script dictionary for this bop_source
                counter = 0
                while counter < len(keys):
                    bop_source.scripts[keys[counter]] = values[counter]
                    counter += 1

    def _validate_categories(self, err_type: str):
        """
        Check if all nodes have categories, and if there are no cycles in the categories.
        Make sure there is a source named after the category to avoid missing links when users navigate through them.
        :param err_type: error domain
        :return: None, or raises an Error
        """
        print("   Validating " + err_type)
        for nodeid in self._unique_nodeids:
            bop_source = self._unique_nodeids[nodeid]
            if len(bop_source.categories) == 0 and bop_source.layout != BopLayouts.hidden:
                raise BopValidationError(err_type, "01",
                                         "Missing categories in {0}".format(bop_source.get_file_name()))
            if bop_source.parent is not None:
                if ",".join(bop_source.parent.categories) not in ",".join(bop_source.categories):
                    raise BopValidationError(err_type, "02",
                                             "Categories '{0}' of {1}\ndo not correspond " \
                                             "to the categories {2}\nof its parent {3}.".format(
                                                 str(bop_source.categories),
                                                 bop_source.get_file_name(),
                                                 str(bop_source.parent.categories),
                                                 bop_source.parent.get_file_name()
                                             )
                                             )
                pattern = re.compile(r'[a-z0-9\-]+')
                for cat in bop_source.categories:
                    if cat not in self._all_categories:
                        self._all_categories[cat] = list()
                    if not re.match(pattern, cat):
                        raise BopValidationError(err_type, "03",
                                                 "Malformed category '{0}' " \
                                                 "found in {1} (must match '[a-z0-0\-]+')".format(
                                                     cat, bop_source.get_file_name()))
                    if cat not in self._category_graph:
                        self._category_graph[cat] = list()
                    if cat not in self._unique_file_names:
                        msg = "No markdown file found for the category "
                        msg += "'{0}' found in {1}".format(cat, bop_source.get_file_name())
                        msg += "\nTo start using this category, you must first add a new source file "
                        msg += "{0}.md to _sources.".format(cat)
                        msg += "\nAlso, give it the same categories as in {0}".format(bop_source.get_file_name())
                        raise BopValidationError(err_type, "04", msg)
                    else:
                        other = self._unique_file_names[cat]
                        if other.categories[-1] != cat:
                            msg = "The file '{0}' is used as a category but has ".format(other.get_file_name())
                            msg += "the categories '{0}'".format(",".join(other.categories))
                            msg += "\nMake sure the file name '{0}' ".format(cat)
                            msg += "is the last category in the front matter."
                            raise BopValidationError(err_type, "05", msg)

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
                self._visit_cat_rec(err_type, cat, visited, self._all_categories)

    def _visit_cat_rec(self, err_type: str, category: str, visited: list, affected_nodes: dict):
        if category in visited:
            raise BopValidationError(err_type, "06",
                                     "Cycle {0} detected within " +
                                     "categories {1} in {2}".format(category,
                                                                    visited,
                                                                    affected_nodes[category][
                                                                        0].get_file_name()))
        visited += [category]
        if category not in self._category_graph:
            # leaf node detected
            pass
        else:
            for child in self._category_graph[category]:
                self._visit_cat_rec(err_type, child, visited, affected_nodes)

    def _validate_issues(self, err_type: str):
        """
        Check if the issues listed in the nodes (if any) belong to known categories.
        :param err_type: error domain
        :return: None, or raises an Error
        """
        print("   Validating " + err_type)
        for bop_source in self._unique_nodeids.values():
            if bop_source.layout != BopLayouts.hidden:
                if bop_source.layout in [BopLayouts.theorem, BopLayouts.corollary, BopLayouts.proposition,
                                         BopLayouts.lemma]:
                    if not self._has_proof(bop_source):
                        bop_source.issues.append("missing-proof")
                else:
                    if self._has_proof(bop_source):
                        bop_source.issues.append("misplaced-proof")
                content = bop_source.get_pre_body() + "\n" + bop_source.get_body()
                if "bookofproofs.org" in content or "\":http" in content:
                    bop_source.issues.append("non-migrated-link")
                if bop_source.keywords == "":
                    bop_source.issues.append("seo-missing-keywords")
                if bop_source.description == "":
                    bop_source.issues.append("seo-missing-description")
                if bop_source.orderid == 0:
                    bop_source.issues.append("missing-order-id")
                if bop_source.layout == BopLayouts.algorithm and not \
                    bop_source.script_has_python(str(bop_source.scripts)):
                    bop_source.issues.append("sourcecode-markdown-broken")


    def _has_proof(self, bop_source):
        for possible_proof in self._unique_nodeids.values():
            if possible_proof.parentid == bop_source.nodeid:
                if possible_proof.layout == BopLayouts.proof:
                    if possible_proof.get_body() != "":
                        return True
        return False

    def _validate_layouts(self, err_type: str):
        """
        Check if the layout of each node is is allowed inside the layout of its parent
        :param err_type: error domain
        :return: None, or raises an Error
        """
        print("   Validating " + err_type)
        errors_found = list()
        erroneous_layouts = list()
        for bop_source in self._unique_nodeids.values():
            if bop_source.parentid != "":
                parent_node = self._unique_nodeids[bop_source.parentid]
                if parent_node.layout not in BopValidator.allowed_layout_combis:
                    raise AssertionError("Unspecified layout '{0}' in "
                                         "BopValidator.allowed_layout_combis found in {1}".format(
                        parent_node.layout,
                        parent_node.get_file_name()
                    ))
                elif bop_source.layout not in BopValidator.allowed_layout_combis[parent_node.layout]:
                    issue = "bad-layout-nesting-" + bop_source.layout + "&#8605;" + parent_node.layout
                    if issue not in bop_source.issues:
                        bop_source.issues.append(issue)
                    errors_found.append(bop_source.nodeid)
                    combi = bop_source.layout + "↝" + parent_node.layout
                    if combi not in erroneous_layouts:
                        erroneous_layouts.append(combi)
        if errors_found:
            print("      Issues with {0}".format(str(erroneous_layouts)))
            print("      (were added to {0})".format(str(errors_found)))

    def _validate_notation(self, err_type: str):
        """
        Check if the notation of each node is is allowed inside the layout of its parent
        :param err_type: error domain
        :return: None, or raises an Error
        """
        print("   Validating " + err_type)
        notation_file = "../_sources/_references/notation.md"
        notation_data = self.sources[notation_file].get_body().splitlines()
        index_file = "../_sources/index/n-index.md"
        unique_categories = dict()
        for line in notation_data:
            pattern = re.compile(r"\[(.*?)\]\[(.*?)\]")
            unique_references_per_notation = set()
            for match in pattern.finditer(line):
                if match.group(2) not in unique_references_per_notation:
                    unique_references_per_notation.add(match.group(2))
                if match.group(2) not in self._unique_nodeids:
                    raise BopValidationError(err_type, "01",
                                             "Unknown id '{0}' found in {1}".format(match.group(2), notation_file))
                else:
                    referenced_node = self._unique_nodeids[match.group(2)]
                    cat_id = ",".join(referenced_node.categories)
                    if cat_id not in unique_categories:
                        unique_categories[cat_id] = list()
                    unique_categories[cat_id].append(line)
            if "Notation" not in line and "Description not in line" and ":---" not in line:
                if len(unique_references_per_notation) > 1:
                    raise BopValidationError(err_type, "02",
                                             "Multiple references '{0}' found in line {1} in {2}".format(
                                                 str(unique_references_per_notation),
                                                 line,
                                                 notation_file)
                                             )
                if len(unique_references_per_notation) == 0:
                    raise BopValidationError(err_type, "03", "Missing references in line {0} found in {1}".format(
                        line,
                        notation_file)
                                             )
                if len(line.split("|")) != 3:
                    raise BopValidationError(err_type, "04", "Notation line {0} does not have 3 columns {1}".format(
                        line,
                        notation_file)
                                             )
        print("   Making symbolic notation index")
        keys = list(unique_categories.keys())
        keys.sort()
        index = ""
        new_table = "\n\nNotation | Description  | Comment\n:------------- | :------------- | :-------------\n"
        for key in keys:
            notation_header = key.replace("branches,", "").replace(",", " / ").replace("-", " ").title()
            index += "### " + notation_header + new_table
            for line in unique_categories[key]:
                index += line + "\n"
            index += "\n\n"
        replaced = self.sources[index_file].get_body()
        replaced = replaced.replace("{{ n-index }}", index)
        self.sources[index_file].set_body(replaced)

    def _validate_persons(self, err_type: str):
        """
        Check if the person names or hyperlinks to person biographies listed in the epoch layout are unique.
        :param err_type: error domain
        :return: None, or raises an Error
        """
        print("   Validating " + err_type)
        unique_names = dict()
        unique_links = dict()
        pattern_name = re.compile(r"^\<a href\=[\"\'](.*?)[\"\']\>(.*?)\<\/a", flags=re.M)
        pattern_link = re.compile(r"^\<a href\=[\"\'](.*?)[\"\']\>", flags=re.M)
        error_msgs = list()
        for bop_source in self._unique_nodeids.values():
            if bop_source.layout == BopLayouts.epoch:
                for match in pattern_name.finditer(bop_source.get_body()):
                    if match.group(2) not in unique_names:
                        unique_names[match.group(2)] = bop_source.get_file_name() + " " + match.group(1)
                    else:
                        error_msgs.append("Duplicate person '{0}'\nin {1}\nand {2}".format(
                            match.group(2),
                            bop_source.get_file_name() + " " + match.group(1),
                            unique_names[match.group(2)]
                        ))
                for match in pattern_link.finditer(bop_source.get_body()):
                    if match.group(1) not in unique_links:
                        unique_links[match.group(1)] = bop_source.get_file_name()
                    else:
                        error_msgs.append("Duplicate reference {0}\nin {1}\nand {2}".format(
                            match.group(1),
                            bop_source.get_file_name(),
                            unique_links[match.group(1)]
                        ))
        if len(error_msgs) > 0:
            raise BopValidationError(err_type, "01", "Person errors found:\n\n".format(len(error_msgs))
                                     + "\n\n".join(error_msgs) + "\n\n{0} errors total".format(len(error_msgs)))

    def get_parent_child_graph(self):
        return self._parent_child_graph

    def get_nodes(self):
        return self._unique_nodeids

    def get_category_graph(self):
        return self._category_graph

    def get_all_categories(self):
        return self._all_categories

    def get_notation(self):
        return self._notation
