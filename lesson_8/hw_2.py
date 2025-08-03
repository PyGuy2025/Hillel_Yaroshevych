from string import punctuation
chars = punctuation + ' '

def is_palindrome(text:str) -> bool:
    f_string = ''.join(char.lower() for char in text if char not in chars)
    return f_string == f_string[::-1]

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")