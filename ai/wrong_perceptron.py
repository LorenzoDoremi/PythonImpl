import random
import math
import matplotlib.pyplot as plt 


# questo percettrone ha una falla costruttiva importante. quale? 


data = []

# Random integer generator
def rint(a, b):
    return random.randint(a, b)

# Solution of the quadratic equation
def eq2(a, b, c):
    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        return False
    return (-b + math.sqrt(discriminant)) / (2 * a)

# Generate 1000 random equations
for i in range(1000):
    a = rint(-10, 10)
    if a == 0:
        a = rint(-4, -1)  # Ensure 'a' is not zero
    b = rint(-30, 30)
    c = rint(-50, 50)
    
    eq = {"a": a, "b": b, "c": c, "sol": eq2(a, b, c)}
    data.append(eq)

# Filter equations with integer solutions
filtered = [d for d in data if d["sol"] != False]

# Initialize weights and learning rate
w1 = random.uniform(0, 1)
w2 = random.uniform(0, 1)
w3 = random.uniform(0, 1)
learning = 0.001

# Train function
def train(data, w1, w2, w3, iterations, learning):
    for i in range(iterations):
        for d in data:
            s = d["a"] * w1 + d["b"] * w2 + d["c"] * w3  # Predicted solution
            err = s - d["sol"]  # Use raw error

            # Update weights based on the error
            w1 -= learning * err * d["a"]  # Gradient update for w1
            w2 -= learning * err * d["b"]  # Gradient update for w2
            w3 -= learning * err * d["c"]  # Gradient update for w3
    
    return w1, w2, w3





# Guess function
def guess(a, b, c, w1, w2, w3):
    return a * w1 + b * w2 + c * w3


x = []
y = []
  
for i in range(0,10000,1000):
    # Train the model
    w1, w2, w3 = train(filtered, w1, w2, w3, i, learning)
    # Compare the actual solution to the predicted solution
    # Select a random filtered equation
    d = filtered[random.randint(0, len(filtered) - 1)]
    actual = eq2(d["a"], d["b"], d["c"])
    predicted = guess(d["a"], d["b"], d["c"], w1, w2, w3)
    x.append(i)
    y.append(abs((actual-predicted)))
    
print("Trained weights:", w1, w2, w3)
plt.plot(x,y)
plt.plot(x,[sum(y)/len(y) for i in x])
plt.show()
'''  

train(data,w1,w2,w3,1000,learning)

d = filtered[random.randint(0, len(filtered) - 1)]

sol = eq2(d["a"], d["b"], d["c"])
predicted = guess(d["a"], d["b"], d["c"], w1, w2, w3)

print("soluzione = ",sol," previsione = ",predicted)


plt.plot([i for i in range(-20,20)], [d["a"]*i**2 + d["b"]*i + d["c"] for i in range(-20,20)])
plt.step([d["a"]*w1+ d["b"]*w2 + d["c"]*w3 for i in range(-20,20)], [i for i in range(-20,20)])
plt.plot([i for i in range(-20,20)], [0 for i in range(-20,20)])
plt.show()'''