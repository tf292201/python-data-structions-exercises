def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    titleized = phrase.title()
    return titleized

print(titleize('this is awesome'))
print(titleize('oNLy cAPITALIZe fIRSt'))

