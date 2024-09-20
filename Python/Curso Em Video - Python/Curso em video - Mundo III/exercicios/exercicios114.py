import urllib
import urllib.request

try:
    site = urllib.request,urllib('http://www.pudim.com.br')
except urllib.error.URLError:
    print('o site pudim não esta acessivel no momento.')
else:
    print('Consegui acessar o site pudim com sucesso!')
    print(site.read())
    