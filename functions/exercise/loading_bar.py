def loading_bar(integer):
    still_loading = True
    list_to_print = []
    if integer == 100:
        still_loading = False
    else:
        number = integer // 10
        for i in range(1, number+1):
            list_to_print.append("%")
        while len(list_to_print) < 10:
            list_to_print.append(".")

    if not still_loading:
        print("100% Complete!")
        print("[%%%%%%%%%%]")
    else:
        result = "".join(list_to_print)
        print(f"{integer}% [{result}]")
        print("Still loading...")


given_integer = int(input())
loading_bar(given_integer)
