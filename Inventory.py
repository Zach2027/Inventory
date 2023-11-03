import random
from characters.character import *
from attacks import *
def full_credits(name):
    print(f'''Congratulations {name} for playing Gladiator!
Gladiator is based of off the real 2000 film Gladiator.
Gladiator was writen by Zach and Kaz.
ChatGPT was used for names of characters.
Well done in your final fight.''')
def fight(player_character, enemy_character, fight_number):
    options = [ATTACK_1, ATTACK_2, ATTACK_3, ATTACK_4, ATTACK_5, ATTACK_6, ATTACK_7, ATTACK_8]
    input('''The battle begins''')
    while enemy_character.health > 0 and player_character.health > 0:
        attack(player_character, enemy_character, options[:fight_number + 1])
        if player_character.health <= 0:
            print("You DIE. You are not a true gladiator of Rome.")
            main()



def attack(player, enemy, attack_options):
    attack_1_10 = input('''As you clash blades with your opponent you see a few things you can do''')
    for index, attack_option in enumerate(attack_options):
        print(f"({index}) {attack_option}")

    while not attack_1_10.isdigit() or int(attack_1_10) >= len(attack_options):
        attack_1_10 = input(f"please enter a 0-{len(attack_options)-1}")
    if attack_1_10 == ("0"):
        trade_blows_1 = random.choice(["hit","small hit","critical miss"])
        if trade_blows_1 == "hit":
            enemy.health = enemy.health - player.strength + enemy.shield
            if enemy.health > 0:
                print(f"You get a clean hit and you have {player.health} left, your opponent has {enemy.health} health left")
            if enemy.health <= 0:
                print(f'''As your opponent swings his sword to you, you manage to side step the blow,
    retaliating with a strike of you own.  As you swing your {player.weapon} at his head, you get a clean strike
    sliceing his head clean off as you win the fight and the crowd''')

        if trade_blows_1 == "small hit":
            enemy.health = enemy.health - player.strength * 0.5 + enemy.shield
            if enemy.health > 0:
                print(f"You find a small and doubtful opening that you take, coming off with a small victory.  You have {player.health} left, your opponent has {enemy.health} health left")
            if enemy.health <= 0:
                print(f'''As a deadly wave of attacks come, you find your self with the high ground but {enemy.name} doesn't give up
    approaching you, he tries to swing at your ankles jumping up you bring your {player.weapon} 
    down in his head spliting it right down the middle, winning the fight and the crowd.''')
        if trade_blows_1 == "critical miss":
            player.health = player.health - enemy.strength + player.shield
            print(f'''  You miss horribly, allowing your opponent to duck your attack slicing your ankle,
    You have {player.health} left, your opponent has {enemy.health} health left''')


    if attack_1_10 == "1":
        play_slow_1 = random.choice(["lose","win","win","win"])
        if play_slow_1 == "lose":
            player.health = player.health - enemy.strength + player.shield
            print(f'''  As you play it safe, you opponent finds an opening,
    throwing a rock at you leg causing a deep cut to form, you have {player.health} 
    left while your opponent has {enemy.health} health left''')
        else:
            enemy.health = enemy.health - 0.25*player.strength
            if enemy.health > 0:
                print(f"""  As you play it slow you manage to get a few small hits on your opponent.
    This does little damage and your opponent is at {enemy.health} health while you are at {player.health} health.""")
            if enemy.health <= 0:
                print(f'''  As you clash blades, you slide your {player.weapon} down the blade of your opponents,
    with a little force you manage to cut {enemy.name}'s hands off killing him and winning the fight but not the crowd''')

    if attack_1_10 == "2":
        big_blow = random.choice(["win","win","lose","lose","lose"])
        if big_blow == "win":
            enemy.health = enemy.health - player.strength*1.5
            if enemy.health > 0:
                print(f"""  You perform an amazing counter to the charging man, slashing him through his chest,
    although this is non lethal, it does a huge amount of damage, you have {player.health} health left
    and your bleeding opponent has {enemy.health} health left.""")
            if enemy.health <= 0:
                print(f'''As {enemy.name} presses you, you see an opening on his leg, 
    taking it you cut his leg off and go for the arm, sliceing it clean off, wining the battle, the day and the crowd.''')
        if big_blow == "lose":
            player.health = player.health - enemy.strength + player.shield
            print(f'''As you take a wrong step forward, the man sees this before you even make your move,
    stabbing you through your chest, you have {player.health} health and the man has {enemy.health} health left''')


    if attack_1_10 == "3":
        side_strike = random.choice(["win", "win", "lose"])
        if side_strike == "win":
            enemy.health = enemy.health - player.strength + enemy.shield
            if enemy.health > 0:
                print(f"""You clash your {player.weapon} with your opponent's weapon, you manage to slide your blade
    around your opponent's hilt slashing his arm. You have {player.health} health left and your opponent has {enemy.health} health left.""")
            else:
                input(f'''As your opponent swings his weapon down on you, you manage to step to the side and cut your opponent in half.
     with the monsters top half sliding off the his legs, you hear {player.name} chanting in the crowds. 
    You won the battle but more importantly you won the crowd.''')
        if side_strike == "lose":
            player.health = player.health - enemy.strength + player.shield
            print(f"As you attack your opponent you get out played. Your opponent steps to the side, causing you to miss your attack and your opponent returns a wooden hilt to the face.  This puts you down to {player.health} health")

    if attack_1_10 == "4":
        slice_up = random.choice(["big_win","win","lose","lose"])

        if slice_up == "big_win":
            enemy.health = enemy.health - 2*player.strength
            if enemy.health > 0:
                print(f"""As you clash the blade of your {player.weapon} against your opponent's weapon, you manage to slice the knee of your opponent
forcing him to open up and oppurtunity which you take and slice your opponent from his lower abbs to his chest
forming a deep cut. Your opponent has {enemy.health} health left""")
            else:
                print(f"""As your opponent swings his weapon horizontaly at your head, you duck, sending an uppercut back with you {player.weapon}
slicing your opponent right in half, spliting him. As his huge body slams against the sand, your hear {player.name} {player.name} {player.name} fill the arena""")

        if slice_up == "win":
            enemy.health = enemy.health - player.strength*0.75
            if enemy.health > 0:
                print(f"""You manage to find a little opeing of your opponent's chest, swinging up, you make a small cut on his chest
your opponent has {enemy.health} health left and you have {player.health} health left.""")
                    
            else:
                print("""As your opponent lunges at you, you manage to side step the attack, sliceing your opponent's hands off.  
    Although this is a non lethal strike, you have one the battle. Your opponent drops to the ground, defenseless. 'kill!' 'kill!' 'kill!' 
    start to fill the air. your opponent's life is in your hands.""")
                save_life = input("Do you (1) listen to the crowd or (2), spare the fighters life")
                while int(save_life) != 1 and int(save_life) != 2:
                    save_life = input("please enter a 1 or a 2")
                    if save_life == "1" or save_life == "2":
                        break

                if save_life == "1":
                    fame = fame + 5
                    player.name = player.name + " the Mercyfull"
                    print("You slice your opponent's head clean off, gaining 5 fame and the new name .")
                if save_life == "2":
                    fame = fame + 10
                    player.name += " the Mercyless"
                    print("You defy the crowd, sparing your opponent's life.  By doing this you become more liked by all giving you 10 fame")
        if slice_up == "lose":
            player.health = player.health - enemy.strength + player.shield

            print(f"""You see an opening as you attack, you go for a lethal blow but your opponent side steps, returning a blade to the chest.
    your opponent has {enemy.health} health left and you have {player.health} health left.""")

            
    if attack_1_10 == "5":
        foot = random.choice(["sweep","miss","sweep",])
        if foot == "sweep":
            enemy.health = enemy.health - player.strength + enemy.shield
            if enemy.health > 0:
                print(f"""You sucsessfully sweep the leg of {enemy.name}, causing him to fall, this is an effective way to tire out {enemy.name}
this puts {enemy.name} down to {enemy.health} health while your at {player.health} health""")
            else:
                print(f"As you Sweep {enemy.name}'s leg, he falls which gives you enough time throw your {player.weapon} down through {enemy.name}'s head, winning the crowd and the Fight.")

        if foot == "miss":
            player.health = player.health - enemy.strength*1.5 + player.shield
            print(f"{enemy.name} steps over you {player.weapon} which is swong at his leg, bashing you with his weapon, you go down to {player.health} health and Korlax has {enemy.health} health left")


    if attack_1_10 == "6":
        stab = random.choice(["big_win","lose","big_lose"])
        if stab == "big_win":
            enemy.health = enemy.health - player.strength*2 + enemy.shield
            if enemy.health > 0:
                print(f"""As {enemy.name} swings down his weapon, you manage to force the blade into a large stone.  
    As {enemy.name} is tring to get his weapon free, you manage to impale him with the tip of your {player.weapon}
    this puts {enemy.name} at {enemy.health} health while you have {player.health} health left.""")
            else:
                print(f'''As {enemy.name} and you exgange blows, you stab {enemy.name} with the tip of your {player.weapon}, forcing it through {enemy.name} you feel the tention be relived
    Then you relized that the tip of you {player.weapon} is sticking out the back of {enemy.name}.  You won the battle and the crowd.''')
        if stab == "lose":
            player.health = player.health - enemy.strength + player.shield
            print(f'''You go for the stab on {enemy.name} but your too slow, taking the side of {enemy.name}'s weapon to your head.
    this puts you down to {player.health} health''')
                
        if stab == "big_lose":
            player.health = player.health - enemy.strength*2 + player.shield
            print(f"""You're starting to get slopy, {enemy.name} is out lasting you. Getting frustrated you go for a risky move that doesn't pay off
    With {enemy.name} easily moving out of the way, stabing you in the arm with a non leathal blox.
        Your at {player.health} health and {enemy.name} is at {enemy.health} health.""")

    if attack_1_10 == "7":
        fake_dead = random.choice(["fake","big lose"])
        if fake_dead == "fake":
            enemy.health = enemy.health - 1.5*player.strenth + enemy.shield
            fame = fame - 1
            if enemy.health > 0:
                print(f"you fake a hamstring injury and {enemy.name} looks up at the crowd as they booooooooo.  As {enemy.name} looks up you stab and the crowd boooos more.")
                print(f"you lost 1 fame and your opponent has {enemy.health} health left")
            else:
                print("As you go down you look like you are dying. As you hunch over your enemy gets ready for a final blow.  As he raises his weapon you stab you enemy through his heart winning the battle")
        if fake_dead == "big lose":
            player.health = player.health - enemy.strength + player.shield
            print(f"""As you fake an injury you opponent stabs you in your exposed hand.  You get up with only {player.health} health left.""")

    if attack_1_10 == "8":
        fake_attack = random.choice(["miss","fake"])        
        if fake_attack == "miss":
            player.health = player.health - enemy.strength + player.shield
            input(f'You attept a fake that is obvios and {enemy.name} slashes you puting you down to {player.health} health')
        if fake_attack == "miss":
            print(f"You successfully fake out {enemy.name} giving you a few options.")
            choice_8 = input("""(0) go for the head
(1) Go for the chest""")
            if choice_8 == "0":
                random.choice(["hit","miss"])
                if choice_8 == "miss":
                    print("You stalemate and come off with nothing")

                if choice_8 == "hit":
                    enemy.health = enemy.health - player.strength*2 + enemy.shield
                    if enemy.health <= 0:
                        print("You go for the head, with out any restraint you cut the head clean off winning the crowd and the battle.")
                    else:
                        print(f"You get a clean hit on the face couseing a huge gash to form on {enemy.name}'s face")
            if choice_8 == "1":
                enemy.health = enemy.health + enemy.shield - player.strength
                if enemy.health > 0:
                    print(f"As you go for the chest you slash {enemy.name} through the chest cutting through his armor cousing him to have {enemy.health} health left")
                else:
                    print(f"As you go for the chest, you swing a bit too hard sliceing {enemy.name} right in half.  As you come away with this brutal victory, you win the crowd")
    if attack_1_10 == "9":
        crowd = "lose"
        if player.name == "gladiator" or player.name == "Gladiator" or player.name == "Spaniard" or player.name =="spaniard":
            crowd = "win"
        elif player.name == "gladiator the Mercyfull" or player.name == "Gladiator the Mercyfull" or player.name == "Spaniard the Mercyfull" or player.name =="spaniard the Mercyfull":
            crowd = "win"
        elif player.name == "gladiator the Mercyless" or player.name == "Gladiator the Mercyless" or player.name == "Spaniard the Mercyless" or player.name =="spaniard the Mercyless":
            crowd = "win"
        if crowd == "win":
            enemy.health = enemy.health - 20
            print(f"You are the chose Gladiator that will bring the future back to rome.  With that you are gifted in battle.  {enemy.name} is at {enemy.health} health")
        else:
            player.health = player.health - 10
            print(f"You are not the chosen Gladiator and the crowd throws junk at you, a metal ball hits you in the head dealling 10 damage to you.  You are at {player.health} health")


