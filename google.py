
#!/usr/bin/env python
# coding: utf-8

#coded by et1m

__author__ = "et1m"
__date__ = "$31/12/2016 19:44:01$"


from google import search

#pergunta = raw_input("VocE deseja salvar os links em um arquivo txt? s ou n")


ip = raw_input ("Digite sua pesquisa: ")


for url in search(ip, stop=20):
    print(url)

     

#if pergunta == "s":

file = "le.txt"
f = open(file, "w+")
type(f)

f.write("\n"+url)
f.close()
