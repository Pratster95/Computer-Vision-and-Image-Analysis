
# coding: utf-8

# # Module 1, Lab 1: Introduction to Azure Notebooks and Python 3.
# 
# In this lab, we are going to give you a very basic introduction to Microsoft Azure Notebooks and to Python 3.
# 
# *Microsoft Azure Notebooks* (https://notebooks.azure.com/) is a free service that provides *Jupyter Notebooks* (http://jupyter.org/) along with supporting packages for R, Python and F#.  We'll be focusing on Python for the purposes of this course, and using it with the Microsoft Cognitive Toolkit.  Azure Notebooks already contain all the libraries and dependencies you will need to run the labs for this course setup for you.
# 
# 
# ## What is Python?
# 
# Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.  It supports modules and packages, encouraging modularity in design, and code reuse. There are two main variants of Python in use currently - 2.x (which an older lineage that is still quite popular), and 3.x (which is the new and improved version of Python).  We'll be focusing on Python 3.5 in this course.
# 
# It also comes with an extensive set of libraries. We'll be using some of these libraries, in particular NumPy in this course. 
# 
# NumPy is a Python library that provides a multidimensional array object (and various related objects derived from this, and a powerful collection of routines for fast operation on arrays - including math, linear algebra, statistics and more.
#                                                                          
# The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed.  If you plan on running our labs locally, perhaps on a machine acceleratedwith an Nvidia GPU, we recommend the use of the Anaconda distribution of the Python as it may simplify setup for you for Jupyter Notebooks. Follow the link (https://www.anaconda.com/download/) to the Anaconda download page where you can learn more about Anaconda.
# 
# 
# The Microsoft Cognitive toolkit has detailed instructions on how to setup from scratch using Anaconda - see https://docs.microsoft.com/en-us/cognitive-toolkit/Setup-CNTK-on-Windows.
# 

# ## Working in Azure Notebook
# 
# Your Azure (Jupyter) Notebook consists of a number of cells. When you create a new notebook,  it will have a single empty cell.
# 
# Cells have types - the most important of which for our purposes are `Markdown` (which is a simple formatting syntax -- these descriptive cells are written in Markdown), or `Code` (which is for Python 3.5 code).
# 
# You can change the type of a cell by using the dropdown control above.
# 
# You can enter code directly into a cell marked as type `Code` and run it by clicking on the Run button, by selecting `Cell->Run Cells` from the menu, or by typing `SHIFT` + `Return`.
# 
# ![Run Cells](images/runCells-AzureNotebooks.png "Run Cells")
# 
# 
# If the cell outputs something, this will be visible right underneath it.  Try running the following cell...

# In[1]:


print ("Hello, World!")


# You'll also see `In [x]` to the left of the cell. The number indicates the order in which the interpreter has run the code cells in the notebook. If the interpreter is busy running a cell,
# you will see `In [*]` there instead, and the number will replace the `*` character when the cell has completed running.

# Markdown text which isn't run yet shows as source. You can run this too and it will format the 
# Markdown for you.  Try pressing `SHIFT` + `Return` in this cell for an example.
# 
# A full list of hotkeys is available in the menu `Help->Keyboard Shortcuts`. This might help you get an overview of 
# how you can interact with the notebook. 

# ## New Cells
# 
# You can add new cells via the `Insert` menu above. You can select `Insert Cell Above` or `Insert Cell Below`.  
# 
# ![Insert Menu](images/insertMenu-AzureNotebooks.png "Insert Menu")
# 
# You can also delete cells by selecting `Cut Cells` or `Delete Cells` from the `Edit` menu, or by selecting the cell and using the Scissors icon above.
# 
# ![Edit Menu](images/editMenu-AzureNotebooks.png "Edit Menu")
# 
# 
# 
# Try inserting some new cells now - try one Python cell that prints a string as per `"Hello, World!"` above, and try a Markdown cell. Run both, and then delete both.

# ## Python Basics
# 
# Python is a dynamically typed language. You don't use an explicit type specifier for declaring variables. 
# You don't need to use separators to mark the end of code lines.
# 
# In Python, indentation is really important. It replaces brackets to delimit blocks of code. You can use
# either tabs or spaces to indent code, but you must be consistent or Python will complain! 
# 
# You cannot mix tabs and spaces for indentation in Python 3.  
# 
# The style guide for Python (https://www.python.org/dev/peps/pep-0008) suggests using 4 spaces per 
# indentation level.
# 
# Comments in Python use the hash character, `#`.
# 
# Functions are defined using the `def` keyword, and take an argument list.
# 
# ### Simple Example
# 
# Let's calculate the area of a square. The square measures 3 metres long by 4 metres high.  We're going to store these in variables `width` and `height` respectively.:

