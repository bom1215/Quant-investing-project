#2562번 문제

# b= []
# max=0
# for i in range(9):
#     a = int(input())
#     b.append(a)
#     if max > a:
#         max != a
#     elif max <= a:
#         max = a
# print(max, b.index(max)+1) 

# 2577번 문제

# A = int(input())
# B = int(input())
# C = int(input())

# D = str(A*B*C)

# for i in range(10):
#     i = str(i)
#     print(D.count(i))


# 3052번 문제

# b=[]
# for i in range(10):
#     a = int(input())
#     b.append(a%42)
# b= set(b)
# print(len(b))

# 1546번 문제

# N = int(input())
# a = list(map(int,input().split()))
# b=[]
# for i in a:
#     b.append(i/max(a)*100)

# print(sum(b)/N)

# 8958번 문제- 못 푼 문제


# N = int(input())

# for i in range(N):
#     a = input()
#     score = 0
#     sumScore = 0
#     for j in a:
#         if j == 'O':
#             score += 1
#         else:
#             score = 0
#         sumScore += score
#     print(sumScore)


# 4344번 문제

    
# import math

# C = int(input())
# for i in range(C):
#     N = list(map(int, input().split()))
#     avg = sum(N[1:])/N[0]
#     cnt= 0
#     for i in N[1:]:
#         if i > avg:
#             cnt += 1
#     R=format(round(cnt/N[0]*100,3),".3f")
#     print(str(R)+"%")

# 10926번 문제

# id= input()
# print(id+"??!")


#18108번 문제
# y= int(input())
# print(y-543)

# 15596번 문제

# def solve(a):
#     ans = 0
#     for i in a:
#         ans += i
#     return ans

# 4673번 문제


# def d(n):
#     a = n
#     n = str(n)
#     for i in range(len(n)):
#         a += int(n[i])
#     return(a) 
# num = 10000
# b = set(range(1,num+1))
# e =set()

# for i in range(num):
#     c =d(i+1)
#     if c <= num:
#         e.add(c)
# f = list(b-e)
# f.sort()
# for i in f:
#     print(i)



# 1065번 문제


# def d(a):
#     a =str(a)
#     for i in range(len(a)-2):
#         if int(a[i+1]) - int(a[i]) == int(a[i+2]) -int(a[i+1]):
#             return 1
#         else:
#             return 0

# a = int(input())
# cnt = 0
# for i in range(a+1):
#     if i == 0:
#         continue
#     if i > 0 and i < 100:
#         cnt +=1
#     else:
#         cnt += d(i)
        
# print(cnt)


# #11654번 문제
# a= input()
# print(ord(a))

#11720번 문제
# N = int(input())
# a = input()
# cnt = 0
# for i in a:
#     i = int(i)
#     cnt +=i
# print(cnt)


#10809번 문제

# s= input()
# for i in "abcdefghijklmnopqrstuvwxyz":
#     if s. find(i) == -1:
#         print(-1)
#     else:
#         print(s.find(i))


# 2675번 문제 - 못 푼 문제

# T= int(input())
# for i in range(T):
#     num, Sw= (input().split())
#     res =''
#     for i in Sw:
#        res += int(num)*i
#     print(res)


# 1157번 문제- 못푼 문제

# words = input().upper()
# unique_words = list(set(words))  # 입력받은 문자열에서 중복값을 제거

# cnt_list = []
# for x in unique_words :
#     cnt = words.count(x)
#     cnt_list.append(cnt)  # count 숫자를 리스트에 append

# if cnt_list.count(max(cnt_list)) > 1 :  # count 숫자 최대값이 중복되면
#     print('?')
# else :
#     max_index = cnt_list.index(max(cnt_list))  # count 숫자 최대값 인덱스(위치)
#     print(unique_words[max_index])


#1152번 문제

# w= input()
# a= w.split()
# cnt = 0
# for i in a:
#     cnt += 1
# print(cnt)

#2908번 문제

# def lis(a):
#     b=[]
#     for i in a:
#         b.append(i)
#     b.reverse()
#     return b

# def rev(b):
#     c =''
#     for i in b:
#         c+= i
#     return c


# a, b= input().split()

# if rev(lis(a)) > rev(lis(b)):
#     print(rev(lis(a)))
# else:
#     print(rev(lis(b)))


#5622번 문제

