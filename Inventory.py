import random
from characters.character import Character
from characters.character import korlox
from characters.character import tigris
print("Gladiator writen by Zach and edited by Kaz")
print('''This is a gladiator game that will bring you through the depths
of battle with rewards and gear, while playing, it will take you through the
key situations of the duel. With every win you get closer to freedom (reach 100 fame to become free)
Good luck to you''')
name = input("what is your name Gladiator?  ")
print('''
      You are a slave forced into battle and your first fight awaits.''')
print('''As you step towards the thundering gates, 
you get offered a choice, 
your pick will stay with you for the rest of your life
(some gear gives you health, strength or maybe defense, 
these will help you survive in battle)''')
fame = 0
player = Character(name, 100, 0, 0)


stats = (f"""your health is {player.health}, 
your strength is {player.strength}, 
you have a defense of {player.shield}, 
and you have {fame} fame""")
while player.health > 0:
  
   
    choice_1 = input("Would like an axe(1) or a long sword(2)")
    while int(choice_1) != 1 and int(choice_1) != 2:
        choice_1 = input("please enter a 1 or a 2")
        if choice_1 == "1" or choice_1 == "2":
            break
    if choice_1 == "1":
        weapon_1 = "Axe"
        player.strength = int(player.strength) + 15
    if choice_1 == "2":
        weapon_1 = "Long Sword"
        player.strength = player.strength + 10
        player.shield = player.shield + 3

    health_1 = 60
    input("As you step out of the gates of rome with your new " + weapon_1 + ", you see your oponent,")
    input(f'''
    you size your self up against your oponent and relize that your bigger. 
You have {player.health} health while the man only has {health_1} health
you have {player.strength} strength but your not quite sure about the man
you also have {player.shield} defense but you also don't know the mans defense''')

    input('''The battle begins''')    
    print('''It is a rather small man who has a sharpend shiny silver sword. 
    Throughout the battle you're going to see key openings and these openings are where you need to strike.''') 
    input(f"As you clash your {weapon_1} against the man's sword, you see a couple of things you can do")

    while health_1 > 0 and player.health > 0:
        attack_1 = input("""
    you can 
(1) attempt to trade blows trying for the upper hand, you can 
(2) play it slow and out last your opponent, or 
(3) go for the a big blow 
                         """)

        while int(attack_1) != 1 and int(attack_1) != 2 and int(attack_1) != 3:
            attack_1 = input("please enter a 1, 2 or a 3")
            if attack_1 == "1" or attack_1 == "2" or attack_1 == "3":
                break
        if attack_1 == "1":
            trade_blows_1 = random.choice(["hit","miss","critical miss"])
            if trade_blows_1 == "hit":
                health_1 = health_1 - player.strength
                if health_1 > 0:
                    print(f"You get a clean hit and you have {player.health} left, your opponent has {health_1} health left")
                if health_1 <= 0:
                    print(f'''As the man swings his sword to you, you manage to side step the blow, 
retaliating with a strike of you own.  As you swing your {weapon_1} at his head, you get a clean strike
sliceing his head clean off as you win the fight and the crowd''')

            if trade_blows_1 == "miss":
                health_1 = health_1 - player.strength*0.5
                if health_1 > 0:
                    print(f"You find a small and doughtful opening that you take, coming off with a small victory.  You have {player.health} left, your opponent has {health_1} health left")
                if health_1 <= 0:
                    print(f'''As a deadly wave of attacks come, you find your self with the high ground but the small man doesn't give up
aproching you he tries to swing at your ankles jumping up you bring your {weapon_1} 
down in his head spliting it right down the midle, winning the fight and the crowd.''')
            if trade_blows_1 == "critical miss":
                player.health = player.health - 15 + player.shield
                print(f'''  You miss horribly, allowing the man to duck your attack slicing your ancle,
You have {player.health} left, your opponent has {health_1} helth left''')
        if attack_1 == "2":
            play_slow_1 = random.choice(["lose","win","win","win"])
            if play_slow_1 == "lose":
                player.health = player.health - 15 + player.shield 
                print(f'''  As you play it safe, you opponent finds an opening,
throwing a rock at you leg cousing a deep cut to form, you have {player.health} 
left while your openent has {health_1} health left''')
            else:
                health_1 = health_1 - 0.25*player.strength
                if health_1 > 0:
                    print(f"""  As you play it slow you manage to get a few small hits on your opponent.
This does little damage and your opponent is at {health_1} health while your at {player.health} health.""")
                if health_1 <= 0:
                    print(f'''  As you clash blades, you slide your {weapon_1} down the blade for the mans sword,
with a little force you mange to cut the mans hands off killing him and winning the fight and the crowd.''')

        if attack_1 == "3":
            big_blow = random.choice(["win","win","win","lose","lose","lose"])
            if big_blow == "win":
                health_1 = health_1 - player.strength*2
                if health_1 > 0:
                    print(f"""  You perform an amazing counter to the charging man, slashing him threw his chest,
although this is non lethal, it did a huge amount of damage, you have {player.health} health left
and your bleeding opponent has {health_1} health left.""")
                if health_1 <= 0:
                    print('''As the small man presses you, you see an opening on his leg, 
taking it you cut his leg off and go for the arm, sliceing it clean off, wining the battle, the day and the crowd.''')
            if big_blow == "lose":
                player.health = player.health - 20
                print(f'''As you take a wrong step forward, the man sees this before you even make your move,
stabbing you through your chest, you have {player.health} health and the man has {health_1} health left''')

    if player.health <= 0:
        break
    input('3 days later')
    fame = fame + 5
    choice_2 = input('''Through out your recoving time, you put your time to good use.
        You relized that you could (1) workout strengthing your self, (2) get a good healling meal or (3) attepmt to get a lesson from an old Gladiator''')
    while int(choice_2) != 1 and int(choice_2) != 2 and int(choice_2) != 3:
        choice_2 = input("please enter a 1, 2 or a 3")
        if choice_2 == "1" or choice_2 == "2" or choice_2 == "3":
            break            

    if choice_2 == "1":
        player.strength = player.strength + 10
        input(f'''You hit the gym, doing push ups, sit ups and bench press.  
    You now have {player.strength} strength.''')
    if choice_2 == "2":
        player.health = player.health + 50
        input(f'''You find a good meal, healling your self up.  As you enjoy your warm meal,
    you regain some health, bring yourself up to {player.health} health''')

    if choice_2 == "3":
        player.shield = player.shield + 3
        input(f'''You find an old man with a lot of gray.  He to is a slave too, as you train, he points something out
    you relize that this suggestion is meaningful.  You ask if there is anything else that the man sees,
    in return he offers a leason, you take it and relized that this will help you with your defense.
        Your new defense is {player.shield} ''')

    input(f'''As time goes on you heal your injureis, but their is something new, you hear word of a certain Gladiator
his name echos threw your camp, all anyone talkes about is a Gladiator named {name}.  Your also relized that you gained 
fame from your fight, puting you at {fame} fame.''')
    player.health = player.health + 30
    Korlox_health = 200
    Korlox_strength = 8
    input(f'''Your next fight is in one hour, as you prep and resarch for imformation on your oppenent, 
you find out you're fighting a big guy. The man's name is Korlox the big.  Korlox is 4-0 on all his fights.
As you study his past fights, you see that Korlox has {Korlox_health} health when you only have a mere {player.health} health.
The upside is that you have {player.strength} strength when Korlox only has {Korlox_strength} strength.
You have {player.shield} defense while Korlox has none.''')
          
    input('''In your next fight, you will have a different type of battle, being able to chose what strike your want to do.
Through this you will be able to have more options and the battle will be more intense.''')
    
    input('''You exit the Gates of an old beaten down arena.  Korlox stands infront of you, as you step out,
    You see Korlox is holding a long axe.  As  the battle begins you start to circle each other, neither one daring to make the fist move
    it is up to you and you see a cople things you can do''')
    while Korlox_health > 0 and player.health > 0:
        attack_2 = input('''You can 
            (1) side strike, hoping for a clean hit, 
            (2) Slice up, attempting for some damage
            (3) go for the foot, trying to trip your openent or 
            (4) go for a stab praying that you turn Korlox into a human kabob.''')
        while int(attack_2) != 1 and int(attack_2) != 2 and int(attack_2) != 3 and int(attack_2) != 4:
            attack_2 = input("please enter a 1, 2, 3 or a 4")
            if attack_2 == "1" or attack_2 == "2" or attack_2 == "3" or attack_2 == "4":
                break
        
        if attack_2 == "1":
            side_strike = random.choice(["win", "win", "lose"])
            if side_strike == "win":
                Korlox_health = Korlox_health - player.strength
                if Korlox_health > 0:
                    print(f"""You clash your {weapon_1} with Korlox's axe, you mange to slide your blade
    around Korlox's hilt slashing his arm. You have {player.health} health left and Korlox has {Korlox_health} health left.""")
                else:
                    input(f'''As Korlox swings his axe down on you, you mange to step to the side and cut the giant in half.
    with the monsters top half sliding off the his legs, you hear {name} chanting in the crowds. 
    You won the battle but more importantly you won the crowd.''')
            if side_strike == "lose":
                player.health = player.health - Korlox_strength + player.shield
                print(f"As you attack Korlox you get out played. Korlox steps to the side, causing you to miss your attack and Korlox returns a wooden hilt to the face.  This puts you down to {player.health} health")

        if attack_2 == "2":
            slice_up = random.choice(["big_win","win","lose","lose"])

            if slice_up == "big_win":
                Korlox_health = Korlox_health - 2*player.strength
                if Korlox_health > 0:
                    print(f"""As you clash the blade of your {weapon_1} against Korlox's axe, you mange to slice his knee of Korlox
    forcing him to open up which you take the opertunity to slice Korlox from his lower abbs to his chest
    forming a deep cut. Korlox has {Korlox_health} health left""")
                else:
                    print(f"""As Korlox swings his axe horizontaly at your head, you duck, sending an uppercut back with you {weapon_1}
    slicing Korlox right in half, spliting him. As his huge body slams against the sand, your hear {name} {name} {name} fill the arena""")
                    
            if slice_up == "win":
                Korlox_health = Korlox_health - player.strength*0.75
                if Korlox_health > 0:
                    print(f"""You mange to find a little opeing of Korlox's chest, swinging up, you make a small cut on his chest
                Korlox has {Korlox_health} health left and you have {player.health} health left.""")
                
                else:
                    print("""As Korlox lunges at you, you manage to side step the attack, sliceing Korlox's hands off.  
                Although this is a non lethal strike, you have one the battle. Korlox drops to the ground, defenseless. 'kill!' 'kill!' 'kill!' 
                start to fill the air. Korlox's life is in your hands.""")
                    Korlox_life = input("Do you (1) listen to the crowd or (2), spare the fighters life")
                    while int(Korlox_life) != 1 and int(Korlox_life) != 2:
                        Korlox_life = input("please enter a 1 or a 2")
                        if Korlox_life == "1" or Korlox_life == "2":
                            break

                    if Korlox_life == "1":
                        fame = fame + 10
                        ("You slice korlox's head clean off, gaining 5 fame.")
                    if Korlox_life == "2":
                        fame = fame + 10
                        ("You dify the crowd, sparing Korlox's life.  By doing this you become more liked by all giving you 10 fame")
            if slice_up == "lose":
                player.health = player.health - Korlox_strength + player.shield

                print(f"""You see an opening as you attack, you go for a leathal blow but Korlox side steps, returning a blade to the chest.
                      Korlox has {Korlox_health} health left and you have {player.health} health left.""")

        
        if attack_2 == "3":
            foot = random.choice(["sweep","miss","sweep",])
            if foot == "sweep":
                Korlox_health = Korlox_health - player.strength*0.25
                if Korlox_health > 0:
                    print(f"""You sucsessfully sweep the leg of Korlox, cousing him to fall, this is an effective way to tire out Korlox
                    this puts Korlox down to {Korlox_health} health while your at {player.health} health""")
                else:
                    print(f"As you Sweep Korlox's leg, he falls which gives you enough time throw your {weapon_1} down through Korlax's head, winning the crowd and the Fight.")

            if foot == "miss":
                player.health = player.health - Korlox_strength*1.5 +player.shield
                print(f"Korlax steps over you {weapon_1} which is swong at his leg, bashing you with his axe, you go down to {player.health} health and Korlax has {Korlox_health} health left")


        if attack_2 == "4":
            stab = random.choice(["big_win","lose","big_lose"])
            if stab == "big_win":
                Korlox_health = Korlox_health - player.strength*2
                if Korlox_health > 0:
                    print(f"""As Korlox swings down his axe, you manage to force the blade into a large stone.  
                As Korlox is tring to get his axe free, you manage to impale him with the tip of your {weapon_1}
                this puts Korlox at {Korlox_health} health while you have {player.health} health left.""")
                else:
                    print(f'''As Korlox and you exgange blows, you stab Korlox with the tip of your {weapon_1}, forcing it through Korlox you feel the tention be relived
                    Then you relized that the tip of you {weapon_1} is sticking out the back of Korlox.  You won the battle and the crowd.''')
            if stab == "lose":
                player.health = player.health - Korlox_strength + player.shield
                print(f'''You go for the stab on Korlox but your too slow, taking the side of Korlox's axe to your head.
                this puts you down to {player.health} health''')
            
            if stab == "big_lose":
                player.health = player.health - Korlox_strength*2 + player.shield
                print(f"""You're starting to get slopy, Korlox is out lasting you. Getting frustrated you go for a risky move that doesn't pay off
                With Korlox easily moving out of the way, stabing you in the arm with a non leathal blox.
                Your at {player.health} health and Korlox is at {Korlox_health} health.""")
    if player.health <= 0:
        print("You died")
        break
    fame = fame + 10
    input(f"""Your victory is widely acknowledged.  Lots of people know the name {name}. 
    You become very popular, your fame becomes {fame} as more people cheer for you""")
    input(f'''The next few days are on the chiller side, you rest eat and sleep. This lasts for about a week before you gain enough strength to train''')    
    input('''As you strength train, a man comes up to you and starts a conversation about how well you fought. 
    He says that he was a slave in his early days and knows your going to be great and he is willing to help
all he askes in return is for you to mention his name when you become great. 
    The man then brings out 2 pairs of armor and says his name is Marcus Aurelius.''')

    armor = input('''Would You like
(1), A highly armord armor set that is made of heavy metal which will help protect you
(2), A lighter chainmail armor set that will protect to a certain degree but is made to be adgile''')

    if armor != "1" and armor != "2":
        armor = input("please entar a 1 or 2")

    if armor == "1":
        player.shield = player.shield + 8
        print(f"Your armor helped your defence mayjorly puting it at {player.shield}")

    if armor == "2":
        player.shield = player.shield + 3
        player.strength = player.strength + 10
        
        print(f"You take the light wieght chainmail armor which puts you defense at {player.shield} and you relize that your stronger when you wear this armor puting you at {player.strength} strength")

    input(f'''As you get ready for your 3rd fight and your owner Antonius Proximo tells you that you and him need to talk.
He tells you that you opponent is a mean killing machine coming out of retirement and he wants blood.  His name is Tigris of Gaul.  
After long talk, Proximo tells you that he was a slave once. set free by the emporor. The pnly way to become free is to win the crowd.
Antonius Proximo tells you that he wasn't great because of his skill but he was great because the crowd loved him.''')
    import tigris   
    print(f'''As you step out of the roaring gates of the same areana you just won in, you hear both names roaring, {name}, Tigris
he comes out you size him up. ''')
    
    




















print("You DIE")
#Kaz Ideas
def print_stats(current_health,current_strength,current_shield,current_fame):
    print(f"""your health is {current_health}, 
    your strength is {current_strength}, 
    you have a defense of {current_shield}, 
    and you have {fame} fame""")