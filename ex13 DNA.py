for i in range(5):
    dna = input('entre com DNA:')
    dna = dna.upper()
    print('DNA:',dna)

    dna = dna.replace('A','@')
    dna = dna.replace('T','A')
    dna = dna.replace('@','T')

    dna = dna.replace('C','@')
    dna = dna.replace('G','C')
    dna = dna.replace('@','G')
    print('DNA COMPLEMENTAR:',dna)