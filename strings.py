course = "Python's for Beginners" #have double quotes for something with an " ' "
course = 'Python for "Beginners"' #have a single quote for something with ' " '
course = '''Python's for "Beginners"''' ##have this for something for triple quotes... or this can work for this:
course = '''
Hi John,

Here is our first email to you.

Thank you, 
Support Team


''' #Multi-line
course = 'Python for Beginners' #something simple for the purpose for indexing
'''INDEXES IN PYTHON:

   print(course[1]) -- this gets the first string in "course" = Output P
   print(course[-1]) -- this get the last string in "course" = Output s
   print(course[-2]) -- this gets the second to last string in "course" = Output r
   print(course[0:3]) -- this gets indexs 0-2 in the string "course"
   print(course[0:]) -- this gets everything, just like using "course" without the indexes
   print(course[1:]) -- this gets everything from index 1 to the end of the string
   print(course[:5]) -- this gets eveything from index 0 up until 5
'''
another = course[:]
print(another)