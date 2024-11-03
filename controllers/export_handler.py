
# export_handler.py - Lida com exportação de documentação gerada

from fpdf import FPDF  # Exemplo para exportar em PDF

def export_to_pdf(documentation, filename="documentation.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, documentation)
    pdf.output(filename)

def export_to_markdown(documentation, filename="documentation.md"):
    with open(filename, "w") as file:
        file.write(documentation)
