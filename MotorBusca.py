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
    palavra=input("digite a palavra: ")
    url="http://libra.ifpi.edu.br/a-instituicao/reitoria"
    obter_links(profundidade,url,palavra)
    pass


def obter_links(profundidade,url,palavra):
    response=requests.get(url)
    res = BeautifulSoup(response.text,"html.parser")
    l=[]
    if(profundidade>0):
        for i in res.find_all("a"):
            procura_links(i,palavra,profundidade)
    if(profundidade==0):
        ocorrencias(response,palavra)
        print(encontrar_palavras(response.text,palavra))
    pass

def procura_links(links,palavra,profundidade):
    profundidade-=profundidade
    list_links=[]
    link=links.get("href").strip("http://")
    if(link.find("#")==0):
        print ("contem cerquilha")
    else:
        r=requests.get("http://"+link)
        bs=BeautifulSoup(r.text,"html.parser")
        for i in bs.find_all("a"):
            print(i.get("href"))
            ocorrencias(bs, palavra)
            list_links.append(i.get("href"))
            '''for j in list_links:
                response=requests.get(j)
                res = BeautifulSoup(response.text,"html.parser")
                for h in res.find_all("a"):
                    print("entrou")
                    ocorrencias(bs, palavra)
                    procura_links(i, palavra)'''
    pass

def ocorrencias(pagina,palavra):
    lista_palavras=re.finditer(palavra,pagina.text)
    lista_match=[]
    for i in lista_palavras:
        lista_match.append(i.string)
    print("Ocorrencias: %d" %(len(lista_match)))
    pass
def encontrar_palavras(response,palavra):
    print(re.findall(palavra,response))
    pass

if __name__=="__main__":
    main()

