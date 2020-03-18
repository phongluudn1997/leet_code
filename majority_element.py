def majority_element(nums):
    '''@nums: List'''
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
            print(candidate)
        count += (1 if num == candidate else -1)
        print('count: {}, candidate: {}'.format(count, candidate))

    return candidate


print(majority_element([2, 1, 1, 1, 2]))
