import sublime, sublime_plugin, re

import html5lib

from bs4 import BeautifulSoup



class AutoindentCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    soup = self.view.substr(sublime.Region(0, min(self.view.size(), 2**14)))
    
    reg = sublime.Region(0, self.view.size())

    soup = BeautifulSoup(soup.encode('raw_unicode_escape'), features="html5lib")

    soup = soup.prettify()

    #print soup.encode('utf-8')

    self.view.replace(edit, reg, soup)
