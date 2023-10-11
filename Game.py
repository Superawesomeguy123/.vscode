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
if role == "human":
    print("Congragulations, you are a human! ")
    strength = 2

print("")
#UPDATE STATS
statdec = input("Would you like to see your character stats? yes or no: ")
if statdec == "yes":
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







print("")