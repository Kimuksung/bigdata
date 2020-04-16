'''
135-806	서울	강남구	개포1동 경남아파트		1
135-807	서울	강남구	개포1동 우성3차아파트	(1∼6동)	2
135-806	서울	강남구	개포1동 우성9차아파트	(901∼902동)	3
'''

import os
try:
    dong = input("동을 입력하세요:")
    file = open("../data/zipcode.txt" ,mode= "r" ,encoding= "utf-8")
    line = file.readline()
    while line :
        add = line.split("\t")
        if add[3].startswith(dong):
            print('['+add[0]+']',add[1],add[2],add[3],add[4])
        line = file.readline() #두번째 줄 주소 읽음

except Exception as e:
    print("except " , e)
finally:
    print("the end")
    file.close()