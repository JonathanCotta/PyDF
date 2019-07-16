from pdfrw import PdfReader, PdfWriter, PageMerge

import sys
import os
import time


def pdfMerge(files_folder):
    files = []
    pdf_writer = PdfWriter()

    for root, directories, files in os.walk(files_folder):
        for file in files:
            if ('.pdf' in file and 'sample' in file):
                pdf_writer.addpages(
                    PdfReader("%s/%s" % (files_folder, file)).pages
                )

    pdf_writer.write("%s/mergedPDF.pdf" % files_folder)


def pdfWaterMark(files_folder):
    water_mark = PageMerge().add(
        PdfReader('%s/wtmrk.pdf' % files_folder).pages[0]
    )[0]

    trailer = PdfReader('%s/mergedPDF.pdf' % files_folder)

    for page in trailer.pages:
        PageMerge(page).add(water_mark, prepend='-u').render()

    PdfWriter("%s/resultPDF.pdf" % (files_folder), trailer=trailer).write()


def cleanTempFiles(files_folder):
    os.remove("%s/mergedPDF.pdf" % files_folder)


def main():
    start = time.time()

    files_folder = sys.argv[1]

    pdfMerge(files_folder)
    pdfWaterMark(files_folder)
    cleanTempFiles(files_folder)

    end = time.time()
    print(end - start)

main()