# In[2]:


# This calculates the area of a square
def CalculateArea(width, height):
    return width * height

width = 3
height = 4
area = CalculateArea(width, height)


# Okay, having calculate the area, let's print it. We can use the Python print function to do that.

# In[3]:


print('The area is {} metres squared'.format(area))


# You can see that Python replaces `{}` from the print string literal with the value of `area` formatted as a string.
# 
# Remember we mentioned Python is object oriented? This `.format` is actually a method belonging to the string class, `str.format()` that takes a variety of types and converts them to strings. You will find this a very useful method to remember.

# ### Basic Types
# 
# Any object in Python can be tested for a truth value - for use in an `if`, `while` or `for` condition, or as an operand of a Boolean operation.  
# 
# The constants `None` and `False` are considered false for Booleans, as are objects that either have a `__bool__()` method that returns `False` or a `__len__()` method that returns zero. All other objects are considered true.
# 
# Conditional statements are ended with a colon before the block of code they guard. For example:
# 

# In[4]:


condition = True
if condition:
    print('The condition is true')
else:
    print('The condition is false')


# String literals in Python can be enclosed in either matched single quotes (`'`) or matched double quotes (`"`). You can use `+` to perform concatenation on strings.

# In[1]:


string1 = 'Hello'
string2 = "There"
string3 = string1 + " " + string2
print(string3)


# If you have developed in C or Java or another high level language, you'll find Python arithmetic pretty familiar. Python can perform the usual types of mixed type arithmetic on integers and floats, and promotes to float where appropriate. For example:

# In[2]:


a = 1
b = 0.5
c = a * b
print("{} * {} = {}".format(a, b, c))


# Bitwise operations are similar, as are Logical operations. Python uses `|,&,^,<<,>>,~` for Bitwise operations, but it uses `or` and `and` for Logical.

# In[3]:


a = 1
b = 2
print("{} | {} = {}".format(a, b, a | b))   # bitwise or

print("{} || {} = {}".format(a, b, a or b)) # logical or


# ### More Advanced Data Structures
# 
# Python supports a list type, which is similar to an array. Each value in the list is numbered, starting from zero - the first one is numbered zero, the second 1, the third 2, and so on. 
# 
# Lists are mutable in that you can add and remove from lists. 

# In[6]:


people = [ 'Mary', 'Kevin', 'Venki', 'Cyril', 'Jane', 'Pierre', 'Xin', 'Andre']

print('The 1st person is {}'.format(people[0])) # counting starts from zero
print('The 5th person is {}'.format(people[4]))

print('The number of people in the array is {}'.format(len(people)))

people.append('Susan')
print('The number of people in the array is now {}'.format(len(people)))

print('The 2nd person is {}'.format(people[1])) # counting starts from zero
people.remove('Kevin')
print('The 2nd person is now {}'.format(people[1])) # counting starts from zero
print (people)


# You can select subsets from lists and also iterate across lists....

# In[5]:


print(people[2:5]) # The range 2:5 specifies the 3rd ('2'), 4th ('3') and 5th elements ('4'). 
                   # The 6th element ('5') is not included in the range.
    
for person in people:
    print("Hello, {}!".format(person))


# Tuples are very similar to lists, but they are immutable --  you can't change the values of an element, and you can't remove individual elements.  For example, the following will result in an error:

# In[7]:


numbers = (1, 2, 3)

numbers.remove(1)


# Dictionaries are similar to arrays, but instead of indexing by number, you index with a 'key'.  The variable the key responds to is called a 'value'.  Like arrays, you can add, modify and remove items from dictionaries.

# In[8]:


groupAges = { 'Alan' : 32, 'Kate' : 18, 'Emmanuel' : 25, 'Greg' : 62 }

groupAges['Alan']


# A variable on its own at the end of a code block will have its value output by Juptyer Notebooks, so you don't always have to use a print statement.  However, only the last variable like this will be output. For example, the following will only output the age of Emmanuel, and not Kate...

# In[9]:


groupAges['Kate']
groupAges['Emmanuel']


# You can list the keys in a dctionary with the `keys()` method:

# In[10]:


groupAges.keys()


# Likewise, you can view all the values in a dictionary:

# In[11]:


groupAges.values()


# You can remove key/value pairs using the `del` keyword:

# In[ ]:


del groupAges['Alan']
groupAges.keys()


# You can view the type of a dictionary value using type:

# In[12]:


