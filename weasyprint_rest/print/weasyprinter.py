import os

from weasyprint import HTML

from .template import Template


class WeasyPrinter:

    def __init__(self, html=None, url=None, template=None):
        self.html = html
        self.url = url
        self.template = template if template is not None else Template()

    def write(self):
        html = HTML(file_obj=self.html, encoding="utf-8", url_fetcher=self.template.url_fetcher, base_url=os.getcwd())
        font_config = self.template.get_font_config()
        styles = self.template.get_styles() if self.template is not None else []

        return html.write_pdf(stylesheets=styles, image_cache=None, font_config=font_config)

    def close(self):
        pass
