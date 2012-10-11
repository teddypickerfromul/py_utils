#!/usr/bin/env 
# -*- coding: utf-8 -*-

import os, re, codecs
import sys

try:
	import itertools
	import argparse
	from pysvg.filter import *
	from pysvg.gradient import *
	from pysvg.linking import *
	from pysvg.script import *
	from pysvg.shape import *
	from pysvg.structure import *
	from pysvg.style import *
	from pysvg.text import *
	from pysvg.builders import *
except:
	print 'You need to install pysvg, itertools, argparse packages.'
	sys.exit()


inf = "./points.txt"
outf = "./result.svg"

def parse(line):
	return map(lambda el: el.strip(), re.split('\s*,\s*|\s*;\s*', line))

def process():

	argparser = argparse.ArgumentParser()
	argparser.add_argument('--input', action="store", dest="input")
	argparser.add_argument('--output', action="store", dest="output")
	options = argparser.parse_args()
	if options.input != None and options.output != None:
		if os.path.exists(options.input):
			s=svg("graph")
			myStyle = StyleBuilder()
			myStyle.setStrokeWidth(1)
			myStyle.setStroke('black')
			f = codecs.open(filename,"r","utf-8")
			for lines in iter(f.readline, ""):
				coords = parse(lines)
				l = line(2*int(coords[0]), 2*int(coords[1]), 2*int(coords[2]), 2*int(coords[3]))
				l.set_style(myStyle.getStyle())
				s.addElement(l)

			myStyle1 = StyleBuilder()
			myStyle1.setStrokeWidth(5)
			myStyle1.setStroke('red')
			p1=circle(80, 200, 5)
			p1.set_style(myStyle1.getStyle())
			s.addElement(p1)
			p2=circle(80, 240, 2)
			p2.set_style(myStyle1.getStyle())
			s.addElement(p2)
			p3=circle(80, 80, 2)
			p3.set_style(myStyle1.getStyle())
			s.addElement(p3)
			if os.path.exists(options.output):
				s.save(options.output)
			else:
				print ("cannot save to desired location")

		else:
			print "give me right input file"

	else:
		print ("give me some params")


if __name__ == '__main__':
	process()