type(groupAges['Kate'])


# ### Loops
# 
# For loops in Python iterate across a list. You can use the `range` method to create a list for numbers. The range is inclusive of the starting number, but exclusive of the terminating number. For example:

# In[13]:


for i in range(0,10):
    print("i is {}".format(i))


# You can also use the library `tqdm` to pretty-print loop iterations. Here is a somewhat contrived example, where we calculate $\sum\limits_{i=1}^{10}{i}$ as follows:

# In[28]:


from tqdm import *
import time
print ("printing the table of 2")
power = 1
for i in tqdm(range(0,10), ascii=True):
    mul = power * 2
    time.sleep(0.5)
    print("2 * ",power,"is {}".format(mul))
    power=power+1


# While loops are similarly implemented:

# In[29]:


i = 0
while i < 10:
    print("i is {}".format(i))
    i += 1 # Python does not have a ++ style increment operator or a -- style decrement operator


# Likewise, we can add `tqdm` to a while loop, but we need to specify the total value (in terms of the range of values):

# In[33]:


i = 0
sum = 0
maxCount=int(input("Set your timer for n seconds"))
stepSize = 1
pbar = tqdm(total=maxCount, ascii=True)

while i < maxCount:
    sum = sum + stepSize
    i = i + stepSize
    pbar.update(stepSize)
    time.sleep(1)
pbar.close()
print("sum is {}".format(sum))


# ### NumPy
# 
# Libraries in Python are imported using the `import` keyword. You can also import libraries using a shorthand alias. For example, we will often import Numpy as np and use np to save typing.

# In[34]:


import numpy as np


# In[35]:


myArray = np.array ([1,2,3,4,5,6,7,8])


# In[36]:


print (myArray)


# NumPy arrays are slightly different to built-in Python arrays. They are generally more compact and faster to access. NumPy arrays also support vectorized operations like elementwise addition and multiplication. For machine learning, we typically prefer using NumPy arrays for performance reasons.

# You can figure out the shape of a NumPy array using `np.shape()`:

# In[37]:


a = np.array([[1, 2], [3, 4], [5, 6]])
np.shape(a)


# #### Broadcasting and Element-wise Operations

# NumPy matrix arithmetic is usually performed on an element by element basis. For example:

# In[38]:


a = np.array([[1, 2, 3],[4, 5, 6]])
b = np.array([[4, 5, 6], [6, 7, 8]])

a * b


# We can see that for each element in a, the above code multiplied it by the corresponding element in b.  What would happen if the arrays are different sizes?

# In[39]:


c = np.array([[1, 2,3], [4, 5, 6], [7, 8, 9]])
d = np.array([1, 2, 3])

c * d


# In NumPy, this is called *Broadcasting*. Broadcasting describes how numpy treats arrays of different dimensions during 
# arithmetic operations. Where possibly, Python will *broadcast* the smaller array across the larger array or matrix so that they have compatible shapes.
# 
# Broadcasting is typically much faster than executing equivalent operations via Python loops.
# 
# When operating on two matrices, NumPy will compare their shapes. It considers their dimensions to be compatible for broadcasting when they are equal, or one of them is 1.
# 
# If the matrices are not compatible, a `ValueError: operands could not be broadcast together ` exception will be thrown.

# In addition to broadcasting with matrics of different sizes, we can also perform operations with scalars and matrices. For example, to multiply each element in a by 2:
# 

# In[40]:


a * 2


# And to add 4 to each element in a:

# In[41]:


a + 4


# Let's consider the transpose of matrix b:

# In[42]:


b.transpose()


# You can also implement transpose using the following syntax:

# In[43]:


b.T


# Although from linear algebra, you might be used to the dot product of something like a 2x3 matrix with a 3x2 matrix, you cannot achieve this with NumPy broadcasting rules. For example (**this following line will cause an expected error**):

# In[44]:


a * b.T


# Instead, you need to use `np.dot()`. The following will work for multiplying a 2x3 by a 3x2 matrix:

# In[45]:


np.dot(a, b.T)


# There are many operations we can perform on arrays. For example, we can find the sum of all the elements:

# In[46]:


a.sum()


# We can also find the maximum, mean (average), and minimum for example:

# In[47]:


print("Maximum value in a is {}, mean value is {}, and minimum value is {}".format(a.max(), a.mean(), a.min()))


# ## Rank Arrays
# 
# In Python, *rank* refers to the number of dimensions of the array. The shape of an array refers to a tuple of integers defining its size along each dimension.
# 
# An interesting quirk of Python is rank-1 arrays, which strictly speaking are neither vectors of row or column order. For example, we are going to initialize the following 3 element rank-1 array:

