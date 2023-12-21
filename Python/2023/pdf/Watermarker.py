import PyPDF2
import os
import sys


def add_watermark(input_filename, watermark_filename, output_filename):
    input_pdf = PyPDF2.PdfFileReader(input_filename)
    watermark_page = PyPDF2.PdfFileReader(watermark_filename).getPage(0)
    output_pdf = PyPDF2.PdfFileWriter()

    for i in range(input_pdf.getNumPages()):
        page = input_pdf.getPage(i)
        page.mergePage(watermark_page)
        output_pdf.addPage(page)

    with open(output_filename, "wb") as output_file:
        output_pdf.write(output_file)


def remove_watermark(input_filename, output_filename):
    input_pdf = PyPDF2.PdfFileReader(input_filename)
    output_pdf = PyPDF2.PdfFileWriter()

    for i in range(input_pdf.getNumPages()):
        page = input_pdf.getPage(i)
        page.mergePage(PyPDF2.pdf.PageObject.createBlankPage(
            width=page.mediaBox.getWidth(), height=page.mediaBox.getHeight()))
        output_pdf.addPage(page)

    with open(output_filename, "wb") as output_file:
        output_pdf.write(output_file)


def remove_file(file_path):
    os.remove(file_path)


if len(sys.argv) < 3:
    print("Usage: python pdf_watermark.py <input_file1> <input_file2> ... <watermark>")
    sys.exit(1)

watermark = sys.argv[-1]
files = sys.argv[1:-1]

try:
    for file in files:
        filename = os.path.basename(file)
        output_filename = os.path.join(
            os.path.dirname(file), f"watermarked_{filename}")

        print(f"Adding watermark to {filename}...\n")
        add_watermark(file, watermark, output_filename)
        print(f"Watermark added to {
              filename} and saved to {output_filename}\n")

    last_step = input("Do you want to remove watermark files? (y/n): ")
    if last_step.lower() == "y":
        print("Removing watermark file...\n")
        remove_file(watermark)
        print("Watermark file removed successfully!")

except Exception as e:
    print(f"An error occurred: {e}")
