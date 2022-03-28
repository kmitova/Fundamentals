def is_winning(ticket):
    if not len(ticket) == 20:
        return "invalid ticket"
    left_half = ticket[:10]
    right_half = ticket[10:]
    winning_symbols = ['@', '#', '$', '^']
    for char in winning_symbols:
        for repetition in range(10, 5, -1):
            char_repetition = char * repetition
            if char_repetition in left_half and char_repetition in right_half:
                if repetition == 10:
                    return f'ticket "{ticket}" - {repetition}{char} Jackpot!'
                elif 6 <= repetition <= 9:
                    return f'ticket "{ticket}" - {repetition}{char}'
    return f'ticket "{ticket}" - no match'


tickets = [s.strip() for s in input().split(", ")]
tickets_states = []
for ticket in tickets:
    tickets_states.append(is_winning(ticket))

for item in tickets_states:
    print(item)
