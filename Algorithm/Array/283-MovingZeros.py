#给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#输入: [0,1,0,3,12]
#输出: [1,3,12,0,0]
def moving_zeros(nums):
    """
    :param nums: array of integers
    :return: array
    """
    idx = 0
    for num in nums:
        if num != 0:
            nums[idx] = num
            idx += 1
    for i in range(idx, len(nums)):
        nums[i] = 0
    return nums

if __name__ == '__main__':
    print(moving_zeros([2, 0, 1, 0, 2]))