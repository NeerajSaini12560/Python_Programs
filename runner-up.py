# n=int(input())
# list=[]
# for i in range(0, n):
#   a=int(input())
#   list.append(a)
# list.sort()
# print(list[-2])

n = int(input())

nums = map(int, input().split())    
print(sorted(list(set(nums)))[-2])
