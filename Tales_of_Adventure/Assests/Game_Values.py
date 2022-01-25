class enemy:
    #Minion
    def Minion():
        minion_Dmg = [8,9,10,11,12,13]
        minion_Def = [4,5,6]
        Minion = (50,"moderate",minion_Dmg,minion_Def)
        return Minion
    #Boss
    def Boss():
        boss_Dmg = [7,8,9,10,11,12,13,14,15]
        boss_Def = [7,8,9,10]
        Boss = (100,"moderate",boss_Dmg,boss_Def)
        return Boss
        
class professions:

    def Warrior_Paths(n): 
        #Berserker Values
        berserker_Dmg = [6,7,8,9,10,11]
        berserker_Def = [1,2,3,4,5]
        Berserker = (80,"fast",berserker_Dmg,berserker_Def)
        
        #Ironlad Values
        ironlad_Dmg = [5,6,7,8,9,10]
        ironlad_Def = [7,8,9,10]
        Ironlad = (120,"slow",ironlad_Dmg,ironlad_Def)

        if n == 1:
            return Berserker
        else:
            return Ironlad


    #Bowman (Archer)
    def Archer_Paths(n): 
        #Bowman Values
        bowman_Dmg = [8,9,10,11,12]
        bowman_Def = [2,3,4,5,6] 
        Bowman = (90,"fast",bowman_Dmg,bowman_Def)
        

        #Arbalist Values
        arbalist_Dmg = [10,11,12,13,14,15]
        arbalist_Def = [3,4,5,6,7]
        Arbalist = (100,"slow",arbalist_Dmg,arbalist_Def)
        
        if n == 1:
            return Bowman
        else:
            return Arbalist

    
    def Caster_Paths(n): 
        #Elementalist Values
        elementalist_Dmg = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        elementalist_Def = [4,5,6]
        Elementalist = (70,"moderate",elementalist_Dmg,elementalist_Def)
        

        #Alchemist Values
        alchemist_Dmg = [7,8,9,10,11,12,13,14,15,16]
        alchemist_Def = [4,5,6]
        Alchemist = (60,"moderate",alchemist_Dmg,alchemist_Def)
        
        if n == 1:
            return Elementalist
        else:
            return Alchemist

class trinkets:

    def apply_trinket(player_stats,trinket_chosen):
        new_stats = list(player_stats)
        if trinket_chosen == "Heart Pendant":
            new_stats[0] += 10
        elif trinket_chosen == "Lion Pendant":
            for x in range(len(new_stats[2])):
                new_stats[2][x] += 3
        elif trinket_chosen == "Shield Pendant":
            for x in range(len(new_stats[3])):
                new_stats[3][x] += 3
        elif trinket_chosen == "Ring of Madness":
            new_stats[0] = new_stats[0] - 20
            for x in range(len(new_stats[2])):
                new_stats[2][x] += 5
        return tuple(new_stats)
