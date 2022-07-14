from tkinter import *
from tkinter import ttk
from quiz import *

tk = Tk()

tk.title('Quiz')    # 윈도우 이름

duration = 2                # 문제가 화면에 나타나는 시간 (단위: 초)
# startIdx, endIdx = 1, 10     # 출제 범위
startIdx, endIdx = 300, 309     # 출제 범위
amount = 10                # 출제 수량

# frame = LabelFrame(tk, padx=10, pady=20)
# frame.pack(padx=20)

label_duration = ttk.Label(tk, text='문제 유지 시간(초)')
label_duration.grid(row=0, column=0)

entry_duration = ttk.Entry(tk)
entry_duration.grid(row=0, column=1)

label_startIdx = ttk.Label(tk, text='출제 범위 시작값')
label_startIdx.grid(row=1, column=0)

entry_startIdx = ttk.Entry(tk)
entry_startIdx.grid(row=1, column=1)

label_endIdx = ttk.Label(tk, text='출제 범위 마지막값')
label_endIdx.grid(row=2, column=0)

entry_endIdx = ttk.Entry(tk)
entry_endIdx.grid(row=2, column=1)

label_amount = ttk.Label(tk, text='문제 수량')
label_amount.grid(row=3, column=0)

entry_amount = ttk.Entry(tk)
entry_amount.grid(row=3, column=1)

def setup():
    try:
        global duration, startIdx, endIdx, amount
        duration = int(entry_duration.get())
        startIdx = int(entry_startIdx.get())
        endIdx = int(entry_endIdx.get())
        amount = int(entry_amount.get())
        templabel['text'] = startIdx+'&'+endIdx
    except ValueError:
        templabel['text'] = '오류: 미입력한 값이 있습니다'
        duration = 2                # 문제가 화면에 나타나는 시간 (단위: 초)
        startIdx, endIdx = 300, 309     # 출제 범위
        amount = 10                # 출제 수량
        # templabel2.update_idletasks()
    finally:
        shuffle(startIdx, endIdx, amount)
        templabel2['text'] = '{0}&{1}&{2}&{3}'.format(startIdx,endIdx,problemOrder,quizlist)
        # tk.after

templabel = ttk.Label(tk)
templabel.grid(row=4)

templabel2 = ttk.Label(tk)
templabel2.grid(row=5)

button_start = ttk.Button(tk, text='시작!')

def start():
    label_duration.grid_forget()
    entry_duration.grid_forget()
    label_startIdx.grid_forget()
    entry_startIdx.grid_forget()
    label_endIdx.grid_forget()
    entry_endIdx.grid_forget()
    label_amount.grid_forget()
    entry_amount.grid_forget()
    button_start.grid_forget()
    
    # TODO 문제 추첨한 리스트를 직접 사용해서 값을 꺼내기

    # TODO loop 한번 돌 때마다 한번 호출하는 함수 만들고, 그 안에서 리스트 하나씩 꺼내쓰기
    while 1:
        try:
            for index in problemOrder:                  # 문제 출제
                for k, v in quizlist[index].items():
                    print(k)
                    # wordlabel.configure(text=k)
                    wordlabel['text'] = k
                    sleep(duration)                     # 제한 시간만큼 노출
        except GeneratorExit as e:
            print('에러 발생: e')
        except:
            break

f = ttk.Frame(tk)
f.grid(columnspan=1)

button_setup = ttk.Button(f, text='설정', command=setup)
button_setup.grid(row=6, column=0)
button_start = ttk.Button(f, text='시작!', command=start)
button_start.grid(row=6, column=1)

wordlabel = ttk.Label(text='text')
wordlabel.grid(row=7)
# wordlabel.place(relx=0.5, rely=0.5)

# TODO shuffle이 충분히 크기가 클 때, 로딩에 오래걸릴 수 있으니 코루틴으로 짜기

# TODO tk가 invoke를 지원하지 않으니 강제로 화면을 넘겨서 우회
# duration만큼 대기하다가 next() 함수를 불러서 화면 갱신

mainloop()
