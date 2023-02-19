import string
alpha =  string.ascii_lowercase + string.ascii_uppercase
print(alpha)
name = '  3  bello hellop ep bango ban ji hello, bangoban '
short = ''

for i in range(len(name)):
    if name[i] == ',':
        break
    else:
        if i == 0 and name[i] in alpha :
            short += name[i].upper()
        elif name[i] == ' ':
            pass
        elif name[i-1] == ' ':
            short += name[i].upper()


            
        
print(short)