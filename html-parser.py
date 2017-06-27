# June 25 2017
# Andrew Xia
# this program will parse the Evernote HTML document

FOLDER = "/home/andrew/Documents/Evernote_170625/"
FILE = "16.html"
# CONTENT = '<html><head><title>Test</title></head><body><h1>Parse me!</h1></body></html>'
CONTENT = ""

from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
  def __init__(self, folder, file = False):
    #init the base class
    HTMLParser.__init__(self)
    #init function
    self.folder = folder
    self.file = file
    self.content = "" # no html content yet
    self.debug = False # do not debug

  def load_content(self):
    if file == False:
        raise "please define a file to look at"
    f = open(self.folder + "/" + self.file)
    for line in f:
      # print line, #print the files
      self.content += line
    if self.debug: print "load_content: done"

  def handle_starttag(self, tag, attrs):
    if self.debug: print "Encountered a start tag:", tag

  def handle_endtag(self, tag):
    if self.debug: print "Encountered an end tag :", tag

  def handle_data(self, data):
    if self.debug: print "Encountered some data  :", data

  def process(self,data = ""):
    """ Desc: Read in stuff
        Args: 
        Returns:
    """

    if data == "":
      data = self.content        
    HTMLParser.feed(self,data)


if __name__ == "__main__":
	# instantiate the parser and feed it some HTML
  parser = MyHTMLParser(FOLDER,FILE)
  parser.debug = True
  parser.load_content()

  parser.process() # read in file