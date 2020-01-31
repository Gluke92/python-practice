Q.Python is an interpreted language. What does that mean?

Interpreted languages don't have to be compiled. PHP, and Ruby are other types

Q.Python is dynamically typed. What does that mean?

Unlike static typed languages, the python interpreter will assign types. You don't have to put it in.

Q.Python can be slow. How do you optimize it?
Python uses C-based extensions, which removes the bottleneck in Python compiling. Num-Py for crunching numbers removes bottleneck in Python compiling

Q. What is a Python dictionary?
It's a 1:1 relationship between key:value, indexed in memory by keys.

Q. What is *args, and what is *kwargs?
If you want multiple paramters, or multiple keywords in yoru function, you can use * to indicate that more than one argument, or keyword, is expected.

Paramters are arguments we pass in to the function at definition. Arguments are passed in when the function is called. *args indicates that the function, when called, will take multiple arguments. *kwargs indicates that the function can be assigned multiple key-value pairs when called. 

Q. What is the negative index in ptyhon?
Negative indexes begin at the end of a string in python

Q. What's the try-except-else statement? When does else run?

Else runs when there's no error.
If there's an except block, then we should hopefully break out

Q. What is floor division?
Rather than % (modulo) or / (division), // (floor division) floors the output that you get. E.g, the output goes to the next integer.

Q. How would your randomize a list?
Import random library, use it to randomize

Q. How is memory managed in Python?
Heap-space. Python has a built-in garbage can to get rid of unnecessary memory allocated after function runs

Q. Are arguments in Python passed in by value or reference?
Everything in Python is passed in as an object. All variables are references pointing to those objects.

Q. What are the immutable and mutalbe types?

3 Mutable - Lists, Sets, Dictionaries (can be modified)

3 Immutables - Str, Numbers, Tuples (can't be modified)

------

Linked Lists - a data struture where each item points to another item, and the structure terminates when the last item points to null

