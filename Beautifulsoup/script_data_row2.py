from bs4 import BeautifulSoup

html_file = open("data_in_table_2.html", mode="r", encoding="utf-8")
soup = BeautifulSoup(html_file, "html.parser")
table = soup.find_all("table")[1]
table_rows = table.find_all("tr")

dadosCursos = []

for linha in table_rows:
    colunas = linha.find_all("td")
    if len(colunas) > 0:
        nomeCurso = colunas[0].text
        interesse = colunas[1].text
        dicCurso = {"nome": nomeCurso, "interesse": interesse}
        dadosCursos.append(dicCurso)

print(dadosCursos)