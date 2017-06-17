Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = {}
>>> a = {"id":101,"name":"Ram"}
>>> a
{'id': 101, 'name': 'Ram'}
>>> a.id
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a.id
AttributeError: 'dict' object has no attribute 'id'
>>> a.keys()
dict_keys(['id', 'name'])
>>> a.values()
dict_values([101, 'Ram'])
>>> for i in a:
	print(i)

id
name
>>> for i in a.items():
	print(i)

('id', 101)
('name', 'Ram')
>>> for i in a.values():
	print(i)

101
Ram
>>> a = {"id":[1,2,3],"name":["Ram","Shyam","Gopal"]}
>>> a
{'id': [1, 2, 3], 'name': ['Ram', 'Shyam', 'Gopal']}
>>> for i in a.values():
	print(i)

[1, 2, 3]
['Ram', 'Shyam', 'Gopal']
>>> x = [{"id":[1,2,3],"name":["Ram","Shyam","Gopal"]},{"age":[20,21,22],"Salary":[12000,15000,50,000]}]
>>> for i in x:
	print(i)

{'id': [1, 2, 3], 'name': ['Ram', 'Shyam', 'Gopal']}
{'age': [20, 21, 22], 'Salary': [12000, 15000, 50, 0]}
>>> a = (1,"Hello",12.5,True)
>>> a
(1, 'Hello', 12.5, True)
>>> x = ["Hello",1,2,3,4,5,"Bye"]
>>> x[1]
1
>>> x[0]
'Hello'
>>> x[1:4]
[1, 2, 3]
>>> x[0] = "Python"
>>> x
['Python', 1, 2, 3, 4, 5, 'Bye']
>>> a
(1, 'Hello', 12.5, True)
>>> a[0]
1
>>> a[0] = "Python"
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    a[0] = "Python"
TypeError: 'tuple' object does not support item assignment
>>> del(a[0])
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    del(a[0])
TypeError: 'tuple' object doesn't support item deletion
>>> 
