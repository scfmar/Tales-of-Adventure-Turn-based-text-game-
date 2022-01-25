import os
import win32api
import time
from Assests.dialogues import Game_dialogue,Class_dialogue,Profession_dialogue,Garv_fight_after_dialogue,Rufus_fight_after_dialogue
from Assests.BM_PvE import PvB, PvM
from Assests.Game_Values import enemy,professions,trinkets

Boss_name = "The Champion"
profile = ["<Name here>","<Class here>","<Path here>","<Trinket Here>"]
GD = Game_dialogue
dialogue_array = GD.array()
Menu_input = "1"
reincarnation = False
def dialogue_output(dialogue,index):
    ctn = 1
    if(index == 0):
        print(dialogue[0])
        print("Press the down arrow key to continue....")
        if reincarnation == True:
            print("Press the up arrow key to skip dialogue....")
        while ctn != len(dialogue):
            x = win32api.GetKeyState(0x28) # down arrow key
            if reincarnation == True:
                y = win32api.GetKeyState(0x26) # up arrow key
                if y<0:
                    os.system('cls')
                    break
            if x<0:
                os.system('cls')
                print(dialogue[ctn])
                ctn += 1
            time.sleep(0.1)

    elif(index == 2):
        ctn = 3
        print(dialogue[2].replace("<Name>",profile[0]))
        print("Press the down arrow key to continue....")
        if reincarnation == True:
            print("Press the up arrow key to skip dialogue....")
        while ctn != len(dialogue):
            x = win32api.GetKeyState(0x28)
            if reincarnation == True:
                y = win32api.GetKeyState(0x26) # up arrow key
                if y<0:
                    os.system('cls')
                    break
            if x<0:
                os.system('cls')
                print(dialogue[ctn].replace("<Name>",profile[0]))
                ctn += 1
            time.sleep(0.1)

    else:
        print(dialogue[0].replace("<Name>",profile[0]))
        print("Press the down arrow key to continue....")
        if reincarnation == True:
            print("Press the up arrow key to skip dialogue....")
        while ctn != len(dialogue):
            x = win32api.GetKeyState(0x28)
            if reincarnation == True:
                y = win32api.GetKeyState(0x26) # up arrow key
                if y<0:
                    os.system('cls')
                    break
            if x<0:
                os.system('cls')
                print(dialogue[ctn].replace("<Name>",profile[0]))
                ctn += 1
            time.sleep(0.1)


