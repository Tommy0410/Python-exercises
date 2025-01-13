'''
Acronim-encriptacio de missatges. Com ja coneixeu, una de les formes
d'encriptacio de paraules es el xifratge Cesar. A continuacio se us demana que implementeu una altra
estrategia de resolucio, que anomenarem acronim-encriptacio. Per tal de codificar un missatge amb la
tecnica acronim-encriptacio, simplement cal agafar la primera lletra de cada paraula, obtenint aixi un nou
missatge. Per exemple, donat el missatge “les vacances de primer quadrimestre estan a punt”, el resultat
de l'acronim-encriptacio seria el missatge “lvdpqeap”. Per tal de resoldre els apartats que segueixen, podeu
suposar que els missatges no contindran lletres majuscules.
'''
'''
[Apartat 1.a] Se us demana que realitzeu la funcio pura encriptaAcronimous, tal que, donat un missatge,
retorni el missatge codificat segons la tecnica acronim-encriptacio. Suposeu que el separador de paraules
dins el missatge es un espai en blanc, i que el missatge unicament contindra lletres alfabetiques.
'''
def encriptaAcronimous(s):
    """
    >>> encriptaAcronimous("les vacances de primer quadrimestre estan a punt")
    'lvdpqeap'
    """
    paraulas=s.split()
    
    paraula_encriptada=""
    for paraula in range(len(paraulas)):
        paraula_encriptada+=paraulas[paraula][0]
    return paraula_encriptada


"""
[Apartat 1.b] En aquest apartat se us demana implementar la funcio decodificaAcronimous, encarregada
de decodificar un missatge secret encriptat amb acronim-encriptacio seguint l'estrategia que es detalla a
continuacio.
Donat un missatge secret, decodificaAcronimous construeix un nou missatge, on cada lletra del missatge
original es canvia per una paraula que comenci per aquesta lletra. En cas que el caracter no sigui alfabetic,
aquest es mante. Finalment, la funcio ha de retornar aquest nou missatge. Per exemple, decodificaAcronimous amb el missatge “nj, nr”, pot retornar “nova jornada, nous reptes”.
Per implementar la funcio, utilitzeu la funcio que se us proporciona resolta, de nom obtenirParaula, tal
que, donat un caracter, retorna una paraula aleatoria que comenci per aquest caracter.
"""

def decodificaAcronimous(s):
    """
    >>> decodificaAcronimous("nj, nr")
    "nova jornada, nous reptes"
    """
    #return obtenirParaula(s)
    

"""
[Apartat 1.c] En aquest cas se us demana gestionar la funcionalitat que permet obtenir una paraula
aleatoria que comenci per una lletra. En aquest cas se us demana 

1.c.1) un script que llegeixi previament
un fitxer de text que contingui un conjunt de paraules, i emmagatzemi optimament cada paraula en una
estructura. Aquesta estructura ha de ser optima de manera que donada una lletra, obtingui la llista de
paraules del fitxer que comencin per aquesta lletra. Suposeu que el fitxer de paraules existeix amb el nom
paraules.txt i que cada paraula en el fitxer esta separada d'una altra per un espai en blanc. Tingueu en
compte que les paraules del fitxer no segueixen cap ordre. I que una mateixa paraula pot estar repetida
en el fitxer varies vegades.
"""
paraules_txt=open("paraules.txt")
paraules_lst=[]
paraulas=[]
dic={}
for linea in paraules_txt:
    paraules_lst+=linea.strip().split()
for palabra in paraules_lst:
    if palabra not in paraulas:
        paraulas+=[palabra]
for paraula in paraulas:
    if paraula[0] in dic: 
        dic[paraula[0]]=dic[paraula[0]]+[paraula]
    else:
        dic[paraula[0]]=[paraula]

    
#print(dic)


"""
Finalment, us cal 1.c.2) implementar la funcio obtenirParaula, tal que utilitzi la estructura de dades
anterior per, donat un caracter, retornar una paraula aleatoria de la llista que comenci per aquest caracter.
Se us demana que el codi Python dels passos c.1) i c.2) amb el funcionament esperat.

"""
'''
import random
def obtenirparaula(a,dic):
    llista=dic[a]
    return random.choice(llista)
'''
def chequejacaixa(m):

    solució=[m[0][:3],m[1][:3],m[2][:3]]
    elements=[]
    valid=True
    for i in range(len(solució)):
        for j in range(len(solució[0])):
            if solució[i][j] in elements:
                valid=False
                return valid
            else:
                elements.append(solució[i][j])
    if valid:
        return valid

chequejacaixa([[2,7,6,3,1,4,9,5,8],[8,5,4,9,6,2,7,1,3],[9,1,3,8,7,5,2,6,4],
[4,6,8,1,2,7,3,9,5],[5,9,7,4,3,8,6,2,1],[1,3,2,5,9,6,4,8,7],
[3,2,5,7,8,9,1,4,6],[6,4,1,2,5,3,8,7,9],[7,8,9,6,4,1,5,3,2]])

'''
Cercant un element. Una de les estrategies utilitzades per comprovar si un
element es troba emmagatzemat en una llista es la cerca binaria. Suposem una llista ordenada ascendentment. El funcionament consisteix en localitzar l'element del centre de la llista i comprovar si es el que
busquem. Si aquest no coincideix amb l'element que es cerca, es determina en quina meitat de la llista ha
de ser-hi. Es cerca en aquesta meitat repetint el proces les vegades que calgui fins trobar l'element, o be fins
que es determini que no es troba a la llista. Fixeu-vos que es tracta d'una estrategia divideix-i-venceras,
donat que en cada pas es minimitza la llargada de la llista a comprovar.
A continuacio s'exemplifica graficament el seu funcionament, suposant que:
la llista es: [0, 1, 2, 8, 13, 17, 19, 32, 42], el valor a cercar correspon al 3.
'''
'''
Se us demana que implementeu la funcio pura binarySearch tal que, donada una llista d'elements ordenada
ascendentment, i un element a cercar, retorni True si l'element es troba a la llista i False en cas contrari,
utilitzant l'estrat`egia cerca bin`aria.
Obviament, la utilitzacio de les funcions predefinides de Python (exc ` epte la funcio len) en la cerca, suposar`a
una puntuacio nul·la.
'''
def binarySearch(llista,valor):
    inici=0
    final=len(llista)-1
    while inici<=final:
        mig=(inici+final)//2
        
        if llista[mig]==valor:
            return True
        else:
            if llista[mig]>valor:
                final=mig-1
            if llista[mig]<valor:
                inici=mig+1
    return False

print(binarySearch( [0, 1, 2, 8, 13, 17, 19, 32, 42],43))