#12
pets = [
    {"nome": "Rex", "tipo": "cachorro", "dono": "João"},
    {"nome": "Mimi", "tipo": "gato", "dono": "Maria"},
    {"nome": "Lola", "tipo": "coelho", "dono": "Carlos"}
]

for pet in pets:
    print(f"Nome: {pet['nome']}, Tipo: {pet['tipo']}, Dono: {pet['dono']}")