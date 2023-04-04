#mGlossary_Final.py
# A quick glossary app using a dictionary data type
from tkinter import *

# key press function:
def nasir():
    entered_text = secondWidget.get()  # collect text from text entry box
    fifthWidget.delete(0.0, END)  # clear text box
    try:
        definition = my_glossary[entered_text]
    except:
        definition = "There is no entry for this word."
    fifthWidget.insert(END, definition)

'''
Explanation on what the function does:
1. On line 8, we created a variable that gets the users input using the created entry widget
which was stored in the variable secondWidget.

2. On line 9, we are utilizing the delete() function to erase the text stored on the fifthWidget
so that when you hit the submit button everything that was displayed earlier gets deleted
in order for us to have a clear text box for the program to insert a new set of definition (see line 14 )
remember to check and understand what the fifthWidget stores and what it actually does.

3. From line 10 - 14:
The try statement says that if the value of the entered_text is not included in variable 
(my_glossary). 
Remember a dictionary stores key:value pairs.
Now if the word which in the case is also referred to as entered_text exists in the created dictionary,
it stores it in the variable definition (see line 11 for reference).
After storing it in the variable definition, we use the insert() function to input the value
of the key pair in the fifthWidget.

Line 14 says any definition would be inserted into the fifthWidget and start from the end of
the cleared text and works its way down
'''

#create a window frame
window = Tk()
# change the title of the window frame
window.title("My Coding Club Glossary")
window.geometry("500x500")
# create label
firstWidget = Label(window, text="Enter the word you want defined:")
# display the created label widget on screen using the .grid() function
firstWidget.grid(row=0, column=0, sticky=W)

# create text entry box
secondWidget = Entry(window, width=20, bg="light green")
# display the created entry widget on screen using the .grid() function
secondWidget.grid(row=1, column=0, sticky=W)

# Add a submit button:
thirdWidget = Button(window, text="SUBMIT", width=5, command=nasir)
# display the created button widget on screen using the .grid() function
thirdWidget.grid(row=2,column=0, sticky=W)

# create another label
fourthWidget = Label(window, text="\nDefinition:")
# display the created label widget on screen using the .grid() function
fourthWidget.grid(row=3, column=0, sticky=W)

# create text box
fifthWidget = Text(window, width=75, height=15, wrap=WORD, background="black", foreground="white")
# display the created text widget on screen using the .grid() function
fifthWidget.grid(row=4, column=0, columnspan=2, sticky=W)

# The dictionary:
my_glossary = {
    'algorithm': 'Step by step instructions to perform a task that a computer could understand.',
    'bug': 'A piece of code that is causing a program to fail to run properly or at all.',
    'binary number': 'A number represented in base 2.'
    }


##### Run mainloop
window.mainloop()

'''
Always remember the fundamental structure when using the tkinter
and everything in tkinter is a widget.
'''

'''
Why we were having the issues in class was as a result of us not adding the conditional statement
which is on line 10 - line 14. 
'''