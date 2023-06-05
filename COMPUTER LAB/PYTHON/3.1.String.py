#string
a= ('hey there!')       #single quoted
b= ("hey there!")       #double quoted
c= ('''hey there!''' )  #triple quoted


#slicing
sa= a[1:4]
print(sa)

sb= a[:8]
print(sb)

sc= a[0:]
print(sc)

se= a[0:5]
print(se)

#skip number while slicing
sc= a[0:6:2]
print(sc)

sd= b[-5:-2]
print(sd)