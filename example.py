arr = [9,8,7,5,5,2,1,1,3,3,4]
n = len(arr)
# Mean
mean = sum(arr) / n
print("Mean:", mean)

# Median
arr.sort()
if len(arr)%2==0:
    median = (arr[n//2] + arr[n//2+1] ) / 2
else:
    median = arr[n//2]    
print("Median:", median) 

# Mode
freq = {x:arr.count(x) for x in arr}
frequencyMax = max(freq.values())

print("Modes: ",end="")
for k,v in freq.items():
    if v == frequencyMax:
        print(k,end=" ")