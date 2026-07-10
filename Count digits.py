def count_digit(text):
    count = 0
    for ch in text:
        if ch.isdigit():
          count +=1
    return count
result = count_digit("11DImplE2322R")  
print(result) 