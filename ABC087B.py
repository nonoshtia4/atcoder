# -*- coding:utf-8 -*-
a = int(input())
b = int(input())
c = int(input())
x = int(input())
total = 0
result = 0

for i in range(a):
    for j in range(b):
        for k in range(c):
            #total = 500 * i + 100 * j + 50 * k
            total = 500 * k + 100 * j + 50 * i
            if total == x:
                result+=1

print(result)
