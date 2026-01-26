import logging
import xml.etree.ElementTree as etree
from typing import Optional

import markdown
from markdown.treeprocessors import Treeprocessor

logger = logging.getLogger(__name__)


class ExternalLinkMarker(Treeprocessor):
    """A mardkdown processor that marks links as external when necessary"""

    def run(self, root: etree.Element) -> Optional[etree.Element]:
        try:
            for anchor_elem in root.findall(".//a"):
                href = anchor_elem.attrib["href"]
                # is_external = is_external_url(href)
                is_external = False
                logger.debug('Marking anchor <a href="%s"> as %s', href, "external" if is_external else "internal")
                if is_external:
                    anchor_elem.set("rel", anchor_elem.get("rel", "") + "external")
        except Exception:
            logger.exception("Cold not process element tree with %s", type(self))


class WrapSectionProcessor(Treeprocessor):
    """A markdown processor that automatically wraps content in <section> tags based on <h2> headings"""

    def run(self, root: etree.Element) -> Optional[etree.Element]:
        try:
            new_root = etree.Element(root.tag, root.attrib)
            cur_section = etree.Element("section")
            new_root.append(cur_section)

            for child in root:
                if child.tag == "h2":
                    cur_section = etree.Element("section")
                    cur_section.append(child)
                    new_root.append(cur_section)
                else:
                    cur_section.append(child)

            return new_root
        except Exception:
            logger.exception("Could not process element tree with %s", type(self))


class SectionIdLinker(Treeprocessor):
    """
    A markdown processor that assigns id= attributes to sections based on the contained <h2> tag
    as well as creating links to the section with a # character after the heading.
    It also creates # links to subheadings but without wrapping them in sections.
    """

    @staticmethod
    def id_from_text(text: str) -> str:
        return (
            text.lower()
                .replace(" ", "-")
                .replace("/", "-")
                .replace("&", "")
                .replace("!", "")
                .replace("(", "")
                .replace(")", "")
                .replace(",", "")
        )
        

    def link_h2(self, root: etree.Element):
        for section in root.findall("section[h2]"):
            heading = section.find("h2")
            sec_id = self.id_from_text(heading.text)
            logger.debug("Linking section with heading %s as id=%s", heading.text, sec_id)

            # add id to section itself
            section.attrib["id"] = sec_id

            # add span containing the actual title
            elem = etree.Element("span")
            elem.text = heading.text + " "
            heading.clear()
            heading.append(elem)

            # add anchor containing a link to the section
            elem = etree.Element("a", {"href": f"#{sec_id}", "title": "Link to this section"})
            elem.text = "#"
            heading.append(elem)

    def link_subsection(self, root: etree.Element, typ: str):
        for subheading in root.iter(typ):
            sec_id = self.id_from_text(subheading.text)
            logger.debug("Linking subheading %s %s as id=%s", typ, subheading.text, sec_id)

            # add span containing the actual title
            elem = etree.Element("span")
            elem.text = subheading.text + " "
            subheading.clear()
            subheading.append(elem)
            subheading.attrib["id"] = sec_id

            # add anchor containing a link to this subheading
            elem = etree.Element("a", {"href": f"#{sec_id}", "title": "Link to this section"})
            elem.text = "#"
            subheading.append(elem)

    def run(self, root: etree.Element) -> Optional[etree.Element]:
        try:
            self.link_h2(root)
            self.link_subsection(root, "h3")
            self.link_subsection(root, "h4")
            self.link_subsection(root, "h5")
        except Exception:
            logger.exception("Could not process element tree with %s", type(self))


class FootnotesAsideTransformer(Treeprocessor):
    """A markdown processor that converts the footnotes <div> container into an <aside>"""

    def run(self, root: etree.Element) -> Optional[etree.Element]:
        try:
            container = root.find("div[@class='footnote']")
            container.tag = "aside"
        except Exception:
            logger.exception("Could not process element tree with %s", type(self))


class BlogMdExt(markdown.Extension):
    """Custom markdown extension which registers the processors defined above"""

    def extendMarkdown(self, md: markdown.Markdown):
        logger.debug("Registering custom markdown processors for blog")
        try:
            md.treeprocessors.register(WrapSectionProcessor(), "wrap-sections", 75)
            md.treeprocessors.register(SectionIdLinker(), "link-sections", 70)
            md.treeprocessors.register(FootnotesAsideTransformer(), "footnote-aside-transformer", 40)
            md.treeprocessors.register(ExternalLinkMarker(), "external-link-marker", 10)
        except Exception:
            logger.exception("Could not register processors for extension %s", type(self))


def render(text: str) -> str:
    return markdown.markdown(
        text=text,
        extensions=["fenced_code", "footnotes", "tables", "sane_lists", "smarty", "codehilite", BlogMdExt()],
    )
