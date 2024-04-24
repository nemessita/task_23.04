# Gömrük proqramı qurun. 5 dəfə təkrar olunsun. Əgər istifadəçi aylıq limiti keçərsə exceptlə qarşısı alınsın

def cal_customs(limit):
    total_customs = 0

    for _ in range(5):
        try:
            item_order = input("Məhsul novu: ")
            item_value = int(input("Məhsul qiymeti: "))
        except ValueError:
            print("Dəyəri düzgün daxil edin.")
            continue
        
        total_customs += item_value

        if total_customs > limit:
            print(f"Ayliq limit ({limit} AZN) olmalidir")
            break
    
    print(f"Mebleg: {total_customs} AZN")

limit = 300.0
cal_customs(limit)
