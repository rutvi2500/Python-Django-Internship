#26/05/2021

#variables
n1=10
n2=10.5
name='Rutvi'
print(n1)
print("n2 is",n2)
print("name is",name)

#variables in single line
x1,x2,Name=10,20.5,'Rutvi Patel'
print(x1)
print("x2 is",n2)
print("Name is",Name)

#Same value of multiple variables
n1=n2=name=10
print(n1)
print("n2 is",n2)
print("name is",name)

#Datatypes
#Number Datatype
a1=10
a2=10+2j
print(a1, type(a1))          #type(a1) will show the datatype i.e. int
print(a2,type(a2))
print("a2 is",isinstance(a2,complex))   #campare whether a2 is complex or not

#String Datatype
name="Rutvi Patel"
print(name)
print(name[2])
print(name[1:5])
print(name[3:])
print(name[:4])
print(name*2)
print("name is "+name)      #concate

#List Datatype
l1=[5,10.5,20.3,'Rutvi']

print(l1)
print(type(l1))
print(l1[1])
print(l1[1:3])
print(l1[2:])
print(l1[:3])

#Tupple Datatype
t1=(5,10.5,20.3,'Rutvi')
print(t1)
print(type(t1))
print(t1[1])
print(t1[1:3])
print(t1[2:])
print(t1[:3])

#Dictionary Datatype
d1={10:'Hello','a1':100,20:200}

print(d1)
print(type(d1))
print(d1[10])
print(d1['a1'])
print(d1[20])





