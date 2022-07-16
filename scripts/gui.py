from tkinter import *
from tkinter import ttk
from tkinter import font
from quiz import *

tk = Tk()

tk.title('Quiz')    # 윈도우 이름
tk.geometry('800x600+100+100')

duration = 2                # 문제가 화면에 나타나는 시간 (단위: 초)
# startIdx, endIdx = 1, 10     # 출제 범위
startIdx, endIdx = 290, 309     # 출제 범위
amount = 10                # 출제 수량

question_font = font.Font(size=128)

frame_setup = ttk.Frame(tk)
frame_setup.pack(side='top', anchor='center', padx=10, pady=40)

label_duration = ttk.Label(frame_setup, text='문제 유지 시간(초)')
label_duration.grid(row=0, column=0)

entry_duration = ttk.Entry(frame_setup)
entry_duration.grid(row=0, column=1)

label_startIdx = ttk.Label(frame_setup, text='출제 범위 시작값')
label_startIdx.grid(row=1, column=0)

entry_startIdx = ttk.Entry(frame_setup)
entry_startIdx.grid(row=1, column=1)

label_endIdx = ttk.Label(frame_setup, text='출제 범위 마지막값')
label_endIdx.grid(row=2, column=0)

entry_endIdx = ttk.Entry(frame_setup)
entry_endIdx.grid(row=2, column=1)

label_amount = ttk.Label(frame_setup, text='문제 수량')
label_amount.grid(row=3, column=0)

entry_amount = ttk.Entry(frame_setup)
entry_amount.grid(row=3, column=1)

def setup():
    try:
        frame_setup.pack(side='top', anchor='center', padx=10, pady=20)
        global duration, startIdx, endIdx, amount
        duration = int(entry_duration.get())
        startIdx = int(entry_startIdx.get())
        endIdx = int(entry_endIdx.get())
        amount = int(entry_amount.get())
        templabel['text'] = startIdx+'&'+endIdx
        button_start['state'] = 'normal'
    except ValueError:
        templabel['text'] = '오류: 미입력한 값이 있습니다'
        duration = 2                # 문제가 화면에 나타나는 시간 (단위: 초)
        startIdx, endIdx = 286, 309     # 출제 범위
        amount = 20                # 출제 수량
        # templabel2.update_idletasks()
    except Exception as e:
        templabel.configure(text='오류: 알 수 없는 오류 발생. 프로그램 재실행 필요')
        # templabel['text'] = '오류: 알 수 없는 오류 발생. 프로그램 재실행 필요'
        print(e)
    finally:
        shuffle(startIdx, endIdx, amount)
        templabel2['text'] = '{0}&{1}&{2}&{3}'.format(startIdx,endIdx,problemOrder,quizlist)
        # button_start['command'] = start()
        button_start['state'] = 'normal'
        tk.update()

templabel = ttk.Label(frame_setup)
templabel.grid(row=4)

templabel2 = ttk.Label(frame_setup, wraplength=300)
templabel2.grid(row=5)

def start():
    frame_setup.forget()
    wordlabel['command'] = showQuestion()
    
def pick_one(integer):
    global amount
    k = list(quizlist[problemOrder[integer]].keys())
    # print(k[0])
    # wordlabel['text'] = k[0]
    wordlabel.configure(text=k[0])

def showQuestion():
    wordlabel.pack()
    button_start['state'] = 'disable'
    global amount
    for i in range(amount):
        pick_one(i)
        tk.update()
        sleep(0.02)
        # sleep(duration)
    button_start.configure(text='정답', state='normal', command=showAnswers)


def showAnswers():  # 정답 공개
    frame_answer.pack(side='top', padx=10 ,pady=40)
    frame_question.forget()
    global quizlist, problemOrder, final_quiz_list
    # answer_label['text'] = final_quiz_list
    for i in range(len(problemOrder)):
        # print(final_quiz_list[i*2], final_quiz_list[i*2+1], sep=' : ')
        answer_tree.insert('', 'end', text=final_quiz_list[i*2], values=final_quiz_list[i*2+1])
        # answer_tree.insert('', 'end', text='', values=final_quiz_list[i*2])
    for index in problemOrder:                  
        for k, v in quizlist[index].items():
            print(k, v)
    button_start.configure(state='disable')
    # tk.update()

frame_question = ttk.Frame(tk)
frame_question.pack(side='top', padx=10 ,pady=40)
frame_answer = ttk.Frame(tk)

wordlabel = ttk.Label(frame_question, text='wordlabel', font=question_font)

# answer_tree = ttk.Treeview(frame_answer, columns=['word', 'meaning'], displaycolumns=['word', 'meaning'], height=20)
answer_tree = ttk.Treeview(frame_answer, columns=['word'], displaycolumns=['word'], height=20)
answer_tree.pack()
answer_tree.column('word', width=200)
answer_tree.heading('word', text='', anchor='center')   # 단어
# answer_tree.column('meaning', width=200)
# answer_tree.heading('meaning', text='', anchor='center')    # 뜻

frame_command = ttk.Frame(tk)
frame_command.pack(side='bottom', padx=10 ,pady=40)
button_setup = ttk.Button(frame_command, text='설정', command=setup)
button_setup.grid(row=0, column=0)
button_start = ttk.Button(frame_command, text='시작!', command=start, state='disable')
button_start.grid(row=0, column=1)

mainloop()
