#!/usr/bin/env python
# coding: utf-8

#coded by et1m

__author__ = "et1m"
__date__ = "$31/12/2016 19:44:01$"

#instale a api do google para funcionar 
#sudo pip install google


from google import search



print ''
print '\033[36m'+'8   8           '+'\033[33m'+' 8""""8   '+'\033[34m'+'8"""8'+'\033[0;0m'
print '\033[36m'+'8   8 e   e eeee'+'\033[33m'+' 8    8   '+'\033[34m'+'8   8   '+'\033[0;0m'+'\033[31m'+' eeeee eeee eeeee eeeee'
print '\033[36m'+'8eee8 8   8 8   '+'\033[33m'+' 8eeee8ee '+'\033[34m'+'8eee8e  '+'\033[0;0m'+'\033[31m'+' 8   " 8  8 8   8 8   8'
print '\033[36m'+'88  8 8e  8 8eee'+'\033[33m'+' 88     8 '+'\033[34m'+'88   8  '+'\033[0;0m'+'\033[31m'+' 8eeee 8e   8eee8 8e  8'
print '\033[36m'+'88  8 88  8 88  '+'\033[33m'+' 88     8 '+'\033[34m'+'88   8  '+'\033[0;0m'+'\033[31m'+'    88 88   88  8 88  8'
print '\033[36m'+'88  8 88ee8 88ee'+'\033[33m'+' 88eeeee8 '+'\033[34m'+'88   8  '+'\033[0;0m'+'\033[31m'+' 8ee88 88e8 88  8 88  8'
print '\n'
print 'C0D3D BY ET1M ---> GITHUB :'+'\033[0;0m'+' https://github.com/3t1n/scripts'
print '\n'                                                         


print("\033[36m"+"""\
                         ______                     
 _________        .---"""      """---.              
:______.-':      :  .--------------.  :             
| ______  |      | :                : |             
|:______B:|      | |  Little Error: | |             
|:______B:|      | |                | |             
|:______B:|      | |  Et1m hacked   | |             
|         |      | |  you ;)        | |             
|:_____:  |      | |                | |             
|    ==   |      | :                : |             
|       O |      :  '--------------'  :             
|       o |      :'---...______...---'              
|       o |-._.-i___/'             \._              
|'-.____o_|   '-.   '-...______...-'  `-._          
:_________:      `.____________________   `-.___.-. 
                 .'.eeeeeeeeeeeeeeeeee.'.      :___:
               .'.eeeeeeeeeeeeeeeeeeeeee.'.         
              :____________________________:    
  """+'\033[0;0m')


ip = raw_input ('\033[34m'+'Digite sua pesquisa:  '+'\033[0;0m')
print ('\n')
numero = raw_input('\033[34m'+"\nDigite o número de requisições: " +'\033[0;0m')
print '\n'

for url in search(ip, stop=numero,user_agent='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19,num=20',pause=2.0):

	
	print url
	file = "url.txt"
	f = open(file, "ab")
	

	f.write("\n"+url)
	



	
f.close()   


print '\033[31m'+'\nSeus links foram salvos em um arquivo .txt com sucesso'+'\033[0;0m'
print '\n'


