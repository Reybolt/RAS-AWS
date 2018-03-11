'''
    Invoice generator based on HTML file and input parameters

    Author: Reynaldo Arteaga
'''

from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML


def generate_invoice(html_file, template_vars):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(html_file)

    html_out = template.render(template_vars)

    HTML(string=html_out).write_pdf("ras_invoice_1.pdf")

if __name__ == '__main__':
    html_file = "invoice_template.html"
    template_vars = {
        'paragraphs':
            ['first paragraph', 'second paragraph', 'third paragraph']
    }
    generate_invoice(html_file, template_vars)
