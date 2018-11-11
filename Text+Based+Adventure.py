#Dominic, Kaleb, Jessica, Ethan
#Introduction
def intro():
    name = input("Enter your name")

    #Story
    print("""You have recently bought a house in Deadman’s Landing, Florida. The home was very
cheap and let’s face it, you’re broke. This is your first time seeing and visiting the house. As you
drive up you see your new estate, a broken down, brown colored building. You try to open the
front door but it won’t budge so you throw yourself against it. The door finally bursts open and
the smell burns your nostrils. You hesitate to walk in but eventually you find the strength to get
past the smell. As you walk in, you close the door behind you but as soon as it closes, you hear
several clicks. You turn around and find the door locked. The door won’t budge but there are
four keyholes that may unlock the door. Now it’s just a matter of finding the keys.""")
    frontRoom()

#Front Room is described and the player is given options
def frontRoom():
    option = input("""As you look around you find yourself in the front room. There’s a rug, couch, TV,
bookcase, and a main window in the room. While the house itself looked nasty, the furniture
looks to be in decent shape. Do you

1) Look under the rug
2) Try to berak the front room window
3) Check the bookcase
4) Turn on the TV
5) Go to kitchen
6) Go up some stairs

""")

    if option == "1":
        print("""All you find under the rug is dust and dirt.""")
        frontRoom()
    
    elif option == "2":
        print("""You pick up a chair and throw it at the window. It bounces back and falls to the floor.
                 The window didn't even crack.""")
        frontRoom()
    
    elif option == "3":
        bookcase()

    elif option == "4":
        print("""You try to turn on the TV but as soon as the screen starts to flicker on, you hear a loud burst
                 and the TV flickers off again.""")
        frontRoom()

    elif option == "5":
        print("""You go to the kitchen.""")
        kitchen()

    elif option == "6":
        print("""You go up the stairs.""")
        attic1()

    else:
        frontRoom()

#Kitchen is described and the player is given options
def kitchen():
    option = input("""The kitchen has a dining table, fridge, stove, window, and plates strewn all of the place.
You notice a closet close to a descending staircase. Do you

1) Open the fridge
2) Throw some plates
3) Turn on the stove
4) Try to break the kitchen window
5) Go down some stairs
6) Go back to the front room

""")

    if option == "1":
        print("""You open the fridge and the worst smell imaginable imgerges from it. There's obviously some rotten
                 meat in the fridge.""")
        kitchen()
    
    elif option == "2":
        print("""You throw a plate to the floor and it shatters. Then you feel two hands on your back and you're pushed
                 to the floor. You turn around and see nothing. You wonder what pushed you.""")
        kitchen()
    
    elif option == "3":
        print("""You turn on the stove and a huge flame bursts in front of your face. You back away quicly but you're
                 pretty sure you burned off some hair.""")
        kitchen()

    elif option == "4":
        print("""You pick up a chair and throw it at the kitchen window. It rebounds and hits you, throwing you to the floor.
                 Maybe you shouldn't try to break windows.""")
        kitchen()

    elif option == "5":
        print("""You go down the stairs.""")
        basement()

    elif option == "6":
        print("You go back to the front room")
        frontRoom()

    else:
        kitchen()

#Closet is described and the player is given options
def closet():
    option = input("""You walk over to the closet door. You hear some scratching inside and you can’t decide
whether you want to open the door or not. You fear what might be inside. Do you

1) Open the door
2) Open the door and step aside
3) Go to kitchen

""")
    count=0
    
    while count != 2:
        if option == "1":
            option2 = input("""You open the door and look inside the closet. You see a bunch of jackets and a diry floor
                     Do you

                     1) Check the jacket pockets
                     2) Look at the dirty floor

                     """)
            
            #Player is given options for inside the closet
            if option2 == "1":
                print("You found a key! Good job.")
                count+=1
                

            elif option2 == "2":
                print("You just find dirty and dust.")
                count+=1
                

        elif option == "2":
            print("""You open the door and step aside. The floor cracks and falls apart underneath you.
                     You fall down and find yourself in the basement.""")
            basement()

        elif option == "3":
            print("You went back to the kitchen")
            kitchen()

        else:
            closet()

