#!/usr/bin/env python
# encoding: utf-8
#codado pelo et1m

import requests
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8') #codifica pra utf-8

url = 'https://www.guiamais.com.br/encontre?'
print 'oq vc quer buscar?'
busca = raw_input('')
payload = { 'searchbox' : 'true','what': busca,'where':'São+Paulo%''2C+SP'} #array com as var do GET
r = requests.get(url, params=payload) #fazendo a request GET
html = r.text #criando o objeto com ohtml 
soup =  BeautifulSoup(r.content, 'html.parser') #pega as informações html da pag


for conteudo in soup.find_all(class_="advAdress"): #vai achar os enderecos da pagina atraves da class
	texto = conteudo.get_text().strip() #vai pegar somente o texto do html e o strip vai tirar os espacos desnecessarios
	texto = texto.replace("Como Chegar", '') #vai apagar em todo o texto a frase como chegar
	arquivo = open('C:\Python27\html.txt', 'a') #local onde vai estar o arquivo txt
	arquivo.write('\n'+str(texto)) #vai escrever no arquivo txt
	arquivo.close() #fecha o arquivo txt

print "conteudo gravado no arquivo html.txt com sucesso!!!"





