
from xhtml2pdf import pisa
import os
import sys
from pathlib import Path
import shutil
try:
    from weasyprint import HTML, CSS
    from weasyprint.text.fonts import FontConfiguration
except:
    pass

sys.path.append(".")
sys.path.append("..")

#os.chdir("testrender/data/source")
os.chdir("manual_test")

dir_temp = "../test_working/"
path_dir_temp = Path(dir_temp)
if path_dir_temp.is_dir():
    shutil.rmtree(path_dir_temp)
path_dir_temp.mkdir()

def convert_weasy_print(name, filename):
    from xhtml2pdf.default import DEFAULT_CSS

    font_config = FontConfiguration()
    css = CSS(string=DEFAULT_CSS, font_config=font_config)
    HTML(name, encoding="utf-8").write_pdf(dir_temp + "weasy-" + filename, stylesheets=[css])


def convert_to_pdf_file(name, filename, weasyprint=False, html=False):
    with open(dir_temp + filename, "wb") as arch:
        with open(name, "r", encoding="utf-8", errors="ignore") as source:
            pdf = pisa.CreatePDF(source, arch, show_error_as_pdf=True)
            if weasyprint:
                convert_weasy_print(name, filename)
            if html:
                with open(dir_temp+filename+".html", "w") as writer:
                    source.seek(0)
                    writer.write(source.read())

def testing_pdfs(weasyprint=False, html=False):

    dir = "."

    for path, dirc, files in os.walk(dir):
        for name in files:
            if name.endswith(".html"):
                filename = name.replace(".html", ".pdf")
                convert_to_pdf_file(name, filename, weasyprint=weasyprint, html=html)


if __name__=="__main__":
    pisa.showLogging()
    #testing_pdfs(weasyprint=True)
    #convert_to_pdf_file("test-unicode-japanese.html", "test-unicode-japanese.pdf")
    #convert_to_pdf_file("test-unicode-thaana.html", "test-unicode-thaana.pdf")
    #convert_to_pdf_file("test-css-fontface.html", "test-css-fontface.pdf")
    #convert_to_pdf_file("test-bidirectional-text.html", "test-bidirectional-text.pdf")
    #convert_to_pdf_file("test-font.html", "test-font.pdf")
    #convert_to_pdf_file("test_rtl.html", "test_rtl.pdf")
    #convert_to_pdf_file("arabic_font_rendering.html", "arabic_font_rendering.pdf")
    #convert_to_pdf_file("ttf_file_metadata_same_name.html",
    #                    "ttf_file_metadata_same_name.pdf", weasyprint=True)

    convert_to_pdf_file("test_form_input.html", "test_form_input.pdf")