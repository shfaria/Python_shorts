import string
alpha =  string.ascii_lowercase + ' ' + string.ascii_uppercase
name = 'Military Institute of Science and Technology (MIST)'
name = name.split(' ')
print(name) 
alist =[]
for i in name:
    if i == 'of' or 'and' or '&' or 'for':
        pass
    if i==',':
        pass
    if i.startswith('('):
        pass
    else:
        alist.append(i[0].upper())
print(alist)
short = ''
for i in range(len(name)):
    if not name[i] in alpha:
        break
    else:
        if i == 0 and name[i] in alpha :
            short += name[i].upper()
        elif name[i] == ' ':
            pass
        elif name[i-1] == ' ':
            short += name[i].upper()

print(short)