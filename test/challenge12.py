
def cross(side: int) -> int:
    
    add = 0
    if side%2!= 0:
        add = 0.5

    for i in range(0, side):
        for j in range(0, side):
            if i == side/2 -add or j == side/2 -add:
                print('*', end='')
            else:
                print(' ', end='')
        print('')
    


cross(5)