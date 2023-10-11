import random

#Welcome user
#Give brief description
#Ask which role they would like to play
#Display their stats
#Begin their adventure

#INTRODUCTION
print("")
print("Welcome to Space Chaos! ")
print("This is an interactive story game ")

print("")

#ROLE SELECTION
#Alien -> Stronger
#Human -> Smarter
print("Pick a role ")
role = input("human or alien? ")
if role == "alien":
    print("Congragulations, you are an alien! ")
    str = 4
    int = 3
    hth = 12
    col = 5
if role == "human":
    print("Congragulations, you are a human! ")
    str = 3
    int = 5
    hth = 10
    col = 3

print("")
#UPDATE STATS
statdec = input("Would you like to see your character stats? yes or no: ")
if statdec == "yes":
    if role == "alien":
        print("")
        print("Alien stats: ")
        print("     Strength: 4 ")
        print("     Intelligence: 3 ")
        print("     Health: 12")
        print("     Coolness: 6 (You are SO cool)")
    if role == "human":
        print("")
        print("Human stats: ")
        print("     Strength: 3 ")
        print("     Intelligence: 5 ")
        print("     Health: 10")
        print("     Coolness: 3 (You are okay I guess...)")
if statdec == "no":
    print("Lame.. I'm still gonna show you anyways. ")
    if role == "alien":
        print("")
        print("Alien stats: ")
        print("     Strength: 4 ")
        print("     Intelligence: 2 ")
        print("     Health: 5")
        print("     Coolness: 6 (You are SO cool)")
    if role == "human":
        print("")
        print("Human stats: ")
        print("     Strength: 2 ")
        print("     Intelligence: 5 ")
        print("     Health: 4")
        print("     Coolness: 3 (You are okay I guess...)")

print("")

#BEGIN ADVENTURE
adv = input("Would you like to begin your adventure: yes or no? ")
if adv == "yes":
    print("AWESOME LET'S BEGIN ")
if adv == "no":
    print("OH MY GOSH JUST COOPERATE WITH ME ")

print("")

#STORY INTRODUCTION

print("Your adventure confusingly begins with your head pounding like a drum and your face in a pool of drool. You must have forgotten. The night before you had a party in your awesome new glob house (The most popular space house made of purple putty and glow rocks. Truly makes for the most comfortable and adaptive living space on the market). You put one hand on the ground after another, and pick yourself up and off the ground. Oh man… your place is a WRECK. Firstly, I think we should fix that stomping in your noggin. Let’s head over to the medicine cabinet and take a look for some Hyperfluid.")
print("")

print("You open the globby magenta cabinet doors and look at all the funky bottles you have. “Wow these are different from the ones on my home planet” you think to yourself. You can barely see, your vision is as blurry as an emoglirp. You decide to take the chance and grab a random bottle.")
print("")
print("")

print("INTELLIGENCE TEST")
print("")
print("")

#Dice roll
print("Because you're a little weirdo.. you decide to roll some dice to make things fun!")
c1d = input("Would you like to roll a dice to see your chance at getting some Hyperfluid? To get successfully win this challenge, your roll output combined with your intelligence must be at least an 8. yes or no to roll? ")
if c1d == "yes":
    print("")
    print("")
    print("GOOD LUCK...")
    d1 = random.randint(1, 6)
    print("You rolled a.. " , d1)
    print("Your combined intelligence is " , d1 + int)
if c1d == "no":
    print("")
    print("")
    print("JUST FOR THAT I HOPE YOU GET POISONED !!! ")
    d1 = random.randint(1, 6)
    print("You rolled a.. " , d1)
    print("Your combined intelligence is " , d1 + int)

#Add the dice roll with the intelligence stat
di1 = d1 + int

print("")
print("")

#Tell player if they rolled successfully or not
if di1 > 7:
    print("Awesome job! You grabbed the Hyperfluid and squirted it into your eyes. ")
else:
    print("Ouch! Your roll was unsucessful and resulted in you pouring Florant in your eyes")
    print("")
    print("-1 Health Points")
    hth = hth - 1
    print("Health: " , hth)

#Health check
if hth == 0:
    print("You are dead please restart")
else:
    print("You live.. for now")

print("")
print("")
print("STRENGTH TEST")
print("")
print("")

print("You feel monstrously famished.  “I can eat a whole flimp flock right now!” you exclaim. You run over to the kitchen and open your vortex fridge. That’s weird. It isn’t opening. You look at the door handle and see an invistopus (invisible space octopus) holding the darn thing shut. Let’s try to fight it off.")
print("")
c2d = input("Would you like to roll a dice to see your chance at fighting off the invistopus? To get successfully win this challenge, your roll output combined with your strength must be at least an 8. yes or no to roll? ")
if c2d == "yes":
    print("")
    print("")
    print("GOOD LUCK...")
    d2 = random.randint(1, 6)
    print("You rolled a.. " , d2)
    print("Your combined strength is " , d2 + str)
