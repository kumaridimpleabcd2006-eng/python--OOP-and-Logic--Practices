def palindrome(text):
    reverse = ""
    
    for ch in text:
        reverse = ch + reverse
    if text == reverse:
            return "palindrome"
    else:
        return "not palindrome"
    
result = palindrome("tatat")           
print(result)       