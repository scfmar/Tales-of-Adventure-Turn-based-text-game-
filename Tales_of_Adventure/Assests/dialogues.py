
class Game_dialogue:
    def array():
        opening_dialogue = ["Our story begins In Ecrast.",
                            "A small village located between the Sacral Forest and the Yormen Mountains.", 
                            "Many of the residence live off the land by cultivating crops, mining ore, and trading with merchants that pass by the tranquil and prosperous town.", 
                            "Everyone in the village was delighted with their livelihood and was contented to live a ordinary and peaceful life.", 
                            "Yet there were still individuals that dreamed to one day seeked glory and riches beyond their usual way of living."]

        after_char_name = ["One such indivdual was a young adventurer named <Name>",
                        "Raised in a middle class family. <Name> was always curious of their surrounding and wanted venture forth to places undiscovered or uncommon.",
                        "With this, <Name> had to learn how to defend themselves in their travels"]

        After_char_creation_dialogue = ["Though <Name> has accomplished so much in their youth. The idea of glory and riches still lingered.", 
                                    "This would all change when news of a noble lord planning to invade the Sacral Forest and Yormen Mountains for its resource.", 
                                    "To do this, the lord had to demolish and conquer the roads and villages that stood in his conquest.",
                                    "Hearing word of this, <Name> felt that this was their opportunity for adventure and to save the village for pending doom."
                                    "With their fiery passion and confidence <Name> readied themselves for the journey ahead.",
                                    "After three days of gathering enough supplies and information about the lord they will be facing,",
                                    "Their parents approached at their child once more and presented a trinket for goodluck.",
                                    ]
        After_char_gets_trinket_dialogue = ["Holding their parent'gift, <Name> couldn't help but hug them one last time and promising them that they will return",
                                            "After one more hug <Name> dawned their cloak and began their long trek the noble's estate outside on the other side of Sacral Forest."]

        Before_first_fight_dialogue = ["After a few days of travel they've made it to the noble's estate where numerous soldiers waited at the front of gates.",
                                       "Enraged by the sight of soldiers that might destroy Ecrast due to the greed of the lord. <Name> look to start their battle against to a soldier.",
                                       "After a few hours battling with the soldiers, A guard from the gates readied himself for battle.",
                                       "He adorn a different armor signifying that he was of upper rank.",
                                       "<Name> stood firmly before locking eyes on what would be their first real obstacle before dealing with the Lord of the Manor.",
                                       "After a couple of steps, the guard stopped and banged his chest. Gestured at <Name> to come at him.",
                                       '"This will be your final resting place peasant!!" The guard screamed.',
                                       "The other soldiers cheered at their higher ranking comrade.",
                                       '"I, Garv, captain of Lord Rufus\'s army, shall give you the honor to die on the excellency\'s rich land." He then raises his blade and jeered at <Name>.',
                                       '"COME AT ME!!!!, AAAAAAAAHHHHHHH" he cried and charged at <Name>.',
                                       "<Name> quickly took a fighting stance and look to strike."]
        
        Entering_the_Manor_dialogue = ["They open the door's of the manor and headed staright for Lord Rufus.",
                                       "In their search, minimal resistance was met before arriving at the Throne room.",
                                       "Within was a noble wearing purple clothing that was lavishing and flashy.",
                                       "They also had rings on each finger and a holding a golden scepter",
                                       "It was no question that <Name> stumbled upon the master of the manor, Lord Rufus.",
                                       "<Name> readied themselves while Lord Rufus looking at them annoyed.",
                                       '"How did you get in here?" Lord Rufus exclaims with disgust.',
                                       '"Guards!!!" On cue, numerous guards swarmed around <Name>',
                                       "In quick movements, <Name> defeated them with ease.",
                                       '"Hmmmm, interesting" Lord Rufus said as he eyes gleamed with surprise.',
                                       '"How would you like to serve me?" The noble came off his throne and walked slowly towards his intruder.',
                                       '"I\'m guessing you hail from Ecrast,the village between wood and stone. Am I correct?" he continues to walk towards <Name>.',
                                       '"Though I care not for your name I do adore your skills in battle." he then stopped to be an arm\'s lenght of <Name>',
                                       '"I heard about you defeating my captain, Garv." he continued',
                                       '"Though he was so loyal and strong, I wouldn\'t mind you joining my ranks."',
                                       '"think about it, I can give you wealth beyond measure and the glory of conquest."',
                                       '"Come now I can give you a better life than that pigsty of a living in Ecrast."',
                                       "The words of Rufus, shook the resolve of the adventurer and little by little lowered their weapon.",
                                       'Rufus smiled "I knew you would understand,"  he then raised his scepter that is now casting a purple light.',
                                       '"Now pledge your alligeance to me." he exclaimed but before he could fully cast his spell <Name> swatted it and lunge at the Lord.',
                                       "At the right moment, the current champion of Lord Rufus came forth and shielded him.",
                                       "<Name> backed up and readied themselves for the battle as Rufus dust himself of.",
                                       '"Why do I even bother with simpletons." He continued to remove on him',
                                       '"But I suppose I can still take you in broken,"He then gestured to his armored champion, who had glowing purple eyes, at <Name>',
                                       "Knowing what is to come, <Name> made ready."
                                       ]

        return [opening_dialogue, after_char_name, After_char_creation_dialogue,After_char_gets_trinket_dialogue,Before_first_fight_dialogue,Entering_the_Manor_dialogue]

