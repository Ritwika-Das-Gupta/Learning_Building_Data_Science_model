Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text="ice cream"
>>> text
'ice cream'
>>> text[0]
'i'
>>> text[1]
'c'
>>> text[0]=='g'
False
>>> text[0]='g'
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    text[0]='g'
TypeError: 'str' object does not support item assignment
>>> # Strings are immutable cant be changed once stored in python thus text[0] cant be g
>>> #Substring
>>> text[0:3]
'ice'
>>> text[4:9]
'cream'
>>> text[4:]
'cream'
>>> text[:3]
'ice'
>>> text="hello"
>>> text='hello'
>>> text='let's learn python'
SyntaxError: invalid syntax
>>> text="Let's learn python"
>>> text='hello "world"'
>>> text
'hello "world"'
>>> address="1 purple street
SyntaxError: EOL while scanning string literal
>>> address=''' 1 purple stree
new york
usa'''
>>> address
' 1 purple stree\nnew york\nusa'
>>> #concatinate:
>>> s1="hello"
>>> s2="world"
>>> s1+s2
'helloworld'
>>> s1+' '+s2
'hello world'
>>> s="total states in USA is:"
>>> num=25
>>> s+num
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    s+num
TypeError: can only concatenate str (not "int") to str
>>> str(num)
'25'
>>> s+str(num)
'total states in USA is:25'
>>> 