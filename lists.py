Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #list of items in grocery store
>>> item1="bread"
>>> item2="pasta"
>>> item3="fruits"
>>> #here we have to create too many variables thus we need lists
>>> items=["bread","pasta","fruits","veggies"]
>>> items
['bread', 'pasta', 'fruits', 'veggies']
>>> items[0]
'bread'
>>> items[2]
'fruits'
>>> items[0]='chips'
>>> items
['chips', 'pasta', 'fruits', 'veggies']
>>> items[0:2]
['chips', 'pasta']
>>> items[-1]
'veggies'
>>> items=["bread","pasta","fruits","veggies"]
>>> items
['bread', 'pasta', 'fruits', 'veggies']
>>> items.append("butter")
>>> items
['bread', 'pasta', 'fruits', 'veggies', 'butter']
>>> items=["bread","pasta","fruits","veggies"]
>>> items
['bread', 'pasta', 'fruits', 'veggies']
>>> items.insert(1,'butter')
>>> items
['bread', 'butter', 'pasta', 'fruits', 'veggies']
>>> #joining two lists
>>> food=["bread","pasta","fruits"]
>>> bathroom=["shampoo","soap"]
>>> items=food+bathroom
>>> items
['bread', 'pasta', 'fruits', 'shampoo', 'soap']
>>> food+"soda"
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    food+"soda"
TypeError: can only concatenate list (not "str") to list
>>> #can't concatinate list with string
>>> len(items)
5
>>> "bread" in items
True
>>> "soda" in items
False
>>> 