class Enemy:
    health = None
    action_Rate = None
    damage = None
    defence = None

    def __init__(self,health,action_Rate,damage,defence):
        self.health = health
        self.action_Rate = action_Rate
        self.damage = damage
        self.defence = defence