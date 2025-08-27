## First Solution at O(n power 2)

nums = [4,3,2,1,2]

n = len(nums)

prefix ,suffix = 1 , 1

answer = [1] * n

for i in range( 0 , n):

    answer[i] = prefix

    prefix = prefix * nums[i]

for j in range(n - 1 , -1 , -1):

    answer[j] = answer[j] * suffix

    suffix = suffix  * nums[j]

print(answer)