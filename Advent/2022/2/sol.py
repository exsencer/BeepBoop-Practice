class rps:
    def __init__(self, action, points):
        self.action = action
        self.points = points
    
    def get_action(self):
        return self.action
    def get_points(self):
        return self.action

# A = R, B = P, C= S
# X = R, Y = P, Z= S
def translate(action):
    if action == 'A' or action == 'X':
        return rps('R', 1)
    elif action == 'B' or action == 'Y':
        return rps('P', 2)
    else:
        return rps('S', 3)

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
        points += battle(opp, me)
    print(points)