def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
        
      
    open_parens = 0
    close_parens = 0
    
    for char in parens:
        if char == '(':
            open_parens += 1
        elif char == ')':
            close_parens += 1
        if close_parens > open_parens:
            return False
    
    return open_parens == close_parens

print(valid_parentheses("()"))
print(valid_parentheses("()()"))
print(valid_parentheses("(()())"))
print(valid_parentheses(")()"))
print(valid_parentheses("())"))
print(valid_parentheses("((())"))
print(valid_parentheses(")()("))
