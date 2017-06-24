Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = [12,33,45,123,56,78,4,1,6,7]
>>> a.sort()
>>> print(a.sort())
None
>>> x = a.sort()
>>> x
>>> a.sort(True)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a.sort(True)
TypeError: must use keyword argument for key function
>>> sort(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    sort(a)
NameError: name 'sort' is not defined
>>> sorted(a)
[1, 4, 6, 7, 12, 33, 45, 56, 78, 123]
>>> sorted(a, reversed=True)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    sorted(a, reversed=True)
TypeError: 'reversed' is an invalid keyword argument for this function
>>> sorted(a, reverse=True)
[123, 78, 56, 45, 33, 12, 7, 6, 4, 1]
>>> a = ['a','c','e','z','b','x','f']
>>> sorted(a)
['a', 'b', 'c', 'e', 'f', 'x', 'z']
>>> a = ['Ram','Akash','Zayn','Deepak']
>>> sorted(a)
['Akash', 'Deepak', 'Ram', 'Zayn']
>>> a = ['Ram','Akash','Zayn','Deepak','Ashish']
>>> sorted(a)
['Akash', 'Ashish', 'Deepak', 'Ram', 'Zayn']
>>> a = ['Ram','Akash','Zayn','Deepak','Ashish','Akash']
>>> sorted(a)
['Akash', 'Akash', 'Ashish', 'Deepak', 'Ram', 'Zayn']
>>> a = [[101,'Ram',7.8],[102,'Shyam',6.8],[103,'Akash',9.7]]
>>> sorted(a)
[[101, 'Ram', 7.8], [102, 'Shyam', 6.8], [103, 'Akash', 9.7]]
>>> a = [[101,'Ram',7.8],[106,'Shyam',6.8],[103,'Akash',9.7],[100,'Zayn',5.7]]
>>> sorted(a)
[[100, 'Zayn', 5.7], [101, 'Ram', 7.8], [103, 'Akash', 9.7], [106, 'Shyam', 6.8]]
>>> sorted(a[1])
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    sorted(a[1])
TypeError: '<' not supported between instances of 'str' and 'int'
>>> a = ["red","green"]
>>> b = a
>>> b
['red', 'green']
>>> b[1] = "blue"
>>> v
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    v
NameError: name 'v' is not defined
>>> b
['red', 'blue']
>>> a
['red', 'blue']
>>> a = ["red","green","blue"]
>>> b = a[:]
>>> b[0] = "yellow"
>>> b
['yellow', 'green', 'blue']
>>> a
['red', 'green', 'blue']
>>> a = ["red","green","blue",["abc","def","ghi"]]
>>> b = a[:]
>>> b[3][1]
'def'
>>> b[3][0]
'abc'
>>> b[3][0] = "Ram"
>>> a
['red', 'green', 'blue', ['Ram', 'def', 'ghi']]
>>> b = slice(a)
>>> b
slice(None, ['red', 'green', 'blue', ['Ram', 'def', 'ghi']], None)
>>> b[:2]
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    b[:2]
TypeError: 'slice' object is not subscriptable
>>> b = a.copy()
>>> b
['red', 'green', 'blue', ['Ram', 'def', 'ghi']]
>>> b[3][0] = "Shyam"
>>> b
['red', 'green', 'blue', ['Shyam', 'def', 'ghi']]
>>> a
['red', 'green', 'blue', ['Shyam', 'def', 'ghi']]
>>> import copy
>>> b = copy.deepcopy(a)
>>> b
['red', 'green', 'blue', ['Shyam', 'def', 'ghi']]
>>> b[3][0] = "Ram"
>>> b
['red', 'green', 'blue', ['Ram', 'def', 'ghi']]
>>> a
['red', 'green', 'blue', ['Shyam', 'def', 'ghi']]
>>> a = {"id":101,"name":"Ram","cgpa":7.6}
>>> a["name"] = "Shyam"
>>> a
{'id': 101, 'name': 'Shyam', 'cgpa': 7.6}
>>> 
