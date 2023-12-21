import PyPDF2
import os
import sys


def merge_pdfs(files, output_filename):
    merger = PyPDF2.PdfFileMerger()
    for file in files:
        merger.append(file)

    with open(output_filename, "wb") as merged_file:
        merger.write(merged_file)


def remove_files(files):
    for file in files:
        os.remove(file)


if len(sys.argv) < 3:
    print("Usage: python pdf_merge.py <input_file1> <input_file2> ...")
    sys.exit(1)

files = sys.argv[1:]

try:
    output_filename = "merged_output.pdf"

    print("Merging files...\n")
    merge_pdfs(files, output_filename)
    print("Merging done\n")

    last_step = input("Do you want to remove merged files? (y/n): ")
    if last_step.lower() == "y":
        print("Removing merged files...\n")
        remove_files(files)
        print("Merged files removed successfully!")

except Exception as e:
    print(f"An error occurred: {e}")
