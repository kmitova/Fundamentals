class Party:
    def __init__(self):
        self.people = []


party = Party()
total = 0

name = input()

while not name == "End":
    party.people.append(name)
    total += 1
    name = input()

print(f"Going: {', '.join(party.people)}")
print(f"Total: {total}")