#Bookcase is described and options are given to the player
def bookcase(name):
    option = input("""You find a secret lever and the bookcase pops opens. You look behind it and find a secret
room. There are newspaper clippings, tools, a diary, and a trophy case in the room. Do you

1) Check the newspaper clippings
2) Look at the tools
3) Read the diary
4) Look in the trophy case
5) Go back to the front room

""")
    
    if option == "1":
        print("""As you read the newspaper clippings, you soon find out that a serial killer used to live in the house.
                 Several murders had been committed around the city but he was eventually sentenced to death.""")
        bookcase()
    
    elif option == "2":
        print("""The tools sit on a table. There are several different types of knives that are all stained and rusted.""")
        bookcase()
    
    elif option == "3":
        print("""The diary reads as follows: I think the police have figured it out. The house is surrounded and I'm stuck
                 inside. As long as they don't find my trophies, they can't sentence me. They don't have any evidence.

                 Another sections reads as follows: Well they caught me and it looks like I'm gonna go to death row. I
                 you enjoy my house.

                 You immediately close the book and put it down.""")
        bookcase()

    elif option == "4":
        print("""As you look into the trophy case, you find several different rings. You wonder why there are so many rings
                 and where they came from.""")
        bookcase()

    elif option == "5":
        print("You go back to the front room")
        frontRoom()

    else:
        bookcase()

#Front door is described and the player is given options
def frontDoor():
    option = input("""You look at the front door. The four keyholes are still there. Do you

1) Insert a key
2) Try to open the door
3) Go back to the front room

""")

    if option == "1":
        print("""""")
        frontDoor()

    elif option == "2":
        print("""""")
        frontDoor()

    elif option == "3"
        print("You go back to the front room")
        frontRoom()

    else:
        frontDoor()


#Kaleb,Dom,Jessica,Ethan
#10-22-#10-12-18
import random
import sys
playerhealth = 100
monsterhealth= 100
playing = True
demonalive = True
def attic1():
      print("Welcome to the attic, it looks archaic, cobwebs over old storage")
      print("the attic is long and wide with a aduct system in the left corner and")
      print("what apperas to be 3 rooms, a small closet like room in the back right") 
      print("a louge wide like room to relax and a room that is giving off a dim light") 
      print("the room with the dim light make you feel uncomfrontable, like there's an ancient evil upon this room")
      print()
      print()
      print()
      print()
      choice = input("1)go attic entrance 2) go to the small closet 3) go to the louge 4) The room with the creepy dim light")
      print()
      print()
      if choice == "1":
            attic1()
      elif choice == "2":
            attic2()
      elif choice == "3":
            attic3()
      else:
            attic1()

def attic2():
      print("You walk over to the small closet")
      print("You open the door and there is some supplies around a letter and what looks like old blood. ouch")
      print("You read the letter and it reads. Watch out for the demon Krvak you never know where he will come from.Grab the liquid,summon the sword conquer him and send him back to his realm.")
      print("We were fools to think he would help, good luck")
      print("You proceed to pick up a candle of some kind and a symbol")
      print("You grab the liquid")
      print()
      print()
      print()
      print()
      choice = input("1)go attic entrance 2) go to the small closet 3) go to the louge 4) The room with the creepy dim light")
      print()
      print()
      if choice == "1":
            attic1()
      elif choice == "2":
            attic2()
      elif choice == "3":
            attic3()
      else:
            attic2()
            
