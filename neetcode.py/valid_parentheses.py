def isValid(s:str):
    string_head = 0
    string_tail = -1
    while len(s)//2 >= string_head + 1:
        if s[string_head] + s[string_tail] in [ "()","[]","{}" ]:
            string_head += 1
            string_tail -= 1
        else:
            return False
    return True

print(isValid("{}"))

[[[]]]
