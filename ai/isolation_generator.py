import numpy as np
import random

# Imposta un generatore di numeri casuali per riproducibilità
np.random.seed(42)
random.seed(42)

# Genera 95 persone con valori normali
dataset = []
nomi_comuni = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hank", "Ivy", "Jack",
               "Karen", "Leo", "Mona", "Nathan", "Olivia", "Paul", "Quinn", "Rachel", "Steve", "Tina"]

for _ in range(95):
    persona = {
        "nome": random.choice(nomi_comuni) + str(random.randint(1, 50)),  # Evita nomi duplicati
        "altezza": round(np.random.normal(1.70, 0.30), 2),  # Media 1.70m, deviazione 10cm
        "peso": round(np.random.normal(70, 20), 1),  # Media 70kg, deviazione 10kg
        "colore": random.choice(["blu", "verde", "rosso", "giallo", "azzurro", "grigio", "nero"])
    }
    dataset.append(persona)

# Aggiunta di 5 outlier
outliers = [
    {"nome": "Gigante", "altezza": 2.50, "peso": 200, "colore": "nero"},  # Troppo alto e pesante
    {"nome": "Minuscolo", "altezza": 1.20, "peso": 30, "colore": "rosa"},  # Troppo basso e magro
    {"nome": "Invisibile", "altezza": 0.00, "peso": 0, "colore": "trasparente"},  # Valori impossibili
    {"nome": "Errore", "altezza": -1, "peso": 70, "colore": "grigio"},  # Altezza mancante
    {"nome": "Strano", "altezza": 1.75, "peso": -10, "colore": "blu"}  # Peso negativo
]

dataset.extend(outliers)

