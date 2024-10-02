matriz = [[0,0,0,], [0,0,0], [0,0,0]]

for l in range(0,3):
    for c in range(0,3):
        matriz [l][c]= int(input(f'digite um valor para {l} e {c}:\n'))
print('-=' * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]', end='')
    print()

'''
sem o: print() --->  caso faça isso a saida: [1][2][3][4][5][6][7][8][9]
ou seja os numeros tudo junto


'''