import pymorphy2
morph = pymorphy2.MorphAnalyzer()

text = open('text.txt', 'r', encoding='utf-8')
a = text.readlines()
text_list = []
for i in a: # Возможно было бы сделать в один прием, но не нашла такого метода строк
    i = i.replace(',', "")
    i = i.replace(".", "")
    i = i.replace("!", "")
    i = i.replace('«', "")
    i = i.replace('»', "")
    i = i.replace("?", "")
    i = i.replace("—", "")
    #i = i.lower() Так можно было бы не использовать map ниже.
    i = i.split()
    for el in i:
        text_list.append(el)

new_list = list(map(lambda x: str(x).lower(), text_list))
my_dict = {}
for el in new_list:
    if el not in my_dict:
        my_dict[el] = 1
    else:my_dict[el] += 1
b = list(my_dict.items())
b.sort(key=lambda x: x[1], reverse=True)
for el in b[:5]:
    print(el[0])


lemma_list = []
for el in new_list:
    el = morph.parse(el)[0]
    el = el.normal_form
    lemma_list.append(el)

my_dict1 = {}
for el in lemma_list:
    if el not in my_dict1:
        my_dict1[el] = 1
    else:my_dict1[el] += 1
b1 = list(my_dict1.items())
b1.sort(key=lambda x: x[1], reverse=True)
for el in b1[:5]:
    print(el[0])
