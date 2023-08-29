print("Enter n: ")
n = int(input())
print('Fill list with n elements: ')
listn = [int(input()) for i in range(n)]

setn = set(listn)

print("Enter m: ")
m = int(input())
print('Fill list with m elements: ')
listm = [int(input()) for i in range(m)]

setm = set(listm)

generic = set.intersection(setn,setm)

print(sorted(generic))