def attic3():
      print("The louge looks comfrontable a few couches a table in the middle a good place to relax")
      print("You walk around and find that the dust as a pattern, like somone or something has been moving around")
      print("You find a mannuel, you pick it up for safe keeping")
      print("You look at this old chest in the corner, you open it and find a key that has a number 4 on it you grab it. could't hurt")
      print("You walk around the corner of the room in a little gap barly visible and find a hole in the wall, its exposing the outside workd. FREEDOM!! But as you go to leave, you cant go out the hole you just run into it like its a wall")
      print("All the sudden the hole turns dark no longer showing the outside world. And words show above the hole saying,only the light can open up the dark")
      print()
      print()
      print()
      print()
      choice = input("1)go attic entrance 2) go to the small closet 3) go to the louge 4) The room with the creepy dim light")
      print()
      print()
      if choice == "1":
            attic2()
      elif choice == "2":
            attic2()
      elif choice == "3":
            attic4(playerhealth,monsterhealth)
      else:
            attic3()
            
def attic4(playerhealth,monsterhealth):
      global demonalive
      print("You come into the room with that light. It's a blood sacrifice. there are carcasses in the coner")
      print("Acient and horrifying symbols are carved in blood illuminated by candles")
      print("You see there is a missing piece to the sacrifice table looks like you need a special candle stand with a symbol of some kind")
      print("You are stone cold all of the sudden, you feel a dark overwhelming presence")
      print("You ignore the feeling and proceed to look around.at the table is a knife that reads agrypnía tou fos")
      print("You grab the knife")
      print()
      print()
      print()
      print()
      choice = input("1)go attic entrance 2) go to the small closet 3) go to the louge 4) The room with the creepy dim light")
      print()
      print()
      demonchance = random.randrange(0,10)
      if demonchance == 9 and demonalive == True:
            fight(playerhealth,monsterhealth)
      if playerhealth > 0:
                  
            if choice == "1":
                  attic3()
            elif choice == "2":
                  attic2()
            elif choice == "3":
                  attic3()
            else:
                  attic4(playerhealth,monsterhealth)
      else:
            print("game over")
            playing = False

def attic5():
      print("walk back down stairs")
      print()
      print()
      print()
      print()
      choice = input("1)go attic entrance 2) go to the small closet 3) go to the louge 4) The room with the creepy dim light")
      print()
      print()
      if choice == "1":
                  attic4(playerhealth,monsterhealth)
      elif choice == "2":
                  attic2()
      elif choice =="3":
                  attic3()
      else:
                  attic5()

def fight(playerhealth, monsterhealth):
      print("Fight scinero")
      choice = input("Fight or flee")
      if choice== "fight":
            fightdamage(playerhealth, monsterhealth)
      elif choice == "flee":
            die()
      
def fightdamage(playerhealth, monsterhealth):
      playerhealth = playerhealth
      monsterhealth= monsterhealth
      loop = 1
      choice =""
      while loop ==1:
            playerdamage=random.randrange(0,101)
            monsterdamage= random.randrange(50,100)
            if playerhealth > 0 and monsterhealth >0:
                  print("You throw the agrypnía tou fos at Krvak the demon")
                  monsterhealth-=playerdamage
                  if monsterhealth >0: 
                        print("Krvak lunges at you strikng you")
                        playerhealth-=monsterdamage
                        choice = input("ask question")
            if choice == "fight" and monsterhealth >0:
                  loop =1
            elif choice == "flee":
                  loop=0
                  die()
            
                        
            if playerhealth >0 and monsterhealth <0:
                  win()
                  loop = 0
            elif monsterhealth >0 and playerhealth <0:
                  die()
                  loop = 0

def die():
      global playing
      print("You have died")
      sys.exit(1)
      
def win():
      global deomonalive
      print("You vanquished the demon. He screetches out with a horricfic noise,then disapates leaving a shroud of light.")
      print("As you get closer to the shroud of light it turns into a key of light. I wonder if it unlocks a warding or curse")
      print("Maybe that's why you could not go through the hole!")
      demonalive = False






