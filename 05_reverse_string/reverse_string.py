def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    return ''.join(reversed(phrase))

print(reverse_string('awesome'))
print(reverse_string('sauce'))