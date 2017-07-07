# June 27 2017
# Andrew Xia
# main program (for testing stuff)

import sys
sys.path.insert(0, 'tomd/')
import tomd
import re

FOLDER = "/home/andrew/Documents/Evernote_170625/Journal/Ch 08"
FILE = "[over]analysis.html"
CONTENT = ""


f = open(FOLDER + "/" + FILE)
for line in f:
  CONTENT += line

converter = tomd.Tomd(CONTENT,FOLDER,FILE)
converter.export('/home/andrew/Documents/Evernote_170625/Ch08_md')

# x = converter.markdown

# file = open('tmp.txt','w')
# file.write(x)
# file.close()

