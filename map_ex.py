d1 = {1:'a',2:'c'}
print(type(d1))
print(d1)
print(d1[1]) # d[key]
d1.get(3,'NA')
d1[0] = 'aa'
keys = list(d1.keys())
print(d1.keys())
print(d1.values())
print(d1.items())
d1[0]='suraj'
for k, v in d1.items():
    print(k, '|',v)

#update dict
d4 = {'name':'suraj','sal':20000}
d5 = {'sal':90000,'city':'Mumbai'}
d4.update(d5)

#copy dict
d6 = d4
d7 = d4.copy()

#clear dict
d7.clear()
l1 = ['name','sal','city']
default_value = 'UNKNOWN'
d8 = dict.fromkeys(l1, default_value)
default_value = [1,2,3]
d9 = dict.fromkeys(l1, default_value)


field_name = ['name','sal','city']
values = ['surajj','30888','Pune']

d10 = {field_name[i]:values[i] for i in range(len(field_name))}

