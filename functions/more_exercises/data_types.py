def data_types(type, data):
    if type == "int":
        return int(data)*2
    elif type == "real":
        return f"{float(data)*1.5:.2f}"
    elif type == "string":
        return f"${data}$"


given_type = input()
input_data = input()
result = data_types(given_type, input_data)
print(result)
