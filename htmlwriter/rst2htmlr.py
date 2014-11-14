#!/usr/bin/env python

# Author: IGARASHI Masanao <syoux2@gmail.com>
# Copyright: This module has been placed in the public domain.

"""
A minimal front end to Another Docutils Publisher, producing HTML.
"""

try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except:
    pass
import htmlwriter

def main():
    from docutils.core import publish_cmdline, default_description

    description = ('Generates HTML documents from standalone reStructuredText '
                   'sources.  ' + default_description)

    publish_cmdline(writer=htmlwriter.Writer(), writer_name='html',
                    description=description)

if __name__ == '__main__':
    main()
