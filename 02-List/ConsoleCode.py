Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = []
>>> a = [1,2,3,4,5,6]
>>> print(a)
[1, 2, 3, 4, 5, 6]
>>> a = [1,"Hi",10.5,True,12]
>>> print(a)
[1, 'Hi', 10.5, True, 12]
>>> for i in a:
	print(i)

1
Hi
10.5
True
12
>>> i
12
>>> a = []
>>> a.append(10)
>>> a
[10]
>>> a.append("Hello")
>>> a
[10, 'Hello']
>>> a.append(10,12,"Hi")
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a.append(10,12,"Hi")
TypeError: append() takes exactly one argument (3 given)
>>> a.append([10,12,"Hi"])
>>> a
[10, 'Hello', [10, 12, 'Hi']]
>>> len(a)
3
>>> a.insert("Python")
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a.insert("Python")
TypeError: insert() takes exactly 2 arguments (1 given)
>>> a.insert(0,"Python")
>>> a
['Python', 10, 'Hello', [10, 12, 'Hi']]
>>> a.insert(6,"Python")
>>> a
['Python', 10, 'Hello', [10, 12, 'Hi'], 'Python']
>>> a.insert(6,"ML")
>>> a
['Python', 10, 'Hello', [10, 12, 'Hi'], 'Python', 'ML']
>>> a.extend("This","is","Python","Programming")
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a.extend("This","is","Python","Programming")
TypeError: extend() takes exactly one argument (4 given)
>>> a.extend(["This","is","Python","Programming"])
>>> a
['Python', 10, 'Hello', [10, 12, 'Hi'], 'Python', 'ML', 'This', 'is', 'Python', 'Programming']
>>> a.pop()
'Programming'
>>> a
['Python', 10, 'Hello', [10, 12, 'Hi'], 'Python', 'ML', 'This', 'is', 'Python']
>>> a.pop()
'Python'
>>> a.remove(10)
>>> a
['Python', 'Hello', [10, 12, 'Hi'], 'Python', 'ML', 'This', 'is']
>>> a.remove('Python')
>>> a
['Hello', [10, 12, 'Hi'], 'Python', 'ML', 'This', 'is']
>>> del(a[1])
>>> a
['Hello', 'Python', 'ML', 'This', 'is']
>>> 
 RESTART: E:/Python/Python_Batches/MachineLearning_WE_Morning/02-List/01-ListIntro.py 
>>> 
 RESTART: E:/Python/Python_Batches/MachineLearning_WE_Morning/02-List/01-ListIntro.py 
Exist
>>> a
['This', 'is', 'Python', 'Prigramming...', 'Python', 'is', 'Awseome']
>>> a
['This', 'is', 'Python', 'Prigramming...', 'Python', 'is', 'Awseome']
>>> 
 RESTART: E:/Python/Python_Batches/MachineLearning_WE_Morning/02-List/01-ListIntro.py 
Exist
>>> a
['This', 'is', 'Python', 'Programming...', 'Python', 'is', 'Awseome']
>>> a.index("Python")
2
>>> a.index("Python")
2
>>> 
 RESTART: E:/Python/Python_Batches/MachineLearning_WE_Morning/02-List/01-ListIntro.py 
2
2
>>> 
 RESTART: E:/Python/Python_Batches/MachineLearning_WE_Morning/02-List/01-ListIntro.py 
2
2
>>> a
['This', 'is', 'Python', 'Programming...', 'Python', 'is', 'Awseome']
>>> a.count("Python")
2
>>> a.index("Python")
2
>>> 
 RESTART: E:/Python/Python_Batches/MachineLearning_WE_Morning/02-List/01-ListIntro.py 
Traceback (most recent call last):
  File "E:/Python/Python_Batches/MachineLearning_WE_Morning/02-List/01-ListIntro.py", line 10, in <module>
    print(a[i])
TypeError: list indices must be integers or slices, not str
>>> 
 RESTART: E:/Python/Python_Batches/MachineLearning_WE_Morning/02-List/01-ListIntro.py 
