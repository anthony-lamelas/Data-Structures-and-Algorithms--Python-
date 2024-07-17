def can_construct(word, letters):
    let = list(letters)  

    for char in word:
        if char in let:
            let.remove(char) 
        else:
            return False 
        
    return True  

print(can_construct("apples", "aplespl"))  
print(can_construct("apples", "aples"))    
