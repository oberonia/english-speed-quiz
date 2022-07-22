# from random import randint
# import csv

# quizlist = list()           # 출제 범위에 해당하는 단어와 그 뜻을 모아둔 추첨 리스트
# # randint 쓰려면 순서가 없는 딕셔너리에서는 무작위 추첨이 불가하여, 리스트로 생성
# # 이중리스트 형태로 구성 [[word,meaning,commentary], [word,meaning,commentary]]
# final_quiz_list = list()    # quizlist를 problemOrder 순서대로 재정렬한 리스트
# problemOrder = list()       # 단어를 출제할 순서, quizlist에서 꺼내올 순서

# def shuffle(startIdx, endIdx, problems, filename):
#     global quizlist, problemOrder
#     if filename == '':
#         filename = 'word list'
#     filename = filename + '.csv'
#     with open(filename, 'r', encoding='utf-8-sig') as file1:
#         # next(file1)                       # 첫번째 열 건너뛰기
#         # params = file1.readlines()          # 리스트 params
#         params = csv.DictReader(file1)
#         if endIdx == 0:
#             endIdx = len(params)-1          # endInx값 미입력 시 마지막 단어까지 범위 지정
#         for item in params:                 # 0번은 tag column이므로 제외
#             # item = item.strip(' \n-')
#             # print(item)
#             # temp = item.split(',')          # 본문 안에 있는 ,와 csv ,구분 못함 -> DictReader로 해결
#             if len(quizlist) == problems:
#                 break
#             try:
#                 if startIdx <= int(item['index']) <= endIdx:          # 출제 범위에 해당하는 단어만 추첨 대상에 추가
#                     quizlist.append([item['word'], item['mean'], item['commentary']])
#             except ValueError as e:
#                 print('에러 발생',e)
#                 continue
#         # print(quizlist)
#     while 1:
#         randnum = (randint(0, len(quizlist)-1))
#         word = quizlist[randnum][0]              # 단어
#         meaning = quizlist[randnum][1]            # 뜻
#         commentary = quizlist[randnum][2]       # 해설
#         if randnum not in problemOrder:
#             problemOrder.append(randnum)
#             final_quiz_list.append((word, meaning,commentary,))
#         if len(problemOrder) == problems:
#             break

