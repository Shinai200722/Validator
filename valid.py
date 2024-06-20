def luhn_algorithm(card_number):
    digits = []
    for x in str(card_number):
        digits.append(int(x))

    doubled_digits = []
    for index, digit in enumerate(digits):
        if index % 2 == 0:
            doubled_digits.append(digit * 2)
        else:
            doubled_digits.append(digit)

    subtracted_digits = []
    for digit in doubled_digits:
        if digit > 9:
            subtracted_digits.append(digit - 9)
        else:
            subtracted_digits.append(digit)

    total = sum(subtracted_digits)
    return total % 10 == 0
def validate_card(card_number):
    card_number = card_number.replace(" ", "")

    if not card_number.isdigit():
        return False
    if len(card_number) < 13 or len(card_number) > 19:
        return False
    if not luhn_algorithm(card_number):
        return False
    return True

import tkinter as tk

def check_card():
    card_number = entry.get()
    if validate_card(card_number):
        second_label.config(text="Валідний.")
    else:
        second_label.config(text="Не валідний.")


interface = tk.Tk()
interface.title("Перевірка кредитної карти")
interface.geometry("720x360")


label = tk.Label(interface, text="Номер кредитної карти:")
label.pack()
entry = tk.Entry(interface)
entry.pack()


check_button = tk.Button(interface, text="Перевірити", command=check_card)
check_button.pack()


second_label = tk.Label(interface, text="")
second_label.pack()
interface.mainloop()
