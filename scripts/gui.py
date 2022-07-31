from time import sleep
from tkinter import *
from tkinter import ttk
from tkinter import font
from random import randint
from playsound import playsound
import csv, os

tk = Tk()

tk.title('Quiz')    # 윈도우 이름
tk.geometry('1024x720+100+30')

duration = 2                # 문제가 화면에 나타나는 시간 (단위: 초)
startIdx, endIdx = 290, 309     # 출제 범위
amount = 10                # 출제 수량

quizlist = list()           # 출제 범위에 해당하는 단어와 그 뜻을 모아둔 추첨 리스트
# randint 쓰려면 순서가 없는 딕셔너리에서는 무작위 추첨이 불가하여, 리스트로 생성
# 이중리스트 형태로 구성 [[word,meaning,commentary], [word,meaning,commentary]]
final_quiz_list = list()    # quizlist에서 단어, 뜻, 해설을 순서대로 입력한 리스트

def shuffle(startIdx, endIdx, problems, filename):
    
    currentPath = os.getcwd()
    global quizlist, final_quiz_list
    filename = filename + '.csv'
    tempOrder = []

    if len(quizlist) != 0:
        quizlist.clear()
        final_quiz_list = []
    with open(currentPath+'/'+filename, 'r', encoding='utf-8-sig') as file1:
        params = csv.DictReader(file1)
        
        if endIdx == 0:
            endIdx = len(params)-1          # endInx값 미입력 시 마지막 단어까지 범위 지정
        
        # 시작값~끝값 사이에서 problems 갯수 무작위 추첨
        while 1:
            randnum = randint(startIdx, endIdx)
            if randnum not in tempOrder:
                tempOrder.append(randnum)
            if len(tempOrder) == problems:
                break
        for item in params:
            # item = item.strip(' \n-')
            # temp = item.split(',')          # 본문 안에 있는 ,와 csv ,구분 못함 -> DictReader로 해결
            if len(quizlist) == problems:
                break
            try:
                if int(item['index']) in tempOrder:          # 출제 범위에 해당하는 단어만 추첨 대상에 추가
                    quizlist.append([item['word'], item['mean'], item['commentary']])
            except ValueError as e:
                errorText = '에러 발생. 재시작 필요'&e
                templabel['text'] = errorText
                tk.update()
                continue
        if len(quizlist) < problems:
            # XXX 중간에 index가 없는 번호가 tempOrder에 추첨된 경우, 첫번째 아이템을 중복으로 계속 추가
            randnum = randint(startIdx, endIdx)
            if randnum not in tempOrder:
                quizlist.append(quizlist[0])

        for i in range(len(quizlist)):
            word = quizlist[i][0]              # 단어
            meaning = quizlist[i][1]            # 뜻
            commentary = quizlist[i][2]       # 해설
            final_quiz_list.append((word, meaning, commentary,))
        
    return final_quiz_list

question_font = font.Font(size=128, family='Helvetica')

frame_setup = ttk.Frame(tk)
frame_setup.pack(expand=True, anchor='center', padx=10, pady=40)

label_duration = ttk.Label(frame_setup, text='문제 유지 시간(초)')
label_duration.grid(row=0, column=0)

entry_duration = ttk.Entry(frame_setup, width=24)
entry_duration.grid(row=0, column=1)

label_startIdx = ttk.Label(frame_setup, text='출제 범위 시작값')
label_startIdx.grid(row=1, column=0)

entry_startIdx = ttk.Entry(frame_setup, width=24)
entry_startIdx.grid(row=1, column=1)

label_endIdx = ttk.Label(frame_setup, text='출제 범위 마지막값')
label_endIdx.grid(row=2, column=0)

entry_endIdx = ttk.Entry(frame_setup, width=24)
entry_endIdx.grid(row=2, column=1)

label_amount = ttk.Label(frame_setup, text='문제 수량')
label_amount.grid(row=3, column=0)

entry_amount = ttk.Entry(frame_setup, width=24)
entry_amount.grid(row=3, column=1)

label_filename = ttk.Label(frame_setup, text='확장자 제외 파일명')
label_filename.grid(row=4, column=0)

entry_filename = ttk.Entry(frame_setup, width=24)
entry_filename.grid(row=4, column=1)

