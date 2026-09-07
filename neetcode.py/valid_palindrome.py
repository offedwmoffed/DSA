def isPalindrome(s:str):
    from string import punctuation
    string_head = 0
    string_tail = -1
    s ="".join(char for char in s.lower().strip() if char not in punctuation+" ")
   
    while len(s)//2 >= string_head + 1:
        if s[string_head] == s[string_tail]:
            string_head += 1
            string_tail -= 1
        else:
            return False
    return True

