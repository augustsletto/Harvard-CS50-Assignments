
number_checked = False
# Makes  the question loop if input not valid
while not number_checked:
    try:
        number = int(input("Number:").strip()) # Strips white space in input
    except ValueError:
        continue
    else:
        number = str(number)
        card_list = list(number)
        
        int_list = [int(i) for i in card_list]

        int_list[-2::-2] = [i*2 for i in int_list[-2::-2]]

        str_list = [str(i) for i in int_list]

        liststring = "".join(str_list)

        sum_list = sum([int(i) for i in liststring])

        if sum_list % 10 == 0:
            if number[0] == "4" and len(number) in [13, 16]:
                print(f"VISA\n")
                number_checked = True
            elif number[0:2] in ["37", "34"] and len(number) == 15:
                print(f"AMEX\n")
                number_checked = True
            elif number[0:2] in ["51", "52", "53", "54", "55"] and len(number) == 16:
                print(f"MASTERCARD\n")
                number_checked = True
            else:
                print(f"INVALID\n")
                number_checked = True
        else:
            print(f"INVALID\n")
            number_checked = True
