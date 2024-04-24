# İstifadəçidən gələn iki ədədin bölünməsindən alınan nəticəni fayla yazdırın. Try except istifadə edərək
#  bölən 0 olduqda exceptlə qarşısını alın

def write_file():
    positive_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]  

    with open("1.txt", "w") as file:
        for number in positive_numbers:
            try:
                if number > 0 and number % 2 == 0:
                    file.write(str(number) + "\n")
                else:
                    pass    
            except ZeroDivisionError:
                print("Error")

write_file()