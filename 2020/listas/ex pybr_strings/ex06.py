data = input("data de nascimento:")
if len(data) != 10:
    print('ERROR')
else:
    data = data.replace('/',' ')
    data = data.split()
    dia = data[0]
    mes = data[1]
    ano = data[2]
    if mes == "01": mes = "janeiro"
    elif mes == "02": mes = "fevereiro"
    elif mes == "03": mes = "março"
    elif mes == "04": mes = "abril"
    elif mes == "05": mes = "maio"
    elif mes == "06": mes = "junho"
    elif mes == "07": mes = "julho"
    elif mes == "08": mes = "agosto"
    elif mes == "09": mes = "setembro"
    elif mes == "10": mes = "outubro"
    elif mes == "11": mes = "novembro"
    elif mes == "12": mes = "dezembro"
    else:
        print('ERROR')
    print(f"\nVocê nasceu em {dia} de {mes} de {ano}")