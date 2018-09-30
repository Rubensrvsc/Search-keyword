import requests
from lxml.html import fromstring as parser
from bs4 import BeautifulSoup
import re

list_palavras=[]
def main():
    obter_pagina_e_profundidade()
    pass

def obter_pagina_e_profundidade():
    print("------digite a palavra a pagina e a profundidade------")
    profundidade=int(input("digite a profundidade: "))
    if(profundidade==0):
        palavra=input("digite a palavra: ")
        url="http://libra.ifpi.edu.br/a-instituicao/reitoria"
        obter_links(profundidade,url,palavra)
    pass


def obter_links(profundidade,url,palavra):
    response=requests.get(url)
    res = BeautifulSoup(response.text,"html.parser")
    l=[]
    for i in res.find_all("a"):
        l.append(i)
    ocorrencias(response,palavra)
    encontra_palavras(response,palavra)
    '''for j in range(len(l)):
        procura_palavras(l[j],palavra)'''
    pass

def procura_links(j,palavra):
    list_links=''
    link=j.get("href").strip("http://")
    if(link.find("#")==0):
        print ("contem cerquilha")
    else:
        r=requests.get("http://"+link)
        bs=BeautifulSoup(r.text,"html.parser")
        for i in bs.find_all("a"):
            print(i.get("href"))
            list_links+=i.get("href")
    return list_links
    pass
def encontra_palavras(response,palavra):
    print(re.findall(palavra,response.text))

def ocorrencias(pagina,palavra):
    lista_palavras=re.finditer(palavra,pagina.text)
    lista_match=[]
    for i in lista_palavras:
        lista_match.append(i.string)
    print("Ocorrencias: %d" %(len(lista_match)))
    pass
def encontrar_palavras(page,palavra):
    lista_palavras=''
    if(page.__contains__(palavra)):
        lista_palavras+=palavra
    return lista_palavras
    pass
if __name__=="__main__":
    main()

#pegar os links de todas as paginas
#pegar as paginas dos links e encontrar as palavras
