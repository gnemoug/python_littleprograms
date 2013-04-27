#!/usr/bin/python
#-*-coding:utf-8-*-

import textwrap
from textwrap_example import sample_text

dedented_text = textwrap.dedent(sample_text).strip()
for width in [ 20, 60, 80 ]:
        print
        print '%d Columns:\n' % width
        print textwrap.fill(dedented_text, width=width)
