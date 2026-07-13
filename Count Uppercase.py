def count_uppercase(text):
    count = 0
    for ch in text:
        if ch.isupper():
            count += 1
     
    return count
result = count_uppercase("DImplER")  
print(result) 