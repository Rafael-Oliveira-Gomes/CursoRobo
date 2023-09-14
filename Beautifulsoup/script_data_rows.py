from bs4 import BeautifulSoup

html_file = open("data_in_table.html", mode="r", encoding="utf-8")
soup = BeautifulSoup(html_file, "html.parser")
table = soup.find(id = "main_table")
table_rows = table.find_all("tr")

print(table_rows)

dadosAlunos = []

for linha in table_rows:
    colunas = linha.find_all("td")
    if len(colunas) > 0:
        codigoEstudante = colunas[0].text
        nomeEstudante = colunas[1].text
        notaEstudante = colunas[2].text
        dictAluno = {
            "codigo": codigoEstudante,
            "nome": nomeEstudante,
            "nota": notaEstudante
        }
        dadosAlunos.append(dictAluno)
        print(f"{codigoEstudante} - {nomeEstudante} - {notaEstudante}")
print(dadosAlunos)