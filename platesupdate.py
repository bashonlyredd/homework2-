def plate():
    your_num = input("Enter your plates : ")
    your_num = your_num.upper()
    lenght = (len(your_num))
    if lenght == 8:
        letter_1 = your_num[0]
        letter_2 = your_num[1]
        letters_sum = letter_1 + letter_2
        letter_3 = your_num[6]
        letter_4 = your_num[7]
        letters_sum2 = letter_3 + letter_4
        a = (your_num[2])
        b = (your_num[3])
        c = (your_num[4])
        d = (your_num[5])
        print(letters_sum, a, b, c, d, letters_sum2)
        print(sum(a, b, c, d))
        return your_num
    else:
        print("No, it's false")

def sum(a, b, c, d, ):
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    s = a + b + c + d
    print(s)