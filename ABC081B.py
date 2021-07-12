# -*- coding:utf-8 -*-
n = int(input())
num_list = input().split()

count = 0
while True:
    for i, j in enumerate(num_list):
        if int(j) % 2 == 1:
            #print('Odd')
            print(count)
            exit()
        else:
            #print('Even')
            num_list[i] = int(j) / 2
    count+=1