0
1
2
3
2
1
6
>>> a[2]
'Python'
>>> a[4]
'Python'
>>> 
 RESTART: E:/Python/Python_Batches/MachineLearning_WE_Morning/02-List/01-ListIntro.py 
Traceback (most recent call last):
  File "E:/Python/Python_Batches/MachineLearning_WE_Morning/02-List/01-ListIntro.py", line 12, in <module>
    del(a[i])
TypeError: list indices must be integers or slices, not str
>>> 
 RESTART: E:/Python/Python_Batches/MachineLearning_WE_Morning/02-List/01-ListIntro.py 
Python
Python
>>> 
 RESTART: E:/Python/Python_Batches/MachineLearning_WE_Morning/02-List/01-ListIntro.py 
This
is
Python
Python
Awseome
>>> 
 RESTART: E:/Python/Python_Batches/MachineLearning_WE_Morning/02-List/01-ListIntro.py 
This
is
Python
Python
Awseome
>>> 
 RESTART: E:/Python/Python_Batches/MachineLearning_WE_Morning/02-List/01-ListIntro.py 
This
is
Python
Python
Awseome
>>> 
 RESTART: E:/Python/Python_Batches/MachineLearning_WE_Morning/02-List/01-ListIntro.py 
This
is
Python
2
Programming...
Python
2
is
Awseome
>>> 
 RESTART: E:/Python/Python_Batches/MachineLearning_WE_Morning/02-List/01-ListIntro.py 
This
is
Python
2
Python
3
Awseome
>>> 
 RESTART: E:/Python/Python_Batches/MachineLearning_WE_Morning/02-List/01-ListIntro.py 
This
is
Python
Python
Awseome
>>> a
['This', 'is', 'Programming...', 'is', 'Awseome']
>>> 
 RESTART: E:/Python/Python_Batches/MachineLearning_WE_Morning/02-List/01-ListIntro.py 
This
is
2
Python
3
Python
Awseome
>>> 
 RESTART: E:/Python/Python_Batches/MachineLearning_WE_Morning/02-List/01-ListIntro.py 
2
3
Awseome
>>> a
['This', 'is', 'Programming...', 'is', 'Awseome']
>>> 
 RESTART: E:/Python/Python_Batches/MachineLearning_WE_Morning/02-List/01-ListIntro.py 
['This', 'is', 'Python', 'Programming...', 'Python', 'is', 'Awseome']
['This', 'is', 'Python', 'Programming...', 'Python', 'is', 'Awseome']
2
['This', 'is', 'Programming...', 'Python', 'is', 'Awseome']
3
['This', 'is', 'Programming...', 'is', 'Awseome']
['This', 'is', 'Programming...', 'is', 'Awseome']
>>> 
 RESTART: E:/Python/Python_Batches/MachineLearning_WE_Morning/02-List/01-ListIntro.py 
This
is
Python
Programming...
Python
is
Awseome
This
is
Python
Programming...
Python
is
Awseome
This
is
Programming...
Python
is
Awseome
This
is
Programming...
is
Awseome
This
is
Programming...
is
Awseome
>>> 
 RESTART: E:/Python/Python_Batches/MachineLearning_WE_Morning/02-List/01-ListIntro.py 
['This', 'is', 'Programming...', 'is', 'Awseome']
>>> 
 RESTART: E:/Python/Python_Batches/MachineLearning_WE_Morning/02-List/01-ListIntro.py 
['This', 'is', 'Programming...', 'is', 'Awseome']
This
is
Programming...
is
Awseome
>>> 
 RESTART: E:/Python/Python_Batches/MachineLearning_WE_Morning/02-List/01-ListIntro.py 
This
is
Programming...
is
Awseome
>>> 
 RESTART: E:/Python/Python_Batches/MachineLearning_WE_Morning/02-List/01-ListIntro.py 
This
is
Programming...
is
Awseome
>>> 
