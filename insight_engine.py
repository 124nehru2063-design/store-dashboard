import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter

print("\nInsight Engine Running...\n")

# LOAD DATA
df = pd.read_csv("sales_data.csv")

# ANALYSIS
product_sales = df.groupby("product_name")["quantity_sold"].sum().sort_values(ascending=False)
day_sales = df.groupby("day_of_week")["total_amount (Rs.)"].sum().sort_values(ascending=False)

top_products = product_sales.head(5)
bottom_products = product_sales.tail(5)

best_day = day_sales.idxmax()
worst_day = day_sales.idxmin()

best_product = product_sales.idxmax()
worst_product = product_sales.idxmin()

# ---------------- PDF SETUP ----------------
doc = SimpleDocTemplate("store_report.pdf", pagesize=letter)
styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    "TitleStyle",
    parent=styles["Heading1"],
    fontSize=18,
    alignment=1,
    spaceAfter=20
)

section_style = ParagraphStyle(
    "SectionStyle",
    parent=styles["Heading2"],
    fontSize=12,
    textColor=colors.darkblue,
    spaceAfter=10
)

normal = styles["Normal"]

content = []

# TITLE
content.append(Paragraph("STORE ANALYTICS REPORT", title_style))

# TOP PRODUCTS
content.append(Paragraph("Top Products", section_style))
for product, qty in top_products.items():
    content.append(Paragraph(f"{product} : {qty}", normal))

content.append(Spacer(1, 10))

# BOTTOM PRODUCTS
content.append(Paragraph("Bottom Products", section_style))
for product, qty in bottom_products.items():
    content.append(Paragraph(f"{product} : {qty}", normal))

content.append(Spacer(1, 10))

# INSIGHTS
content.append(Paragraph("Insights", section_style))
content.append(Paragraph(f"Best Product: {best_product}", normal))
content.append(Paragraph(f"Worst Product: {worst_product}", normal))
content.append(Paragraph(f"Best Day: {best_day}", normal))
content.append(Paragraph(f"Worst Day: {worst_day}", normal))

content.append(Spacer(1, 10))

# SUMMARY TABLE
content.append(Paragraph("Summary Table", section_style))

table_data = [
    ["Metric", "Value"],
    ["Best Product", best_product],
    ["Worst Product", worst_product],
    ["Best Day", best_day],
    ["Worst Day", worst_day],
]

table = Table(table_data)
table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.grey),
    ("TEXTCOLOR", (0,0), (-1,0), colors.whitesmoke),
    ("GRID", (0,0), (-1,-1), 0.5, colors.black),
    ("PADDING", (0,0), (-1,-1), 6),
]))

content.append(table)

# BUILD PDF
doc.build(content)

print("REPORT GENERATED SUCCESSFULLY ✔")
print("Clean PDF created: store_report.pdf")