Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print("Hello \n world")
Hello 
 world
>>> print(r"Hello \n world")
Hello \n world
>>> a = "Salary of Ram is 25000 and Salary of Shyam is 32000"
>>> import re
>>> re.search("Ram",s)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    re.search("Ram",s)
NameError: name 's' is not defined
>>> re.search("Ram",a)
<_sre.SRE_Match object; span=(10, 13), match='Ram'>
>>> re.search("Rama",a)
>>> str = "Win 100000$ and iphone....call@80980980"
>>> str = "Hey Ravi, Win 100000$ and iphone, participate in GK Quiz for that...by Amit"
>>> a.group()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a.group()
AttributeError: 'str' object has no attribute 'group'
>>> x = re.search("Ram",s)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    x = re.search("Ram",s)
NameError: name 's' is not defined
>>> x = re.search("Ram",a)
>>> x
<_sre.SRE_Match object; span=(10, 13), match='Ram'>
>>> x.group()
'Ram'
>>> a = "Hello ravi@gmail.com ...blah blah blah by amit@gmail.com"
>>> x = re.search('[A-Z]')
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    x = re.search('[A-Z]')
TypeError: search() missing 1 required positional argument: 'string'
>>> x = re.search('[A-Z]', a)
>>> x
<_sre.SRE_Match object; span=(0, 1), match='H'>
>>> x = re.search('[a-z]', a)
>>> x
<_sre.SRE_Match object; span=(1, 2), match='e'>
>>> x = re.findall('[a-z]', a)
>>> x
['e', 'l', 'l', 'o', 'r', 'a', 'v', 'i', 'g', 'm', 'a', 'i', 'l', 'c', 'o', 'm', 'b', 'l', 'a', 'h', 'b', 'l', 'a', 'h', 'b', 'l', 'a', 'h', 'b', 'y', 'a', 'm', 'i', 't', 'g', 'm', 'a', 'i', 'l', 'c', 'o', 'm']
>>> x = re.search('[\w]+@[\w]', a)
>>> x
<_sre.SRE_Match object; span=(6, 12), match='ravi@g'>
>>> x = re.search('[\w]@[\w]', a)
>>> x
<_sre.SRE_Match object; span=(9, 12), match='i@g'>
>>> x = re.search('[A-Z]', a)
>>> x
<_sre.SRE_Match object; span=(0, 1), match='H'>
>>> x = re.search('[A-Z]+', a)
>>> x
<_sre.SRE_Match object; span=(0, 1), match='H'>
>>> x = re.search('[A-Z]+\w', a)
>>> x
<_sre.SRE_Match object; span=(0, 2), match='He'>
>>> x = re.search('[A-Z]+\w+', a)
>>> x
<_sre.SRE_Match object; span=(0, 5), match='Hello'>
>>> x = re.search('[\w]+@+', a)
>>> x
<_sre.SRE_Match object; span=(6, 11), match='ravi@'>
>>> x = re.search('[\w]+@[\w]', a)
>>> x
<_sre.SRE_Match object; span=(6, 12), match='ravi@g'>
>>> x = re.search('[\w]+@[\w]+', a)
>>> x
<_sre.SRE_Match object; span=(6, 16), match='ravi@gmail'>
>>> x = re.search('[\w]+@[\w.]+', a)
>>> x
<_sre.SRE_Match object; span=(6, 20), match='ravi@gmail.com'>
>>> a = "Hello ravi_12@gmail.com ...blah blah blah by amit-abcd@gmail.com"
>>> x = re.search('[\w]+@[\w.]+', a)
>>> x
<_sre.SRE_Match object; span=(6, 23), match='ravi_12@gmail.com'>
>>> a = "Hello ravi-12@gmail.com ...blah blah blah by amit-abcd@gmail.com"
>>> x = re.search('[\w]+@[\w.]+', a)
>>> x
<_sre.SRE_Match object; span=(11, 23), match='12@gmail.com'>
>>> x = re.search('[\w-]+@[\w.]+', a)
>>> x
<_sre.SRE_Match object; span=(6, 23), match='ravi-12@gmail.com'>
>>> x = re.findall('[\w-]+@[\w.]+', a)
>>> x
['ravi-12@gmail.com', 'amit-abcd@gmail.com']
>>> 
