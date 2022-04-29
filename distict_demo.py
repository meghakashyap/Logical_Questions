
# list  = [1,7,2,4]
# def nonDivisibleSubset(S):
#     i = 0
#     k = 3
#     divide=0
#     no_divi =0
#     while i<len(list):
#         j = i+1
#         while j<len(list):
#             print(list[i],list[j])
#             sum = list[i]+list[j]
#             print(sum,"its a sum of",list[i],list[j])
#             if sum%k==0:
#                 divide+=1
#             else:
#                 no_divi+=1
#             j+=1
#         print(no_divi)
       
#         i+=1
        # return no_divi

# n,k = map(int,input("1.Enter the lenght of list 2.Enter the divisor: ").split())
# S = list(map(int,input("Enter the elements of list : ").split(" ",n)))
# nonDivisibleSubset(list)

def nonDivisibleSubset(S):
    index = 0
    divide = 0
    no_divide = 0

    while index < len(S):
        j = index + 1
        while j < len(S):
            sum = S[index]+S[j]
            if sum % k == 0:
                divide += 1
            else:
                no_divide += 1
            j+=1
        index+=1

    # return no_divide
k=4
S=[19,10,12,10,24,25,22]
# n,k = map(int,input("1.Enter the lenght of list 2.Enter the divisor: ").split())
# S = list(map(int,input("Enter the elements of list : ").split(" ",n)))
print(nonDivisibleSubset(S))
# distinct integer



# # a =[19,10,12,10,24,25,22]
# from collections import Counter
# def nonDivisibleSubset(a):
#     c = Counter((i%k for i in a))
#     print(c,"its c")
#     count = 0
#     blacklist = set()
#     for x,y in c.most_common():
#         # print(x,"its a x",y,"its a y")
#         if x == k/2 or x==0:
#             print("yes")
#             count+=1
#         elif k-x not in blacklist:
#             print(k-x,"itsa k-x")
#             print("no")
#             count+=y
#             blacklist.add(x)
#     return count

# k=4
# a =[19,10,12,10,24,25,22]
# # # n,k = map(int,input("1.Enter the lenght of list 2.Enter the divisor: ").split())
# # # a = list(map(int,input("Enter the elements of list : ").split(" ",n)))
# print(nonDivisibleSubset(a))

# # b=Counter(i%k for i in a)
# # print(b,"bamd")
# # print(b.most_common())
# # for x ,y in b.most_common():
# #     print(k/2)
# # # for i in b:
# # #     # print(i,"yvfhkiiiiiiiiiiii")
# # #     print(b[i],"b")

# # #     c=i%k
# #     # print(c,"dgbuiweybi")



 
# Returns maximum size of subset
# with no pair sum divisible by K
def subsetPairNotDivisibleByK(arr, N, K):
 
    # Array for storing frequency
    # of modulo values
    f = [0 for i in range(K)]
 
    # Fill frequency array with
    # values modulo K
    for i in range(N):
        f[arr[i] % K] += 1
 
    # if K is even, then update f[K/2]
    if (K % 2 == 0):
        f[K//2] = min(f[K//2], 1)
 
    # Initialize result by minimum of 1 or
    # count of numbers giving remainder 0
    res = min(f[0], 1)
 
    # Choose maximum of count of numbers
    # giving remainder i or K-i
    for i in range(1,(K // 2) + 1):
        res += max(f[i], f[K - i])
 
    return res
     
# Driver Code
arr = [19,10,12,10,24,25,22]
N = len(arr)
K = 4
print(subsetPairNotDivisibleByK(arr, N, K))
 

 # def nonDivisibleSubset(S):
#     index = 0
#     divide = 0
#     no_divide = 0

#     while index < len(S):
#         j = index + 1
#         while j < len(S):
#             sum = S[index]+S[j]
#             if sum % k == 0:
#                 divide += 1
#             else:
#                 no_divide += 1
#             j+=1
#         index+=1

#     return no_divide

# n,k = map(int,input("1.Enter the lenght of list 2.Enter the divisor: ").split())
# S = list(map(int,input("Enter the elements of list : ").split(" ",n)))
# print(nonDivisibleSubset(S))
# # distinct integer



a=[19,10,12,10,24,25,22]
k=4
def fun():
    for i in a:
        c=i%k
        # print(c)
fun()

d=[]
no=[]
def nonDivisibleSubset(S):
    index = 0
    divide = 0
    no_divide = 0

    while index < len(S):
        j = index + 1
        while j < len(S):
            sum = S[index]+S[j]
            print(sum,S[index],S[j],"hy its")
            if sum % k == 0:
                d.append(sum)
                divide += 1
            else:
                no_divide += 1
                no.append(sum)
            j+=1
        index+=1
        # print(no,"ni")
        # print(d,"yes")

    return no_divide


S=[19,10,12,10,24,25,22]
k=4
print(nonDivisibleSubset(S))
# distinct integer


# [19,10,12,10,24,25,22] 19%4=3,2,0,2,0,1,2
# [4]