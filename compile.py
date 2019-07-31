import sys
sys.path.append("/home/anirudh1200/python/compile")

import util.c as c
import util.cpp as cpp
import util.java as java
import util.python3 as python3
import os

dir = './tmpcode/'

def init():
	try:
		os.mkdir(dir)
	except Exception as e:
		print(e)

def compile(code, source, input, fn, timeout=5):
	if code==1:
		c.compile(source, input, fn, timeout)
	elif code==2:
		cpp.compile(source, input, fn, timeout)
	elif code==3:
		java.compile(source, input, fn, timeout)
	elif code==4:
		python3.compile(source, input, fn, timeout)
	else:
		fn({'stdout':None, 'stderr': 'Invalid code number'})