class Class_dialogue:
    def choice(x):
        switcher = {
           # Warrior_Dialogue
           1:  ["Warrior","Berserker and Ironlad","In their spare time, <Name> would practice their swordmanship and combat prowess on near by trees with the longest stick they could find.",
               "In their constant training, <Name>'s muscles grew giving them the strength of 5 men and have an affinity with close-range weapons such as the sword and the battle axe.",
               "They took a chance in enlisting to the village's guardpost but found that they were best suited to be on the frontlines of war. "],
           # Archer_Dialogue
           2: ["Archer","Bowman and Arbalist","After recieving a sling from their Father, <Name> would practice skipping pebbles and rocks by the lake or shooting out birds in the sky to eat.",
              "Impressed by their dexterity with the sling, <Name>'s Father handed them a short bow and some dull arrows.",
              "To <Name>'s surprise, they learn they had a knack for archery and grew up to be a hunter for the village."],
           # Caster_Dialogue
           3: ["Caster","Elementalist and Alchemist","After learning that their Mother was a practioner in the Arcana, <Name>'s curiousity sparked.",
              "They began to learn and discover the untapped potential of harnessing the elements.",
              "In time, <Name> growed to be studious in learning magic under the guidance of their mother. They learned about casting spells to crafting potions that could heal or harm a person."]
           } 
        return switcher.get(x)
    
   

