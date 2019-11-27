m_preço = 0
produt = input('Nome do produto:')

while produt != 'xxx':
    preço = float(input('Preço:'))

    if  preço > m_preço:
        m_preço = preço

