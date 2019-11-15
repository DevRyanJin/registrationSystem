#!/usr/bin/env python

import sys
from os import environ

fields = {}



    queryText = sys.stdin.readlines()
    for keyValuePair in queryText[0].split('&'):
        (key, value) = keyValuePair.split('=')
        fields[key] = value

if fields['creditcard'][0] == '4' and fields['creditcard'][1] == '5' and len(fields['creditcard']) == 16:
    print "Set-Cookie: name={0}".format(fields['name'])
    print "Set-Cookie: creditcard={0}".format(fields['creditcard'])
    print "Content-type:text/html\n\n"
    print ""
    print "<html> \n <body>"
    print "weclome, {0}, to this useless page.".format(fields['name'])
    print "You credit card is {0}. Goodbye.".format(fields['creditcard'])
    print ""
    print '<form action="dereg.cgi">'
    print '<input type="submit" value="De-register" />'
    print '</form>'

    print "</body></html>"
else:
    print "Content-type:text/html"
    print ""
    print "<html> \n <body>"
    print "Hi ...{0}..., ...{1}... is really a credit card number ?_?\r\n.".format(fields['name'],fields['creditcard'])
    print "</body></html>"
