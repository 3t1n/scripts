#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup


print 'digite o site:'
url = raw_input("")
print ''
print 'oq vc quer buscar?'
busca = raw_input('')

searchbox=true&what=Supermercados&where=São+Paulo%2C+SP

payload = {'what': busca,'where':''}
r = requests.get(url, params=payload)
html = r.text
teste = BeautifulSoup(html)
conteudo = teste.find_all('main', {'class': 'advertiserContent'})

print conteudo

