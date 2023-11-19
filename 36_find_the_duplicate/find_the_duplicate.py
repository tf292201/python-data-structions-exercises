def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """
    
        # create a set to store the numbers
        # iterate through the list
        # if the number is in the set, return the number
        # if not, add the number to the set
        # if no duplicates, return None
    
    num_set = set()
    
    for num in nums:
        if num in num_set:
            return num
        else:
            num_set.add(num)
    
    return None

print(find_the_duplicate([1, 2, 1, 4, 3, 12]))
print(find_the_duplicate([6, 1, 9, 5, 3, 4, 9]))
print(find_the_duplicate([2, 1, 3, 4]))
