# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples both are data structures that can contain information. One primary difference is that tuples are however immutable. Lists on the other hand, are ordered structures that have can have entries added or removed. For tuples to have a similar effect, a new one would have to be created. Tuples are formed such that each position has different designations as types of data. Lists have each position being the same type of data. Tuples work better as a dictionary key as they cannot be changed. 

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets are both collections of elements, however sets are an unordered collection of unique elements while lists are ordered collection of elements.  
List example : 
```python
list_example = [3, 4, 5, 5, 8]  
list_example.pop  
```  
Set example :
```python  
set_example = {3, 4, 5, 8}  
3 in set_example  
```  
Sets should be quicker at finding an element as they are unique, while in a list elements are not necessarily unique.  
---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> lambda is a keyword used for creating functions with a single expression.  
lambda example :  
```python  
sorted(example_tuples, key = lambda ex: ex[1]) #Sorted by index 1  
``` 

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are ways to construct a list in a simple manner.
```python  
lc_example = [x**2 for x in range(10)]  
map_example = list(map(lambda x: x**2, range(10)))  

lc_example2 = [x for x in lc_example if x % 2 == 0]  
filter_example = list(filter(lambda x: x % 2 == 0, lc_example))  
```  

Map applies to a function all the items in the input_list.  Filter creates a list of elements for which a function returns true. The functions have fairly different purposes.  

```python  
set_example = { x**2 for x in range(10)}  
dict_example = {x:x**2 for x in range(10)}  
```  

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days  

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days  

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days  

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





