import io

from PyPDF2 import PdfWriter, PdfReader
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen.canvas import Canvas


# pdfmetrics.registerFont(TTFont('Plex', 'IBMPlexSans-Regular.ttf'))

def create_template(client_name):
    page_width, page_height = A4
    LEFT = 0.1 * page_width
    TOP = 0.9 * page_height
    FONT_SIZE = 16
    FONT = 'Times-Roman'
    text = f'Olá {client_name}, abaixo está seu resultado'
    image_path = 'roda.png'

    canvas = Canvas('resultado.pdf', pagesize=A4)
    canvas.setFont(FONT, FONT_SIZE)
    canvas.drawString(LEFT, TOP, text)

    # Gráfico
    img = ImageReader(image_path)
    img_width, img_height = img.getSize()
    print(f'{img_width} {img_height}')
    aspect = img_height / float(img_width)
    display_width = 400
    display_height = (display_width * aspect)
    canvas.drawImage(image_path,
                     x=(page_width - display_width) / 2,
                     y=(page_height - display_height) * 0.25,
                     width=display_width,
                     height=display_height,
                     mask='auto',
                     preserveAspectRatio=True,
                     anchor='c')
    canvas.save()


def add_image(chart):
    in_pdf_file = 'template.pdf'
    out_pdf_file = 'resultado.pdf'
    chart_file = 'roda.png'
    chart.savefig(chart_file)

    page_width, page_height = A4
    packet = io.BytesIO()
    can = Canvas(packet)

    image_width = 400
    image_height = 400

    x_position = (page_width - image_width) * 0.5
    y_position = page_height * 0.5

    can.drawImage(chart_file,
                  x=x_position,
                  y=y_position,
                  width=image_width,
                  height=image_height,
                  preserveAspectRatio='true',
                  mask='auto',
                  anchor='c')

    can.showPage()
    can.showPage()
    can.showPage()
    can.save()

    packet.seek(0)

    new_pdf = PdfReader(packet)
    existing_pdf = PdfReader(open(in_pdf_file, 'rb'))
    output = PdfWriter()

    for i in range(len(existing_pdf.pages)):
        page = existing_pdf.pages[i]
        page.merge_page(new_pdf.pages[i])
        output.add_page(page)

    outputStream = open(out_pdf_file, 'wb')
    output.write(outputStream)
    outputStream.close()
