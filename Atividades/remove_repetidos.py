def remove_repetidos(lista):
    nova = []
    for item in lista:
        if item not in nova:
            nova.append(item)
        
        nova.sort()
    return nova


    
    