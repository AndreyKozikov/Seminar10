# Задача 44
 
 В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
 Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
```
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
```

Условием домашнего задания не было определено создать ли таблицу вида One Hot в сущействующем DataFrame или в новом.
При выполнении исходим из создания в существующем DataFrame.
Для создания таблицы в новом DataFrame просто создадим новый и цикл перепишем, заменив имя DataFrame на новый