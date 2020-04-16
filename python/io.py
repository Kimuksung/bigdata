'''
text file io
open(file,mode='r','w','a')

'''

import os #파일 경로

try:
    #print(os.getcwd())
    '''
    file = open("C:/ITWILL/3_Python-I/workspace/chap07_IO/data/ftest.txt" , mode='r')
    print(file.read())

    file = open('../data/ftest.txt')
    print(file.read())
    
    file2 = open('../data/ftest2.txt' , mode = 'w')
    file2.write("my first text~~")

    file2 = open('../data/ftest2.txt', mode='a')
    file2.write("\nadditional second text~")

    file.read() : 전체 문서 한 번에 읽기
    file.readLine() : 전체 문서에서 한 줄 읽기
    file.readLines() : 전체 문서를 줄 단위로 읽기

    file = open('../data/ftest.txt')
    for i in file.readlines():
        print(i.strip())
    '''
    #with
    with open("../data/ftext3.txt" , mode ='w' , encoding= "utf-8") as file3:
        file3.write("파이썬 파일 작성 연습")
        file3.write("\n파이썬 파일 작섭 연습2")
        file3.write("\n파이썬 파일 작섭 연습3")

    with open("../data/ftext3.txt" , mode ='r' , encoding= "utf-8") as file4:
        print(file4.read())

except FileNotFoundError as e:
    print(e)
finally:
    #file.close()
    pass

