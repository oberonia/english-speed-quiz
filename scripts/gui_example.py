from tkinter import *
from tkinter import ttk

root = Tk()
# label = Label(tk, text= 'Hello world')
# label.pack()
# tk.mainloop()
root.title('Quiz')

'''
def event():
    # text 속성에 접근하여 텍스트 재할당
    button['text'] = '버튼의 텍스트가 바뀌는 이벤트'

def Ft2Cm():
    ft2cm = entry1.get()
    entry2.delete(0, 'end')
    entry2.insert(0, round(float(ft2cm)*30.48, 4))

label1 = Label(tk, text='ft').grid(row=0, column=0)
label2 = Label(tk, text='cm').grid(row=1, column=0)

entry1 = Entry(tk)
entry2 = Entry(tk)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

# button = Button(tk, text='누르면 event 함수 실행', command=event)
button = Button(tk, text='누르면 event 함수 실행', command=event).grid(row=2, column=0)
button2 = Button(tk, text='변환', command=Ft2Cm).grid(row=2, column=1)
# button.pack(side=LEFT, padx=10, pady=30)
# button.pack()
'''

def start():
    b.configure(text='Stop', command=stop)
    l['text'] = 'Working...'
    global interrupt; interrupt = False
    root.after(1, step)
    
def stop():
    global interrupt; interrupt = True
    
def step(count=0):
    p['value'] = count
    if interrupt:
        result(None)
        return
    root.after(100)  # next step in our operation; don't take too long!
    if count == 20:  # done!
        result(42)
        return
    root.after(1, lambda: step(count+1))
    
def result(answer):
    p['value'] = 0
    b.configure(text='Start!', command=start)
    l['text'] = "Answer: " + str(answer) if answer else "No Answer"
    
f = ttk.Frame(root); f.grid()
b = ttk.Button(f, text="Start!", command=start); b.grid(column=1, row=0, padx=5, pady=5)
l = ttk.Label(f, text="No Answer"); l.grid(column=0, row=0, padx=5, pady=5)
p = ttk.Progressbar(f, orient="horizontal", mode="determinate", maximum=20); 
p.grid(column=0, row=1, padx=5, pady=5)

root.mainloop()