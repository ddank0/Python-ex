def print_words(filename):
  word_count = word_count_dict(filename)
  # pegamos as chaves de forma ordenada
  words = sorted(word_count.keys())
  # percorremos cada palavra (já ordenada)
  for word in words:
    # ...e  imprimimos <word> <count>
    print word, word_count[word]

def print_top(filename):
  word_count = word_count_dict(filename)

  # Ordenamos as chaves conforme as ocorrências (valor de 'count')
  # Utilizamos a função "get_count()" para auxiliar a extrair o valor de 'count'
  items = sorted(word_count.items(), key=get_count, reverse=True)

  # Imprimimos apenas os 20 primeiros resultados
  for item in items[:20]:
    print item[0], item[1]

def get_count(word_count_tuple):
  return word_count_tuple[1]

def word_count_dict(filename):
  word_count = {}  # Mapa de cada palavra contada
  input_file = open(filename, 'r')
  # percorrer cada linha do arquivo...
  for line in input_file:
    words = line.split()
    # percorrer cada palavra da linha...
    for word in words:
      word = word.lower()
      # Caso espcial se nos estivermos vendo esta palavra pela primeira vez.
      if not word in word_count:
        word_count[word] = 1
      else:
        word_count[word] = word_count[word] + 1

  input_file.close()  # Não estritamente necessário, mas é uma boa forma.
  return word_count
