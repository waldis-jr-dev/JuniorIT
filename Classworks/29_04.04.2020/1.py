def txt_to_dict(file_name):
  with open(file_name,'r', encoding='utf-8') as file:
    answ = {}
    for i in file:
      i = i.strip(';\n')
      i = i.split(' - ')
      i[1] = i[1].split(', ')
      answ[i[0]] = i[1]
  return answ


def dictionary_changer(x):
  answ = {}
  for key, value in x.items():
    for i in value:
      answ[i] = key
  return answ


def dict_to_file(file_name, p):
  with open(file_name,'w', encoding='UTF-8') as file:
    for i in p.keys():
      str1 = f'{i} - {p[i]};\n'
      file.write(str1)


a = txt_to_dict('r.txt')
b = dictionary_changer(a)
dict_to_file('dict2.txt', b)