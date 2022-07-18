from numpy import sqrt


def square_equation_solver(coeffs):

    a, b,c = coeffs[0], coeffs[1], coeffs[2] 
    delta = b**2 - 4*a*c
    if delta < 0 :
        return [False, False]
 
    return [(-b + sqrt(delta))/(2*a),(-b - sqrt(delta))/(2*a)]



# x^2 + 2x - 8
solutions = square_equation_solver([1,2,+8])
print(solutions)



