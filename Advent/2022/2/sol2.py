class rps:
    def __init__(self, action, points):
        self.action = action
        self.points = points
    
    def get_action(self):
        return self.action
    def get_points(self):
        return self.action

# A = R, B = P, C = S
# X = L, Y = D, Z = W
def translate(action):
    if action == 'A':
        return rps('R', 1)
    elif action == 'B':
        return rps('P', 2)
    elif action == 'C':
        return rps('S', 3)
    elif action == 'X':
        return rps('L', 0)
    elif action == 'Y':
        return rps('D', 0)
    elif action == 'Z':
        return rps('W', 0)

def find_action(opp, me):
    if me.action == 'D':
        new_me = opp
    if me.action == 'W':
        if opp.action == 'R':
            new_me = rps('P', 2)
        elif opp.action == 'P':
            new_me = rps('S', 3)
        elif opp.action == 'S':
            new_me = rps('R', 1)
    if me.action == 'L':
        if opp.action == 'S':
            new_me = rps('P', 2)
        elif opp.action == 'R':
            new_me = rps('S', 3)
        elif opp.action == 'P':
            new_me = rps('R', 1)
    return opp, new_me


def battle(opp, me):
    if me.action == opp.action:
        return 3 + me.points
    elif me.action == 'R':
        if opp.action == 'P':
            return 0 + me.points
        else:
            return 6 + me.points
    elif me.action == 'P':
        if opp.action == 'S':
            return 0 + me.points
        else:
            return 6 + me.points
    elif me.action == 'S':
        if opp.action == 'R':
            return 0 + me.points
        else:
            return 6 + me.points


with open('input.txt') as f:
    points = 0
    for round in f:
        actions = round.strip().split()
        opp, me = map(lambda x: translate(x), actions)
        opp2, me2 = find_action(opp, me)
        points += battle(opp2, me2)
    print(points)