class Profession_dialogue:
    def Warrior_profession_dialogue(n):
        Berseker_dialogue=("After years of service on the frontlines, <Name> was feared by many.",
                           "Their duty was portrayed in bloodshed and absolute savagery.",
                           "Armed with twin axes and little to no armor,they became the personification of war.")

        Ironlad_dialogue=("As the years went by on the frontlines, <Name> learned that the best offense was an unpenetrable defense.",
                          "Adorned in steel and unending-resolve, they withstood blow after blow until the enemies' weapons dulled.",
                          "Weilding a inferior sword, they've earned the nickname 'Iron Behemoth'")

        if n == 1:
            return Berseker_dialogue
        else:
            return Ironlad_dialogue

    def Archer_profession_dialogue(n):
        Bowman_dialogue=("As the young <Name> continued hunting for the village, their proficiency of with the bow and arrow grows.",
                         "In quick sucession a flurry of arrows are fired by the young bowman, hitting their mark one way or the other.",
                         "Now armed with a longbow, even prey as quick as deer or silent like a fox stand no chance from the arrows of <Name>.")

        Arbalist_dialogue=("As years passed in the wild, <Name> realized if they were gonna be the best. They needed the best equipment.",
                           "With aid from their Father, The hunter became an arbalist, wielder of the crossbow.",
                           "Steady and quick on the trigger, nothing escapes <Name>'s eyes when aiming to kill.")
        
        if n == 1:
            return Bowman_dialogue
        else:
            return Arbalist_dialogue

    def Caster_profession_dialogue(n):
        Elementalist_dialogue=("As the young scholar continued practice the arts of the arcana, <Name> natural talent with the elements flourished.",
                               "The earth beneath them listened, fires quivered at first glance, messages in the wind whispered to in their ear.",
                               "All the elements obeyed them and crowned <Name> the greatest elementalist of their generation.")

        Alchemist_dialogue=("Though <Name> was not able to harness magic, their enthusiasm drived them to be an alchemist.",
                            "Through countless discovery of potions, they've relized that magic doesn't need to come from spells.",
                            "With their skills many of the townspeople rejoice in <Name> discoveries and expanded the idea of magic.")
        
        if n == 1:
            return Elementalist_dialogue
        else:
            return Alchemist_dialogue


    

   

class Garv_fight_after_dialogue:
    def dialogue(Status):
        Win_dialogue = ["Strike after strike, the two fought ferociously.", 
                        "But with a final blow Garv crumbles to the ground.",
                        "<Name> took a quick breather before walking up to the dying soldier.",
                        "Grumbling on the dirt, couldn't believe he lost to someone of lower status.",
                        '"This shouldn\'t have happened?" Garv said with a painful wheeze.',
                        'He looked up to <Name> filled with rage but quickly smirked at them',
                        '"But I suppose it doesn\'t matter. My lord will defeat you."',
                        "Garv struggle to stand, which tensed <Name> for another fight",
                        "After finally putting his feet under him, he laughed maniacally.",
                        '"OH GREAT LORD RUFUS!" he started screaming at the sky "SMITE THIS FOOL WITH YOU EXTRAORDINARY VIGOR".', 
                        "He then looked at <Name>, who is at the ready, one last time before walking a few steps back to gate and collapsing.",
                        "The soldiers in the surrounding couldn't believe it.",
                        "Most dropped their weapons and walked away from the battlefield",
                        "Some went into the manor to warn the others.",
                        "Meanwhile, <Name> breathe in some relief and tried to shake off the tension.",
                        "After mending their wounds, <Name> readied themselves one's more to face the Lord of the Manor, Rufus."]

        Lose_dialogue = ["Struggling to keep up with their opponent, <Name> was down on one knee",
                         "Catching themselves from the many wounds they sustained, Garv couldn't help but laugh at <Name>'s condition.",
                         '"Just I suspected," He said while flourishing his blade and the soldiers cheering at his victory.',
                         '"You are nothing but a spec of dirt in the Lord\'s magnificent territory."',
                         "He then kicked the injured adventurer to ground and raised his blade high.",
                         '"Maybe in another life you\'ll be more wise to not cross these lands."',
                         "Unable to move away from the next attack of Garv, <Name> knew this was the end.",
                         '"DEATH TO YOU AND YOUR NEXT OF KIN!!!!" Garv exclaimed before plunging his sword into the gut of <Name>',
                         "And that is end of <Name>'s story."]
        
        if (Status==1):
            return Win_dialogue
        else:
            return Lose_dialogue

