#!/usr/bin/env python

import sys
from os import environ

print "Content-type:text/html\n\n"
print ""

if environ.has_key("HTTP_COOKIE"):
    temp = environ['HTTP_COOKIE'].split(';')
    cookies = {}
    for cookie in temp:
        (key, value) = cookie.split('=', 1)
        key = key.strip()
        cookies[key] = value.strip()
    if cookies.has_key('name') and cookies.has_key('creditcard'):
        if cookies['name'] != '' and cookies['creditcard'] != '':
            print '<META HTTP-EQUIV="REFRESH" CONTENT="0;URL=verify.cgi">'
        else:
            print '<head>'
            print '<META HTTP-EQUIV="REFRESH" CONTENT="0;URL=../regpage.html">'
            print '</head>'
    else:
        print '<head>'
        print '<META HTTP-EQUIV="REFRESH" CONTENT="0;URL=../regpage.html">'
        print '</head>'

else:
    print '<head>'
    print '<META HTTP-EQUIV="REFRESH" CONTENT="0;URL=../regpage.html">'
    print '</head>'

print "<html> \n <body>"
print "</body></html>"