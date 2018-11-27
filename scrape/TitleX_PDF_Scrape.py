# ----------------------------------------------------------
# Title: Scrape of Title X members from PDF 
# Author: Ryan Gan
# Date Created: 2018-11-20
# ----------------------------------------------------------

# Importing read_pdf function from the tabula library
from tabula import read_pdf

# define file pathy
pdf_file = ("Title-X-FamiTitle-X-Family" + 
            "-Planning-Directory-September2018.pdf")
print(pdf_file)
titleX_pdf = read_pdf()