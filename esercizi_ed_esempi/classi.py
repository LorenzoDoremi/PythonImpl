class warrior:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def __str__(self):
        return "Name: "+str(self.name)+"  --  Power: "+str(self.power)


def change_warrior(old_warrior: warrior):
    gugus = warrior("Gugus il folle", 20)
    old_warrior = gugus



def create_warrior():
    gugus = warrior("Gugus il pazzo",100)
    return gugus


def change_stats(old_warrior):
    old_warrior.power = 1000


# ---------------------------------------------------------
eldenmaster = warrior("Eldenmaster", 198)
print(eldenmaster)


# modifico all'interno di un loop
for i in range(0, 1):

    gugus = warrior("Urok il pazzoide", 50)
    eldenmaster = gugus

# cosa stamperà?
print(eldenmaster)

# modifico creando un nuovo guerriero nella funzione
change_warrior(eldenmaster)
print(eldenmaster)

# modifico i parametri della classe nella funzione
change_stats(eldenmaster)
print(eldenmaster)

eldenmaster = create_warrior()
print(eldenmaster)