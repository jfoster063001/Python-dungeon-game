import time  # this is to create the text come out line by line to make it easier to read

inventory = []
inventory2 = []
kitchen_item = ['Plumbus']
mortys_room_item = ['Mega seeds']  # This is all the rooms items to be able to add them to
ricks_garage_item = ['Shrink ray']  # the inventory lists that are empty
anatomy_park_item = ['Note with lair location']
summers_room_item = ['Purge suit']
dining_room_item = ['Laser gun']
underground_lab_item = ['Portal gun']


def main():
    # infinite loop to control program flow
    while True:

        def check_inventory():  # this function just prints out the inventories
            time.sleep(2)
            print(inventory + inventory2)

        def living_room():  # this function is the basic outline for each room
            print('\nYou are in the Living Room\n'  # this is the prompt for the player
                  'What do you wanna do?\n')
            time.sleep(2)
            living_room_choice = input(
                'Go North\nGo South\nGo West\nShow inventory\n')  # these are their options to choose from

            if 'Go South' and 'go south' in living_room_choice:  # this is the move statements calling to a different function
                mortys_room()  # that will be the room they move to

            elif 'Go North' and 'go north' in living_room_choice:
                dining_room()

            elif 'Go West' and 'go west' in living_room_choice:
                kitchen()

            elif 'Show Inventory' and 'show inventory' in living_room_choice:  # this shows the inventory and then
                check_inventory()  # calls back to that specific room
                living_room()
            elif 'exit' in living_room_choice.lower():
                print("Oh... you don't wanna keep playing??")
                time.sleep(2)
                print("That's cool I guess broh, well")
                print('Thanks for Playing!')
            else:
                print("Rick makes you pass out because you don't know how to spell")
                time.sleep(2)  # this else statement brings them back to the living room
                print(
                    'you wake up and realize\n')  # as a punishment for spelling a word wrong as a way to make the game harder
                time.sleep(2)  # I could reroute it back to the same room and say invalid input but
                living_room()  # I think this way is more fun

        def ricks_garage():
            print('\nYou are in Ricks Garage\n'
                  'What do you wanna do?\n')
            time.sleep(2)
            if 'Shrink ray' not in inventory:  # this and the next statement checks the inventory to see if the room item is in there
                ricks_garage_choice = input(
                    'Go East\nGrab Shrink ray\nShow inventory\n')  # if it is, the prompt is different from
            elif 'Shrink ray' in inventory:  # if it isn't
                ricks_garage_choice = input('Go East\nShrink\nShow Inventory\n')
            if 'Go East' and 'go east' in ricks_garage_choice:
                kitchen()
            elif 'Show Inventory' and 'show inventory' in ricks_garage_choice:
                check_inventory()
                ricks_garage()
            elif 'Shrink' and 'shrink' == ricks_garage_choice:
                anatomy_park()
            elif 'Grab Shrink Ray' and 'grab shrink ray' in ricks_garage_choice:  # this is the grab function that adds the item
                inventory.append('Shrink ray')  # to the inventory and takes out the item from
                ricks_garage_item.remove('Shrink ray')  # the room inventory
                ricks_garage()
            elif 'exit' in ricks_garage_choice.lower():
                print("Oh... you don't wanna keep playing??")
                time.sleep(2)
                print("That's cool I guess broh, well")
                print('Thanks for Playing!')
            else:
                print("Rick makes you pass out because you don't know how to spell")
                time.sleep(2)
                print('you wake up and realize\n')
                time.sleep(2)
                living_room()

        def kitchen():
            print('\nYou are in the Kitchen\n'
                  'What do you wanna do?\n')
            time.sleep(2)
            if 'Plumbus' not in inventory:
                kitchen_choice = input('Go East\nGo West\nGrab Plumbus\nShow inventory\n')
            elif 'Plumbus' in inventory:
                kitchen_choice = input('Go East\nGo West\nShow inventory\n')
            if 'Go East' and 'go east' in kitchen_choice:
                living_room()
            elif 'Go West' and 'go west' in kitchen_choice:
                ricks_garage()
            elif 'Grab Plumbus' and 'grab plumbus' in kitchen_choice:
                inventory.append('Plumbus')
                kitchen_item.remove('Plumbus')
                kitchen()
            elif 'Show Inventory' and 'show inventory' in kitchen_choice:
                check_inventory()
                kitchen()
            elif 'exit' in kitchen_choice.lower():
                print("Oh... you don't wanna keep playing??")
                time.sleep(2)
                print("That's cool I guess broh, well")
                print('Thanks for Playing!')
            else:
                print('Rick makes you pass out because you cant spell')
                time.sleep(2)
                print('you wake up and realize\n')
                time.sleep(2)
                living_room()

        def mortys_room():
            print('\nYou are in Mortys room\n'
                  'What do you wanna do?\n')
            time.sleep(2)
            if 'Mega seeds' not in inventory:
                mortys_room_choice = input('Go North\nGrab Mega seeds\nShow inventory\n')
            elif 'Mega seeds' in inventory:
                mortys_room_choice = input('Go North\nShow inventory\n')
            if 'Go North' and 'go north' in mortys_room_choice:
                living_room()
            elif 'Grab Mega seeds' and 'grab mega seeds' in mortys_room_choice:
                inventory.append('Mega seeds')
                mortys_room_item.remove('Mega seeds')
                mortys_room()
            elif 'Show Inventory' and 'show inventory' in mortys_room_choice:
                check_inventory()
                mortys_room()
            elif 'exit' in mortys_room_choice.lower():
                print("Oh... you don't wanna keep playing??")
                time.sleep(2)
                print("That's cool I guess broh, well")
                print('Thanks for Playing!')
            else:
                print('Rick makes you pass out because you cant spell')
                time.sleep(2)
                print('you wake up and realize\n')
                time.sleep(2)
                living_room()

        def dining_room():
            print('\nYou are in the Dining room\n'
                  'What do you wanna do?\n')
            time.sleep(2)
            if 'Laser gun' not in inventory:
                dining_room_choice = input('Go East\nGo North\nGo South\nGrab Laser gun\nShow inventory\n')
            elif 'Laser gun' in inventory:
                dining_room_choice = input('Go East\nGo North\nGo South\nShow Inventory\n')
            if 'Go East' and 'go east' in dining_room_choice:
                underground_lab()
            elif 'Go South' and 'go south' in dining_room_choice:
                living_room()
            elif 'Go North' and 'go north' in dining_room_choice:
                summers_room()
            elif 'Show Inventory' and 'show inventory' in dining_room_choice:
                check_inventory()
                dining_room()
            elif 'Grab Laser gun' and 'grab laser gun' in dining_room_choice:
                inventory.append('Laser gun')
                dining_room_item.remove('Laser gun')
                dining_room()
            elif 'exit' in dining_room_choice.lower():
                print("Oh... you don't wanna keep playing??")
                time.sleep(2)
                print("That's cool I guess broh, well")
                print('Thanks for Playing!')
            else:
                print("Rick makes you pass out because you don't know how to spell")
                time.sleep(2)
                print('you wake up and realize\n')
                time.sleep(2)
                living_room()

        def anatomy_park():
            print('\nWelcome to Anatomy Park\n'
                  'What do you wanna do?\n')
            time.sleep(2)
            if 'Note with lair location' not in inventory:
                anatomy_park_choice = input('Unshrink\nGrab Note with lair location\nShow inventory\n')
            elif 'Note with lair location' in inventory:
                anatomy_park_choice = input('Unshrink\nShow inventory\n')
            if 'Unshrink' and 'unshrink' in anatomy_park_choice:
                ricks_garage()
            elif 'Grab Note with lair location' and 'grab note with lair location' in anatomy_park_choice:
                inventory.append('Note with lair location')
                anatomy_park_item.remove('Note with lair location')
                anatomy_park()
            elif 'Show Inventory' and 'show inventory' in anatomy_park_choice:
                check_inventory()
                anatomy_park()
            elif 'exit' in anatomy_park_choice.lower():
                print("Oh... you don't wanna keep playing??")
                time.sleep(2)
                print("That's cool I guess broh, well")
                print('Thanks for Playing!')
            else:
                print('Rick makes you pass out because you cant spell')
                time.sleep(2)
                print('you wake up and realize\n')
                time.sleep(2)
                living_room()

        def summers_room():
            print('\nYou are in Summers room\n'
                  'What do you wanna do?\n')
            time.sleep(2)
            if 'Purge suit' not in inventory:
                summers_room_choice = input('Go South\nGrab Purge suit\nShow inventory\n')
            elif 'Purge suit' in inventory:
                summers_room_choice = input('Go South\nShow inventory\n')
            if 'Go South' and 'go south' in summers_room_choice:
                dining_room()
            elif 'Grab Purge suit' and 'grab purge suit' in summers_room_choice:
                inventory.append('Purge suit')
                summers_room_item.remove('Purge suit')
                summers_room()
            elif 'Show Inventory' and 'show inventory' in summers_room_choice:
                check_inventory()
                summers_room()
            elif 'exit' in summers_room_choice.lower():
                print("Oh... you don't wanna keep playing??")
                time.sleep(2)
                print("That's cool I guess broh, well")
                print('Thanks for Playing!')
            else:
                print('Rick makes you pass out because you cant spell')
                time.sleep(2)
                print('you wake up and realize\n')
                time.sleep(2)
                living_room()

        def underground_lab():
            print('\nYou are in the Underground lab\n'
                  'What do you wanna do?\n')
            time.sleep(2)

            if 'Portal gun' not in inventory2:
                underground_lab_choice = input('Go West\nGrab Portal Gun\nShow inventory\n')
            elif 'Portal gun' in inventory2:
                underground_lab_choice = input('Set Portal to lair\nGo West\nShow inventory\n')
            if 'Set Portal to lair' and 'set portal to lair' in underground_lab_choice:
                if len(inventory + inventory2) == 7:
                    mortys_evil_lair()
                else:
                    print('Nah man you are not ready for this get all of the items first')
                    underground_lab()
                print('You need to have all the items to go there, Are you sure?\n')
                time.sleep(2)
            elif 'Go West' and 'go west' in underground_lab_choice:
                dining_room()
            elif 'Grab Portal gun' and 'grab portal gun' in underground_lab_choice:
                inventory2.append('Portal gun')
                underground_lab_item.remove('Portal gun')
                underground_lab()
            elif 'Show Inventory' and 'show inventory' in underground_lab_choice:
                check_inventory()
                underground_lab()
            elif 'exit' in underground_lab_choice.lower():
                print("Oh... you don't wanna keep playing??")
                time.sleep(2)
                print("That's cool I guess broh, well")
                print('Thanks for Playing!')
            else:
                print('Rick makes you pass out because you cant spell')
                time.sleep(2)
                print('You wake up and realize\n')
                time.sleep(2)
                living_room()

        def mortys_evil_lair():  # this is the final sequence of the game basically winning
            print('You are in Evil Mortys Lair\n'
                  'You see Morty next to you he says\n')
            time.sleep(2)
            print('Its about time bro!\n'
                  'Where have you been?\n'
                  "Never mind that doesn't matter right now.\n")
            time.sleep(5)
            print('Help me defeat Evil Morty\n'
                  'You look over and see Evil Morty\n'
                  '\n'
                  '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@\n'
                  '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(@@@@@@@@@@@@@@@@@@@@@@@@@\n'
                  '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*@@@@@@@@@@@@@@@@@@@@@@@@@\n'
                  '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(&@@@@@@@@@@@@@@@@@@@@@@@@\n'
                  '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(#@@@@@@@@@@@@@@@@@@@@@@@@\n'
                  '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@(/@@@@@@@@@@@@@@@@@@@@@@@@\n'
                  '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@@%/,@@@@@@@#@@@@@@@@@@@@@@@@\n'
                  '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@@#/,@@@@@@@*@@@@@@@@@@@@@@@@\n'
                  '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%(@@@@@@//,&@@@@@@,@@@@@@@@@@@@@@@@\n'
                  '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@((@@@@@@*/,(@@@@@@,&@@@@@@@@@@@@@@@\n'
                  '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*(@@@@@@,/,/@@@@@@,/@@@@@@@@@@@@@@@\n'
                  '######################################################################%,(#####&,*,,#####&,*###############\n'
                  '######################################################################%,/#####%,*,,%####&*,&##############\n'
                  '######################################################################(,/######,**,%####%*,###############\n'
                  '######################################################################*,/#####(,**,(####%*,*##############\n'
                  '#####################################################################,,,(######&#&&#####%#,,,(############\n'
                  '##################################################################(*,**&#####%*@%#@#%#####@**,,*##########\n'
                  '########################################%%(,,*,,,,*#&%########&@/%*/#(,,,,,,,%@####@&,,,,,,*#(*/##&#######\n'
                  '####################################&,,*,,,,,,,,,,,,,,,,,*%#######@@/#&@&*##,,*@&%@*,,##*&@##(@###########\n'
                  '##################################/**,,,,,,,,,,,,,,,,,,,,,,,%##############%@@#%(&#(@&####################\n'
                  '################################%,,,,,,,,*/###(/*/#%%(#%,,,**,&########&&(,,,,**,*,**,,,&@################\n'
                  '###############################(,,,,,&,,,,,,,,,,,,,,,,,,,*(*,,%&###########&&,**,*,*,&####################\n'
                  '##############################@#,,,%,,,,,,,,,,,,,,,,,,,,,,,,#&@%#######%&&&&%@,*,***%%&&&&%###############\n'
                  '###############################@&**,,,,,,,,,,,,,,,,,,,,,,,,#@&*&##########&@/,,*,****#%###################\n'
                  '###############################,(@@/,,,,,,,,,,,,,,,,,,,,(@@(*,%,&############@,/,*#*######################\n'
                  '##############################*,/,**(@@@@@@@@@@@*,,(@@@@,,,&(,%,*#############@/,*(%######################\n'
                  '##############################(,/,,,&@@@@@@@@@@@@%,#,,*&%,,,,%%&###############***(#######################\n'
                  '################################%%,,*@@@@@@@@@@@@*,**,,,,,,,,/%##############%%,//,&######################\n'
                  '##############################%**,%,,*@@@@@@@@@(,,,(,&*,,,*%,%,&###############%,,%#######################\n'
                  '##############################/,,,((*,,,,*/*,*,,*%,/*,,,,,,,(,,&###############&##%#######################\n'
                  '##############################*%,,,,,/%*,,,*#(*,,*,,,,,,,*#,*%*&###############&,,%#######################\n'
                  '#############################%,*,,#*,,,,,*&*,,,*,,,*,#%%*,*/,,/################&,,%#######################\n'
                  '##########################%#,,,,,,*%#**&*,*,,#**,,,*&*,**,,#/,,,###############&,,%#######################\n'
                  '#########################,,,,,,,,,,,,*,,(#,/#,,/*,%,*/,#*,,*#%(%&##############&,,%#######################\n'
                  '######################%,,,,((,&,,,*,,,(&/,*,/#,&&&(,%,,&*,,,,*&,###############&,,%#######################\n'
                  '#####################/*,(*,,,%,,,,,,*%,,,,,,(((%**%%&,,*&,,,,*#(&##############&,,%#######################\n'
                  '###################%*,,/,,,%*#,&(,,#,%,,,,,,,,&/%(&#,,,,**%*&,,,,,&###########&&,,@%######################\n'
                  '##################&,,#,*,,#%*/%%*#,,,#,,,,,,,,,,@%,,,,,,,,,,,*@,,**#*/%*,,,/%,(,(,,,%#####################\n'
                  '#################&,*%,,,#,,,%,,%,,,,,#,,,,,,,,,,,,,,,,,*,,,,,*##&**,,,(,,,,,(,*#*/*#&#####################\n'
                  '################&,,#*,#*&%*,,(*,,,,,*(,,,,,,,,,,,,,,,,,,,,,*,%######%&@,,,,,#/,(%%%%######################\n'
                  '###############%,,#,,*(%#/%&#*,,,,,,**,,,,,,,,,,,,,,,,,,,,,,###################&,*&#######################\n'
                  '##############/*,(,,,,#,(**/%*,,,,,,*,,,,,,,,,,,,,,,,,,,*,,/###################%,,%#######################\n'
                  '############%*/(*,,,,,(,/,*,%,,,,,,,/,,,,,,,,,,,,,,,,,,,*,*/###################%,,%#######################\n'
                  '##########%,/***,,,,,,/*/,,,%,,,,,,,(,,,,,,,,,,,,,,,,,,,/**####################%,,%#######################\n'
                  '########&,,&,,,,,,,,,,,//*,,%,,,,,,,%,,,,,,,,,,,,,,,,,,*(,%####################&,,%#######################\n'
                  '######&,#*,,,,,,,,,,,,*(/&&%#*,,,,,,%,,,,,,,,,,,,,,,,,,*#,&####################&,,%#######################\n'
                  '####/,&*,*,,,,,,,,,,,,,(/%%#/*,,,,,,%,,,,,,,,,,,,,,,,,,,&*#####################&,,%#######################\n'
                  '#&,%*,,*,,,,,,,,,,,,,,*#(%*(///%,,,**/&*,*,,,,,,,,,,*,*&/%#####################&,,%#######################\n'
                  '%,*,,,,,,,,,,,,,,,,,,,,(,#*,,((*,,,,(,,,,,,,*,,,,,*,,,,*@######################&,,%#######################\n'
                  '*,,,,,,,,,,,,,,,,,,,,,,,%&%(&&/,,,,,&,,,,,,,#%&%&(,,,,,,#######################&,,%#######################\n'
                  '*,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,#,,,,,,*(*,,,*,,,,,,,######################&,,%#######################\n'
                  '*,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,*(,,,,,,%,,,,,@,,,,,,*%#####################&,,%#######################\n'
                  '*,,,,,,,,,,,,,,,,,,*,,,*,,,,,,,,,,,/,,,,,,,#,,,,,,,,,,,,,&#####################&,,%#######################\n'
                  '*,,,,,,,,,,,,,,,,,/#%,,,,,,,,,,,,,,#,,,,,,#,,,,,,,@,,*,,,/#####################&,,%#######################\n'
                  '*,,,,,,,*,,,,,,,&##%*,,,,,,,,,,,,,,&,,,,,*#,,,,,,,,,,,,,,,#####################&,,%#######################\n'
                  '*,,,,,,,/&%#%,,##(,,,,,,,,,,,,,,,,,#,,,,,(,,,,,,*,*@,,,,,*&####################&,,%#######################\n'
                  '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n'
                  '@@@@&(,,,,,/@@(,%@@&/,%@&#,#@@#,,@@@@@@@@@@@@&,,&(*,/&#*,(@@@&%,,,,,*%@@&#,,,,,,(@@#,,,,,,,,@@#,,@@@&,*@@@\n'
                  '@@@&/,&@@@@@@@#,%@@&/,%@@#,#@@#,,@@@@@@@@@@@@&*,@@&/,@@&(,%@@&**@@@%*,@@&#,#@@&#,%@@@@%*,@@@@@#,*@@@%,/@@@\n'
                  '@@@&/*,,,,,/@@%,,@@%,,@@@#,#@@#,,@@@@@@@@@@@@&*,@@&/,@@&(,&@@&,*@@@%*,@@&#,**,,,*@@@@@%*,@@@@@@%*,,,,@@@@@\n'
                  '@@@@%**,,,,/@@@&(,,,%@@@@#,#@@#,,,,,,*@@@@@@@&*,@@&/,@@&(,%@@%,,,,,,,,@@&#,#@@@#,,@@@@%*,@@@@@@@@%**@@@@@@\n'
                  '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n'
                  '')
            time.sleep(8)
            print('Ok man lets attack him!')
            time.sleep(2)
            print('You guys attack him and save the house!\n'
                  'You win!\n')
            time.sleep(5)

        living_room()


