with open('Day5/input.txt', 'r', encoding='utf-8') as f:
    data = f.read().split('\n\n')

rules = [x.split('|') for x in data[0].split('\n')]

updates = [x.split(',') for x in data[1].split('\n')]

incorrect_updates = []

part_1 = 0
for update in updates:
    correct_order = True
    relevant_rules = [x for x in rules if x[0] in update and x[1] in update]
    for rule in relevant_rules:
        if update.index(rule[0]) > update.index(rule[1]):
            correct_order = False
            incorrect_updates.append(update)
            break
    if correct_order:
        part_1 += int(update[int(len(update)/2)])
print(part_1)

def order_update(rules, update:list):
    fixed = False
    i = 0
    while not fixed:
        element_rules = [x for x in rules if x[0] == update[i]]
        for rule in element_rules:
            if i > update.index(rule[1]):
                swap = update[i]
                update[i] = update[i-1]
                update[i-1] = swap
                i = 0
                break
        i += 1
        if i == len(update):
            return(update)

part_2 = 0
for update in incorrect_updates:
    relevant_rules = [x for x in rules if x[0] in update and x[1] in update]

    update = order_update(relevant_rules, update)
    part_2 += int(update[int(len(update)/2)])
print(part_2)