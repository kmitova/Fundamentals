quests = input().split(", ")

command = input()
while not command == "Retire!":
    current = command.split(" - ")
    action = current[0]
    if action == "Start":
        quest = current[1]
        if quest not in quests:
            quests.append(quest)
    elif action == "Complete":
        quest = current[1]
        if quest in quests:
            quests.remove(quest)
    elif action == "Side Quest":
        quest_and_side_quest = current[1].split(":")
        quest = quest_and_side_quest[0]
        side_quest = quest_and_side_quest[1]
        if quest in quests and side_quest not in quests:
            quest_index = quests.index(quest)
            quests.insert(quest_index+1, side_quest)
    elif action == "Renew":
        quest = current[1]
        if quest in quests:
            quests.remove(quest)
            quests.append(quest)
    command = input()

print(", ".join(quests))
