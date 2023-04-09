def contpalabras(palabra):
    dic_palabras = {}
    palabra = palabra.split()
    for pal in palabra:
        if pal in dic_palabras:
            dic_palabras[pal]=dic_palabras[pal]+1
        else:
            dic_palabras[pal]=1

    return dic_palabras