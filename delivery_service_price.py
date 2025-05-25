# Mahsulot narxlarini kiritish
prices_input = input("Mahsulot narxlarini kiriting ($, vergul bilan): ")
prices = [float(p.strip()) for p in prices_input.split(',') if p.strip()]

# Masofani kiritish
distance = float(input("Masofani kiriting (km): "))

# Yetkazib berish narxini hisoblash (masalan, har 1 km uchun $2.23)
delivery_price = round(distance * 2.23, 2)

# Umumiy narxlarni hisoblash
total = sum(prices) + delivery_price
rounded_total = round(total, 2)

print(f"Yetkazib berish narxi: ${delivery_price:.2f} (seven dollars and eighty cents, семь долларов восемьдесят центов)")
print(f"Umumiy narx: ${total:.2f}")
print(f"Yaxlitlangan narx: ${rounded_total:.2f}")
