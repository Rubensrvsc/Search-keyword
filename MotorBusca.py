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
    palavra=raw_input("digite a palavra: ")
    url="http://libra.ifpi.edu.br/a-instituicao/reitoria"
    obter_links(profundidade,url,palavra)
    pass


def obter_links(profundidade,url,palavra):
    response=requests.get(url)
    res = BeautifulSoup(response.text,"html.parser")
    l=[]
    if(profundidade>0):
        for i in res.find_all("a"):
            procura_links(i,palavra)
    if(profundidade==0):
        ocorrencias(response,palavra)
        #encontra_trecho(response.content,palavra)
        print(encontrar_palavras(response.text,palavra))
    pass

def procura_links(links,palavra):
    list_links=[]
    link=links.get("href").strip("http://")
    if(link.find("#")==0):
        print ("contem cerquilha")
    else:
        r=requests.get("http://"+link)
        bs=BeautifulSoup(r.text,"html.parser")
        for i in bs.find_all("a"):
            print(i.get("href"))
            list_links.append(i.get("href"))
    for j in list_links:
        response=requests.get(j)
        res = BeautifulSoup(response.text,"html.parser")
        for h in res.find_all("a"):
            procura_links(i)
    pass
'''def encontra_trecho(response,palavra):
    lista=[]
    for i in re.finditer(palavra.lower(),response.lower()):
        print(tuple(i.groups()))
        lista.append(i)
    lista_palavras=[]
    for j in lista:
        lista_palavras.append(lista[-10:+10])
    for h in range(len(lista_palavras)):
        print(lista_palavras[h])'''

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

#pegar os links de todas as paginas
#pegar as paginas dos links e encontrar as palavras
