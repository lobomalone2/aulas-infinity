from fpdf import FPDF


pdf = FPDF()

pdf.add_page()

pdf.set_font("Arial",size=12)

pdf.cell(200,10,txt="pdfdomalone",ln=True,align='C')

pdf.ln(20)

texto = """

Era uma vez, em uma pequena vila cercada por montanhas verdes e rios cristalinos, um jovem chamado Lucas. 
Ele sempre sonhou em explorar o mundo além das colinas que cercavam sua casa. Um dia, ele encontrou um mapa antigo escondido no sótão de sua avó. 
O mapa prometia aventuras e tesouros escondidos. 

Com coragem e determinação, Lucas decidiu seguir o mapa, enfrentando desafios e fazendo novos amigos ao longo do caminho. 
Cada passo o levava mais perto de descobrir não apenas os segredos do mapa, mas também a verdadeira essência da coragem e da amizade.


"""

pdf.multi_cell(0,10,texto)
pdf.output("PDFmalone.pdf")

print('PDF gerado com sucesso!')