def main():
    print('''This is a gladiator game that will bring you through the depths
    of battle with rewards and gear, while playing, it will take you through the
    key situations of the duel. With every win you get closer to freedom (reach 100 fame to become free)
    Good luck to you''')
    print("Some Storyline requires you to hit enter to advance")
    player = Character(input("what is your name Gladiator?  "), 100, 0, 0, )
    print('''
        You are a slave forced into battle and your first fight awaits.''')
    print('''As you step towards the thundering gates, 
    you get offered a choice, 
    your pick will stay with you for the rest of your life
    (some gear gives you health, strength or maybe defense, 
    these will help you survive in battle)''')
    fame = 0


    
    while player.health > 0:
        weapon_1 = input("Would like an axe(1) or a long sword(2)")

        while int(weapon_1) != 1 and int(weapon_1) != 2:
            weapon_1 = input("please enter a 1 or a 2")
            if weapon_1 == "1" or weapon_1 == "2":
                break
        if weapon_1 == "1":
            player.weapon = axe
            player.strength += 20
        if weapon_1 == "2":
            player.weapon = long_sword
            player.strength += 20
            player.shield += 3
            

        enemy_1 = small_man
        
       

        input(f"As you step out of the gates of rome with your new {player.weapon}, you see your opponent,")
        input(f'''
        you size your self up against your opponent and realize that your bigger. 
    You have {player.health} health while the man only has {enemy_1.health} health
    you have {player.strength} strength and your opponent has {enemy_1.strength}
    you also have {player.shield} defense and your opponent has {enemy_1.shield}''')
        print(''' Throughout the battle you're going to see key openings and these openings are where you need to strike.''') 
        fight(player, enemy_1, 1)
        player.health += 30
        fame += 5
        input('3 days later')
        choice_2 = input('''Through out your recovering time, you put your time to good use.
            You realize that you could (1) workout strengthing your self, (2) get a good healing meal or (3) attempt to get a lesson from an old Gladiator''')
        while int(choice_2) != 1 and int(choice_2) != 2 and int(choice_2) != 3:
            choice_2 = input("please enter a 1, 2 or a 3")               

        if choice_2 == "1":
            player.strength = player.strength + 10
            input(f'''You hit the gym, doing push ups, sit ups and bench press.  
        You now have {player.strength} strength.''')
        if choice_2 == "2":
            player.health = player.health + 50
            input(f'''You find a good meal, healing your self up.  As you enjoy your warm meal,
        you regain some health, bring yourself up to {player.health} health''')

        if choice_2 == "3":
            player.shield = player.shield + 4
            input(f'''You find an old man with a lot of gray.  He to is a slave too, as you train, he points something out
        you realize that this suggestion is meaningful.  You ask if there is anything else that the man sees,
        in return he offers a leason, you take it and realize that this will help you with your defense.
            Your new defense is {player.shield} ''')

        input(f'''As time goes on you heal your injuries, but their is something new, you hear word of a certain Gladiator
    his name echos threw your camp, all anyone talkes about is a Gladiator named {player.name}.  Your also realize that you gained 
    fame from your fight, puting you at {fame} fame.''')
        player.health = player.health + 50






        enemy_1 = korlox
        input(f'''Your next fight is in one hour, as you prep and research for imformation on your oppenent, 
    you find out you're fighting a big guy. The man's name is {enemy_1.name} the big.  {enemy_1.name} is 4-0 on all his fights.
    As you study his past fights, you see that {enemy_1.name} has {enemy_1.health} health when you only have a mere {player.health} health.
    The upside is that you have {player.strength} strength when {enemy_1.name} only has {enemy_1.strength} strength.
    You have {player.shield} defense while {enemy_1.name} has none.''')
            
        input('''In your next fight, you will have a different type of battle, being able to chose what strike your want to do.
    Through this you will be able to have more options and the battle will be more intense.''')
        
        input(f'''You exit the Gates of an old beaten down arena.  {enemy_1.name} stands infront of you, as you step out,
        You see {enemy_1.name} is holding a long axe''')
        
        fight(player, enemy_1, 2)
        player.health += 30
        fame += 5






        if player.health <= 0:
            print("You died")
            break
        fame = fame + 10
        player.health = player.health + 30
        input(f"""Your victory is widely acknowledged.  Lots of people know the name {player.name}. 
        You become very popular, your fame becomes {fame} as more people cheer for you""")
        input('''The next few days are on the chiller side, you rest eat and sleep. This lasts for about a week before you gain enough strength to train''')    
        input('''As you strength train, a man comes up to you and starts a conversation about how well you fought. 
        He says that he was a slave in his early days and knows your going to be great and he is willing to help
    all he askes in return is for you to mention his name when you become great. 
        The man then brings out 2 pairs of armor. You see his face and realize this is your owner, Proximo.''')

        armor = input('''Would You like
    (1), A highly armord armor set that is made of heavy metal which will help protect you
    (2), A lighter chainmail armor set that will protect to a certain degree but is made to be agile''')

        while armor != "1" and armor != "2":
            armor = input("please enter a 1 or 2")

        if armor == "1":
            player.shield = player.shield + 8
            print(f"Your armor helped your defence majorly puting it at {player.shield}")

        if armor == "2":
            player.shield = player.shield + 3
            player.strength = player.strength + 8
            
            print(f"You take the light wieght chainmail armor which puts you defense at {player.shield} and you relize that your stronger when you wear this armor puting you at {player.strength} strength")

        input('''As you get ready for your 3rd fight and your owner Antonius Proximo tells you that you and him need to talk.
    He tells you that you opponent is a mean killing machine coming out of retirement and he wants blood.  His name is Tigris of Gaul.  
    After long talk, Proximo tells you that he was a slave once. set free by the emporor. The only way to become free is to win the crowd.
    Antonius Proximo tells you that he wasn't great because of his skill but he was great because the crowd loved him.''')
        
        print(f'''As you step out of the roaring gates of the same areana you just won in, you hear both names roaring, {player.name}, Tigris
    he comes out you size him up. ''')
        enemy_1 = tigris
        print(f''' The man's name is {enemy_1.name} the great.  {enemy_1.name} is 7-0 on all his fights.
    As you study his past fights, you see that {enemy_1.name} has {enemy_1.health} health when you have {player.health} health.
    You have {player.strength} strength when {enemy_1.name} has {enemy_1.strength} strength.
    You have {player.shield} defense while {enemy_1.name} has {enemy_1.shield}.''')
        fight(player, enemy_1, 3)
        player.health += 30
        fame += 5
        input(f''' After you leave the stadium, you hear a small boy shouting {player.name}! Then another person joins in, then another says {player.name}, it starts to multiply one person after another.
              Eventually every is chanting {player.name}, {player.name}, {player.name}! You now have 3 options ''')
        crowd_add = input(''' 
(1) Ignore the crowd
(2) Start flexing in front of the crowd
(3) Throw your sword up in the air at the organizers attempting to hype everyone up''')
                          
        while crowd_add != "1" and crowd_add != "2" and crowd_add != "3":
            crowd_add = input("please enter a 1, 2, or 3")

        if crowd_add == "1":
            fame = fame + 3
            print(f"The crowd thinks you are as tough as a soldier, you now have {fame} fame")

        if crowd_add == "2":
            fame = fame + 5
            print(f"The crowd is amazed by your physique, and roar in approval, you now have {fame} fame")
        if crowd_add == "3":
            odds = random.choice([1,2])
            if odds == 1:
                fame = fame - 10
                print(f"You hit a senator in the leg, the crowd cheers, but the senator is well respected, causing you to now only have {fame} fame")
            else:
                fame = fame + 10
                print(f"Your {player.weapon} perfectly spears a pig, sending a wave of laughter through the crowd, they love it, you now have {fame} fame")
        enemy_1 = spartacus
        pre_fight = input('''A few days pass, and you are about to get into your next fight. 
                 Before you step into the arena,  you find yourself in a dimly lit chamber, adorned with ancient weaponry and the distant echoes of the crowd's anticipation. 
                 Your heart is pounding, and the weight of your impending battle pressed heavily upon your shoulders. 
                 Two options lay before you:
                    (1) Pray to the gods up above
                    (2) Consider every tacting a move that could possibly occur''')
        
        while pre_fight != "1" and pre_fight != "2":
            pre_fight = input("please enter a 1 or 2")
        if pre_fight == "1":
            print("A flash of dry lightning is heard and seen in the arena, the gods have answered your prayers.")
            player.strength += 10
            player.health += 20
        if pre_fight == "2":
            print(f'''You think of everything that {enemy_1} could possibly do.
            You begin rack your brain for what Proximo told you about {enemy_1}'s strategy in his past fights.
            You remeber how aggresive {enemy_1} is, and replace your shield, getting a better one.''')
            player.shield += 8
        
        print(f'''
As you step through the grand entrance, the deafening roar of the crowd chanting {enemy_1} louder than {player.name}, is something that sends shivers down your spine.
You finally see your opponent, who is named {enemy_1.name}. {enemy_1.name} is undefeated. From his past fights, you know that {enemy_1.name} has {enemy_1.health} health compared to your {player.health} health.
You have {player.strength} strength while {enemy_1.name} has {enemy_1.strength} strength.
You defense is {player.shield} while {enemy_1.name} has {enemy_1.shield}.''')
        fight(player, enemy_1, 4)
        player.health += 30
        fame += 5
        input("Two days later...")
        input("your body still aches, and the wounds you sustained remind you of the fierce struggle you endured. The cheers of the crowd have faded into memory, replaced by the solemnity of the training grounds as you prepare for your next bout")
        extra_health_1 = input('''The scars on your flesh serve as a reminder of the price you pay for glory in the unforgiving world of the gladiator. You are faced with a choice:
(1) Wrap your wounds in bandages, as you were taught in your training
(2) Apply a special ointment, hoping it doesn't poison you''')
        while extra_health_1 != "1" and extra_health_1 != "2":
            extra_health_1 = input("please enter a 1 or 2")
        if extra_health_1 == "1":
            player.health += 70
            print(f"The bangdages are healing your wounds, you now have {player.health}health")
        if extra_health_1 == "2":
            player.health += 50
            player.shield += 5
            print(f"The ointment cleans and heals your wounds, it also clears your mind, you now have {player.health} health and {player.shield} defense")
        enemy_1 = lucius_verus
        input(f'''
As you step through the roaring entrance of a new area, The new arena is quiet but as you step out, {enemy_1.name} , {enemy_1.name} booms much more {player.name}, is something that butterflies through your stomach.
You finally see your opponent, who is named {enemy_1.name}. {enemy_1.name} is 12-0. From his past fights, you know that {enemy_1.name} has {enemy_1.health} health compared to your {player.health} health.
You have {player.strength} strength while {enemy_1.name} has {enemy_1.strength} strength.
You defense is {player.shield} while {enemy_1.name} has {enemy_1.shield}.''')
        fight(player, enemy_1, 5)
        input("""As you walk away from your fallen enemy you walk right out, no reaction.  This leads rumors of your victory that your not human.  
Your something more.""")
        fame += 5
        player.health = player.health + 30
        print("""5 days pass and you have a lot of down time.  You are stuck inside, when a messenger tells you that you are invited to the Colosseum.
    You can't fight there without at least an 8-0 record so you need to fight more.""")

        upgrade = input("""As time passes you have a couple options:
(1) Sharpen your sword, with a fine grade rock
(2) Do ab drils to increase you toughness and endurance""")
        while upgrade != "1" and upgrade != "2" and upgrade != "3":
            print("please enter a 1 or a 2")
            break
        
        if upgrade == "1":
            player.strength += 10
            print("You Sharpen your Weapon and you gain strength sharpening")
        if upgrade == "2":
            player.shield += 8
            print("Your work on toughness.  Strengthing your muscles and bones you gain some shield")

        if upgrade == "3":
            player.strength += 15
            player.shield += 10
            print("You work on both becoming more toughness and strength.")

    
   
        enemy_1 = galius
        input(f'''
With the news of the Colosseum in your head, The arena sounds silent even thought it is roaring {player.name}, You finally see  {enemy_1.name}. 
He is much smaller than expected and {enemy_1.name} is only 5-0 . From what you have heard, you know that {enemy_1.name} has {enemy_1.health} health compared to your {player.health} health.
You have {player.strength} strength while {enemy_1.name} has {enemy_1.strength} strength.
You defense is {player.shield} while {enemy_1.name} has {enemy_1.shield}.''')
        fight(player, enemy_1, 6) 
        input(f''' As you travel through the Turkish deserts, you arrive at a town.
              The town Samsun is bustling with activity. You arrive in the middle of the town and hear some kids saying {player.name} you are me hero!
              The ask you to follow them and eventually they lead you to a group of vendors.''')
        input(f'''
The first vendor has a golden gladiator helmet.
The golden helmet is a breathtaking masterpiece
cast from pure, gleaming gold that shimmers under the arena's intense sunlight.
Its design is elegantly simple yet regal, featuring a rounded shape that fully encases your head and a polished, reflective surface that captures the attention of all who gaze upon it. 
Engraved on the side is {player.name}''')
        input('''
Next you see a beatiful diamond encrusted chestplate. 
The diamond-encrusted chestplate is a breathtaking masterpiece, a dazzling display of extravagance and strength. 
Crafted from sturdy metal, it is meticulously adorned with a multitude of flawless, brilliant-cut diamonds, creating a shimmering armor that commands attention on the battlefield.''')
        armor_choice_2 = input('''Do you choose the:
(1) The golden helmet
(2) The diamond encrusted chestplate''')
        while armor_choice_2 != "1" and armor_choice_2 != "2":
            armor_choice_2 = input("please enter a 1 or 2")
        if armor_choice_2 == "1":
            player.shield += 5
            fame += 5
        if armor_choice_2 == "2":
            player.shield += 10
            
        fame += 5
        player.health = player.health + 30







        enemy_1 = decimus
        input(f'''
You get ready to come out of the gates of the Colosseum. {player.name} is roaring throguh the crowd, You see  {enemy_1.name} standing on the other side of the arena. 
He is a very raw gladitor who is trying to make a name for himself. {enemy_1.name} is only 5-0 . 
From what you have heard, {enemy_1.name} is a cold killer and has
{enemy_1.health} health compared to your {player.health} health.
You have {player.strength} strength while {enemy_1.name} has {enemy_1.strength} strength.
You defense is {player.shield} while {enemy_1.name} has {enemy_1.shield}.''')
        fight(player, enemy_1, 7)
        player.health = player.health + 30
        fame += 10
        input(f"""As you leave the arena with blood covering you, You hear {player.name}, {player.name}, {player.name}
You raise your blood drenched {weapon_1} and applause fills the arena.  Gaurds come out and circle you with spears pointing at you.
'Live' 'Live' 'Live' fills the air and you look up and 
Commodus, Emporer of Rome holds his hand in a fist with his thumb up.  With this, more cheering fills the air.""")

        print("3 days past and you")
        prep = input(f"""You can:
(1) Devolop your skills with your {weapon_1}
(2) Plan out a stratagy for next fight""")
        

        while prep != "1" and prep != "2":
            print("please enter a 1 or a 2")
            
        if prep == "1":
            player.strength += 15
            print(f"You focus on building your skills puting you at {player.strength} strength")

        if prep == "2":
            player.shield += 8
            print(f'''You mentaly train for your next fight seeing every attack your next opponent could do
    This puts you at {player.shield} shield''')



    enemy_1 = corvus
    input(f'''You are getting ready for battle when you hear news that the emporer is a big fan of yours
He will be watching this fight as well as he was keeping track of your last few fights.
Athough he apears as a fan you know deep down that he has hated you ever sense your 4th fight.
You also have hated him when he made the choice to leave you out to die in the battle field
This can't get in the way of the fight so you start to look at {enemy_1}''')
    input(f'''You have {player.health} when {enemy_1.name} has {enemy_1.health}
You have{player.strength} while {enemy_1.name} has {enemy_1.strength}
You have {player.shield} while {enemy_1.name} has {enemy_1.shield}''')
    fight(player, enemy_1, 8)
    player.health = player.health + 30
    input(f"""It has been a long fight with blood on your hands and blood on your {weapon_1.name}.
50 or so soldiers apear, spears out ready to kill.  All around you when the emperor comes out, he wants to meet you.
'I am Commodus, Emperor of Rome and who are you.
'I am {player.name}'
'tell me your real name slave' """)
    real_name = input("Your real name")
    real_name = real_name + random.choice([" the commander of the Armies of the North, General of the Felix Legions","the Commander of the Armies of the South, General of the Shadow Legions", "the Commander of the Armies of the East, General of the Fire Legions"])
    real_strength = player.strength
    player.strength = 15
    real_shield = player.shield 
    player.shield = 5
    real_health = player.health
    player.health = 60
    enemy_1 = commodus


    input(f"""I am {real_name}
    'Why won't you just die'
Gasps fall over the crowd becuase you were the greatest General in all of rome, now forced to fight.
You are now standing in front of the man who killed your family and he knows it.  A sign of relief falls over Commodus's face when he says
'I will fight you to the death in one weeks time to prove my strength as your Emperor' Commodus Yells out
The crowd aplauses and the great battle will happen in 1 week.""")


    input(f"""Time zips by when you realize you have 1 hour until you take your revenge.  
    Out of no where 4 guards rush in and you black out
          
When you wake you relize the Commodus is standing in front of you. 'This is going to be an easy fight he says as he stabs you through the chest.
    Your armor gets put on top, concealing your wound and you get dragged out into the Colosseum.  Your weak but you need to get your revenge in this life or the next
You have {player.health} health, you have {player.shield} shield and {player.strength}
The battle begins as Comodus walks out.""")
    fight(player, enemy_1, 9)
    fame += 20

    player.shield = real_shield
    player.strength = real_strength 
    player.health = real_health 
    input(f''' As you take in the chanting of the surrounding crowd, all you can think about is your sweet sweet revenge. 
        You, {real_name} have gotten your revenge on the tyrant who murdered your family, and Marcus Aurelius the True King of Rome. 
        The chanting begins to fade, and a sharp pain is felt all over your body. As you begin to limp your legs go numb, and you collapse.
        The only thought in your mind is of your late family, and the glory you have brought to Rome.''')
    if fame > 100:
        input(f'''Your Supporters storm the arena, bringing your lifeless body to a medical bay, attempting to save you.
        You wake up, and see a crowd of thousands chanting king, king, king. A man walks up to you with a crown. He says '{real_name}' you are the only Emperor of Rome, and hands you a crown.
        You walk out and place the crown atop your head. You greet your people, and recite 'I {real_name} am your true emperor. You shall be treated as the true people of Rome.'
        ''')
    else:
        print("The people honor you, but as nothing more than a martyr. They give you a hero's funeral.")
      
    CREDITS = input("would you like to see the full credits?")
    if CREDITS.lower().startswith("y"):
        full_credits(player.name)
    extra_fight = input(" ")
    if extra_fight == "final fight":
        enemy_1 = maximus
        print("You have discovered our easter egg! Good Job!")
        fight(player, enemy_1, 10)
        


main()