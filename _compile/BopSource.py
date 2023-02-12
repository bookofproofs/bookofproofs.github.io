import os.path
import re
import html
from FileMgr import FileMgr
from BopValidationError import BopValidationError


class BopLayouts:
    algorithm = "algorithm"
    application = "application"
    axiom = "axiom"
    branch = "branch"
    chapter = "chapter"
    corollary = "corollary"
    default = "default"
    definition = "definition"
    epoch = "epoch"
    example = "example"
    explanation = "explanation"
    hidden = "hidden"
    index = "index"
    lemma = "lemma"
    motivation = "motivation"
    notation = "notation"
    part = "part"
    person = "person"
    proof = "proof"
    problem = "problem"
    proposition = "proposition"
    root = "root"
    section = "section"
    solution = "solution"
    subsection = "subsection"
    topic = "topic"
    theorem = "theorem"


class BopSource:
    related_layouts = [BopLayouts.proof, BopLayouts.solution, BopLayouts.example, BopLayouts.explanation,
                       BopLayouts.corollary, BopLayouts.application, BopLayouts.motivation]
    root_nodes = ["bookofproofs$0", "bookofproofs$2", "bookofproofs$i"]
    repo_name = "bookofproofs.github.io"
    url_root = "https://" + repo_name
    url_images = "https://github.com/bookofproofs/{0}/blob/main/_sources".format(repo_name)
    url_commits = "https://github.com/bookofproofs/{0}/commits/main/_sources".format(repo_name)
    nodeid_pattern = r"[a-z0-9]+\$[A-Za-z0-9\-\_]+"
    ai_contributors = ["@ChatGPT"]

    def __init__(self, file_name: str):
        self.fm = FileMgr()
        source = self.fm.get_file_content("_sources", file_name)
        contents = re.split("^---$", source, flags=re.M)
        if len(contents) != 3 and len(contents) != 4:
            raise BopValidationError("STRUCTURE", "02", "Malformed front matter found in " + file_name)
        if len(contents) == 3:
            self._pre_body = contents[1].strip()
            self._body = contents[2].strip()
            self._script_source = ""
        else:
            self._pre_body = contents[1]
            self._body = contents[2]
            self._script_source = contents[3]
        self._file_name = file_name
        self.name = os.path.splitext(os.path.basename(file_name))[0]
        self.layout = ""
        self.description = ""
        self.keywords = list()
        self.title = ""
        self.nodeid = ""
        self.parentid = ""
        self.publisher = ""
        self.orderid = "0"
        self.publisher = ""
        self.references = list()
        self._references_md = ""
        self.categories = list()
        self.contributors = list()
        self.links = dict()
        self.referencing_nodes = dict()
        self.scripts = dict()
        self.issues = list()
        self.tags = list()
        self.born = 0
        self.died = 0
        self._init_properties(contents[0])
        self._sanitize_lists()
        self._content = ""
        self._toc = ""
        self.parent = None
        self.predecessor = None
        self.successor = None

    def __str__(self):
        if self.title != "":
            return self.layout + ": " + self.title
        else:
            return self.layout + ": " + self.get_long_title()

    def get_file_name(self):
        return self._file_name

    def set_references_md(self, references_md):
        self._references_md = references_md

    def get_references_md(self):
        return self._references_md

    def _init_properties(self, properties):
        properties_split = properties.split("\n")
        for prop in properties_split:
            prop = prop.strip()
            if prop != "":
                property_name = re.search("\w+:", prop)
                if property_name is None:
                    raise BopValidationError("E02", "Malformed property " + properties + " in " + self._file_name)
                else:
                    prop_split = list()
                    prop_split.append(property_name.string[0:property_name.span()[1] - 1])
                    prop_split.append(prop[property_name.span()[1]:])
                prop_split[0] = prop_split[0].strip()
                prop_split[1] = prop_split[1].strip()
                if prop_split[0] == "layout":
                    self.layout = prop_split[1]
                elif prop_split[0] == "categories":
                    self.categories = prop_split[1].split(",")
                elif prop_split[0] == "contributors":
                    self.contributors = prop_split[1].split(",")
                elif prop_split[0] == "description":
                    self.description = html.escape(prop_split[1]).strip()
                    self.description = self.description.replace("\n", "")
                elif prop_split[0] == "keywords":
                    self.keywords = html.escape(prop_split[1]).strip().replace("\n", "").split(",")
                elif prop_split[0] == "title":
                    self.title = html.escape(prop_split[1]).strip()
                    self.title = self.title.replace("\n", "")
                elif prop_split[0] == "nodeid":
                    self.nodeid = prop_split[1].strip()
                elif prop_split[0] == "publisher":
                    self.publisher = prop_split[1].strip()
                elif prop_split[0] == "orderid":
                    self.orderid = prop_split[1].strip()
                elif prop_split[0] == "parentid":
                    self.parentid = prop_split[1].strip()
                elif prop_split[0] == "references":
                    self.references = prop_split[1].split(",")
                elif prop_split[0] == "tags":
                    self.tags = prop_split[1].split(",")
                elif prop_split[0] == "born":
                    try:
                        self.born = int(prop_split[1].strip())
                    except:
                        raise BopValidationError("PERSON", "02",
                                                 "born '{0}' must be an integer in {1}".format(
                                                     prop_split[1].strip(),
                                                     self._file_name)
                                                 )
                elif prop_split[0] == "died":
                    try:
                        self.died = int(prop_split[1].strip())
                    except:
                        raise BopValidationError("PERSON", "02",
                                                 "died '{0}' must be an integer in {1}".format(
                                                     prop_split[1].strip(),
                                                     self._file_name)
                                                 )
                elif prop_split[0] == "issues":
                    self.issues = prop_split[1].split(",")
                else:
                    raise NotImplementedError("Unknown property " + prop_split[0] + " found in " + self._file_name)

    def _sanitize_lists(self):
        self.references = self._sanitize_list(self.references)
        self.contributors = self._sanitize_list(self.contributors)
        self.categories = self._sanitize_list(self.categories)
        self.issues = self._sanitize_list(self.issues)
        self.tags = self._sanitize_list(self.tags)
        self.keywords = self._sanitize_list(self.keywords)

    def _sanitize_list(self, l: list):
        new_list = list()
        for el in l:
            el = el.strip()
            if el != "":
                new_list.append(el)
        return new_list

    def get_content_of_node(self):
        if self.layout == BopLayouts.default:
            return self.get_body()
        elif self.layout in BopSource.related_layouts:
            return self._get_content_related_node()
        elif self.layout.strip() == "":
            raise NotImplementedError("Please provide a layout for " + self.name + " in " + self._file_name)
        else:
            return self._get_content_node()

    def get_file_destination(self):
        return "/".join(self.categories)

    def get_link_references(self):
        ret = "\n\n"
        for link in self.links:
            ret += "[" + link + "]:" + self.links[link] + "\n"
        return ret

    def url(self):
        destination = self.get_file_destination()
        if destination == "":
            return BopSource.url_root + "/" + self.name + ".html"
        else:
            return BopSource.url_root + "/" + destination + "/" + self.name + ".html"

    def get_contributors(self):
        ret_github = "<dt><span class='navigation'>Github:</span></dt><dd>"
        github = False
        ret_non_github = "<dt><span class='navigation'>non-Github:</span></dt><dd>"
        non_github = False
        ret_ai = "<dt><span class='navigation'>AI:</span></dt><dd>"
        ai = False
        for contributor in self.contributors:
            if contributor.startswith("@") and contributor not in BopSource.ai_contributors:
                non_github = True
                # named non-github contributor
                if ret_non_github != "":
                    ret_non_github += "</dd><dd>"
                ret_non_github += contributor
            elif contributor.startswith("@") and contributor in BopSource.ai_contributors:
                ai = True
                # named ai contributor
                if ret_ai != "":
                    ret_ai += "</dd><dd>"
                ret_ai += contributor
            else:
                github = True
                if ret_github != "":
                    ret_github += " "
                # contributor from github
                ret_github += "<a title='github user {0}' href='https://github.com/{1}'>".format(contributor,
                                                                                                 contributor)
                ret_github += "<img src='https://github.com/{0}.png?size=32' alt='{1}'/>".format(contributor,
                                                                                                 contributor)
                ret_github += "</a>"
        ret = "<dl>"
        if github:
            ret += "</dd>" + ret_github + "<br>"
        if non_github:
            ret += "</dd>" + ret_non_github + "<br>"
        if ai:
            ret += "</dd>" + ret_ai + "<br>"
        return ret + "</dl>"

    def _get_content_related_node(self):
        ret = self._pre_body
        ret += self.__get_title()
        if self.parent.title != "":
            ret += " (related to <a href='" + self.parent.url() + "'>" + self.parent.get_plane_title() + "</a>)\n\n"
        if self._body.strip() == "":
            ret += "_(no contents provided yet)_"
        else:
            ret += self._body
            if self.layout == BopLayouts.proof:
                ret += "<div class='qed'>&#8718;</div>"
        return ret

    def _get_content_node(self):
        ret = self._pre_body + "\n"
        ret += self.__get_title()
        if self._body.strip() == "":
            ret += "_(no contents provided yet)_"
        else:
            ret += self._body
        return ret

    def get_body(self):
        return self._body

    def set_body(self, body: str):
        self._body = body

    def get_pre_body(self):
        return self._pre_body

    @staticmethod
    def get_plural_layout_title(layout: str):
        if layout == BopLayouts.branch:
            return "Branches"
        elif layout == BopLayouts.corollary:
            return "Corollaries"
        else:
            return BopSource.get_layout_title(layout) + "s"

    @staticmethod
    def get_layout_title(layout: str):
        if layout == BopLayouts.algorithm:
            return "Algorithm"
        elif layout == BopLayouts.application:
            return "Application"
        elif layout == BopLayouts.axiom:
            return "Axiom"
        elif layout == BopLayouts.branch:
            return "Branch"
        elif layout == BopLayouts.chapter:
            return "Chapter"
        elif layout == BopLayouts.corollary:
            return "Corollary"
        elif layout == BopLayouts.definition:
            return "Definition"
        elif layout == BopLayouts.example:
            return "Example"
        elif layout == BopLayouts.explanation:
            return "Explanation"
        elif layout == BopLayouts.lemma:
            return "Lemma"
        elif layout == BopLayouts.part:
            return "Part"
        elif layout == BopLayouts.problem:
            return "Problem"
        elif layout == BopLayouts.proof:
            return "Proof"
        elif layout == BopLayouts.motivation:
            return "Motivation"
        elif layout == BopLayouts.proposition:
            return "Proposition"
        elif layout == BopLayouts.section:
            return "Section"
        elif layout == BopLayouts.solution:
            return "Solution"
        elif layout == BopLayouts.subsection:
            return "Subsection"
        elif layout == BopLayouts.theorem:
            return "Theorem"
        elif layout == BopLayouts.epoch:
            return "Epoch"
        elif layout == BopLayouts.topic:
            return "Topic"
        elif layout == BopLayouts.root:
            return "."
        elif layout == BopLayouts.default:
            return "."
        elif layout == BopLayouts.index:
            return "Index"
        elif layout == BopLayouts.hidden:
            return "."
        elif layout == BopLayouts.notation:
            return "."
        elif layout == BopLayouts.person:
            return "Person"
        else:
            raise NotImplementedError(layout)

    def get_long_title(self):
        title = self.title
        if title == "" and self.layout in BopSource.related_layouts:
            title = "(related to " + self.parent.get_plane_title() + ")"
        if title == "" and self.nodeid in BopSource.root_nodes:
            title = self.categories[0].capitalize()
        return title

    def __get_title(self):
        title = self.get_plane_title()
        if title != "":
            return "# " + title + "\n\n"
        return ""

    def get_plane_title(self):
        ret = BopSource.get_layout_title(self.layout)
        if self.title != "" and ret != ".":
            ret += ": " + self.title
        elif self.title == "" and ret != ".":
            return ret
        else:
            ret = self.title
        return ret

    def get_plane_long_title(self):
        ret = BopSource.get_layout_title(self.layout)
        title = self.get_long_title()
        if title != "" and ret != ".":
            ret += ": " + title
        else:
            ret = title
        return ret

    def _get_content_branch(self):
        return self._body

    def set_compiled_content(self, content):
        self._content = content

    def get_compiled_content(self):
        return self._content

    def set_toc(self, toc: str):
        self._toc = toc

    def get_toc(self):
        return self._toc

    def content_contains(self, search_str: str):
        return search_str in self._body + " " + self._pre_body

    def get_referencing_nodes_html(self):
        ret = ""
        if len(self.referencing_nodes) != 0:
            ret += "<h3 class='navigation'>Mentioned in:</h3>\n\n"
            internal_references = list(self.referencing_nodes.values())
            internal_references.sort(key=lambda x: x.layout + " " + ", ".join(x.categories) + ", " + x.get_sort_title())
            counter = 0
            current_layout = ""
            for bop_source in internal_references:
                counter += 1
                if current_layout != bop_source.layout:
                    if current_layout != "":
                        ret += "<br>"
                    ret += BopSource.get_plural_layout_title(bop_source.layout) + ": "
                    current_layout = bop_source.layout
                ret += "<a href='{0}' title='{1}'>{2}</a> ".format(bop_source.url(),
                                                                   bop_source.get_title_for_anchor(),
                                                                   counter)
            ret += "<br>"
        return ret

    def get_relevant_tags_html(self):
        ret = ""
        if len(self.tags) != 0:
            ret += "<h3 class='navigation'>Tags relevant for this {0}:</h3>\n\n".format(self.layout)
            pretty_tags = list()
            for tag in self.tags:
                pretty = tag.replace("-", " ").title()
                pretty_tags.append(pretty)
            ret += "> " + ", ".join(pretty_tags)
        return ret

    def get_title_for_anchor(self):
        cats = self.categories.copy()
        if len(cats) > 1:
            cats = cats[1:]
        for i in range(0, len(cats)):
            cats[i] = cats[i].replace("-", " ").title()
        return html.escape(" / ".join(cats) + " / " + self.get_plane_long_title())

    def get_titled_anchor(self, count, level):
        outline = BopSource.get_layout_title(self.layout)
        if outline == ".":
            outline = ""
        else:
            outline += ": "

        if count > 0:
            ret = "<span class='caret'>{0}</span><a href='{1}' title='{2}'>{3}</a> ({4}) \n".format(
                outline,
                self.url(),
                self.get_title_for_anchor(),
                self.get_long_title(),
                count
            )
        elif count == 0:
            ret = " " * level + "<li><span>{0}</span><a href='{1}' title='{2}'>{3}</a></li>\n".format(
                outline,
                self.url(),
                self.get_title_for_anchor(),
                self.get_long_title()
            )
        else:
            ret = " " * level + "<span>{0}</span><a href='{1}' title='{2}'>{3}</a>\n".format(
                outline,
                self.url(),
                self.get_title_for_anchor(),
                self.get_long_title()
            )
        return ret

    def get_categories_links(self):
        ret = "<h3 class='navigation'>"
        if self.layout != BopLayouts.default:
            parent_link = "&#x25B2"
            predecessor_link = "&#x25C0;"
            successor_link = "&#x25B6;"
            if self.parent is not None:
                parent_link = "<a href='{0}'>{1}</a>".format(self.parent.url(), parent_link)
                if self.predecessor is not None:
                    predecessor_link = "<a href='{0}'>{1}</a>".format(self.predecessor.url(), predecessor_link)
                if self.successor is not None:
                    successor_link = "<a href='{0}'>{1}</a>".format(self.successor.url(), successor_link)
            else:
                if self.successor is not None:
                    successor_link = "<a href='{0}'>{1}</a>".format(self.successor.url(), successor_link)
            ret += "{0} {1} {2}".format(predecessor_link, parent_link, successor_link)
        path = list()
        path_link = BopSource.url_root
        for cat in self.categories:
            path_link += "/" + cat
            path.append("<a href='{0}'>{1}</a>".format(path_link + "/" + cat + ".html", cat.capitalize()))
        path_title = BopSource.get_layout_title(self.layout)
        if path_title != ".":
            path_title = self.get_plane_title()
        path.append(path_title)
        ret += " / ".join(path) + "</h3>\n\n<hr>\n"
        return ret

    def get_script_source(self):
        return self._script_source

    def get_sort_title(self, leading_zeros=5):
        title = self.get_long_title()
        pattern = re.compile(r"(\d+)")
        title = re.sub(pattern, r"\1".zfill(leading_zeros), title)
        return title

    @staticmethod
    def script_has_python(script: str):
        return "```" in script and ".python" in script

    def to_md(self):
        ret = ""
        ret += "layout: person\n"
        ret += "nodeid: " + self.nodeid + "\n"
        ret += "categories: " + ",".join(self.categories) + "\n"
        ret += "parentid: " + self.parentid + "\n"
        ret += "tags: " + ",".join(self.tags) + "\n"
        ret += "orderid: " + str(self.orderid) + "\n"
        ret += "title: " + self.title + "\n"
        ret += "born: " + str(self.born) + "\n"
        ret += "died: " + str(self.died) + "\n"
        ret += "keywords: " + ",".join(self.keywords) + "\n"
        ret += "description: " + self.description + "\n"
        ret += "references: " + ",".join(self.references) + "\n"
        ret += "contributors: " + ",".join(self.contributors) + "\n"
        ret += "\n---\n\n"
        ret += self.get_pre_body() + "\n"
        ret += "\n---\n\n"
        ret += self.get_body() + "\n"
        return ret
