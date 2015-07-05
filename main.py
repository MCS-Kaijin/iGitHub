# coding: utf-8

import ui
import urllib
import zipfile

def getrepo(sender):
    fmt = 'https://codeload.github.com/{usr}/{rep}/zip/master'
    url = fmt.format(**sender.superview.__dict__)
    filename, headers = urllib.urlretrieve(url)
    with zipfile.ZipFile(filename) as zip_file:
        zip_file.extractall()

class iGitHub(ui.View):
    def did_load(self):
        self.usr = "MCS-Kaijin"   # GitHub user
        self.rep = "iGitHub"      # GitHub repo
        """There will be a way to change these in-app later...  """
        self["sb"].action=getrepo

gui = ui.load_view()  # ("iPhone_main")
gui.present("fullscreen", hide_title_bar=True)
