my_dict={'Gennadiy':1949,'Maxim':1983,'Sergey':1998,'Marya':2004}
print('Жили-были:',my_dict)
print('А младшенькая родилась:',my_dict['Marya'])
print('Мечтала она о братике по имени maxik:',my_dict.get('Maxik'))
my_dict.update({'Roman':1971,'Natalya':1972})
print('А люди приходили:',my_dict)
Death = my_dict.pop('Gennadiy')
print('и уходили:',Death,' RIP')
print('Оставшиеся погоревали, но жить продолжали:',my_dict)
my_set = {1,4,8,8,8,9,'лекарство','пеницилин','пеницилин',1,2,6,1,2,6}
print(my_set)
my_set.remove(4), my_set.remove(9), my_set.add(16), my_set.add(25)
print(my_set)