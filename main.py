from PyPDF4 import PdfFileMerger
import os

merger = PdfFileMerger()

for items in os.listdir():
    if items.endswith('.pdf'):
        merger.append(items)

merger.write("output/Final.pdf")
merger.close()
