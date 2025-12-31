from fpdf import FPDF
from datetime import datetime


def gerar_pdf(metricas):
    pdf = FPDF()
    pdf.add_page()

    # TÍTULO
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Relatório de Vendas", ln=True, align="C")

    # DATA
    pdf.ln(5)
    pdf.set_font("Arial", size=10)
    data_atual = datetime.now().strftime("%d/%m/%Y")
    pdf.cell(0, 10, f"Data do relatório: {data_atual}", ln=True, align="C")

    pdf.ln(10)

    # RESUMO
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Resumo Geral", ln=True)

    pdf.ln(3)

    pdf.set_font("Arial", size=11)
    pdf.cell(0, 8, f"Total faturado: R$ {metricas['total_faturado']:.2f}", ln=True)
    pdf.cell(0, 8, f"Média de vendas: R$ {metricas['media']:.2f}", ln=True)
    pdf.cell(0, 8, f"Maior venda: R$ {metricas['maior_venda']:.2f}", ln=True)
    pdf.cell(0, 8, f"Menor venda: R$ {metricas['menor_venda']:.2f}", ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Vendas por mês", ln=True)
    pdf.ln(5)
    pdf.image("vendas_por_mes.png", x=15, w=180)


    pdf.output("relatorio.pdf")
