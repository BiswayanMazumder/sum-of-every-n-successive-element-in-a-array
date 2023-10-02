
def Code(length,n,arr=[]):
    res=[]
    for i in range(n-1,length,n):
        res.append(arr[i])
    return sum(res)

length=int(input())
n=int(input())
arr=list(map(int,input().split()))
print(Code(length,n,arr))