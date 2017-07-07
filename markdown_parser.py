# July 7 2017
# Andrew Xia
# this program will read in a markdown file and be able to do some stuff

# import pandas as pd
import matplotlib.pyplot as plt

import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

class MarkdownParser:
  def __init__(self,folder,file,header="",content="",options=None):
    self.file = file
    assert (self.file[-3:]==".md"),"file must be markdown format!"
    self.folder = folder
    self.header = header
    self.content = content
    self.options = options # dictionary of options, to implement later

  def load(self,file='',folder=''):
    # this function loads the markdown 
    if file == '': file = self.file
    assert (self.file[-3:]==".md"),"file must be markdown format!"
    if folder == '': folder = self.folder
    self.content = ''
    f = open(folder + "/" + file)
    for line in f:
      if "+++" in line:  #everything above goes in the header
        self.header = self.content
        self.content = ""
      else:
        self.content += line
    f.close()

  def word_freq(self,top=100):
    # count frequency of words in a document
    # top is the top frequency that we want to see
    wordList = self.content.split()
    # print "num words:", len(wordList)
    self.wordDict = {}
    for word in wordList:
      if word in self.wordDict:
        self.wordDict[word] += 1
      else:
        self.wordDict[word] = 1 #count freq
    # print self.wordDict

    # plt.bar(range(len(self.wordDict)), self.wordDict.values(), align='center')
    # plt.xticks(range(len(self.wordDict)), self.wordDict.keys())
    # plt.show()

    i = 0
    xplt = []
    yplt = []
    for w in sorted(self.wordDict, key=self.wordDict.get,reverse=True):
      # print w, self.wordDict[w]
      xplt.append(w) # add to word
      yplt.append(self.wordDict[w]) #add to freq
      i+=1 #count
      if i > top:
        break

    plt.bar(range(len(yplt)), yplt, align='center')
    plt.xticks(range(len(xplt)), xplt)
    plt.show()



if __name__ == "__main__":
  FOLDER = '/home/andrew/Documents/Evernote_170625/Ch08_md'
  FILE = "[over]analysis.md"
  mdp = MarkdownParser(FOLDER,FILE)
  mdp.load()
  mdp.word_freq()
  # print repr(mdp.content)
