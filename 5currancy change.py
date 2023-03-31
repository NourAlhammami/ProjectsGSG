currency_from = input("What currency do you want change from: ").strip().upper()
currency_to = input("What currency do you want change to: ").strip().upper()
how_much_in = float(input("How much do you want change: ").strip())

if currency_from == "USD":
    if currency_to == "EUR":
        how_much_out = how_much_in * 0.99
    elif currency_to == "SAR":
        how_much_out = how_much_in * 3.75
    else:
        how_much_out = how_much_in
elif currency_from == "EUR":
    if currency_to == "USD":
        how_much_out = how_much_in / 0.99
    elif currency_to == "SAR":
        how_much_out = how_much_in / 0.99 * 3.75
    else:
        how_much_out = how_much_in
else:
    if currency_to == "USD":
        how_much_out = how_much_in / 3.75
    elif currency_to == "EUR":
        how_much_out = how_much_in / 3.75 + 0.99
    else:
        how_much_out = how_much_in

print(f"You will give {round(how_much_in,2)}, and you will take {round(how_much_out,2)}")