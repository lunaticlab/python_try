# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 03:34:39 2021

@author: 劉之岳
"""
x=-20;xnew=0
r=0.1 #learning_rate
count=0
# function=(2x+1)^2 求 minimum
while True :
    count+=1
    if count==10:
        break
    xnew=x*(1-8*r)-4*r
    x=xnew
#    print(xnew)
print("ans",xnew)

x1=1;x2=1 #feature data
w1=10;w2=5;#guess weight right answer is w1=0,w2=0
# 可想成解 w1^2+w2^2 min.
count=0
function=w1^2*x1+w2^2*x2
while True:
    count+=1
    if count==10:
        break
    w1_new=w1*(1-2*r)
    
    w2_new=w2*(1-2*r)
    w1=w1_new
    w2=w2_new
    
print(w1,w2)


x1=1;x2=1 #feature data
w1=10;w2=5;#guess weight right answer is w1=0,w2=0
function=(w1*x1+w2*x2)^2
count=0
r=0.1 #learning_rate
while True:
    count+=1
    if count==50:
        break
    w1_new=w1-0.1*(2*(w1*x1+w2*x2)*x1)
    w2_new=w2-0.1*(2*(w1*x1+w2*x2)*x2)
    w1=w1_new
    w2=w2_new
function=(w1*x1+w2*x2)**2
print(w1,w2,function)