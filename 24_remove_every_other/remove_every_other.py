def remove_every_other(lst):
    """Return a new list with every other item removed.

    >>> lst = [1, 2, 3, 4, 5]
    >>> remove_every_other(lst)
    [1, 3, 5]

    This should return a new list, not mutate the original:
    >>> lst
    [1, 2, 3, 4, 5]
    """
    new_lst = []
    for i in range(len(lst)):
        if i % 2 == 0:
            new_lst.append(lst[i])
    return new_lst

print(remove_every_other([1, 2, 3, 4, 5]))
print(remove_every_other([1, 2, 3, 4, 5, 6]))
print(remove_every_other([1, 2, 3, 4, 5, 6, 7]))