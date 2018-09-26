import requests
from lxml.html import fromstring as parser
from bs4 import BeautifulSoup

def main():
    pass

def obter_pagina_e_profundidade():
    profundidade=input("digite a profundidade: ")
    palavra=input("digite a palavra: ")
    busca_palavras_pagina(palavra,profundidade)
    pass

def busca_palavras_pagina(palavra,profundidade):
    palavras_encontradas=[]
    if(profundidade==1):
        page=obter_links_com_profundidade(profundidade)
        encontrar_palavras(page)
        pass
    if(profundidade>1):
        pass
    pass

def obter_links_com_profundidade(profundidade):
    site="http://www.google.com"
    if(profundidade==1):
        response=requests.get(site)
        html = parser(response.text)
        soup = BeautifulSoup(response.text,"lxml")
        return soup
    if(profundidade>1):
        response=requests.get(site)
        html = parser(response.text)
        soup = BeautifulSoup(response.text,"lxml")
        all_links=soup.find_all("a")
        obter_paginas_dos_links(all_links)
    pass

def obter_paginas_dos_links(all_links):
    pass

def encontrar_palavras(page):
    pass
if __name__=="__main__":
    main()