if c2d == "no":
    print("")
    print("")
    print("JUST FOR THAT I HOPE YOU LOSE !!! ")
    d2 = random.randint(1, 6)
    print("You rolled a.. " , d2)
    print("Your combined strength is " , d2 + str)

#Add the dice roll with the intelligence stat
di2 = d2 + str

print("")
print("")

#Tell player if they rolled successfully or not
if di2 > 7:
    print("Awesome job! You fought off the invistopus. ")
else:
    io = input("Ouch! Your roll was unsucessful and resulted in you getting bit. Would you like to roll for damage taken? yes or no: ")
    if io == "yes":
        print("")
        print("")
        print("GOOD LUCK...")
        d2a = random.randint(1, 4)
        print("You rolled a.. " , d2a)
        print("")
        print("-1 Health Points")
        hth = hth - d2a
        print("Health: " , hth)
    if io == "no":
        print("")
        print("")
        print("JUST FOR THAT I HOPE IT BITES YOUR FACE OFF !!! ")
        d2a = random.randint(1, 4)
        print("You rolled a.. " , d2a)
        print("")
        print("-1 Health Points")
        hth = hth - d2a
        print("Health: " , hth)

#Health check
if hth == 0:
    print("You are dead please restart")
else:
    print("You live again!")

#STAT BUFF

print("Alright now that that’s done.. You should get dressed before we go outside and beg people to help clean our house. You take your soft round blirp disc stairs up. The floating stair disc technology is definitely your favorite part of the house. Once upstairs, you head to your room. Through the door you enter your room and ask your robot for an awesome outfit.")
print("")

c3d = input("Would you like to roll to see if your robot butler gives you a nice outfit? yes or no: ")
if c3d == "yes":
    print("")
    print("")
    print("GOOD LUCK...")
    d3 = random.randint(1, 6)
    print("You rolled a.. " , d3)
    print("WIcked, your coolness is increased by, +" , d3)
    print("Your coolness is now a whopping " , d3 + col)
    cool = d3 + col
if c3d == "no":
    print("")
    print("")
    print("YOU CANNOT GO OUTSIDE NAKED !!! ")
    d3 = random.randint(1, 6)
    print("You rolled a.. " , d3)
    print("WIcked, your coolness is increased by, +" , d3)
    print("Your coolness is now a whopping " , d3 + col)
    cool = d3 + col

print("")
print("")
#CLEAN yOUR HOUSE

print("Now that you are fully equipped with what your robot assistant has picked out for you. You head for the world. Not to tackle the world, your house is still in shambles. Your current task is to find some people and persuade them into aiding you in cleaning your house")
c4d = input("You see three yamps, should you ask them? yes or no: ")
print("Roll for persuasion !!! ")
if c4d == "yes":
    print("")
    print("")
    print("GOOD LUCK...")
    d4 = random.randint(1, 6)
    print("You rolled a.. " , d4)
    print("Your coolness is now a whopping " , d4 + cool)
    coool = d4 + cool
if c4d == "no":
    print("")
    print("")
    print("I HOPE THEY JUMP YOU...")
    d4 = random.randint(1, 6)
    print("You rolled a.. " , d4)
    print("Your coolness is now a whopping " , d4 + cool)
    coool = d4 + cool

if coool > 10:
    print("They listened to you! They followed you home.. AND YOU MURDERED THEM MUAHAHHAHAHHA. No just kidding, they helped you clean the house and in turn you decide to party with them. Oh no.. You start drinking some crimflax.. Parties over and you're laying on the floor with your face in a pool of drool")
    print("")
    print("THIS")
    print("FEELS")
    print("FAMILIAR")
else:
    print("Whoops now they're jumping you")
    for i in range(3):
        ii = input("They each take turns hitting you. Would you like to roll for damage taken? yes or no: ")
        if ii == "yes":
            print("")
            print("")
            print("GOOD LUCK...")
            d2a = random.randint(1, 3)
            print("You rolled a.. " , d2a)
            print("")
            print("-1 Health Points")
            hth = hth - d2a
            print("Health: " , hth)
        if ii == "no":
            print("")
            print("")
            print("YOU'LL DIE FOR THAT !!! ")
            d2a = random.randint(1, 3)
            print("You rolled a.. " , d2a)
            print("")
            print("-1 Health Points")
            hth = hth - d2a
            print("Health: " , hth)
if hth < 1:
    print("Loser, please restart")


print("")