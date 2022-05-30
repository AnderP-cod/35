

def polyndrome(a_list):
    if len(a_list) < 1:
        return True
    else:
        if a_list[0] == a_list[-1]:
            return polyndrome(a_list[1:-1])
        else:
            return False


a = str(input("Введите слово: "))
if (polyndrome(a) == True):
    print("Полиндром")
else:
    print("НЕ полиндром")
