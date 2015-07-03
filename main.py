# coding: utf-8

import ui
from sys import exit
	

class iGitHub(ui.View):
	def side_bar_menu(self):
		self["label1"].text="Hiya!"

	def did_load(self):
		self["side_bar"].action=self.side_bar_menu

gui = ui.load_view("iPhone_main")
gui.present("fullscreen")
