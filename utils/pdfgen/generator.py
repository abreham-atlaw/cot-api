import typing
from abc import ABC, abstractmethod

from jinja2 import Environment
from weasyprint import HTML



class PDFGenerator:

	def __init__(self):
		self.__environment = Environment()

	def _load_template(self, path) -> str:
		with open(path, "r") as file:
			return file.read()

	def _render_html(self, template: str, context: typing.Dict) -> str:
		jinja_template = self.__environment.from_string(source=template)
		return jinja_template.render(context)

	def __generate_pdf(self, html, outpath):
		html = HTML(string=html)
		html.write_pdf(outpath)

	def generate(self, template_path: str, context: typing.Dict, outpath: str):
		template = self._load_template(template_path)
		html = self._render_html(template, context)
		self.__generate_pdf(html, outpath)