#! /usr/bin/python
# coding: utf-8

import pystache
from os.path import join as OS_join

class PartialsLoader(object):

	def __init__(self):
		self.templateLoader = pystache.loader.Loader(file_encoding='utf-8')
		self.templateDir = "../template"

	def get(self, templateName):
		return self.templateLoader.load_file(OS_join(self.templateDir,templateName))

renderer = pystache.Renderer(
	file_extension = "html",
	search_dirs = "../template/",
	file_encoding = 'utf-8'
)

data = {
	"res_path": u"../res",
	"css_path": u"../style/cc.css",
	"first_name": u"Alexander",
	"last_name": u"Schäfer",
	"company_name": u"HHC Düsseldorf",
	"content": u"""Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.

At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.""",
	"comments": [
		{
			"first_name": u"Kundendienst",
			"last_name": u"",
			"content": u"""Guten Tag,

das können wir so nicht bestätigen!""",
			"answers": [
				{
					"first_name": u"Alexander",
					"last_name": u"Schäfer",
					"content": u"""Antwort1!"""
				},
				{
					"first_name": u"Alexander",
					"last_name": u"Schäfer",
					"content": u"""Antwort 2


Geht auch hier noch weiter :-)"""
				},
				{
					"first_name": u"Alexander",
					"last_name": u"Schäfer",
					"content": u"""Antwort    3"""
				}
			]
		},
		{
			"first_name": u"Kundendienst",
			"last_name": u"",
			"content": u"""Guten Tag,

das können wir so nicht bestätigen!""",
			"answers": [
				{
					"first_name": u"Alexander",
					"last_name": u"Schäfer",
					"content": u"""Fieß!"""
				}
			]
		}
	]
}

def encodeNewLines(string):
	return "<br />".join(string.split("\n"))

def encodeNewLinesFromData(data):
	data["content"] = encodeNewLines(data["content"])
	for comment in data["comments"]:
		comment["content"] = encodeNewLines(comment["content"])
		for answer in comment["answers"]:
			answer["content"] = encodeNewLines(answer["content"])

encodeNewLinesFromData(data)

html = renderer.render_name('facebook_template', data)
f = open("output.html", "w")
f.write(html.encode("UTF-8"))
f.close()
