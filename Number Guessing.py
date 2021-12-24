from tkinter import *
import random

root = Tk()
root.geometry("400x200")
root.config(bg="#F27D16")
root.resizable(False, False)
root.title("Number Guessing Game")

ranNum = random.randint(0, 10)
chance = 5
disp = StringVar()


def guess():
    global chance
    global ranNum
    guessed = int(ent.get())
    if chance > 0:
        if guessed == ranNum:
            msg = f'You won! {ranNum} is the right answer.'
        elif guessed > ranNum:
            chance -= 1
            msg = f'{guessed} is greater. You have {chance} attempt left.'
        elif guessed < ranNum:
            chance -= 1
            msg = f'{guessed} is smaller. You have {chance} attempt left.'
        else:
            msg = 'Something went wrong!'
    else:
        msg = f'You Lost! you have {chance} attempt left.'

    disp.set(msg)


lbl = Label(root, text='Guess The Number', font=('sans-serif', 20), relief=SOLID, padx=10, pady=10, bg='#F27D16')
lbl.pack(pady=(10, 0))

ent = Entry(root, width=25, font=50)
ent.pack(pady=(50, 10))

btn = Button(root, text='Submit Guess', command=guess)
btn.pack()

disp_lbl = Label(root, textvariable=disp, bg='#F27D16', font=50)
disp_lbl.pack()

root.mainloop()