def setup():
    try:
        global duration, startIdx, endIdx, amount
        duration = float(entry_duration.get())
        startIdx = int(entry_startIdx.get())
        endIdx = int(entry_endIdx.get())
        amount = int(entry_amount.get())
        filename = str(entry_filename.get())
        # templabel2['text'] = '{0}&{1}&{2}'.format(startIdx,endIdx,quizlist)
        shuffle(startIdx, endIdx, amount, filename)
        button_start['state'] = 'normal'
        tk.update()
    except ValueError:
        templabel['text'] = '오류: 미입력한 값이 있거나, 올바르지 않은 유형을 입력함'
        duration = 0.02                # 문제가 화면에 나타나는 시간 (단위: 초)
        startIdx, endIdx = 1, 40     # 출제 범위
        amount = 6                # 출제 수량
        filename = 'BASIC_Day1'     # 파일명에 한글 들어있으면 오류남
        shuffle(startIdx, endIdx, amount, filename)
        # button_start['state'] = 'normal'
        tk.update()
    except Exception as e:
        templabel.configure(text='오류: 알 수 없는 오류 발생. 프로그램 재실행 필요')
        print(e)

templabel = ttk.Label(frame_setup)
templabel.grid(row=5, columnspan=2)

templabel2 = ttk.Label(frame_setup, wraplength=300)
templabel2.grid(row=6, columnspan=2)

def start():
    frame_setup.forget()
    wordlabel['command'] = showQuestion()
    
def pick_one(integer):
    global amount
    k = quizlist[integer][0]
    wordlabel.configure(text=k)

def showQuestion():
    button_setup.configure(state='disable')
    frame_question.pack(expand=True)
    wordlabel.pack(expand=True, fill='both')
    button_start['state'] = 'disable'
    filename = 'paper.mp3'
    
    global amount
    for i in range(amount):
        pick_one(i)
        tk.update()
        sleep(duration)
        playsound(filename)
    
    button_start.configure(text='정답', state='normal', command=showAnswers)

def showAnswers():  # 정답 공개
    frame_answer.pack(side='top', padx=10 ,pady=40)
    frame_question.forget()
    style = ttk.Style(tk)
    style.configure('Treeview', rowheight=40)       # 열 높이 변경
    global quizlist, final_quiz_list
    for row in answer_tree.get_children():
        answer_tree.delete(row)
    for i in range(len(final_quiz_list)):
        answer_tree.insert('', 'end', text=i+1, values=final_quiz_list[i])
    button_setup.configure(text='처음으로', state='normal', command=gotoMain)
    button_start.configure(state='disable')

def gotoMain():
    frame_answer.pack_forget()
    frame_setup.pack(expand=True, anchor='center', padx=10, pady=40)
    templabel.configure(text='')
    button_setup.configure(text='설정', state='normal', command=setup)
    button_start.configure(text='시작!', state='disable', command=start)

frame_question = ttk.Frame(tk)
frame_question.pack(expand=True)
frame_answer = ttk.Frame(tk)

wordlabel = ttk.Label(frame_question, text='wordlabel', font=question_font)

answer_tree = ttk.Treeview(frame_answer, columns=['word', 'meaning','commentary'], displaycolumns=['word', 'meaning','commentary'], height=(amount+2))
answer_tree.column('#0', width=70)
answer_tree.heading('#0', text='Q')   # 순번
answer_tree.column('word', width=200)
answer_tree.heading('word', text='단어', anchor='center')   # 단어
answer_tree.column('meaning', width=280)
answer_tree.heading('meaning', text='뜻', anchor='center')    # 뜻
answer_tree.column('commentary', width=200)
answer_tree.heading('commentary', text='해설', anchor='center')
answer_tree.pack()

verticalSlide = ttk.Scrollbar(tk, orient='vertical', command=answer_tree.yview)
verticalSlide.pack(side='right', fill='y')
answer_tree.configure(yscrollcommand=verticalSlide.set)

frame_command = ttk.Frame(tk)
frame_command.pack(side='bottom', padx=10 ,pady=40)
button_setup = ttk.Button(frame_command, text='설정', command=setup)
button_setup.grid(row=0, column=0)
button_start = ttk.Button(frame_command, text='시작!', command=start, state='disable')
button_start.grid(row=0, column=1)

mainloop()
