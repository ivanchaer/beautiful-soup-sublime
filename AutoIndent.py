import sublime, sublime_plugin, re

from BeautifulSoup import BeautifulSoup



class AutoindentCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    soup = self.view.substr(sublime.Region(0, min(self.view.size(), 2**14)))
    
    reg = sublime.Region(0, self.view.size())

    soup = BeautifulSoup(soup.encode('raw_unicode_escape'))

    soup = soup.prettify()

    self.view.replace(edit, reg, soup.decode('utf-8'))
