import re
print("--- Conversor para xml ---")

#arquivoXml = str(input('Digite o nome do arquivo de entrada: ')).strip()
arquivoXml = 'inserts-funcionalidade-url.sql'
nomeDoNovoArquivo = 'teste.xml'
#nomeDoNovoArquivo = str(input('Nome do novo arquivo: '))

nomeDoArquivo = open(nomeDoNovoArquivo, 'a')

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

    novosValores = re.split(' , ', listaDeValores[0])
    novosValores = valores.split()
    novosParametros= re.split(' , ', listaDeParametros[0])
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
   
    if contador < 1:
        try:
            with nomeDoArquivo as arquivo:
                arquivo.write(f'<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
                arquivo.write(f'<databaseChangeLog xmlns="http://www.liquibase.org/xml/ns/dbchangelog" xmlns:ext="http://www.liquibase.org/xml/ns/dbchangelog-ext" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog-ext http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-ext.xsd http://www.liquibase.org/xml/ns/dbchangelog http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-3.1.xsd">\n')
                arquivo.write(f'\t<property name="now" value="now()" dbms="mysql"/>\n')
                arquivo.write(f'\t<changeSet author="pacto" id="0000">\n')
                arquivo.write(f'\t\t<insert tableName="{novoParametro[0]}">\n')
                for n in range(len(novoParametro)): 
                    arquivo.write(f'\t\t\t<column name="{novoParametro[n + 1]}" value="{novoValor[n + 1]}"/>\n' )
        except:
            print(f'Aconteceu algum erro ao gerar o arquivo 1 {nomeDoNovoArquivo}')

    
    if contador >= 1:
        try:
            with open(nomeDoNovoArquivo, 'a') as arquivo:
                arquivo.write(f'\t\t<insert tableName="{novoParametro[0]}">\n')
                for n in range(len(novoParametro)): 
                    arquivo.write(f'\t\t\t<column name="{novoParametro[n + 1]}" value="{novoValor[n + 1]}"/>\n' )
        except:
            print(f'Aconteceu algum erro ao gerar o arquivo 2 {nomeDoNovoArquivo}')

    contador += 1
    

with nomeDoArquivo as arquivo:
    arquivo.write(f'\t\t</insert>\n')
    arquivo.write(f'\t</changeSet>\n')
    arquivo.write(f'</databaseChangeLog>\n')

