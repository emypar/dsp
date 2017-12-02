# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both lists and tuples are sequence types and support slicing and
   indexing. However the lists are mutable: an element can be changed
   in place, or more elements can be appended to it, whereas tuples
   are immutable. Because tuples are immutable they can be used as
   keys in dictionaries (provided that all their elements are
   immutable as well).

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> A set is an unordered collection of distinct hashable objects
>> wheras a list is an ordered sequence which allows duplicates. Sets
>> are very efficient for removing duplicates and testing membership
>> because the lookup works in constant time O(0), unlike lists which
>> require linear time O(n), n being the size of the list.
>>
>>     a_list = [1, 1, 2, 4, 2, 1]
>>     a_list_no_dups = set(a_list)
>>
>> The following lookups yield the same result
>>
>>     i in a_list
>>     i in a_list_no_dups
>>
>> the latter being more efficient.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> lambda's are anonymous functions restricted to a single
>> expression. They are typically used where a small function is
>> needed as an argument.
>>
>> Example: sort a list of tuples by the 2nd element:
>>
>>      a_list = [(1, 10), (2, 9), (3, 8)]
>>      sorted(a_list, key=lambda x: x[1])
>>
>> will result into
>>
>>      [(3, 8), (2, 9), (1, 10)
---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List (or set/dictionary) comprehensions represent convenient
>> shortcut methods for building objects. They consist of an
>> expression with arguments taking values from a sequence/iterable
>> subject to optional conditions.
>>
>> List example: given a list of integers, build the list of squares for
>> multiples of 3:
>>
>>      int_list = range(13, 111)
>>      m3_squares = [i**2 for i in int_list if not i % 3]
>>
>> the same can be achieved by using map over a (filtered) list:
>>
>>      m3_squares = map(lambda i: i**2, filter(lambda i: not i % 3,
>>                                              int_list))
>>
>> Set example: build the set of unique characters used in a text:
>>
>>      text = 'This is the text for which we have to find ' + \
>>             'all unique characters, case insensitive.'
>>
>>      text_chars = {c for c in text.lower()}
>>
>> Dictionary example: build a cache for square root of frequently
>> needed numbers:
>>
>>      freq_nums = [1.1, 2.34, 19, 8]
>>      sqrt_cache = {x: x**.5 for x in freq_nums}
>>
---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