# a = input()
# cnt = 0
# for i in a:
#     if i == "A" or i == "B" or i == "C":
#         cnt += 3
#     elif i == "D" or i == "E" or i == "F":
#         cnt += 4
#     elif i == "G" or i == "H" or i == "I":
#         cnt += 5
#     elif i == "J" or i == "K" or i == "L":
#         cnt += 6
#     elif i == "M" or i == "N" or i == "O":
#         cnt += 7
#     elif i == "P" or i == "Q" or i == "R" or i =="S":
#         cnt += 8
#     elif i == "T" or i == "U" or i == "V":
#         cnt += 9
#     else:
#         cnt += 10
# print(cnt)

#2941번 문제 - 못 푼 문제

# a= input()
# exc = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
# for i in exc:
#     a = a.replace(i, "0")
# print(len(a))

#1316번 문제 - 못 푼 문제

# N= int(input())
# gw= 0
# for i in range(N):
#     w = input()
#     error =0
#     for i in range(len(w)-1):
#         if w[i] != w[i+1]:
#                 nw=w[i+1:]
#                 if nw.count(w[i]) > 0:
#                     error +=1
#     if error ==0:
#         gw += 1
# print(gw)

# 1712번 문제 - 못푼 문제



# A, B, C= map(int,input().split())


# if B >= C:
#     print(-1)
# else:
#     print(int((A/(C-B))+1))


# 2292번

# a= int(input())
# n=1
# b=0

        
# while True
#     b= 3*(n-1)**2+3*(n-1)+1
#     if a > b:
#         n+=1
#     else:
#         print(n)
#         break
        

#1193번 문제

# X= int(input())
# n=0
# while True:
#     n=n+1
#     s= int(n*(n+1)/2)
#     if X-s < 0:
#         if n%2 ==0:
#             rs =int((n-1)*n/2)
#             print(str(X-rs)+"/"+str(n-(X-rs-1)))
#             break
#         elif n%2 != 0:
#             rs =int((n-1)*n/2)
#             print(str(n-(X-rs-1))+"/"+str(X-rs))
#             break
#     elif X-s == 0:
#         if n%2 ==0:
#             print(str(n)+"/"+"1")
#             break
#         else: 
#             print("1"+"/"+str(n))
#             break
#     else:
#         continue


#2869번 문제- 못 푼 문제
# import math

# A,B,V = map(int,input().split())
# n = (V-B)/(A-B)
# print(math.ceil(n))



# 10250번 문제

# T= int(input())
# for i in range(T):
#     H,W,N = map(int, input().split())
#     for i in range(1,W+1):
#         if N <= H*i:
#             Garo = str(i)
#             Sero = str(N-H*(i-1))
#             break
#         else:
#             continue
#     if int(Garo) < 10:
#         print(Sero+"0"+Garo)
#     else:
#         print(Sero+Garo)


# 2775번 문제 - 못 푼 문제 -> 풀었음

# T= int(input())

# for a in range(T):
#     k= int(input())
#     n= int(input())
#     F0 = list(range(1,n+1))
#     for b in range(k):
#         for i in range(n):
#             F0[n-i-1] = sum(F0[:n-i])
#     print(F0[n-1])


# 2839번 문제


# N= int(input())
# A=3
# B=5

# res_list =[]
# for i in range((N//3)+1):
#     C= (N-3*i)/5
#     if C - int(C) ==0:
#         res_list.append(i+C)

# if len(res_list)==0:
#     print(-1)
# else:
#     print(int(min(res_list)))

# 10757번 문제
# A, B= map(int, input().split())
# print(A+B)


#1011번 문제x=0
# T= int(input())
# for i in range(T):
#     x,y= map(int,input().split())
#     a= y-x
#     if a**(1/2)-int(a**(1/2))==0:
#         print(int(a**(1/2))*2-1)
#     else:
#         n=int(a**(1/2))
#         b= a-n**2
#         if b%n ==0:
#             print(int(a**(1/2))*2-1+b//n)
#         else:
#             print(int(a**(1/2))*2-1+b//n+1)


#1978번 문제

# N = int(input())
# A = list(map(int,input().split()))
# nososu=[]

# for a in A:
#     for i in range(2,a):
#         if a%i == 0:
#             nososu.append(a)
#         else:
#             continue

# nososu = set(nososu)
# nososu.add(1)
# print(len(set(A)-nososu))


#2581번 문제

# M= int(input())
# N= int(input())
# lis = set(list(range(M,N+1)))

