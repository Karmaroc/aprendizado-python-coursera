"""
function reverse_word(string word)
    reversed = ""
    for letter in word:
            reversed = letter + reversed
    return reversed

function check_all_palindromes(array arr)
    if arr[0] == reverse_word(arr[0])
            if arr[1] == reverse_word(arr[1])
                    if arr[2] == reverse_word(arr[2])
                            return true
    return false
    
    =========================================
"""

def reverse_word(x):
    reverso = ""
    
    for letra in x:
        reverso = letra + reverso 
    return reverso

def check(arr):
    if arr[0] == reverse_word(arr[0]):
        if arr[1] == reverse_word(arr[1]):
            if arr[2] == reverse_word(arr[2]):
                return True

    return False

print(check(['racecar', 'shoe', 'moon']))


"""
function reverse_word(string word)
    reversed = ""
    for letter in word:
            reversed = letter + reversed
    return reversed

function is_palindrome(string word)
        return word == reverse_word(word)

function check_all_palindromes(array arr)
        for word in arr:
                if is_palindrome(word) == false
                        return false
        return true
    
    =========================================
"""

def reverse_word(x):
    reverso = ""
    
    for letra in x:
        reverso = letra + reverso 
    return reverso

def is_palindrome(x):
    return x == reverse_word(x)

def check(arr):
    for x in arr:
        if is_palindrome(x) == False:
            return False
    
    return True
    
print(check(['racecar', 'shoe', 'moon']))
"""
    
function reverse_word(string word)
    reversed = ""
    for letter in word:
            reversed = letter + reversed
    return reversed

function check_all_palindromes(array arr)
        reversed1 = reverse_word(word1)
        reversed2 = reverse_word(word2)
        reversed3 = reverse_word(word3)

        if arr[0] does not equal reversed1:
                return false

        if arr[1] does not equal reversed2:
                return false

        if arr[2] does not equal reversed3:
                return false
        return true"""

def reverse_word(x):
    reverso = ""
    
    for letra in x:
        reverso = letra + reverso 
    return reverso

def check(arr):
    
    reverso1 = reverse_word("racecar")
    reverso2 = reverse_word("noon")
    reverso3 = reverse_word("civic")
    
    if arr[0] != reverso1:
        return False
    if arr[1] != reverso2:
        return False 
    if arr[2] != reverso3:
        return False 
    
    return True

print(check(['racecar', 'shoe', 'moon']))