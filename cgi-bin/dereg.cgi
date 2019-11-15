#!/usr/bin/env python

import sys
from os import environ

if environ.has_key("HTTP_COOKIE"):
    print "Set-Cookie: name=''; expires=Thu, 01 Jan 1970 00:00:00 GMT"
    print "Set-Cookie: creditcard=''; expires=Thu, 01 Jan 1970 00:00:00 GMT"
    print "Content-type:text/html\n\n"
    print ""

    print '<head>'
    print '<META HTTP-EQUIV="REFRESH" CONTENT="0;URL=../regpage.html">'
    print '</head>'
    print "<html> \n <body>"
    print "</body></html>"
else:
    print "Content-type:text/html\n\n"
    print ""

    print 'no cookies are set">'
    print "<html> \n <body>"
    print "</body></html>"

