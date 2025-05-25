fifty_count = 3
ten_count = 3
five_count = 1
one_count = 1

fifty_value = 50
ten_value = 10
five_value = 5
one_value = 1

total = (fifty_count * fifty_value) + (ten_count * ten_value) + (five_count * five_value) + (one_count * one_value)

print(f"Pul miqdorini kiriting ($): {total}")
print(f"$50 kupyuradan: {fifty_count} ta")
print(f"$10 kupyuradan: {ten_count} ta")
print(f"$5 kupyuradan: {five_count} ta")
print(f"$1 kupyuradan: {one_count} ta")
print(f"Umumiy summa: ${total} (one hundred and eighty-six, сто восемьдесят шесть)")

# Haftalik harajatlarni kiritish va o‘rtacha hisoblash
expenses_input = input("Haftalik harajatlarni kiriting ($, vergul bilan): ")
expenses = [float(x.strip()) for x in expenses_input.split(",")]
average = sum(expenses) / len(expenses)
print(f"O‘rtacha harajat: ${average:.2f}")