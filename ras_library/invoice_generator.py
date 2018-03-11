'''
    Invoice generator based on HTML file and input parameters

    Author: Reynaldo Arteaga
    Date: March 2018
'''

from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML


def generate_invoice(html_file, template_vars, pdf_file):
    '''
        Arguments:
            html_file (str):        The name (incl. extension) of the HTML file
            template_vars (dict):   All parameters used in the HTML render
            pdf_file (str):         The name (incl. extension) of the pdf file
        Returns:
            success (bool):         True or false whether the pdf was generated

    '''
    success = False
    try:
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template(html_file)

        html_out = template.render(template_vars)

        HTML(string=html_out).write_pdf(pdf_file)

        success = True
        print('PDF Generated {}'.format(pdf_file))

    except Exception as error:
        print(
            'PDF Generation failed for HTML: {}, Variables: {} and PDF: {}. '
            'Error: {}'.format(html_file, template_vars, pdf_file, error))
    
    return success



if __name__ == '__main__':
    html_file = "invoice_template.html"
    template_vars = {
        'bill_id': 1,
        'date_created': '2018-3-11',
        'due_date': '2018-3-11',
        'labour_cost': 30.0,
        'parts_cost': 20.50,
        'total_before_tax': 50.50,
        'tax_percentage': 13.0,
        'tax_total': 6.565,
        'total_after_tax': 57.065,
        'description': 'We changed the oil',
        'parts_replaced': ['oil', 'windshield fluid'],
        'customer_id': 14,
        'payment_status': 'unpaid',
    }
    pdf_file = "ras_invoice_1.pdf"
    generate_invoice(html_file, template_vars, pdf_file)
