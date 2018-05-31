import tkinter as tk

root = tk.Tk()

labe1 = tk.Label(root, text='Hello_World', fg='red', bg='blue')
labe1.pack()

button = tk.Button(root, text='Close', command=root.quit)
button.pack()

root.mainloop()