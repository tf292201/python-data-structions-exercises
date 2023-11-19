def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1 = str(num1)
    num2 = str(num2)
    num1_dict = {}
    num2_dict = {}
    for num in num1:
        num1_dict[num] = num1_dict.get(num, 0) + 1
    for num in num2:
        num2_dict[num] = num2_dict.get(num, 0) + 1
    return num1_dict == num2_dict

print(same_frequency(551122, 221515))
print(same_frequency(321142, 3212215))
print(same_frequency(1212, 2211))
