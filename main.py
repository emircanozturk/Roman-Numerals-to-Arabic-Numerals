import tkinter as tk


def button_func():
    data = user_input.get()
    result_label.config(text="")
    result_heading.config(text="")
    single_digit = {"I": 1,
                    "V": 5,
                    "X": 10,
                    "L": 50,
                    "C": 100,
                    "D": 500,
                    "M": 1000}
    try:
        if len(data) == 1:
            converted_single_digit = single_digit[data]
            result_label.config(text=converted_single_digit)
        else:
            char_list = []
            for char in data:
                char_list.append(char)

            values = []
            for item in char_list:

                item_index = char_list.index(item)
                if item_index + 1 == len(char_list) or single_digit[item] >= single_digit[char_list[item_index + 1]]:
                    values.append(single_digit[item])
                elif single_digit[item] <= single_digit[char_list[item_index + 1]]:
                    values.append(-single_digit[item])

                result = sum(values)
                result_label.config(text=result)
        result_heading.config(text="Arabic Numeral")


    except:
        result_label.config(text="Please Enter a Valid Data"
                                 "\nCheck Your Data According to Conditions Below"
                                 "\n- Your roman number must be less than 5000"
                                 "\n- Enter valid roman-numeral characters")

    result_heading.pack(pady=5)
    result_label.pack()


# user interface
window = tk.Tk()
window.minsize(600, 350)
window.title("Romen Numerals")

frame1 = tk.Frame(window)
frame1.pack()
frame2 = tk.Frame(window)
frame2.pack()
frame3 = tk.Frame(window)
frame3.pack()

# heading
heading = tk.Label(frame1, text="Romen Numerals", font=("Bahnschrift", 24, "bold"))
heading.pack(pady=10)

# user input
input_label = tk.Label(frame1, text="Enter Your Roman-Numeral", font=("Bahnschrift", 14))
user_input = tk.Entry(frame1)
user_input.config(font=("Bahnschrift", 12), width=24, justify="center")
convert_button = tk.Button(frame3, text="Convert", command=button_func, font=("Bahnschrift", 10, "bold"))
input_label.pack()
user_input.pack()
convert_button.pack()

# additional buttons
characters = ["I", "V", "X", "L", "C", "D", "M"]

for character in characters:
    character_button = tk.Button(frame2, text=character, font=("Bahnschrift", 10), width=3,
                                 command=lambda char=character: user_input.insert("end", char))
    character_button.pack(side="left", padx=5, pady=10)

# result heading
result_heading = tk.Label(frame3, font=("Bahnschrift", 14, "bold"))

# result label
result_label = tk.Label(frame3, font=("Bahnschrift", 14))

window.mainloop()
