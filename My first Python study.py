# i = int(input())

# for n in range(i):
#     print("*"*(n+1))
#_____________________________
# i = int(input())

# for n in range(i):
#     print("*"*(i-n))
#______________________________
# n = int(input())

# for i in range(n):
#     print(" "*i+"*"*(n-i))
#_______________________________
# n = int(input())

# for i in range(n):
#     print("*"*n)
#________________________________
# n = int(input())

# if n%2==0:
#     print("enjoy")
# else:
#     print("oh my god")
#________________________________

# a,b=input().split()
# n=int(a)
# k=int(b)
# sum=(n+k)
# if n%2==0:
#     print("짝수+",end='')
# else:
#     print("홀수+",end='')
# if k%2==0:
#     print("짝수=",end='')
# else:
#     print("홀수=",end='')
# if (sum)%2==0:
#     print("짝수")
# else:
#     print("홀수")
# _______________________________
# a,b=input().split()
# n=int(a)
# k=int(b)
# t=(90-n)

# s=t//5
# if t%5==0:
#     print(s+k) 
# else:
#     print(s+k+1)
# ____________________________
# n = int(input())

# if n <= 10:
#     print("정상")
# elif n>20:
#     print("비만")
# else:
#     print("과체중")
# ____________________________ 
# a,b,c=input().split()
# x=int(a)
# y=int(b)
# z=int(c)
# i=(90-x)
# j=i//5
# k=y+j

# if i%5 != 0:
#     k=k+1
#     if k==z:
#         print("same")
#     elif k>z:
#         print("win")
#     else:
#         print("lose")
# else:
#     if k==z:
#         print("same")
#     elif k>z:
#         print("win")
#     else:
#         print("lose")
# ____________________________

# a,b=input().split()
# x=float(a)
# y=float(b)

# n=(x-100)*0.9
# k=((y-n)*100)/n

# if k<=10:
#     print("정상")
# elif k>20:
#     print("비만")
# else:
#     print("과체중")
# __________________________
#4/9
# a,b=input().split()
# key=float(a)
# mom=float(b)

# if key<150:
#     pyo=(key-100)
# elif key>=160:
#     pyo=(key-100)*0.9
# else:
#     pyo=(key-150)/2+50

# bi=(mom-pyo)*100/pyo
# if bi<=10:
#     print("정상")
# elif bi>20:
#     print("비만")
# else:
#     print("과체중")
# ________________________
# a,b=input().split()
# k=int(a) 
# h=int(b) 

# if k%2 ==0:
#     k=k*5
# else:
#     k=k//2+1 
# if h%2 ==0:
#     h=h*5
# else:
#     h=h//2+1 

# print(k+h)
# ____________________
# a,b=map(int,input().split())
# sum=0
# for i in range(a,b+1):
#     if i%2==0:
#         sum-=i
#     else:
#         sum+=i
# print(sum)
# ___________________    
    

