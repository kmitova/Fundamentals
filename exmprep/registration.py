import re

pattern = r"U\$([A-Z]{1}[a-z]{2,})U\$P@\$([A-Za-z]{5,}\d{1,})P@\$"

n = int(input())
count = 0
for i in range(n):
    text = input()
    matches = re.findall(pattern, text)
    if matches:
        for match in matches:
            username = match[0]
            password = match[1]
            print("Registration was successful")
            print(f"Username: {username}, Password: {password}")
            count += 1
    else:
        print("Invalid name or password")

print(f"Successful registrations: {count}")
