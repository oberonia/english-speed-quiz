'''
1. 엑셀 파일에서 단어와 뜻을 읽어온다
    1) 인덱스 시작 또는 끝값을 지정하면 해당 값 범위의 무작위 단어를 긁어올 것
    2) 시작, 끝 인덱스가 없을 때는 전체 단어가 범위
2. 원하는 수량만큼 읽어온다
    1) 희망하는 단어 갯수를 입력받는다
3. 화면에는 문제 단어를 희망 시간만큼 보여주고, 다음 단어로 넘어간다
4. 모든 단어를 보여준 후에는, 정답지를 보여준다.
    1) 정답지는 보여준 순서대로 단어와 뜻을 함께 보여준다.
'''

from random import randint
from time import sleep
# from openpyxl import workbook

# TODO 각 변수는 사용자 입력을 받되, 미입력시에도 동작할 수 있도록 기본값 할당
# duration = 2                # 문제가 화면에 나타나는 시간 (단위: 초)
# # startInx, endInx = 0, 0     # 출제 범위
# startInx, endInx = 300, 309     # 출제 범위
# problems = 10                # 출제 수량
quizlist = list()           # 출제 범위에 해당하는 단어와 그 뜻을 모아둔 추첨 리스트
# randint 쓰려면 순서가 없는 딕셔너리에서는 무작위 추첨이 불가하여, 리스트로 생성
# 리스트의 각 항목은 딕셔너리 형태로 구성 [{word:meaning}, {word:meaning}]
final_quiz_list = list()    # quizlist를 problemOrder 순서대로 재정렬한 리스트
problemOrder = list()       # 단어를 출제할 순서, quizlist에서 꺼내올 순서
# answerlist = list()         # 출제한 순서대로 저장한 문제/정답 리스트

def shuffle(startIdx, endIdx, problems):
    global quizlist, problemOrder
    with open('word list.csv', 'rt') as file1:
        # next(file1)                       # 첫번째 열 건너뛰기
        params = file1.readlines()          # 리스트 params
        if endIdx == 0:
            endIdx = len(params)-1          # endInx값 미입력 시 마지막 단어까지 범위 지정
        for item in params[1:]:             # 0번은 tag column이므로 제외        
            item = item.strip(' \n-')
            temp = item.split(',')
            if len(quizlist) == problems:
                break
            if startIdx <= int(temp[0]) <= endIdx:          # 출제 범위에 해당하는 단어만 추첨 대상에 추가
                quizlist.append({temp[1]:temp[2]})
        # print(quizlist)
    while 1:
        randnum = (randint(0, len(quizlist)-1))
        if randnum not in problemOrder:
            problemOrder.append(randnum)
            final_quiz_list.append(list(quizlist[randnum].keys()))
            final_quiz_list.append(list(quizlist[randnum].values()))
        if len(problemOrder) == problems:
            break

# def quizstart(self):
#     global quizlist, problemOrder
#     try:
#         for index in problemOrder:                  # 문제 출제
#             for k, v in quizlist[index].items():
#                 yield k                             # 코루틴 밖으로 값 전달
#                 print(k)
#                 # sleep(0.2)
#                 # sleep(duration)                     # 제한 시간만큼 노출
#     except GeneratorExit as e:
#         print('에러 발생: e')
#     print('=== end of quiz ===')

# def showAnswers():
#     global quizlist, problemOrder
#     for index in problemOrder:                  # 정답 공개
#         for k, v in quizlist[index].items():
#             print(k, v)
#     print('end')