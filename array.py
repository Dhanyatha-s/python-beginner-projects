# 50 array questions
# 1. find the peak element in the array where it neighbour should be less than the array element

def findpeak(arr, n):
    if n==1:
        return 0
    if arr[0]>=arr[1]:
        return 0
    if arr[n-1]>= arr[n-2]:
        return n-1
    
    for i in range(n):
        if arr[i]>= arr[i-1] and arr[i]>= arr[i+1]:
            return i
arr = [1,2,10,20,4]
n=len(arr)
print("index of peak element", findpeak(arr, n))

    
