# coding: utf-8

import ui
import tempfile
import zipfile
import urllib
from console import alert

def getrepo(sender):
	user=sender.superview.usr
	repo=sender.superview.rep
	with tempfile.NamedTemporaryFile(mode='w+b', suffix='.zip') as f:
		urllib.urlretrieve('https://codeload.github.com/'+user+'/'+repo+'/zip/master',f.name)
		z=zipfile.ZipFile(f)
		z.extractall()

class iGitHub(ui.View):
	def did_load(self):
		
		"""							"""
		self.usr="MCS-Kaijin"		# GitHub user
		self.rep="iGitHub"		# GitHub repo
		"""There will be a way to change these in-app later...	"""
		
		self["sb"].action=getrepo

gui = ui.load_view("iPhone_main")
gui.present("fullscreen", hide_title_bar=True)
