text = """song abrac ones abracadabra one !!! One two tree, golden one push push one
            computer and or. one One two tree, golden abracadabra one one One two tree , golden abracadabra
            one One two abracadabra tree, golden golden abrac"""

with open("mod_15.txt", 'w', encoding="utf8" ) as myFile:
    myFile.write((text))

with open('mod_15.txt', encoding='utf8') as mf:
    a = mf.read()
# def changeText(text):

for i in '!"\'#$%&()*+-,/:;<=>?@[\\]^_{|}~': # избавляемся от символов
    a = a.replace(i, '')

a= a.split() # переводим текст в список слов
# fileText = text
az = len(a)
print ('Получаем список')
print (a)
print ("всего слов", az)

al='' # ищем самое длинное тексто в слове

for j in range(az):
    count = 0
    for i in range(az):
        if len(a[i])> len(al):
            al = a[i]
            count += 1
print ('самое длинное слово ',  al)


n_a = [] # новый список без повторений. но с числом количества повторов
a_l = [] # подсчет повторений с запоминанием числа повторов
lsr = 3 # сколько повторяющихся слов вывести
lenght = 3 # только слова больше N сиволов
print (f'ищем самое повторяющеся слово. у которого длина больше чем три символа,\n выводим первые {lsr} слова.')
qty_most_common = 0
for item in a:
    if len(item) > lenght:   #не рассматириваем слова меньше length символов
        qty = (a.count(item))
        a_l = (qty, item)
        n_a.append(a_l)

n_a = list(set(n_a))
n_a = (sorted (n_a, key=lambda n_a: n_a[0], reverse=True)) # разворачиваем список

a_l=[] # подсчет повторений с запоминанием числа повторов(обнуляемб можно было придумать новый список)
for i in range(lsr):
    a_l.append(n_a[i])
print (a_l)





