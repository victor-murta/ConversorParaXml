print("--- Conversor para xml ---")
#arquivo = str(input())
try:
    arquivo = open("test.txt", "r")
except:
    print("Falha ao abrir o arquivo, tente novamente!")

listaDeValores = []
listaDeParametros = []

for line in arquivo:
    removendoValuesInicio = line.rfind('VALUES')
    removendoValuesFinal = removendoValuesInicio + 6

    valores = line[removendoValuesFinal:]
    parametros = line[:removendoValuesInicio]

    removendoInserInto = parametros.rfind('INSERT')
    parametrosSemInsert = parametros[11:]

    listaDeValores.append(valores)
    listaDeParametros.append(parametrosSemInsert)

    for palavras in listaDeValores:
        removendoParenteses1 = palavras.replace('(', "")
        removendoParenteses2 = removendoParenteses1.replace(')', "")
        removendoPontosEVirgulas = removendoParenteses2.replace(';', "")
    
    for palavras in listaDeParametros:
        removendoParenteses1 = palavras.replace('(', "")
        removendoParenteses2 = removendoParenteses1.replace(')', "")
        removendoPontosEVirgulas = removendoParenteses2.replace(';', "")


listaDeValores = listaDeValores[0].split()
listaDeParametros = listaDeParametros[0].split()

linha1 =f'<?xml version="1.0" encoding="UTF-8" standalone="no"?>'
linha2 =f'<databaseChangeLog xmlns="http://www.liquibase.org/xml/ns/dbchangelog" xmlns:ext="http://www.liquibase.org/xml/ns/dbchangelog-ext" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog-ext http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-ext.xsd http://www.liquibase.org/xml/ns/dbchangelog http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-3.1.xsd">'
linha3 =f'<property name="now" value="now()" dbms="mysql"/>'
for palavras in range(len(listaDeParametros)): 
    linha4 =f'<changeSet author="pacto" id=>'
    linha5 =f'<insert tableName={listaDeParametros[]}>'
    linha6 =f'<column name={listaDeParametros[0]} value={listaDeValores[0]}/>'
    linha7 =f'<column name={listaDeParametros[1]} value={listaDeValores[1]}/>'
    linha8 =f'<column name={listaDeParametros[2]} value={listaDeValores[2]}/>'
    linha9 =f'<column name={listaDeParametros[3]} valueDate="{listaDeValores[3]}"/>'
    
linha10 = f'</insert>'
linha11 = f'</changeSet>'
linha12 = f'</databaseChangeLog>'