# In[48]:


r = np.random.randn(3)
r


# Let's look at the rank and shape of this:

# In[49]:


np.shape(r)


# This `(x,)` is indicative of a rank-1 array.

# In[50]:


np.dot(r, r.T)


# We can use the `reshape()` method to convert from a rank-1 array to a NumPy vector.

# In[51]:


r1 = r.reshape(1,3)
r1


# The double square brackes `[[` and `]]` indicate a NumPy array rather than a Python native array.

# In[52]:


np.dot(r1, r1.T)


# In[53]:


np.shape(np.dot(r1, r1.T))


# We can also multiple two matrices element wise:

# In[54]:


np.multiply(r1, r1)


# And with broadcasting...

# In[55]:


np.multiply(r1, r1.T)


# # Jupyter Notebooks: Important Tips and Tricks
# 
# A Jupyter Notebook is a very useful tools for mixing documentation (in Markdown) and code (in our case, in Python) in a single online editable notebook. You can run the code, and evaluate its output live in the notebook.
# 
# When you execute code in a Juptyer Notebook, it actually runs in a `kernel` - that is, a small piece of code running either in Azure Notebooks, or locally in your own Jupyter Notebooks server.  The output from this kernel is then rendered in your web browser.
# 
# The kernel's environment is built up as you run cells of code. Therefore, it is important in many of the labs to run the code blocks in the order they appear in the notebook. Some of these earlier blocks are importing libraries and setting up data structures and variables that will be referenced later in the lab. If you run the code out of order, you might see strange errors. You can always select `Kernel->Restart` to clear the slate if things go funny.
# 
# There is always the chance that something goes wrong, the Internet connection dies, or the kernel in the backend has a problem.
# You can try the menu option `Kernel->Reconnect` to see if it is  possible to connect again to running kernel without interrupting computations (but some part of your output may already be lost).
# 
# If you find the Notebook is becoming fully unresponsive after waiting a significant period of time, you can click on the `Kernel` menu, and select `Interrupt` and try running that cell again. You can also select `Restart` but this will clear the kernel of any memory it had previously, so you will need to start running code from the start of the notebook again.
# 
# Azure Notebooks are run on individual virtual machines (one per user) that offer approximately 4GiB of RAM and plenty of storage for your notebooks. However, we will be challenging this system with our computational requirements for running deep learning training. There is a chance that you will see occasional `MemoryError` exception messages in your notebooks. If you do, don't panic -- our advice is simply to select `Shutdown` from the main Azure Notebooks page to ensure all kernel processes have stopped. Then, `Restart and Clear Output` on your notebook and try again.  
# 
# ![Shutdown Azure Notebook Kernels](images/shutdown-AzureNotebookKernels.png "Shutdown Azure Notebook Kernels")
# 
# We strongly advise not running multiple notebooks at once in Azure Notebooks, particularly for the deep learning notebooks in Module 3 and 4 of this course.
# 
# ### Local Data
# 
# In Azure Notebooks, the libraries containing the actual notebooks themselves are stored on persistent but slow storage. However, there are other paths which are transient (they are lost when the session ends - times out, or is shutdown explicitly, for example) but they are much faster.  
# 
# In many of the later labs, we will explicitly copy our data sets to these transient areas for speed - but bare in mind they will be lost when the session ends, and thus there is often a setup portion (delay) at the start of each lab. Where this is the case, it will be clearly called out to you.
# 
# ### Timeouts
# 
# Your notebook server will automatically be shutdown after a period of inactivity.
# 
# When you are in a notebook server, your session is active as long as you are interacting with it - the timeout is set to 60 minutes. If you are inactive for more than 60 minutes, your notebook server will be reclaimed and recycled.  However, your notebooks themselves are safe - you just have to log back in to see them. 
# 
# You may also occasionally see "Connection failed" messages if there has been an internet connection issue. 
# The "Kernel" menu has several options for interrupting or reconnecting to a stuck kernel.
# 
# There is comprehensive help on Azure Notebooks available at https://notebooks.azure.com/help/jupyter-notebooks
# 

# # Conclusions
# 
# In this lab we introduced Azure Notebooks (which is a cloud-service offering free Jupyter Notebooks) and we introduced Python 3 and NumPy.
# 
# At this stage, you should feel confident enough to open any of the labs in Azure Notebooks, and to start playing around with them. The concepts covered in the labs will be explained in the related course videos and materials, but please feel free to experiment in the Jupyter Notebooks and get a feel for how these work.
# 
