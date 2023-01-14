# Create pdf file with headings and pages form csv
# Iterate over ranges
# Create a nested for loop

from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0) # In order to make subtext work

df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font('Times', style='B', size=24)
    pdf.set_text_color(100, 100, 100) # = grey (RGB)
    pdf.cell(w=0, h=24, txt=row['Topic'], align='L', ln=1, border=0)
    for y in range(27, 298, 10):
        pdf.line(10, y, 200, y)


    # Set the footer
    pdf.ln(250) # Add 278 breaklines on each page - to the btm of page.
    pdf.set_font('Times', style='I', size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row['Topic'], align='R', ln=1, border =0)
    
    
    for i in range(row['Pages'] -1):
        pdf.add_page()
        # Set the footer
        pdf.ln(273) # Add 278 breaklines on each page - to the btm of page.
        pdf.set_font('Times', style='I', size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row['Topic'], align='R', ln=1, border =0)
        for y in range(16, 298, 10):
            pdf.line(10, y, 200, y)

       

    



pdf.output('output.pdf')