#Jessica's Code
choice = input("")
def basement():
    print("""The room around was dimly lit by a lamp in the corner. You could see the stairs leading up, the lamp, a desk with some items on it, and 3 rooms with the number 1, 2, and 3 on them.
              Number 1 was wide open. Door number 2 was closed and 3 was slightly cracked.""")

    choice = input(" ")

    if "1" in choice:
        room_2()
        
    elif "2" in choice:
        room_3()

    elif "3" in choice:
        room_4()
        
    elif "desk" in choice:
        print("Upon the desk you see an open drawer and some paper. Do you look at the paper or the drawer?")
        choice = input("")

    if "paper" in choice:
        print("You look at the paper. Your face has mixed reactions of what you've stared at. But you don't understand what it means, ‘Find 4 cardboard boxes and you may find the key.’")

    elif "drawer" in choice:
        print("You see in the drawer, you have a flashlight and a hammer. Do you take the flashlight or hammer, or both?")
        choice = input("")

    if "flashlight" in choice:
        print ("congrats you have some light.")

    elif "hammer" in choice:
       print ("Congrats, you can now repair things. Or maybe destroy things…")

    elif "both" in choice:
        print("You've found a hammer and a flashlight. Congrats, they may provide use on this journey.")

    elif "stairs" in choice:
        print("You've gone upstairs to the first floor.")
        frontRoom()

    else:
        basement()

def room_2():
    print("The room you enter looked similar to the one before having a similar layout. This room had a bed against a window with bars on it, a rug in the middle of the floor, and a closet in the corner.")

    choice = input(" ");

    if "bed" in choice:
        print("You haven't found anything useful, it's just a plain bed in the middle of a plain room.")
    elif "rug" in choice:
        print("Do you want to move rug? (Yes or No)")
        choice = input("")

    if "Yes" in choice:
        print("You've found a cardboard box. You can't open it yet. Keep looking.")

    elif "No" in choice:
        room_2()

    elif "closet" in choice:
        print("You found a boring closet, there isnt anything in here. Turn around and try again.")
        room_2()
              
    else:
        print("Did you want to go back to main room?")
        choice = input("")

    if "yes" in choice:
        basement()

    if "no" in choice:
        room_2()

def room_3():
    print("You open the door and this room looks quite different from the rest. There’s nothing in here, just 4 walls. But there’s a little sag in the wall. Do you take the hammer to that section of the wall? Yes or no.")

    choice = input("")

    if "yes" in choice:
        print("You destoryes the wall. Revealing a small hole. There happens to be a cardboard box in there. You can't open it yet. Keep looking")

    elif "no" in choice:
        print ("You came in here for nothing")
        room_3()
              
    else: 
        print("Did you want to go back to main room?")
        choice = input("")

    if "yes" in choice:
        basement()

    if "no" in choice:
        room_3()

def room_4():
    print ("You open 3 to find nothing but a piece of carpet in the center of the room. Do you move it? Yes or no.")
    choice = input("")
              
    if "yes" in choice:
        print("You move the carpet to find a hole  in the floor. Your presented with 4 cardboard boxes in the middle of the floor. Which one do you choose? (1,2,3,4).")
        choice = input("")

    if "1" in choice:
        print("Try Again. The key seems to not be in here.")

    elif "2" in  choice:
        print (" The boxes have randomly been shuffled as you dropped them. You were wrong yet again.")

    elif "3" in choice:
        print("As you open the box you dread yet again failing and being stuck in this house any longer. You see something glinting at the bottom, but it must of been your imagination as there is nothing here. Try again.")

    elif "4" in choice:
        print("Just as you think you down. You haven't found the key yet, but there at the bottom is your hope. There lies the golden key.")

    else:
        print ("Try again, you were not successful in typing something I understood.")
        room_4()

    if "no" in choice:
        print ("Your choice doesn’t make sense to me, but I’ll accept it.")
        room_4()

    else: 
        print("Did you want to go back to main room")
        choice = input("")

    if "yes" in choice:
        basement()

    if "no" in choice:
        room_4()

# START
intro()
