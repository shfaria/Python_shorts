import string
alpha =  string.ascii_lowercase + ' ' + string.ascii_uppercase
name = ' Jagannath  University '
name = name.split(' ')
print(name) 
alist =[]
for i in name:
    print(i)
    if i in ['of' , 'and' , '&' , 'for' , ',', '', ' ']:
        pass
    elif i.startswith('(') and i.endswith(')'):
        i =i[1:-1]
        b = i
        break
        # pass
    else:
        alist.append(i[0].upper())
        b=''.join(alist)
print(alist)
print(b)
