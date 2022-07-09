from tkinter import *
from quiz import *

tk = Tk()

tk.title('Quiz')    # 윈도우 이름


duration = 2                # 문제가 화면에 나타나는 시간 (단위: 초)
startIdx, endIdx = 300, 309     # 출제 범위
amount = 10                # 출제 수량

# frame = LabelFrame(tk, padx=10, pady=20)
# frame.pack(padx=20)

label_duration = Label(tk, text='문제 유지 시간(초)')
label_duration.grid(row=0, column=0)

entry_duration = Entry(tk)
entry_duration.grid(row=0, column=1)

label_startIdx = Label(tk, text='출제 범위 시작값')
label_startIdx.grid(row=1, column=0)

entry_startIdx = Entry(tk)
entry_startIdx.grid(row=1, column=1)

label_endIdx = Label(tk, text='출제 범위 마지막값')
label_endIdx.grid(row=2, column=0)

entry_endIdx = Entry(tk)
entry_endIdx.grid(row=2, column=1)

label_amount = Label(tk, text='문제 수량')
label_amount.grid(row=3, column=0)

entry_amount = Entry(tk)
entry_amount.grid(row=3, column=1)

def setup():
    global duration, startIdx, endIdx, amount
    duration = int(entry_duration.get())
    startIdx = int(entry_startIdx.get())
    endIdx = int(entry_endIdx.get())
    amount = int(entry_amount.get())
    templabel = Label(tk, text=f'{startIdx}&{endIdx}')
    templabel.grid(row=5)

button_start = Button(tk, text='시작!', command=setup)
button_start.grid(row=4, columnspan=2)




# TODO tk가 invoke를 지원하지 않으니 강제로 화면을 넘겨서 우회
# duration만큼 대기하다가 next() 함수를 불러서 화면 갱신

mainloop()
