from tkinter import Tk, Entry, Text, BOTH

def record(event):
    if len(event.keysym) > 1:
        text.insert('end','It is a non-alphanumeric key\n')
    elif event.keysym >= 'a' and event.keysym <= 'z':
        text.insert('end', 'It is a lowercase letter\n')
    elif event.keysym >= 'A' and event.keysym <= 'Z':
        text.insert('end', 'It is an uppercase letter\n')
    elif event.keysym >= '0' and event.keysym <= '9':
        text.insert('end', 'It is a number\n')
root = Tk()
entry = Entry(root)
text = Text(root, width = 30, height = 5)
entry.bind('<KeyPress>', record)

entry.pack()
text.pack(expand = True, fill = BOTH)
root.mainloop()