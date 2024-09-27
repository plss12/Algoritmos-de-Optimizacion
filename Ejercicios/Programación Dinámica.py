import math

def coste_min(costes):
    n = len(costes)

    # Creamos una lista donde guardaremos los costes mínimos
    # de llegar al nodo i desde el nodo 0
    res = [math.inf] * n
    res[0] = 0
    
    # Iteramos sobre todos los nodos
    for i in range(1, n):
        # Para cada nodo iteramos sobre todos los nodos anteriores
        for j in range(i):
            # Comprobamos si hay camino entre j e i
            if costes[j][i] != math.inf:
                # Elegimos el camino de coste mínimo
                res[i] = min(res[i], res[j] + costes[j][i])

    # Si existe devolvemos el coste mínimo de llegar al nodo n desde el nodo 0
    return res[n-1] if res[n-1] != math.inf else -1

costes = [[math.inf, 5, 4, 3, math.inf, math.inf, math.inf],
            [math.inf, math.inf, math.inf, 2, 3, math.inf, 11],
            [math.inf, math.inf, math.inf, 1, math.inf, 4, 10],
            [math.inf, math.inf, math.inf, math.inf, 5, 6, 9],
            [math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, 4],
            [math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, 3],
            [math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf]]

print(coste_min(costes))