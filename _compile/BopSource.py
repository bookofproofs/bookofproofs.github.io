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
    part = "part"
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
    url_root = "https://bookofproofs.github.io"
    url_images = "https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources"

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
        self.keywords = ""
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
        self.scripts = dict()
        self.issues = list()
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
                    self.keywords = html.escape(prop_split[1]).strip()
                    self.keywords = self.keywords.replace("\n", "")
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
                elif prop_split[0] == "issues":
                    self.issues = prop_split[1].split(",")
                else:
                    raise NotImplementedError("Unknown property " + prop_split[0] + " found in " + self._file_name)

    def _sanitize_lists(self):
        self.references = self._sanitize_list(self.references)
        self.contributors = self._sanitize_list(self.contributors)
        self.categories = self._sanitize_list(self.categories)
        self.issues = self._sanitize_list(self.issues)

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
        ret = ""
        for contributor in self.contributors:
            if contributor.startswith("@"):
                # named contributor
                if ret != "":
                    ret += " "
                ret += contributor
            else:
                if ret != "":
                    ret += " "
                # contributor from github
                ret += "<a href='https://github.com/" + contributor + "'>"
                ret += "<img src='https://github.com/" + contributor + ".png?size=32' alt='" + contributor + "'/>"
                ret += "</a>"
        ret += " <a class='improve' title='{0}' href='{1}/{2}'>{3}</a><br>".format(
            'improve this site',
            BopSource.url_images,
            self.get_file_destination() + "/" + self.name + ".md",
            "<img src='" + BopSource.url_images + "/_assets/images/edit-black.png?raw=true' alt=''>")
        return ret

    def _get_content_related_node(self):
        ret = self._pre_body
        ret += self.__get_title()
        if self.parent.title != "":
            ret += " (related to <a href='" + self.parent.url() + "'>" + self.parent.get_plane_title() + "</a>)\n\n"
        if self._body.strip() == "":
            ret += "_(no contents provided yet)_"
        else:
            ret += self._body
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