# nososu =[]
# for a in range(M,N+1):
#     for i in range(2,a):
#         if a%i ==0:
#             nososu.append(a)
#         else:
#             continue
# nososu = set(nososu)
# nososu.add(1)
# sosu = list((lis-nososu))
# sosu.sort()


# if sosu:
#     print(sum(sosu))
#     print(sosu[0])
# if not sosu:
#     print(-1)


#11653번 문제- 못푼 문제 -> 풀었음

# N =int(input())
# n=2

# while N >=n:
#     if N % n ==0:
#         N = N//n
#         print(n)
#     else:
#         n= n+1

# 1929번 문제 - 못푼 문제 -> 풀었음

# A= [True for i in  range(10**6+1)]
# A[0]= False
# A[1]= False

# n=1
# while n < (100**6)**(1/2)+1:
#     n= n+1
#     for i in range(1,10**6+1):
#         try:
#             A[n*(i+1)] = False
#         except:
#             break

# M, N = map(int, input().split())
# for i in range(M,N+1):
#     if A[i] == True:
#         print(i)
#     else:
#         continue


#4948번 문제 - 못푼 문제 -풀었음

# A= [True for i in  range(123456*2+1)]
# A[0]= False
# A[1]= False

# n=1
# while n < (123456*2)**(1/2)+1:
#     n= n+1
#     for i in range(1,123456*2+1):
#         try:
#             A[n*(i+1)] = False
#         except:
#             break
# n=1

# while True:
#     n= int(input())
#     if n ==0:
#         break
#     elif n ==1:
#         print(1)
#     else:
#         cnt=0
#         for i in range(n+1,2*n):
#             if A[i] == True:
#                 cnt +=1
#             else:
#                 continue
#         print(cnt)



#9020번 문제 - 못푼 문제 -> 풀었음.

# A= [True for i in  range(10001)]
# A[0]= False
# A[1]= False

# n=1
# while n < (10000)**(1/2)+1:
#     n= n+1
#     for i in range(1,10001):
#         try:
#             A[n*(i+1)] = False
#         except:
#             break
# T = int(input())
# for i in range(T):
#     a = int(input())
#     n= a//2
#     while True:
#         if A[n] == True and A[a-n] == True:
#             print(n, a-n)
#             break
#         else:
#             n -=1






#1085번 문제

# x, y, w, h = map(int, input().split())

# res = [x, y, h-y, w-x]
# res.sort()
# print(min(res))

# 3009번 문제

# a, b= map(int, input().split())
# c, d= map(int, input().split())
# e, f= map(int, input().split())
# x = [a,c,e]
# y = [b,d,f]

# for i in x:
#     if x.count(i) ==1:
#         print(i, end=" ")
# for i in y:
#     if y.count(i) ==1:
#         print(i)


# 4153번 문제

# while True:
#     a = list(map(int, input().split()))
#     if a == [0,0,0]:
#         break
#     else:
#         a.sort()
#         if (a[0])**2 +(a[1])**2 == (a[2])**2:
#             print("right")
#         else:
#             print("wrong")



# 3053번 문제

# import math

# r= int(input())
# print(f"{r*r*math.pi:.6f}")
# print(f"{r*2*r*2*0.5:.6f}")


# 1002번 문제


# import math
# T= int(input())
# for i in range(T):
#     x1, y1, r1, x2, y2, r2= map(int, input().split())
#     d= ((x1-x2)**2 + (y1-y2)**2)**(1/2)
#     if d == 0 and r1==r2:
#         print(-1)
#     else:
#         if r1+r2 < d:
#             print(0)
#         elif r1+r2 == d:
#             print(1)
#         elif abs(r1-r2) < d and d < r1+r2:
#             print(2)
#         elif abs(r1-r2) == d:
#             print(1)
#         elif abs(r1-r2) > d and r1 != r2:
#             print(0)


#10872번 문제

# def factorial(n):
#     result = 1
#     if n > 0:
#         result = n * factorial(n-1)
#     return result

# n = int(input())
# print(factorial(n))


#10870번 문제

# def pibo(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     else:
#         result = pibo(n-1)+pibo(n-2)
#         return result

# n= int(input())
# print(pibo(n))


#2447번 문제 - 못푼 문제


# 11729번 문제 - 못푼문제


