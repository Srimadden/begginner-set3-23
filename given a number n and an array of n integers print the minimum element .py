def smallest(arr,n):
    min=arr[0]
    for i in range(1,n):
        if arr[i]<min:
            min=arr[i]
        return min
arr=[2,10]
n=len(arr)
ans=smallest(arr,n)
print("minimum number in given array is",ans)

