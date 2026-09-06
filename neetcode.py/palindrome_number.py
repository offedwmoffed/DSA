def palindrome_number(number:int):
    number = list(str(number))

    if len(number) % 2 == 0 :
        while number:
            if number[0] == number[-1]:
                number.pop(0)
                number.pop(-1)
            else:
                return False
        return True
    else:
        while len(number) != 1:
            if number[0] == number[-1]:
                number.pop(0)
                number.pop(-1)
            else:
                return False
        return True


print(palindrome_number(0))
               
            
        



