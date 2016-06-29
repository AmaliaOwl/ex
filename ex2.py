import re

def func(address):
    f = open(address, 'r', encoding = 'utf-8')
    arr = f.readlines()            
    for line in arr:
        srch = re.findall('[А-Я]\. [А-Я][а-я]{2,30}', line)
        for line in srch:
            if line:
                print(line)
     for line in arr:
         srch2 = re.findall('([А-Я]\. ){1,2}[А-Я]{1}[а-я]{2,30}', line)
         for line in srch2:
            if line:
                print(line)
    f.close()


    

arr = func('C:\\Users\\student\\Desktop\\zamok.txt')