if __name__ == "__main__":
    os.system('cls')
    while (Menu_input == "1"):
        print("Welcome to Tales of Adventure!, a text turn based game." + 
              "\nMenu:"+
              "\n[1]:Start"
              "\n[2]:Exit")
        Menu_input = input("Input:")
        if(Menu_input == "2"):
            os.system('cls')
            print("Till the next adventure.")
            exit()
        elif(Menu_input != "1"):
            os.system('cls')
            print("invalid input. Try again")
            Menu_input = "1"       
        else:
            while (1):
                for y in range(len(dialogue_array)+1):
                    if y == 0:
                        os.system('cls')
                        dialogue = dialogue_array[y]
                        dialogue_output(dialogue,y)


                    if y == 1:
                        os.system("cls")
                        dialogue = dialogue_array[y]
                        while 1:
                            name_input = input("Insert Name here:")
                            if reincarnation == True:
                                if name_input == Boss_name:
                                    os.system("cls")
                                    print("That name is forbidden")
                                else:
                                    profile[0] = name_input
                                    break
                            elif name_input[0] == " " or name_input == "":
                                os.system("cls")
                                print("No name was found")
                            else:
                                profile[0] = name_input
                                break
                        dialogue_output(dialogue,y)


                    if y == 2:
                        os.system('cls')
                        dialogue = dialogue_array[y]
                        CD = Class_dialogue
                        check = 0
                        while check != 1:
                            print("Choose your class:"+
                                    "\n [1]:Warrior"+
                                    "\n [2]:Archer"+
                                    "\n [3]:Caster")
                            class_input = input("Input Class:")
                            if class_input !="1" and class_input != "2" and class_input !="3":
                                os.system("cls")
                                print("Invalid input")
                            
                            else:
                                dialogue_class = CD.choice(int(class_input))
                                profile[1] = dialogue_class[0]
                                os.system('cls')
                                dialogue_output(dialogue_class,y)
                                print("Type of "+profile[1]+" that can be chosen: "+ dialogue_class[1])
                                while 1:
                                    class_check = input("Would you like to choose another class(Y/N)")
                                    if class_check.upper() == "Y":
                                        os.system("cls")
                                        break
                                    elif class_check.upper() == "N":
                                        check = 1
                                        break
                                    else:
                                        print("Invalid Input. Only Y & N")

                    if y == 3:
                        os.system('cls')
                        PD = Profession_dialogue
                        PV = professions
                        prof = dialogue_class[1].split(" and ")
                        check = 0
                        
                        while check != 1:
                            os.system("cls")
                            print("Choose your Path:")
                            for x in range(len(prof)):
                                print(f"[{x+1}] {prof[x]}")
                            class_input = input("Input Profession:")
                            if class_input !="1" and class_input != "2":
                                os.system("cls")
                                print("Invalid input")
                            else:
                                switcher = {
                                    "Warrior":PD.Warrior_profession_dialogue(int(class_input)),
                                    "Archer":PD.Archer_profession_dialogue(int(class_input)),
                                    "Caster":PD.Caster_profession_dialogue(int(class_input)),
                                }
                                dialogue_profression = switcher.get(profile[1])
                                dialogue_output(dialogue_profression,y)
                                switcher_values ={
                                    "Warrior":PV.Warrior_Paths(int(class_input)),
                                    "Archer":PV.Archer_Paths(int(class_input)),
                                    "Caster":PV.Caster_Paths(int(class_input))
                                }
                                base_player_stats = switcher_values.get(profile[1])
                                dmg_min = int(base_player_stats[2][0])
                                dmg_max = int(base_player_stats[2][-1])
                                def_min = int(base_player_stats[3][0])
                                def_max = int(base_player_stats[3][-1])
                                print ("Your character stats:"+
                                    "\nMax Health="+str(base_player_stats[0])+
                                    "\nAction_rate="+str(base_player_stats[1])+
                                    "\nDamage=" +str(dmg_min)+ " - " + str(dmg_max)+
                                    "\nDefense=" +str(def_min)+ " - " + str(def_max))
                                while 1:
                                    prof_check = input("Would you like to choose another Path(Y/N)")
                                    if prof_check.upper() == "Y":
                                        os.system("cls")
                                        break
                                    elif prof_check.upper() == "N":
                                        profile[2] = prof[int(class_input)-1]
                                        check = 1
                                        break
                                    else:
                                        print("Invalid Input. Only Y & N")
                        dialogue = dialogue_array[y-1]
                        dialogue_output(dialogue,y)
                    
                    if y == 4:
                        TV = trinkets
                        print("Choose your Trinket:")
                        print("[1] Heart Pendant(+10 max health)\n",
                            "[2] Lion Pendant(+3 dmg)\n",
                            "[3] Shield Pendant(+3 def)\n",
                            "[4] Ring of Madness(-20 max health, +5 dmg)\n",
                            "[5] Ring of Light")
                        trinket_input = input("Trinket input:")
                        if trinket_input == "stop":
                                exit()
                        elif trinket_input !="1" and trinket_input != "2" and trinket_input !="3" and trinket_input !="4" and trinket_input !="5":
                            os.system("cls")
                            print("Invalid input")
                        else:
                            switcher = {
                                "1":"Heart Pendant",
                                "2":"Lion Pendant",
                                "3":"Shield Pendant",
                                "4":"Ring of Madness",
                                "5":"Ring of Light"
                            }
                        profile[3] = switcher.get(trinket_input)
                        final_player_stats = TV.apply_trinket(base_player_stats,profile[3])
                        dmg_min = int(final_player_stats[2][0])
                        dmg_max =int(final_player_stats[2][-1])
                        def_min = int(final_player_stats[3][0])
                        def_max = int(final_player_stats[3][-1])
                        print("New character stats:"+
                                "\nMax Health= "+str(final_player_stats[0])+
                                "\nAction_rate= "+str(final_player_stats[1])+
                                "\nDamage= " +str(dmg_min)+ " - " + str(dmg_max)+
                                "\nDefense= "+str(def_min)+ " - " + str(def_max))
                        dialogue = dialogue_array[y-1]          
                        dialogue_output(dialogue,y)

                    if y == 5:
                        #Minion enemy
                        EV = enemy
                        PM = PvM
                        GFD = Garv_fight_after_dialogue
                        Enemy_stat = enemy.Minion()
                        dialogue = dialogue_array[y-1]
                        dialogue_output(dialogue,y)
                        results=PM.PvM_play(profile[0],Enemy_stat,final_player_stats)
                        os.system("cls")
                        dialogue_output(GFD.dialogue(results),y)
                        if results == 1:
                            continue
                        else:
                            profile = ["<Name here>","<Class here>","<Path here>","<Trinket Here>"]
                            break
                        
                    if y == 6:
                        #Boss enemy
                        RFD =  Rufus_fight_after_dialogue
                        EV = enemy
                        dialogue = dialogue_array[y-1]
                        dialogue_output(dialogue,y)
                        PB = PvB
                        Enemy_stat = enemy.Boss()
                        results=PB.PvB_play(Boss_name,profile[0],Enemy_stat,final_player_stats)
                        dialogue = RFD.dialogue(results,profile[3])
                        dialogue_output(dialogue[0],y)
                        if results == 1 and profile[3] == "Ring of Light":
                            dialogue_output(dialogue[1],y)
                            Boss_name = "The Champion"
                            profile = ["<Name here>","<Class here>","<Path here>","<Trinket Here>"]
                        elif results == 1 and profile[3] != "Ring of Light":
                            print(dialogue[1].replace("<Name>",profile[0]))
                            Boss_name = profile[0]
                            profile = ["<Name here>","<Class here>","<Path here>","<Trinket Here>"]
                            reincarnation = True
                        else:
                            Boss_name = profile[0]
                            profile = ["<Name here>","<Class here>","<Path here>","<Trinket Here>"]
                            reincarnation = True
                        break
                
                while 1:
                    TA=input("Would you like to tell another story(Y/N):")
                    if TA.upper() == "Y":
                        os.system("cls")
                        break
                    elif TA.upper() == "N":
                        print("Till the next adventure.")
                        exit()
                    else:
                        print("Invalid Input. Only Y & N")