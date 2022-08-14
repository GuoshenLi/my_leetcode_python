nums = [5,6,8,7,9,0]
target = 500
nums.sort()
target = str(target)

def search(nums, target):
    low, high = 0, len(nums) - 1
    while low < high:
        mid = low + (high - low + 1) // 2
        if nums[mid] <= target:
            low = mid
        else:
            high = mid - 1
    return nums[low] if nums[low] <= target else -1

def getMaxNumbers(nums, target):
    res, ans, flag = [], 0, False
    for i in range(len(target)):
        if flag:
            res.append(nums[-1])
            continue
        subtarget = target[i]
        temp = search(nums, int(subtarget))
        if temp == -1:
            if i == 0:
                if len(target) == 1:
                    return 0
                else:
                    return str(nums[-1]) * (len(target) - 1)
            else:
                index = i - 1
                while temp == -1 and index >= 0:
                    temp = search(nums, int(target[index]) - 1)
                    index -= 1
                if temp == -1:
                    return str(nums[-1]) * (len(target) - 1)
                res[index + 1] = temp
                for j in range(index + 2, i):
                    res[j] = nums[-1]
                res.append(nums[-1])
                flag = True
        else:
            if temp == int(subtarget):
                res.append(temp)
            else:
                res.append(temp)
                flag = True
    for i in range(len(res)):
        ans = ans * 10 + res[i]
    return ans

print(getMaxNumbers(nums, target))



from typing import List
"""
arr:可使用数字的数组
nums:目标数字对应的整数数组
preEq:之前是否每一位都使用了相等的值
index:当前考虑到了第几位，从0开始
函数语义：返回第index位后可组成的最大的数字，包括第index位
"""
def dfs(nums, target, preEq, index):
    #如果考虑完了最后一位，那么能组成的最大值为0
    if index == len(target):
        return 0

    if preEq:#如果前面使用的都是相等的数字
        for i in range(len(nums) - 1, -1, -1):#从最大的往下排
            if index == len(target) - 1:
                if nums[i] < target[index]:#在前面使用的都是相同的数字，那么最后一位的数字不能是相等的，这个看具体面试官的要求
                    temp = dfs(nums, target, nums[i] == target[index], index + 1)
                    if temp == -1:#向下深搜发现没有满足要求的值，则选用更小的数字
                        continue
                    # 向下深搜发现了满足要求的值，那说明我们找到结果了，把这一层的结果加进去，之后层层返回即可
                    return nums[i] * pow(10, len(target) - index - 1) + temp
            else:
                if nums[i] <= target[index]:#非最后一位的数字是可以相等的
                    temp = dfs(nums, target, nums[i] == target[index], index + 1)
                    if temp == -1:
                        continue
                    return nums[i] * pow(10, len(target) - index - 1) + temp
        #如果上面的for循环走完都没有return的话，那就说明这一层所有的数字都不满足要求
        #如果是第一个数字都无法满足的话，那就直接从第二位开始，将preEq置为False递归
        if index == 0:
            if len(target) == 1:
                return -1
            else:
                return dfs(nums, target, False, index + 1)
        # 如果上面的for循环走完都没有return的话，而且也不是第一位，那就返回-1，回退递归
        return -1
    else:
        #如果前面不是都选用了相等的数字，那就直接每次挑最大的数字就行了。
        return nums[len(nums) - 1] * pow(10, len(target) - index - 1) + dfs(nums, target, False, index + 1)


def find(N, nums):
    nums.sort()
    target = [int(i) for i in str(N)]
    #递归的初始条件，preEq=True，index=0
    return dfs(nums, target, True, 0)



arrInputList = [
    [2,3,4,5],
    [2,3,4,5],
    [2,3,4,5],
    [2,3,4,5],
    [5,6,8,7,9,0],
    [6,7,8,9]
]

NList =   [1234,2234,2231,2134,500, 2]
ansList = [555, 2233,2225,555,99, -1]
for i in range(len(NList)):
    ans = find(NList[i], arrInputList[i])
    print(NList[i], arrInputList[i], ans)
