# Returns maximum size of subset
# with no pair sum divisible by K
def nonDivisibleSubset (arr, N, K):
 
    # Array for storing frequency
    # of modulo values
    f = [0 for i in range(K)]
    print(f)
 
    # Fill frequency array with
    # values modulo K
    for i in range(N):
        f[arr[i] % K] += 1
        print(f)
        print(arr[i] % K ,"ashdk")
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
print(nonDivisibleSubset (arr, N, K))


# def nonDivisibleSubset(S,k):
#     count = [0] * k

#     for i in S:
#         remainder = i % k
#         count[remainder] +=1
    
#     ans = min( count[0] , 1)         

#     if k % 2 == 0:                    
#         ans += min(count[k//2] ,1 )n

#     for i in range( 1 , k//2 + 1):    
#         if i != k - i:           
#             ans += max(count[i] , count[k-i])
#     return ans

# n,k = map(int,input("1.Enter the lenght of list 2.Enter the divisor: ").split())
# S = list(map(int,input("Enter the elements of list : ").split(" ",n)))
# print(nonDivisibleSubset(S,k))

