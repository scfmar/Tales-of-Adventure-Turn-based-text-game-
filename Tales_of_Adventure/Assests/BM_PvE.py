import random
import time
from Assests.Enemies import Enemy
from Assests.Professions import Profession

class PvM: 
    
    def PvM_play(Name,Enemy_stats,Player_stats):

        def player_Atk(Minion_HP,pDmg):# Player Attacks
            NewM_HP = Minion_HP - pDmg
            return NewM_HP

        def player_Rest(Player_HP,value): #Player Resting
           
            NewP_HP = Player_HP + value
            return NewP_HP

        def player_Atk_brittle(pDmg): # Brittle Attack
            reduction = round(pDmg *0.2)
            Newdmg = pDmg-reduction
            return Newdmg

        def m_Atk(Player_HP,mDmg): #Minion Attacks
            NewP_HP = Player_HP - mDmg
            return NewP_HP

        select_Op = None
        select_OpM = None
        p_Iatk = 1 # Iterate variable for attack 
        p_Idef = 1 # Iterate varaible for defend
        p_Irest = 1 # Iterate varaible for Rest
        Player = Profession(Player_stats[0],Player_stats[1],random.choice(Player_stats[2]),random.choice(Player_stats[3]))
        Minion = Enemy(Enemy_stats[0],Enemy_stats[1],random.choice(Enemy_stats[2]),random.choice(Enemy_stats[3]))
        player_Char = [Player.health,Player.action_Rate,Player.damage,Player.defence]
        minion_Stat = [Minion.health,Minion.action_Rate,Minion.damage,Minion.defence]
        Player_HP = player_Char[0]
        Minion_HP = Enemy_stats[0]
        switcher = {
                "fast": -1,
                "moderate": 0,
                "slow": 1
            }
        Player_Cooldown = switcher.get(player_Char[1])
        Current_Player_Cooldown = Player_Cooldown
        vulnerable = False
        brittle = False
        Delayed = False
        player_Def = 0
        Minion_def = 0
        #Player Actions
        while Player_HP >= 0 and Minion_HP >=0:
            if Player_HP <= 0:
                break
            if Minion_HP <= 0:
                print("Garv has been defeated.")
                break
            if Current_Player_Cooldown != 1:
                if Delayed == True:
                    print(Name + " felt drowsy and left themselves open to Garv.(Enemy gains an extra action.)")
                    Delayed = False
                    Current_Player_Cooldown = Player_Cooldown
                else:
                    while(Current_Player_Cooldown < 1):
                        if Minion_HP <= 0:
                            print("Garv has been defeated.")
                            break
                        print(Name +"\'s Health: "+str(Player_HP))
                        if player_Def > 0:
                            print(Name + f" Shield Points:{player_Def}")
                        if vulnerable == True:
                            print("Vulnerable")
                        if brittle == True:
                            print("Attack Brittled")
                        print("\nGarv's Health:"+str(Minion_HP))
                        if Minion_def > 0:
                            print(f"Garv Shield Points:{Minion_def}")
                        print( Name + " thought of their next move." + "\n[a/A] - Attack" + "\n[d/D] - Defence" + "\n[r/R] - Rest")

                        select_Op = str(input("Your action choice is: "))

                        if select_Op == "a" or select_Op =="A":
                            p_Idef = 1
                            p_Irest = 1
                            initial_dmg = player_Char[2]
                            if brittle == True:
                                true_dmg = player_Atk_brittle(initial_dmg)
                            else:
                                true_dmg =  initial_dmg 
                            if Minion_def == 0:
                                print(Name + f" strikes and does {true_dmg} damage.")
                                Minion_HP = player_Atk(Minion_HP,true_dmg)
                            else:
                                reduce_dmg =  true_dmg - Minion_def 
                                if reduce_dmg <= 0:
                                    print("The minion has fully shielded the attack. (Minion has no more defense)")
                                else:
                                    print(Name + f" Attacks for {true_dmg} but does {reduce_dmg} damage")
                                    Minion_HP = player_Atk(Minion_HP,int(reduce_dmg))
                                Minion_def = 0

                            if brittle == True:
                                    print("After a few moments, "+Name+" mustered back their bravado once more. (Brittle effect removed)")
                                    brittle = False

                            if p_Iatk == 2:
                                print(Name + " has becomed exhausted and brittled. (the next attack will do less damage).")
                                brittle = True
                                
                            elif p_Iatk == 1:
                                pass
                            elif p_Iatk > 2:
                                p_Iatk = 1 
                            else:
                                pass
                            p_Iatk += 1
                            Current_Player_Cooldown+=1

                        elif select_Op == "d" or select_Op == "D":
                            p_Iatk= 1
                            p_Irest = 1
                            player_Def = player_Char[3]
                            print(Name + f" holds a defensive posture to block {player_Def} damage")
                            if p_Idef == 2:
                                print("By defending consecutively the enemy sees an opening.("+ Name + " became vulnerable and will take more damage)")
                                vulnerable = True
                            
                            if p_Idef > 2:
                                p_Idef = 1
                            else:
                                pass
                            p_Idef += 1
                            Current_Player_Cooldown+=1

                        elif select_Op =="r" or select_Op =="R":
                            p_Iatk = 1
                            p_Idef = 1 
                            rest_value = [7,8,9]
                            value = random.choice(rest_value)
                            print(Name+f" chose to Rest and recovered {value} HP.")
                            Player_HP = player_Rest(Player_HP,value)
                            if Player_HP > player_Char[0]:
                                Player_HP = player_Char[0]
                            
                            if p_Irest == 2:
                                Delayed = True
                            
                            if p_Irest > 2: 
                                p_Irest = 1
                            else:
                                pass
                            p_Irest += 1
                            Current_Player_Cooldown+=1

                        else:
                            print("Invalid choice")
                        
            #Enemy Actions    
            minion_Choice = [1,2]
            select_OpM = (random.choice(minion_Choice))
            if select_OpM == 1:
                time.sleep(1)
                minion_initial_dmg = minion_Stat[2]
                if vulnerable == True:
                    minion_initial_dmg =  minion_initial_dmg * 2
                    print("Garv lunges for and deal extra dmg!")
                
                if player_Def == 0:
                    print(f"Garv Attacks and deals {minion_initial_dmg} damage")
                    Player_HP = m_Atk(Player_HP, minion_initial_dmg)
                else:
                    Minion_reduce_dmg =  minion_initial_dmg  - player_Def
                    if Minion_reduce_dmg < 0:
                        print("Garv's attack was completely nullified.")
                    else:
                        print(f"Garv strike for {minion_initial_dmg} but was reduce to {Minion_reduce_dmg} damage.")
                        Player_HP = m_Atk(Player_HP,int(Minion_reduce_dmg))
                    if  vulnerable == True:
                        print(Name+" shook away the heavy blow and became alert once again.")
                        vulnerable = False
                    print("("+Name + " has no more temporary hit points.)")
                    player_Def = 0

            elif select_OpM ==2:
                Minion_def = minion_Stat[3]
                time.sleep(1)
                print(f"Garv brings up a shield and is defending for {Minion_def} damage")
                
            else:
                print("Wrong choice")

            if Current_Player_Cooldown == 1:
                if player_Char[1] == "slow":
                    Current_Player_Cooldown -= 1
                else:
                    Current_Player_Cooldown = Player_Cooldown

        if Minion_HP <= 0:
            return 1
        elif Player_HP <= 0:
            return 0

