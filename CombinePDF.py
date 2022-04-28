from fpdf import FPDF
import os


pdf = FPDF()
pdf.set_auto_page_break(0)

# use a folder that you created (here it's imgs)
img_list = [x for x in os.listdir('pngs.pdf')] 
# add new pages with the image 
for img in img_list:
    pdf.add_page()
    pdf.image(img)

# save the output file
pdf.output("Images.pdf")
print("Adding all your images into a pdf file")
print("Images pdf is created and saved it into the following path folder:\n",
      os.getcwd())
