import sys

sys.setrecursionlimit(10**6)


def longest_path(v: int) -> int:
    """
    Definimos un metodo recursivo que recibe un diccionario que posee para cada vertice el conjunto de aristas.
    Se calculará el camino más largo para el vertice recibido por parametro.
    Para el vertice recibido visitara cada vertice que sea adyacente a este y realizara el calculo del camino maximo visitando recursivamente los demas vertices.

    Si el vértice no se encuentra en el diccionario de adyacentes se retornara 0 ya que no tiene salida a ningun lado.
    Si el vértice v ya se encuentra calculado se retorna el valor.
    Recorreremos cada vertice adyacente al vertice v y calculamos el máximo entre todos los caminos posibles, guardando el valor máximo calculado en el diccionario auxiliar para evitar cálculos innecesarios.

    Args:
        v (int):
            Vértice actual que se esta visitando.

    Returns:
        int:
            Retorna la longitud del camino más largo que se puede recorrer desde el vértice v.
    """
    if v not in adj:
        aux_mem[v] = 0
        return 0
    if v in aux_mem:
        return aux_mem[v]
    max_path: int = 0
    for a in adj[v]:
        max_path = max(max_path, longest_path(a) + 1)
    aux_mem[v] = max_path
    return max_path


nodos, aristas = map(int, sys.stdin.readline().split())
# Ponemos en uso la variable de nodos para definir un diccionario con la cantidad de nodos que recibimos.
adj: dict = {i: [] for i in range(1, nodos + 1)}
for _ in range(0, aristas):
    # Loopeamos por el total de aristas recibidas e iteramos por el input agregando la arista a su respectivo vertice.
    v, a = map(int, sys.stdin.readline().split())
    adj[v].append(a)

# Definimos un diccionario auxiliar para guardar la longitud de cada camino calculado para evitar calculos innecesarios.
aux_mem: dict = {}
longest: int = 0
for nodo in adj.keys():
    longest = max(longest, longest_path(nodo))
print(longest)
