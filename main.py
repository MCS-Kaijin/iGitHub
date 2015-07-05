# coding: utf-8

import ui
import urllib
import zipfile

mb_isopen = False

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


# 'Get Repository' options screen
lbl1 = ui.Label()
lbl1.name='label1'
lbl1.text='User: '
lbl1.frame=(6,6,60,20)
usrt = ui.TextField()
usrt.frame = (66, 6, 150, 20)
usrt.name = 'usr'
usrt.autocapitalization_type=False
usrt.autocorrection_type=False
lbl2=ui.Label()
lbl2.frame = (6,26,60,20)
lbl2.text='Repo: '
lbl2.name='label2'
psdt = ui.TextField()
psdt.name='rep'
psdt.frame=(66,26,150,20)
psdt.autocapitalization_type=False
psdt.autocorrection_type=False
btn = ui.Button()
btn.name = 'getrepo'
btn.title = 'Get Repo'
btn.frame = (6,52,75,20)
btn.background_color='green'
btn.tint_color='white'


class side_bar(ui.View):
	def did_load(self):
		self["sb"].alpha=0

class iGitHub(ui.View):
	def did_load(self):
		self["mb"].action=show_menu_bar

gui = ui.load_view('iPhone_main')

def getrepo(sender):
	usr = sender.superview["usr"].text
	rep = sender.superview["rep"].text
	url = 'https://codeload.github.com/{}/{}/zip/master'.format(usr, rep)
	filename, headers = urllib.urlretrieve(url)
	with zipfile.ZipFile(filename) as zip_file:
		zip_file.extractall()

def sb_clicked(sender):
	button = sender.items[sender.selected_row]['title']
	scroll = gui["scrollview1"]
	show_menu_bar(gui["view1"]["mb"])
	if(button == 'Get Repository'):
		scroll.add_subview(lbl1)
		scroll.add_subview(usrt)
		scroll.add_subview(lbl2)
		scroll.add_subview(psdt)
		scroll.add_subview(btn)
		gui["scrollview1"]["getrepo"].action=getrepo

gui["view2"]["sb"].delegate.action=sb_clicked

gui.present("fullscreen", hide_title_bar=True)
