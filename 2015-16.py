def sexagesimalDecimal(a):
    """
    >>> sexagesimalDecimal("42:8:9.96")
    42.1361
    >>> sexagesimalDecimal("42:23:60.0")
    42.4
    """
    a=a.split(":")
    return float(a[0])+(float(a[1])/60)+(float(a[2])/3600)
def decimalSexagesimal(a):
    """
    >>> decimalSexagesimal(42.1361)
    "42:8:9.96"
    >>> decimalSexagesimal(42.4)
    "42:23:60.0"
    """
    a=str(a)
    a=a.split(".")
    graus=a[0]
    decimals="0."+a[1]
    minuts=float(decimals)*60
    a=str(minuts)
    a=a.split(".")
    minuts=a[0]
    decimals="0."+a[1]
    segons=float(decimals)*60
    return f"{graus}:{minuts}:{segons}"

def parellesProperes(a):
    doc=open(f"{a}")
    dic={}
    for line in doc:
        line=line.strip().split()
        dic[line[1]]=int(float(line[0]))
    keys=list(dic.keys())
    lista=[]
    for i in range(len(keys)):
        for j in range(len(keys)):
            if i<j and dic[keys[i]]==dic[keys[j]]:
                    lista.append((keys[i],keys[j])) 
    return lista


import sys

if __name__=="__main__":
    if len(sys.argv)==1:
        print ("Manquen dades")
    #else:
        #print (parellesProperes(sys.argv[1]))
def sumDiagonal(m):
    """
    >>> sumDiagonal({(0, 3): 1, (1, 4): 3, (2, 0): 3, (2, 1): 1, (3, 1): 2})
    0
    >>> sumDiagonal({(0, 3): 1, (1, 4): 3, (2, 0): 3, (2, 1): 1, (3, 1): 2, (4, 4): 1})
    1
    """
    keys_diagonal=[]
    values=[]
    keys=list(m.keys())
    for key in keys: 
        if key[0]==key[1]:
            keys_diagonal.append(key)
    for j in keys_diagonal:
        values+=[m[j]]
    return sum(values)
def guessOrder(m):
    """
    >>> guessOrder({(0, 3): 1, (1, 4): 3, (2, 0): 3, (2, 1): 1, (3, 1): 2})
    (4, 5)
    >>> guessOrder({(0, 3): 1, (1, 4): 3, (2, 0): 3, (2, 1): 1, (3, 1): 2, (4, 4): 1})
    (5, 5)
    """
    keys=m.keys()
    fila=0
    columna=0
    for key in keys:
        if key[0]>fila:
            fila=key[0]
        if key[1]>columna:
            columna=key[1]
    return (fila+1,columna+1)
def compressRow(m):
    """
    >>> compressRow({(0, 3): 1, (1, 4): 3, (2, 0): 3, (2, 1): 2, (3, 1): 2})
    {(0, 1): 1.0, (3, 1): 2.0, (1, 1): 3.0, (2, 2): 2.5}
    >>> compressRow({(0, 0): 1, (0, 3): 2, (1, 0): 2, (1, 1): 1, (1, 3): 1, (2, 3): 1})
    {(1, 3): 1.3333333333333333, (0, 2): 1.5, (2, 1): 1.0}
    """
    keys=list(m.keys())
    new_dic={}
    for key in keys:
        media=0
        numero=0
        for key1 in keys:
            if key[0]==key1[0]:
                media+=m[key]
                numero+=1
        if numero!=0:
            media=media/numero
        new_dic[(key[0],numero)]=media
    return new_dic
#compress row esta incompleto
def selectionSort(m):
    lista=m
    for i in range(len(m)):
        inicio=m[i]
        final=m[i]
        for j in range(1,len(m)):
            if m[j]<final:
                final=m[j]
                posicion=j
        
        lista[i]=final
        lista[posicion]=inicio
    return lista
print(selectionSort([3,9,7,1,5,2]))




            