def instructions():
    print(
        'H-H-Hey man, im Morty, umm welcome to my house or whatever.\n')  # this is the intro for the game describing
    time.sleep(3)  # the actions that are possible
    print('My mom said I have to T-Tell you a couple of rules.\n')
    time.sleep(3)
    print('I-If you wanna, like, go to a different room, just say a direction or whatever\n'
          'im not your boss.\n')
    time.sleep(5)
    print('But if you spell a word wrong man, my Grandpa Rick will make you pass out and wake\n'
          "up back here in the living room. Don't ask me why!\n"
          "After he went to the Alphabet World he joined the language police\n"
          "so he has to correct and punish anyone who has bad grammar and cant spell.\n"
          "It's soo lame! *psst* if you use all lowercase letters that helps too.\n")
    time.sleep(12)
    print("Also if you wanna grab an item you can just say 'grab' and whatever y-y-you wanna pick up.\n")
    time.sleep(3)
    print("Well i think that's everything my mom told me to tell you, so go explore the house or whatever.\n")
    time.sleep(3)
    print("Wait!? Did y-y-you hear that?\n")
    time.sleep(3)
    print('It sounds like someone is trying to attack us!\n'
          'Is that Evil Morty?\n')
    time.sleep(6)
    print('Find every item you can and bring it with you I will meet you at his lair.\n')
    time.sleep(3)
    print("(You think to yourself i don't even know where his lair is)\n")
    time.sleep(4)


instructions()
main()
