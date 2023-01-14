# Create pdf file with headings and pages form csv

from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')

df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font('Times', style='B', size=24)
    pdf.set_text_color(100, 100, 100) # = grey (RGB)
    pdf.cell(w=0, h=24, txt=row['Topic'], align='L', ln=1, border=0)
    pdf.line(10, 28, 200, 28) # x1, y1, x2, y2)

    for i in range(row['Pages'] -1):
        pdf.add_page()


pdf.output('output.pdf')