class PvB:

    def PvB_play(Boss_name,Name,Enemy_stats,Player_stats):
        def player_Atk(Minion_HP,pDmg):# Player Attacks
            NewM_HP = Minion_HP - pDmg
            return NewM_HP

        def player_Rest(Player_HP,value): #Player Resting
           
            NewP_HP = Player_HP + value
            return NewP_HP

        def player_Atk_brittle(pDmg): # Brittle Attack
            reduction = round(pDmg *0.2)
            Newdmg = pDmg-reduction
            return Newdmg

        def m_Atk(Player_HP,mDmg): #Minion Attacks
            NewP_HP = Player_HP - mDmg
            return NewP_HP

        select_Op = None
        select_OpM = None
        p_Iatk = 1 # Iterate variable for attack 
        p_Idef = 1 # Iterate varaible for defend
        p_Irest = 1 # Iterate varaible for Rest
        Player = Profession(Player_stats[0],Player_stats[1],random.choice(Player_stats[2]),random.choice(Player_stats[3]))
        Minion = Enemy(Enemy_stats[0],Enemy_stats[1],random.choice(Enemy_stats[2]),random.choice(Enemy_stats[3]))
        player_Char = [Player.health,Player.action_Rate,Player.damage,Player.defence]
        minion_Stat = [Minion.health,Minion.action_Rate,Minion.damage,Minion.defence]
        Player_HP = player_Char[0]
        Minion_HP = Enemy_stats[0]
        switcher = {
                "fast": -1,
                "moderate": 0,
                "slow": 1
            }
        Player_Cooldown = switcher.get(player_Char[1])
        Current_Player_Cooldown = Player_Cooldown
        vulnerable = False
        brittle = False
        Delayed = False
        player_Def = 0
        Minion_def = 0
        
        #Player Actions
        while Player_HP >= 0 and Minion_HP >=0:
            if Player_HP <= 0:
                break
            if Minion_HP <= 0:
                print("Lord Rufu's Champion has been defeated.")
                break
            if Current_Player_Cooldown != 1:
                if Delayed == True:
                    print(Name + " felt drowsy and left themselves open to Garv.(Enemy gains an extra action.)")
                    Delayed = False
                    Current_Player_Cooldown = Player_Cooldown
                else:
                    while(Current_Player_Cooldown < 1):
                        if Minion_HP <= 0:
                            print("Lord Rufu's Champion has been defeated.")
                            break
                        print(Name +"\'s Health: "+str(Player_HP))
                        if player_Def > 0:
                            print(Name + f" Shield Points:{player_Def}")
                        if vulnerable == True:
                            print("Vulnerable")
                        if brittle == True:
                            print("Attack Brittled")
                        print("\n"+Boss_name+"'s Health:"+str(Minion_HP))
                        if Minion_def > 0:
                            print(Boss_name+f" Shield Points:{Minion_def}")
                        print( Name + " thought of their next move." + "\n[a/A] - Attack" + "\n[d/D] - Defence" + "\n[r/R] - Rest")

                        select_Op = str(input("Your action choice is: "))

                        if select_Op == "a" or select_Op =="A":
                            p_Idef = 1
                            p_Irest = 1
                            initial_dmg = player_Char[2]
                            if brittle == True:
                                true_dmg = player_Atk_brittle(initial_dmg)
                            else:
                                true_dmg =  initial_dmg 
                            if Minion_def == 0:
                                print(Name + f" strikes and does {true_dmg} damage.")
                                Minion_HP = player_Atk(Minion_HP,true_dmg)
                            else:
                                reduce_dmg =  true_dmg - Minion_def 
                                if reduce_dmg <= 0:
                                    print(Boss_name+" has fully shielded the attack. (Minion has no more defense)")
                                else:
                                    print(Name + f" Attacks for {true_dmg} but does {reduce_dmg} damage")
                                    Minion_HP = player_Atk(Minion_HP,int(reduce_dmg))
                                Minion_def = 0

                            if brittle == True:
                                    print("After a few moments, "+Name+" mustered back their bravado once more. (Brittle effect removed)")
                                    brittle = False

                            if p_Iatk == 2:
                                print(Name + " has becomed exhausted and brittled. (the next attack will do less damage).")
                                brittle = True
                                
                            elif p_Iatk == 1:
                                pass
                            elif p_Iatk > 2:
                                p_Iatk = 1 
                            else:
                                pass
                            p_Iatk += 1
                            Current_Player_Cooldown+=1

                        elif select_Op == "d" or select_Op == "D":
                            p_Iatk= 1
                            p_Irest = 1
                            player_Def = player_Char[3]
                            print(Name + f" holds a defensive posture to block {player_Def} damage")
                            if p_Idef == 2:
                                print("By defending consecutively the enemy sees an opening.("+ Name + " became vulnerable and will take more damage)")
                                vulnerable = True
                            
                            if p_Idef > 2:
                                p_Idef = 1
                            else:
                                pass
                            p_Idef += 1
                            Current_Player_Cooldown+=1

                        elif select_Op =="r" or select_Op =="R":
                            p_Iatk = 1
                            p_Idef = 1 
                            rest_value = [7,8,9]
                            value = random.choice(rest_value)
                            print(Name+f" chose to Rest and recovered {value} HP.")
                            Player_HP = player_Rest(Player_HP,value)
                            if Player_HP > player_Char[0]:
                                Player_HP = player_Char[0]
                            
                            if p_Irest == 2:
                                Delayed = True
                            
                            if p_Irest > 2: 
                                p_Irest = 1
                            else:
                                pass
                            p_Irest += 1
                            Current_Player_Cooldown+=1

                        else:
                            print("Invalid choice")
                        
            
            #Enemy Actions
            minion_Choice = [1,2]
            select_OpM = (random.choice(minion_Choice))
            if select_OpM == 1:
                time.sleep(1)
                boss_initial_dmg = minion_Stat[2]
                if vulnerable == True:
                    boss_initial_dmg = boss_initial_dmg * 2
                    print(Boss_name+" sweeps at the hero and deal extra dmg!")
                
                if player_Def == 0:
                    print(Boss_name+f" attacks and deals {boss_initial_dmg} damage")
                    Player_HP = m_Atk(Player_HP, boss_initial_dmg)
                else:
                    Boss_reduce_dmg =  boss_initial_dmg - player_Def
                    if Boss_reduce_dmg < 0:
                        print(Name+" fully blocked "+Boss_name+"'s blow")
                    else:
                        print(Boss_name+f" strike for {boss_initial_dmg} but was reduce to {Boss_reduce_dmg} damage")
                        Player_HP = m_Atk(Player_HP,int(Boss_reduce_dmg))
                    if  vulnerable == True:
                        print(Name+" shook away the heavy blow and became alert once again.(Vulnerable effect removed)")
                        vulnerable = False
                    player_Def = 0

            elif select_OpM ==2:
                Minion_def = minion_Stat[3]
                time.sleep(1)
                print(Boss_name+f" brings up a shield and is defending for {Minion_def} damage")
                
            else:
                print("Wrong choice")

            if Current_Player_Cooldown == 1:
                if player_Char[1] == "slow":
                    Current_Player_Cooldown -= 1
                else:
                    Current_Player_Cooldown = Player_Cooldown

        if Minion_HP <= 0:
            return 1
        elif Player_HP <= 0:
            return 0

