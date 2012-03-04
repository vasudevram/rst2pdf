#!/usr/bin/env python
# -*- coding: utf-8 -*-

#$HeadURL: https://rst2pdf.googlecode.com/svn/trunk/rst2pdf/tests/parselogs.py $
#$LastChangedDate: 2010-03-07 21:25:16 -0600 (Sun, 07 Mar 2010) $
#$LastChangedRevision: 1730 $

# See LICENSE.txt for licensing terms

'''
Parses log files in output directory generated by autotest.py
into stupid HTML output.
'''

import os, sys

from parselogs import getcategories

def dumpinfo():
    ifiles = set(os.listdir('input'))
    mydict = getcategories()
    if not mydict:
        print '\nNo log files found'
    exts = '.txt .style .cli'.split()
    for name, values in sorted(mydict.iteritems()):
        print '<h2>'
        print '\nCategory "%s"\n        (%d tests)\n' % (name, len(values))
        print '</h2>'
        print '<table>'
        href = 'http://code.google.com/p/rst2pdf/issues/detail?id='
        for testname, checksum in sorted(values):
            if os.path.exists(os.path.join('input',testname+'.ignore')):
                continue

            print '<tr>'
            print '<td>'
            if testname.startswith('test_issue_'):
                testnum = testname.split('_')[2]
                print '<a href="%s%s">%s</a>' % (href, testnum, testname)
            else:
                print testname
            print '</td>'
            print '<td>'
            print '<a href="output/%s.pdf">%s</a>' % (testname, checksum)
            print '</td>'
            for fname in exts:
                print '<td>'
                fname = testname + fname
                if fname in ifiles:
                    print '<a href="input/%s">%s</a>' % (fname, fname)
                print '</td>'

            print '</tr>'
        print '</table>'
    print

if __name__ == '__main__':
    print '<html><body>'
    dumpinfo()
    print '<pre>'
    print '\n\n'.join(10*'.')  # A bit of separation from end for scrolling...
    print '</pre>'
    print '</body></html>'
