# Linked List exploration

obj1 = {'a': True}
obj2 = obj1
obj1['a']= 'booya'
del obj1
obj2 = 'hello'
# print(obj1)
print(obj2)

#Python is garbage collected.
#if we delete the value the pointer is pointing to,
#the objects will be undefined and need
#to be reassigned

