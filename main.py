from tkinter import Tk, Entry, Frame, FLAT
from tkinter.ttk import Button, Style

# Root window
root = Tk()
root.resizable(False, False)
root.title("Python Calculator")
root.config(bg="orangered")


# functions



def clearEverything():
    screen.delete(0, 'end')

    
def appendToExpression(e):
    text = e.widget.cget('text')

    if text == '\u2212':
        screen.insert('end', '-')

    elif text == '\u00d7':
        screen.insert('end', '*')

    elif text == '\u00f7':
        screen.insert('end', '/')

    elif text == '\u00b7':
        screen.insert('end', '.')

    else:
        screen.insert('end', text)

def calculate():
    result = eval(screen.get())
    clearEverything()
    screen.insert(0, result)



# Screen for display
screen = Entry(root, justify='center', width=15, font=('Helvetica', 30))
screen.pack(padx=8, pady=8)

# Frame for buttons
btnFrame = Frame(root)
btnFrame.pack()
btnFrame.config(background='orangered')

# Style for the buttons

style = Style()
style.configure(
    'TButton',
    font=('Helvetica', 30, 'bold'),
    height=60,
    width=4,
    relief=FLAT,
    background='orangered'
)


# Buttons

# Row 0

cButton = Button(btnFrame, text='C', style='TButton', command=clearEverything)
cButton.grid(column=0, row=0, padx=8, pady=8)

equalButton = Button(btnFrame, text='=', style='TButton', command=calculate)
equalButton.grid(column=1, row=0, padx=8, pady=8)

divideButton = Button(btnFrame, text='\u00f7', style='TButton')
divideButton.grid(column=2, row=0, padx=8, pady=8)
divideButton.bind('<Button-1>', appendToExpression)


# Row 1

plusButton = Button(btnFrame, text='+', style='TButton')
plusButton.grid(column=0, row=1, padx=8, pady=8)
plusButton.bind('<Button-1>', appendToExpression)

minusButton = Button(btnFrame, text='\u2212', style='TButton')
minusButton.grid(column=1, row=1, padx=8, pady=8)
minusButton.bind('<Button-1>', appendToExpression)

multiplyButton = Button(btnFrame, text='\u00d7', style='TButton')
multiplyButton.grid(column=2, row=1, padx=8, pady=8)
multiplyButton.bind('<Button-1>', appendToExpression)

# Row 2

zeroButton = Button(btnFrame, text='0', style='TButton')
zeroButton.grid(column=0, row=2, padx=8, pady=8)
zeroButton.bind('<Button-1>', appendToExpression)

doubleZeroButton = Button(btnFrame, text='00', style='TButton')
doubleZeroButton.grid(column=1, row=2, padx=8, pady=8)
doubleZeroButton.bind('<Button-1>', appendToExpression)

dotButton = Button(btnFrame, text='\u00b7', style='TButton')
dotButton.grid(column=2, row=2, padx=8, pady=8)
dotButton.bind('<Button-1>', appendToExpression)

# Row 3

sevenButton = Button(btnFrame, text='7', style='TButton')
sevenButton.grid(column=0, row=3, padx=8, pady=8)
sevenButton.bind('<Button-1>', appendToExpression)

eightButton = Button(btnFrame, text='8', style='TButton')
eightButton.grid(column=1, row=3, padx=8, pady=8)
eightButton.bind('<Button-1>', appendToExpression)

nineButton = Button(btnFrame, text='9', style='TButton')
nineButton.grid(column=2, row=3, padx=8, pady=8)
nineButton.bind('<Button-1>', appendToExpression)


# Row 4

fourButton = Button(btnFrame, text='4', style='TButton')
fourButton.grid(column=0, row=4, padx=8, pady=8)
fourButton.bind('<Button-1>', appendToExpression)

fiveButton = Button(btnFrame, text='5', style='TButton')
fiveButton.grid(column=1, row=4, padx=8, pady=8)
fiveButton.bind('<Button-1>', appendToExpression)

sixButton = Button(btnFrame, text='6', style='TButton')
sixButton.grid(column=2, row=4, padx=8, pady=8)
sixButton.bind('<Button-1>', appendToExpression)


# Row 5

oneButton = Button(btnFrame, text='1', style='TButton')
oneButton.grid(column=0, row=5, padx=8, pady=8)
oneButton.bind('<Button-1>', appendToExpression)

twoButton = Button(btnFrame, text='2', style='TButton')
twoButton.grid(column=1, row=5, padx=8, pady=8)
twoButton.bind('<Button-1>', appendToExpression)

threeButton = Button(btnFrame, text='3', style='TButton')
threeButton.grid(column=2, row=5, padx=8, pady=8)
threeButton.bind('<Button-1>', appendToExpression)


# Mainloop
root.mainloop()