
import numpy

# algoritmo che risolve il problema della matrice di fiumi (calcolare quanti fiumi e la loro lunghezza, determinata da 1 in una matrice)
def visit(matrix, i,j, visited : set, store):
  if i >= 0 and j >= 0 and i < len(matrix) and j < len(matrix[i]) and matrix[i][j] == 1 and (i,j) not in visited:
        visited.add((i,j))
      # aggiungo 1 di lunghezza al fiume attuale
        store[0] += 1
        # down
        visit(matrix,i+1,j,visited,store)
        #left
        visit(matrix,i,j+1,visited,store)
        #right
        visit(matrix,i,j-1,visited,store)
        #up
        visit(matrix,i-1,j,visited,store)
      

def find_rivers(matrix):

    visited = set()
    results = []
    # faccio partire la cosa da tutti i punti di una matrice bidimensionale
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[i])):
          
          #il valore della lunghezza del fiume attuale
          store = [0]

          #considero il nuovo punto solo se è parte di un fiume che non ho già visto (e quindi raggiunto da visit())
          if matrix[i][j] == 1 and (i,j) not in visited:
            visit(matrix, i, j, visited, store)
            results.append(store[0])
    return results

                




fiumi = [

    [1,0,0,1],
    [1,0,0,1],
    [1,0,1,0],
    [0,0,1,1]
]

array = find_rivers(fiumi)
print(array)