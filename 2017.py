#1.a
"""
Dissenyeu la funcio obtenirQueryParameters(url) tal que, donada una URL,
mostri per pantalla la informacio dels query parameters. Per a l'exemple anterior, caldria que
printes la informacio que segueix. Adoneu-vos que el simbol + en les query parameters es indicador d'espai en blanc.
http://www.google.com/search?sourceid=chrome&ie=UTF-8&q=query+parameters
sourceid: chrome
ie: UTF-8
q: query parameters
O be en un exemple de Facebook,
http://graph.facebook.com/search?q=watermelon&type=post
q: watermelon
type: post
"""
'''

def obtenirQueryParameters(url):
    """
    >>> obtenirQueryParameters("http://www.google.com/search?sourceid=chrome&ie=UTF-8&q=query+parameters")
    sourceid: chrome
    ie: UTF-8
    q: query parameters
    >>> obtenirQueryParameters("http://graph.facebook.com/search?q=watermelon&type=post")
    q: watermelon
    type: post
    >>> obtenirQueryParameters("https://www.google.es/search?q=how+to+use+prezi&client=ubuntu&
    channel=cs&aq=f&oq=how+to+use+prezi&aqs=chrome.0.57j65.18849&sourceid=chrome&ie=UTF-8")
    q: how to use prezi
    client: ubuntu
    channel: cs
    aq: f
    oq: how to use prezi
    aqs: chrome.0.57j65.18849
    sourceid: chrome
    ie: UTF-8
    """

# 1. b Convertiu la funcio anterior en booleana i afegiu que retorni True si la consulta realitzada te a veure amb how to. En els doctests anteriors, unicament el darrer test retornariaTrue. Els dos primers retornarien
    url = url.split("?")
    values=[]
    querys=  url[1].split("&")
    for query in range(len(querys)):
        parameters=querys[query]
        key,value=parameters.split("=")
        value=value.replace("+"," ")
        print(key+":",value)
        values.append(value)
    for i in values:
        if "how to" in i:

            return True
    return False

'''
'''
Suposant que disposeu de la funcio obtenirQueryParameters de lApartat 1.b,
correctament implementada, escriviu un script tal que donats un conjunt de URLs que es troben
en el fitxer queries.txt amb el format: una linia per URL, escrigui en el fitxer estadistiques.txt,
quin percentatge d'aquestes URLs te a veure amb consultes de tipus how to.
#contingut fitxer queries.txt
https://www.google.es/search?q=how+to+use+prezi&client=ubuntu&channel=cs&aq=f&oq=how+to+us&aqs=chrome.0.59j57j62l3.2339&sourceid=chrome&ie=UTF-8
https://www.google.es/search?q=how+to+program+in+java&client=ubuntu&channel=cs&aq=f&oq=how+to+program&aqs=chrome.0.59j57j60j62l3.2098&sourceid=chrome&ie=UTF-8
https://www.google.es/search?q=pictures+of+nutshell&client=ubuntu&channel=cs&aq=f&oq=pictures+of+nutshell&aqs=chrome.0.57.3219&sourceid=chrome&ie=UTF-8
https://www.google.es/search?client=ubuntu&channel=fs&q=selection+sort+algorithm&ie=utf-8&oe=utf-8&gfe_rd=cr&dcr=0&ei=6rdUWvPsCZLY8geNwpPYBg
#el contingut del fitxer estadistiques.txt hauria de ser
50%
'''
'''
urls=open("queries.txt")
urls_ls=[]
lineas=0
for linea in urls:
    linea=linea.strip()
    urls_ls.append(linea)
    lineas+=1
coincidencies=0
for i in range(lineas):
    if obtenirQueryParameters(urls_ls[i]):
        coincidencies+=1

estadistica=(coincidencies/lineas)*100
estadistiques=open("estadistiques.txt","w")
estadistiques.write(str(int(estadistica))+"%")


urls.close()
estadistiques.close()

'''