#2798번 문제- 못푼문제
# N, M= map(int, input().split())
# A= list(map(int, input().split()))
# b=[]
# for i in range(N):
#     for j in range(N):
#         for k in range(N):
#             if A[i] < A[j] and A[j] < A[k]:
#                 if A[i]+A[j]+A[k] <= M:
#                     b.append(A[i]+A[j]+A[k])
                    
# print(max(b))



#2231번 문제 -못푼문제

# N=int(input())
# result=[]
# for i in range(1,N):
#     lis=[str(i)[j] for j in range(len(str(i)))]
#     ss=i
#     for k in lis:
#         ss += int(k)
#     if ss == N:
#         result.append(i)
    
# if len(result)==0:
#     print(0)
# else:
#     print(min(result))


#7568번 문제 - 못푼문제
# N=int(input())
# A=[]
# cnt=1

# for i in range(N):
#     W,H = map(int, input().split())
#     A.append([W,H])

# for i in range(N):
#     for j in range(N):
#         if A[i][0] < A[j][0] and A[i][1] < A[j][1]:
#             cnt+=1
#     print(cnt, end=" ")
#     cnt=1

#1018번 문제 
# N, M = map(int, input().split())
# lis=[]


# for i in range(N):
#     colors = input()
#     lis.append(colors)

# White = ['WBWBWBWB', 'BWBWBWBW']*4
# Black = ['BWBWBWBW', 'WBWBWBWB']*4
# cnt=0
# result=[]
# for i in range(N-7):
#     for j in range(M-7):
#         sample_matrix= [i[j:j+8] for i in lis[i:i+8]]
#         for k in range(8):
#             for l in range(8):
#                 if sample_matrix[k][l] != White[k][l]:
#                     cnt +=1
#         result.append(cnt)
#         cnt=0
# for i in range(N-7):
#     for j in range(M-7):
#         sample_matrix= [i[j:j+8] for i in lis[i:i+8]]
#         for k in range(8):
#             for l in range(8):
#                 if sample_matrix[k][l] != Black[k][l]:
#                     cnt +=1
#         result.append(cnt)
#         cnt=0

# print(min(result))

#1436번 문제

# def Jong_num(a):
#     for i in range(len(a)-2):
#         if a[i] == "6":
#             if a[i+1] == "6":
#                 if a[i+2] == "6":
#                     return True
                    
         
# N = int(input())
# cnt=599
# n=0
# while n < N:
#     cnt+=1
#     if Jong_num(str(cnt)) == True:
#         n +=1

# print(cnt)


#2750번 문제

#2981번 문제

#3036번 문제

# import fractions


# N= int(input())

# A= list(map(int, input().split()))

# for i in range(1,len(A)):
#     a= fractions.Fraction(A[0])/fractions.Fraction(A[i])
#     if a.denominator == 1:
#         print(str(a)+"/"+"1")
#     else:
#         print(a)

#110501번 문제
# import math

# n, k = map(int, input().split())
# print(int(math.factorial(n)/math.factorial(k)/math.factorial(n-k)))

# 11051번 문제

# 1010번 문제

# 2525번 문제

# H, M = map(int, input().split())
# add_m= int(input())

# if M+add_m > 59:
#     result_H = H + (M+add_m)//60 
#     result_M = (M+add_m) % 60
#     if result_H > 23:
#         print(result_H-24, end= " ")
#         print(result_M)
#     else:
#         print(result_H, end=" ")
#         print(result_M)
# else:
#     if H > 23:
#         print(H-24, end= " ")
#         print(M+add_m)
#     else:
#         print(H, end = " ")
#         print(M+add_m)


#2480번 문제

# from collections import Counter

# lis = list(map(int, input().split()))
# lis2 = list(set(lis))

# if len(lis2) ==3:
#     print(max(lis)*100)
# elif len(lis2)==2:
#     lis2 = Counter(lis)
#     for key, value in lis2.items():
#         if value >=2:
#             print(1000+key*100)
# elif len(lis2)==1:
#     print(10000+lis2[0]*1000)


#10989번 문제
N = int(input())
a=[]
for i in range(N):
    a.append(int(input()))
print(a)

b=[0]*(max(a)+1)
for i in range(len(b)):
    if i in a:
        cnt= a.count(i)
        b[i]=cnt

b.reverse()
for i in range(len(b)):
    if i >=1:
        b[i] += b[i-1]
b.reverse()
print(b)
# for i in a:
#     print(b[i])



