import PyPDF2
import os
import sys


def merge_pdfs(files, output_filename):
    merger = PyPDF2.PdfFileMerger()
    for file in files:
        merger.append(file)

    with open(output_filename, "wb") as merged_file:
        merger.write(merged_file)


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


def remove_files(files):
    for file in files:
        os.remove(file)


def remove_watermark(watermark_filename):
    os.remove(watermark_filename)


if len(sys.argv) < 3:
    print("Usage: python pdf.py <file1> <file2> ... <watermark>")
    sys.exit(1)

watermark = sys.argv[-1]
files = sys.argv[1:-1]

try:
    print("Merging files...\n")
    merge_pdfs(files, "temp_merged.pdf")
    print("Merging done\n")

    print("Adding watermark...\n")
    add_watermark("temp_merged.pdf", watermark, "final_merged.pdf")
    print("Adding watermark done\n")

    last_step = input("Do you want to remove files? (y/n): ")
    if last_step.lower() == "y":
        print("Removing files...\n")
        remove_files(files)
        print("Files removed successfully!")

    second_last_step = input("Do you want to remove watermark? (y/n): ")
    if second_last_step.lower() == "y":
        print("Removing watermark file...\n")
        remove_watermark(watermark)
        print("Watermark file removed successfully!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if os.path.exists("temp_merged.pdf"):
        os.remove("temp_merged.pdf")
