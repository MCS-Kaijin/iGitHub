# coding: utf-8

import ui
import urllib
import zipfile

mb_isopen = False

def getrepo(sender):
	fmt = 'https://codeload.github.com/{usr}/{rep}/zip/master'
	url = fmt.format(**sender.superview.__dict__)
	filename, headers = urllib.urlretrieve(url)
	with zipfile.ZipFile(filename) as zip_file:
		zip_file.extractall()

def show_menu_bar(sender):
	global mb_isopen
	mb = sender.superview.superview["view2"]
	sb = mb["sb"]
	def animation():
		if not mb_isopen:
			mb.frame=(0,65.5,175,568)
			sb.frame=(0,0,175,568)
		else:
			mb.frame=(0,65.5,20,568)
			sb.frame=(0,0,20,568)
	ui.animate(animation, duration=1.0)
	if not mb_isopen:
		mb.background_color=(1,1,1,1)
		mb.border_width=1
		mb.border_color=(0,0,0,1)
		sb.alpha=1
		mb_isopen=True
	else:
		mb.background_color=(0,0,0,0)
		mb.border_width=0
		mb.border_color=(0,0,0,0)
		sb.alpha=0
		mb_isopen=False

class side_bar(ui.View):
	def did_load(self):
		self["sb"].alpha=0

class iGitHub(ui.View):
	def did_load(self):
		self.usr = "MCS-Kaijin"   # GitHub user
		self.rep = "iGitHub"      # GitHub repo
		"""There will be a way to change these in-app later...  """
		self["mb"].action=show_menu_bar

gui = ui.load_view("iPhone_main")
gui.present("fullscreen", hide_title_bar=True)
