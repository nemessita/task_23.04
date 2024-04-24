# Müxtəlif ədədlərdən ibarət Fayl yaradın. Faylın daxilində 2yə bölünən müsbət ədələri başqa bir fayla 
# yazdırınç 2yə bölünmədiyi halda exceptlə qarşısını alın.

def write_file():
    positive_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]  
    with open("2.txt", "w") as file:
        for number in positive_numbers:
            if number > 0 and number % 2 == 0:  
                file.write(str(number) + "\n")  
            else:
                pass  

write_file()
