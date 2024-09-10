import numpy


#sub-optimal needleman-wunsh algorithm (missing the multiple path search.)

dna1 = "tatga"

dna2 = "tacga"
matrix = numpy.zeros((len(dna2)+1,len(dna1)+1))
matrix[0] = [-i*2 for i in range(0,len(dna1)+1)]
for i in range(0,len(dna2)+1):
    matrix[i][0] = -i*2
matrix[0][0] = 0
    
print(matrix)
        
for i in range(1,len(dna2)+1):
    for j in range(1,len(dna1)+1):
        left = matrix[i][j-1]-2
        top  = matrix[i-1][j]-2
        topleft = matrix[i-1][j-1]
        if(dna1[j-1] == dna2[i-1]):
            topleft +=1
        else:
            topleft -=1
        matrix[i][j] = max(left,top,topleft)

path = []

print(matrix)
#inserisco l'angolo in basso a destra
path.append(matrix[len(dna2)][len(dna1)])

def p(seq1,seq2,matrix,path,curry,currx):
     if(currx != 0 and curry != 0):
         if(seq1[currx-1] == seq2[curry-1]):
             #vado in diagonale
             print("diag ->"+str(matrix[currx-1][curry-1]))
             path.append(matrix[currx-1][curry-1])
             p(seq1,seq2,matrix,path,currx-1,curry-1)
         else: 
             if(matrix[currx-1][curry] > matrix[currx][curry-1]):
                print("left ->" +str( matrix[currx-1][curry]))
                path.append(matrix[currx-1][curry])
                p(seq1,seq2,matrix,path,currx-1,curry)
             else: 
                print("top ->"+str(matrix[currx-1][curry]))
                path.append(matrix[currx-1][curry])
                p(seq1,seq2,matrix,path,currx-1,curry)  




p(dna1,dna2,matrix,path,len(dna2),len(dna1))
print(path)
score = sum(path)
print("score =",score)
             