import requests
from lxml.html import fromstring as parser
from bs4 import BeautifulSoup

def main():
    obter_pagina_e_profundidade()
    pass

def obter_pagina_e_profundidade():
    profundidade=input("digite a profundidade: ")
    palavra=input("digite a palavra: ")
    url="http://libra.ifpi.edu.br/a-instituicao/reitoria"
    obter_links(profundidade,url,palavra)
    pass


def obter_links(profundidade,url,palavra):
    response=requests.get(url)
    res = BeautifulSoup(response.text,"html.parser");
    l=[]
    for i in res.find_all("a"):
        l.append(i)
    for j in range(len(l)):
        procura_palavras(l[j],palavra)
    pass

def procura_palavras(j,palavra):
    link=j.get("href").strip("http://")
    if(link.find("#")==0):
        print ("contem cerquilha")
    else:
        r=requests.get("http://"+link)
        print(r.text)
    pass

'''def obter_paginas_dos_links(profundidade,site):
    response=requests.get(site)
    html = parser(response.text)
    soup = BeautifulSoup(response.text,"lxml")
    all_links=soup.find_all("a")
    paginas=soup.find_all("body")
    if(profundidade==0):
        return paginas
    else:
        obter_paginas_dos_links(profundidade-1,site)
    pass

def encontrar_palavras(page,palavra):
    lista_palavras=[]
    if(page.__contains__(palavra)):
        lista_palavras.append(palavra)
    pass'''
if __name__=="__main__":
    main()

#pegar os links de todas as paginas
#pegar as paginas dos links e encontrar as palavras
