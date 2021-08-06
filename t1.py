print("--- Conversor para xml ---")

arquivoXml = "0001_create_table_tipo_vinculo.txt".strip()
#nomeDoNovoArquivo = str(input('Nome do novo arquivo: '))

try:
    arquivo = open(arquivoXml, "r")
except:
    print("Falha ao abrir o arquivo, tente novamente!")

listaDeValores = []
listaDeParametros = []
contador = 0

for line in arquivo:
    contador += 1
    removendoValuesInicio = line.rfind('VALUES')
    removendoValuesFinal = removendoValuesInicio + 6

    valores = line[removendoValuesFinal:]
    parametros = line[:removendoValuesInicio]

    removendoInserInto = parametros.rfind('INSERT')
    parametrosSemInsert = parametros[11:]

    procurandoInto = parametros.rfind('INTO')
    procurandoParenteses = parametros.rfind('(')
    nomeDaTabela = parametros[procurandoInto + 5 :procurandoParenteses]

    listaDeValores.append(valores)
    listaDeParametros.append(parametrosSemInsert)

    for palavras in listaDeValores:
        removendoParenteses1 = palavras.replace('(', " ")
        removendoParenteses2 = removendoParenteses1.replace(')', " ")
        removendoPontosEVirgulas = removendoParenteses2.replace(';', " ")
        removendoVirgulas = removendoPontosEVirgulas.replace(',', " ")
    
    for palavras in listaDeParametros:
        removendoParenteses1 = palavras.replace('(', "")
        removendoParenteses2 = removendoParenteses1.replace(')', "")
        removendoPontosEVirgulas = removendoParenteses2.replace(';', "")

listaDeValores = listaDeValores[0].split()
listaDeParametros = listaDeParametros[0].split()
print(listaDeValores)

linha1 =f'<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n'
linha2 =f'<databaseChangeLog xmlns="http://www.liquibase.org/xml/ns/dbchangelog" xmlns:ext="http://www.liquibase.org/xml/ns/dbchangelog-ext" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog-ext http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-ext.xsd http://www.liquibase.org/xml/ns/dbchangelog http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-3.1.xsd">\n'
linha3 =f'<property name="now" value="now()" dbms="mysql"/>\n'
for palavras in range(contador): 
    linha4 =f'<changeSet author="pacto" id="{arquivoXml[:4]}">\n'
    linha5 =f'<insert tableName="{nomeDaTabela}">\n'
    linha6 =f'<column name={listaDeParametros[0]} value={listaDeValores[0]}/>\n'
    linha7 =f'<column name={listaDeParametros[1]} value={listaDeValores[1]}/>\n'
    linha8 =f'<column name={listaDeParametros[2]} value={listaDeValores[2]}/>\n'
    linha9 =f'<column name={listaDeParametros[3]} valueDate="{listaDeValores[3]}"/>\n'    
linha10 = f'</insert>\n'
linha11 = f'</changeSet>\n'
linha12 = f'</databaseChangeLog>\n'

"""

try:
    with open(nomeDoNovoArquivo, 'w') as arquivo:
        arquivo.write(linha1)
        arquivo.write(linha2)
        arquivo.write(linha3)
        arquivo.write(linha4)
        arquivo.write(linha5)
        arquivo.write(linha6)
        arquivo.write(linha6)
        arquivo.write(linha7)
        arquivo.write(linha8)
        arquivo.write(linha9)
        arquivo.write(linha10)
        arquivo.write(linha11)
        arquivo.write(linha12)
except:
    print(f'Aconteceu algum erro ao gerar o arquivo {nomeDoNovoArquivo}')"""

