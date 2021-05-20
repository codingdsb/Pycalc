from tkinter import Tk, Entry, Frame, FLAT
from tkinter.ttk import Button, Style

# Tk, Entry, Frame (tkinter)
# Style, Buttons (tkinter.ttk)


# Root window
root = Tk()
root.resizable(False, False)
root.title('Pycalc')
root.config(background='orange')

# Screen for display
screen = Entry(root, justify='center', width=25)
screen.pack(padx=8, pady=8)

# Frame for creating buttons
btnFrame = Frame(root)
btnFrame.pack()
btnFrame.config(background='orange')

# Style for buttons

style = Style()
style.configure(
    'TButton',
    font=('Helvetica', 15, 'bold'),
    height=60,
    width=4,
    relief=FLAT,
    background='orange'
)


# Buttons

# Row 0

cButton = Button(btnFrame, text='C', style='TButton')
cButton.grid(column=0, row=0, padx=8, pady=8)


equalsButton = Button(btnFrame, text='=', style='TButton')
equalsButton.grid(column=1, row=0, padx=8, pady=8)

divideButton = Button(btnFrame, text='÷', style='TButton')
divideButton.grid(column=2, row=0, padx=8, pady=8)


# Row 1 

plusButton = Button(btnFrame, text='+', style='TButton')
plusButton.grid(column=0, row=1, padx=8, pady=8)

minusButton = Button(btnFrame, text='—', style='TButton')
minusButton.grid(column=1, row=1, padx=8, pady=8)

multiplyButton = Button(btnFrame, text='×', style='TButton')
multiplyButton.grid(column=2, row=1, padx=8, pady=8)


# Row 2

zeroButton = Button(btnFrame, text='0', style='TButton')
zeroButton.grid(column=0, row=2, padx=8, pady=8)

doubleZeroButton = Button(btnFrame, text='00', style='TButton')
doubleZeroButton.grid(column=1, row=2, padx=8, pady=8)

dotButton = Button(btnFrame, text='·', style='TButton')
dotButton.grid(column=2, row=2, padx=8, pady=8)


# Row 3

sevenButton = Button(btnFrame, text='7', style='TButton')
sevenButton.grid(column=0, row=3, padx=8, pady=8)

eightButton = Button(btnFrame, text='8', style='TButton')
eightButton.grid(column=1, row=3, padx=8, pady=8)

nineButton = Button(btnFrame, text='9', style='TButton')
nineButton.grid(column=2, row=3, padx=8, pady=8)


# Row 4

fourButton = Button(btnFrame, text='4', style='TButton')
fourButton.grid(column=0, row=4, padx=8, pady=8)

fiveButton = Button(btnFrame, text='5', style='TButton')
fiveButton.grid(column=1, row=4, padx=8, pady=8)

sixButton = Button(btnFrame, text='6', style='TButton')
sixButton.grid(column=2, row=4, padx=8, pady=8)


# Row 5

oneButton = Button(btnFrame, text='1', style='TButton')
oneButton.grid(column=0, row=5, padx=8, pady=8)

twoButton = Button(btnFrame, text='2', style='TButton')
twoButton.grid(column=1, row=5, padx=8, pady=8)

threeButton = Button(btnFrame, text='3', style='TButton')
threeButton.grid(column=2, row=5, padx=8, pady=8)



# mainloop
root.mainloop()