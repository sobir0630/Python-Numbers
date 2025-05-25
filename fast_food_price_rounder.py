# fast_food_price_rounder.py

def parse_prices(input_str):
    # Remove $ and split by comma
    prices = [float(p.strip().replace('$', '')) for p in input_str.split(',')]
    return prices

def total_price(prices):
    return round(sum(prices), 2)

def number_to_words_en(n):
    # Simple conversion for dollars and cents (0-99)
    ones = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    teens = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    tens = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

    def two_digits(num):
        if num < 10:
            return ones[num]
        elif 10 <= num < 20:
            return teens[num-10]
        else:
            t, o = divmod(num, 10)
            return tens[t] + ('' if o == 0 else ' ' + ones[o])

    dollars = int(n)
    cents = int(round((n - dollars) * 100))
    dollar_words = two_digits(dollars)
    cent_words = two_digits(cents)
    return f"{dollar_words} dollars and {cent_words} cents"

def number_to_words_ru(n):
    # Simple conversion for dollars and cents (0-99)
    ones = ["ноль","один","два","три","четыре","пять","шесть","семь","восемь","девять"]
    teens = ["десять","одиннадцать","двенадцать","тринадцать","четырнадцать","пятнадцать","шестнадцать","семнадцать","восемнадцать","девятнадцать"]
    tens = ["","","двадцать","тридцать","сорок","пятьдесят","шестьдесят","семьдесят","восемьдесят","девяносто"]

    def two_digits(num):
        if num < 10:
            return ones[num]
        elif 10 <= num < 20:
            return teens[num-10]
        else:
            t, o = divmod(num, 10)
            return tens[t] + ('' if o == 0 else ' ' + ones[o])

    dollars = int(n)
    cents = int(round((n - dollars) * 100))
    dollar_words = two_digits(dollars)
    cent_words = two_digits(cents)
    return f"{dollar_words} долларов {cent_words} центов"

def main():
    input_str = input("Mahsulot narxlarini kiriting ($, vergul bilan): ")
    prices = parse_prices(input_str)
    total = total_price(prices)
    print(f"Umumiy narx: ${total:.2f} ({number_to_words_en(total)}, {number_to_words_ru(total)})")
    print(f"Yaxlitlangan narx: ${total:.2f} ({number_to_words_en(total)}, {number_to_words_ru(total)})")

if __name__ == "__main__":
    main()
