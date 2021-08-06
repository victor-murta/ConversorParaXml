import re
print("--- Conversor para xml ---")

arquivoXml = str(input('Digite o nome do arquivo de entrada: ')).strip()
nomeDoNovoArquivo = str(input('Nome do novo arquivo: '))

try:
    arquivo = open(arquivoXml, "r")
except:
    print("Falha ao abrir o arquivo, tente novamente!")

listaDeValores = []
listaDeParametros = []
novoValor = []
novoParametro = []
contador = 0

for line in arquivo:  
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

    novosValores = valores.split()
    novosParametros = parametrosSemInsert.split()

    for palavras in novosValores:
        palavras = palavras.replace(')', "")
        palavras = palavras.replace('(', "")
        palavras = palavras.replace(';', "")
        palavras = palavras.replace(',', "")
        palavras = palavras.replace("'", "")
        if palavras not in novoValor:
            novoValor.append(palavras)  
            
    for palavras in novosParametros:
        palavras = palavras.replace(')', "")
        palavras = palavras.replace('(', "")
        palavras = palavras.replace(';', "")
        palavras = palavras.replace(',', "")
        if palavras not in novoParametro:
            novoParametro.append(palavras)
                
    if '.' in novoParametro[0]:
        procurandoPonto = novoParametro[0].rfind('.') + 1
        encontrandoAntesDoPonto = novoParametro[0][:procurandoPonto] 
        novoParametro[0] = novoParametro[0].replace(encontrandoAntesDoPonto, "")
        
    nomeDoArquivo = open(nomeDoNovoArquivo, 'a')

    if contador < 1:
        try:
            with nomeDoArquivo as arquivo:
                arquivo.write(f'<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
                arquivo.write(f'<databaseChangeLog xmlns="http://www.liquibase.org/xml/ns/dbchangelog" xmlns:ext="http://www.liquibase.org/xml/ns/dbchangelog-ext" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog-ext http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-ext.xsd http://www.liquibase.org/xml/ns/dbchangelog http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-3.1.xsd">\n')
                arquivo.write(f'\t<property name="now" value="now()" dbms="mysql"/>\n')
                arquivo.write(f'\t<changeSet author="pacto" id="{arquivoXml[:4]}">\n')
                arquivo.write(f'\t\t<insert tableName="{novoParametro[0]}">\n')
                for n in range(len(novoParametro)): 
                    arquivo.write(f'\t\t\t<column name="{novoParametro[n]}" value="{novoValor[n]}"/>\n' )
        except:
            print(f'Aconteceu algum erro ao gerar o arquivo {nomeDoNovoArquivo}')

    else:
        try:
            with nomeDoArquivo as arquivo:
                arquivo.write(f'\t\t<insert tableName="{novoParametro[0]}">\n')
                for n in range(len(novoParametro)): 
                    arquivo.write(f'\t\t\t<column name="{novoParametro[n]}" value="{novoValor[n]}"/>\n' )
        except:
            print(f'Aconteceu algum erro ao gerar o arquivo {nomeDoNovoArquivo}')

    contador += 1

with open(nomeDoNovoArquivo, "a") as arquivo:
    arquivo.write(f'\t\t</insert>\n')
    arquivo.write(f'\t</changeSet>\n')
    arquivo.write(f'</databaseChangeLog>\n')

    
