import collections


d = collections.OrderedDict(one=1, two=2, three=3)
print(d)
d['four'] = 4
print(d)


dd = collections.defaultdict(list)
# Попытка доступа к отсутствующему ключу его создает и
# инициализирует, используя принятую по умолчанию фабрику,
# то есть в данном примере list():
dd['собаки'].append('Руфус')
dd['собаки'].append('Кэтрин')
dd['собаки'].append('Сниф')
print(dd['собаки'])


dict1 = {'один': 1, 'два': 2}
dict2 = {'три': 3, 'четыре': 4}
chain = collections.ChainMap(dict1, dict2)
# ChainMap выполняет поиск в каждой коллекции в цепочке
# слева направо, пока не найдет ключ (или не потерпит неудачу):
print(chain['три'])
print(chain['один'])
print(chain['отсутствует'])


from types import MappingProxyType
writable = {'один': 1, 'два': 2}  # доступный для обновления
read_only = MappingProxyType(writable)
print(read_only['один'])
# read_only['один'] = 23
# Обновления в оригинале отражаются в прокси:
writable['один'] = 42
print(read_only)
