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


'''
Ej 2 Xarxes socials. Suposant que teniu una xarxa social representada
com un graf tal com mostra la Figura 1 esquerra.
Suposeu que dita xarxa sha representat amb un diccionari, de nom xarxa, on cada clau daquest
sera el nick duna persona, i el valor associat, una llista de nicks de les persones amb les quals
es amic. Suposeu ara que cada persona de la xarxa social te un animal preferit. A tal efecte, es
creu un nou diccionari, animals, on per cada clau corresponent al nick dun usuari de la xarxa
social, semmagatzema com a valor el seu animal preferit.
Direm que una persona de la xarxa social es un hipster si el seu animal preferit es diferent de
tots els animals preferits dels seus amics. La Figura 1 dreta exemplifica aquesta situacio. Per
exemple, en la xarxa social, el conjunt de hipsters correspon a AngJolie, JuliaRoberts, Shakira
i DavidBeckham. Se us demana que, implementeu optimament la funcio hipster, tal que,
donats els dos diccionaris anteriors, retorni la llista de nicks daquells usuaris que son hipster. A
continuacio segueixen els doctests.

'''
'''
def hipster(d,e):
    """
    >>> hipster({"AngJolie": ["BradPitt", "JuliaRoberts"], "JuliaRoberts": ["AngJolie",
    "BradPitt", "Shakira", "DavidBeckham"],"BradPitt": ["AngJolie", "JuliaRoberts", "TomCruise",
    "Shakira"], "TomCruise": ["BradPitt", "Shakira"], "Shakira": ["TomCruise", "BradPitt", "JuliaRoberts",
    "DavidBeckham"], "DavidBeckham": ["JuliaRoberts", "Shakira"]}, {"AngJolie": "koala", "JuliaRoberts":
    "hamster", "BradPitt": "tigre", "TomCruise": "tigre", "Shakira": "koala", "DavidBeckham": "tigre"})
    ["AngJolie", "JuliaRoberts", "Shakira", "DavidBeckham"]
    """
    persones=d.keys()
    hipsters=[]
    for persona in persones:
        hipster=True
        amics=d[persona]
        animal_persona=e[persona]
        for amic in amics:
            animal_amic=e[amic]
            if animal_persona == animal_amic:
                hipster=False
        if  hipster:
            hipsters.append(persona)
    return hipsters

print(hipster({"AngJolie": ["BradPitt", "JuliaRoberts"], "JuliaRoberts": ["AngJolie",
    "BradPitt", "Shakira", "DavidBeckham"],"BradPitt": ["AngJolie", "JuliaRoberts", "TomCruise",
    "Shakira"], "TomCruise": ["BradPitt", "Shakira"], "Shakira": ["TomCruise", "BradPitt", "JuliaRoberts",
    "DavidBeckham"], "DavidBeckham": ["JuliaRoberts", "Shakira"]}, {"AngJolie": "koala", "JuliaRoberts":
    "hamster", "BradPitt": "tigre", "TomCruise": "tigre", "Shakira": "koala", "DavidBeckham": "tigre"}))

'''

'''
Ej 3 Algorisme dinserció. Suposant una llista correctament ordenada
en ordre ascendent, i un valor a inserir, se us demana el disseny optim duna funció pura tal que,
donats aquests parametres, retorni una nova llista amb lelement inserit en la posició correcta,
de manera que la llista continui estant ordenada ascendentment. La llista pot contenir valors
repetits. Obviament, la utilització de les funcions predefinides de P  ython sobre llistes suposara
una puntuació nul·la. Es pot utilitzar el metode len, les llesques/slices i loperació de concatenació
de llistes. A continuació segueixen els doctests.
'''
'''
def insereixValor(valor,llista):
    """
    >>> insereixValor(4, [3, 5, 7, 8])
    [3, 4, 5, 7, 8]
    >>> insereixValor(18, [1, 9, 12])
    [1, 9, 12, 18]
    >>> insereixValor(-4, [1, 2, 3])
    [-4, 1, 2, 3]
    >>> insereixValor(2, [])
    [2]
    >>> insereixValor(45, [-1, 22, 33, 45, 104, 208])
    [-1, 22, 33, 45, 45, 104, 208]
    """
    if len(llista)==0:
        return [valor]
    llista1=[]
    max=llista[-1]
    min=llista[0]
    if min>valor:
        llista1=[valor]+llista
        return llista1
    if max<valor:
        llista1=llista+[valor]
        return llista1
    
    for i in range(len(llista)):
        if llista[i]>valor:
            llista1=llista[:i]+[valor]+llista[i:]
            return llista1
'''
'''
Se us demana que dissenyeu optimament la funcio aplicarKerning, tal que, donades dues matrius
de 0s i 1s corresponents a lletres i un kerning, retorni la matriu resultant d'ajuntar les dues lletres
amb el kerning indicat. Podeu suposar que l'alcada de les dues matrius sera la mateixa. No
obstant, l'amplada de cada matriu pot diferir. Suposeu tambe que el kerning donat no es negatiu i es inferior a l'amplada de qualsevol de les dues imatges. Noteu que si el kerning es zero, la
imatge resultant sera l'amplada de les dues imatges posades juntes. A mesura que el valor del
kerning augmenti, l'amplada de la imatge resultant disminuira. Suposeu que les matrius donades
seran sempre correctes i no seran mai buides.
NOTA: No esta permes l'us de llesques/slices ni la copia de llistes. El seu us comportara una
puntuacio nul·la.
A continuacio se us mostra el resultat d'aplicar diferents valors de kernings.

'''

##EJ4 pendiente
def aplicarKerning(matrix1,matrix2,kerning):