class Rufus_fight_after_dialogue:
    def dialogue(status,trinket):
        Almost_win_dialogue=["After the difficult battle the champion has fallen.",
                             "The body then crumbled to dust as Lord Rufus looks shocked at the outcome.",
                             "<Name> started walking towards Lord Rufus to finish their quest.",
                             '"Hang on, hang on. We don\'t need to do this." The lord started to feel the fear of death as <Name> gets closer.',
                             '"Come now, no need to be violent." Rufus said quivering and backing away to his throne.',
                             '"D-d-do you want gold, I-I-I have some. How about land, you can take from me."',
                             "He then tripped and started to crawl backwards.",
                             "Closing in on the vunerable Lord. <Name> shook their head and readied to deal the final blow.",
                             "In a quick moments, both individuals met each other closer and blood was spilled.",
                             "...."
                             "...",
                             "..",
                             "."
                             '"Pathetic" said Rufus who stabbed <Name> in the chest.',
                             "Not knowing what happened, <Name> fell to their knees bleeding from their chest.",
                             '"Did you like my trick," he said with glee as he wiped the blood of his dagger hidden in the throne.',
                             '"Now since you have beaten my champion, you will be quite a substitute." He then picked up his scepter and pointed at <Name>\'s forehead',
                             "Struggling to move Lord Rufus couldn't help but smirk at their efforts to still fight.",
                             '"Oh do not worry, the poison won\'t kill you. I am in need of living body not a dead one." Rufus exclaimed.',
                             '"Now serve me." He then pushed the scepter onto <Name>\'s forehead.']

        True_win_dialogue=["Before the purple flash shined. The trinket that <Name> held was warmed around their fingers.",
                           "In the brilliant light, the strength of the adventurer came back and swatted the scepter once again to rise quickly back to their feet.",
                           "Lord Rufus quickly backed off and also dropped the knife he was holding.", 
                           '"How did you resist my mag-" in rapid movements, <Name> managed to grab the knife from the ground and stabbed The lord in the gut.',
                           "Unable to scream or acknowledge the chain of events, Lord Rufus was completely stunned and started to feel the poison flow in him.",
                           '"I... can\'t... believe... it." he uttered softly before finally going limp on the top of <Name>',
                           "They tossed aside the corpse of the noble and quickly sat back down to cath their breath.",
                           "Numerous feelings and questions flooded their mind as a faint purple light came from the scepter",
                           "The light from the scepter flickered for few moments before quickly dying out.",
                           "A sudden gust of wind passed through the victorious adventurer and a light whispered was heard around them.",
                           '"Thank you."',
                           '"You freed us."',
                           '"May you live longer."',
                           "The whispers then died out and the room was once again silent.",
                           "Confused at what just occured, <Name> couldn't help being proud at their achievement.",
                           "The day was won and <Name> looked forward going back home.",
                           "But before they could, <Name> couldn't help but look around the mansion first and see if was anything valuable.",
                           "After some time, <Name> came out triumphant with some loot in tow.",
                           "With a skip in their step, they marched triumphantly back to Ecrast.",
                           "The story of <Name> continues."]

        Lose_dialogue=["Even after years of experience in their craft, the mighty champion stood victorious.",
                       "<Name> was on the ground bloodied and beaten, which delighted the Lord immensely.",
                       '"I hope you know blood really didn\'t need to be spilled here." he mockingly tells the fallen hero.',
                       '"Look at you." he said as he gets closer to pin them with the scepter.',
                       '"Although you looked beaten down like easy prey, you\'ll still prove useful in the end."',
                       "The scepter then glowed as he moved it to the forehead of <Name>.",
                       "<Name> felt a seering pain as the scepter touched their forehead",
                       '"Now be mine forever," Lord Rufus said sinisterly, "You\'ll make such a wonderful puppet to play with."',
                       "As the purple light flashes everything went dark and the <Name>'s eyes illuminated purple",
                       "And that is end of <Name>'s story."]
        
        if status == 1 and trinket == "Ring of Light":
            return Almost_win_dialogue, True_win_dialogue
        elif status == 1 and trinket != "Ring of Light":
            return Almost_win_dialogue, Lose_dialogue[-1]
        else:
            return Lose_dialogue,""
        return 