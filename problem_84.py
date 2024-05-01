import random
def euler_84():
    field = ['GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3',
             'JAIL', 'C1', 'U1', 'C2', 'C3', 'R2', 'D1', 'CC2', 'D2', 'D3',
             'FP', 'E1', 'CH2', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2', 'F3',
             'G2J', 'G1', 'G2', 'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2']
    probabilities = {'GO': 0, 'A1': 0, 'CC1': 0, 'A2': 0, 'T1': 0, 'R1': 0, 'B1': 0, 'CH1': 0, 'B2': 0, 'B3': 0,
                     'JAIL': 0, 'C1': 0, 'U1': 0, 'C2': 0, 'C3': 0, 'R2': 0, 'D1': 0, 'CC2': 0, 'D2': 0, 'D3': 0,
                     'FP': 0, 'E1': 0, 'CH2': 0, 'E2': 0, 'E3': 0, 'R3': 0, 'F1': 0, 'F2': 0, 'U2': 0, 'F3': 0,
                     'G2J': 0, 'G1': 0, 'G2': 0, 'CC3': 0, 'G3': 0, 'R4': 0, 'CH3': 0, 'H1': 0, 'T2': 0, 'H2': 0}
    CC = ['GO', 'JAIL', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
    random.shuffle(CC)
    CH = ['GO', 'JAIL', 'C1', 'E3', 'H2', 'R1', 'next R', 'next R', 'next U', 'back 3', '-', '-', '-', '-', '-', '-']
    random.shuffle(CH)
    current_position = 0
    triple_double = 0
    tosses = 10000000
    for i in range(tosses):
        dice_1 = random.randint(1, 4)
        dice_2 = random.randint(1, 4)
        if dice_1 == dice_2:
            triple_double += 1
        else:
            triple_double = 0
        if triple_double == 3:
            current_position = field.index('JAIL')
            triple_double = 0
        else:
            current_position = (current_position + dice_1 + dice_2) % 40
            if current_position == field.index('G2J'):
                current_position = 10
            elif field[current_position].startswith('CH'):
                if CH[0] == 'back 3':
                    current_position -= 3
                elif CH[0] == 'next R':
                    while not field[current_position].startswith('R'):
                        current_position = (current_position + 1) % 40
                elif CH[0] == 'next U':
                    while not field[current_position].startswith('U'):
                        current_position = (current_position + 1) % 40
                elif CH[0] == '-':
                    pass
                else:
                    current_position = field.index(CH[0])
                el = CH.pop(0)
                CH.append(el)
            if field[current_position].startswith('CC'):
                if CC[0] != '-':
                    current_position = field.index(CC[0])
                el = CC.pop(0)
                CC.append(el)
        probabilities[field[current_position]] += 1
    for k, v in sorted(probabilities.items(), key=lambda x: x[1], reverse=True):
        print(f'({field.index(k)}) {k} = {100 * v / tosses}%')
