# -*- coding: utf-8 -*-
"""Add language to highlighted code.

"""

from pygments import highlight as pygments_highlight
from pygments.formatters.html import HtmlFormatter
from pyquery import PyQuery as pq
from markdown import Extension
from markdown.extensions import codehilite
from lxml.html import tostring as html2str


class CodeHiliteLangExtension(Extension):

    def extendMarkdown(self, md, md_globals):
        md.registerExtension(self)

        def new_codehilite_highlight(src, lexer, formatter):
            lang = lexer.name.lower().replace(' ', '-')
            result = pygments_highlight(src, lexer, formatter)
            if isinstance(formatter, HtmlFormatter):
                d = pq(result)
                d.add_class('language-{}'.format(lang))
                result = html2str(d[0], encoding='unicode')
            return result

        codehilite.highlight = new_codehilite_highlight


def makeExtension(**kwargs):
    return CodeHiliteLangExtension(**kwargs)
