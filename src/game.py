#/usr/bin/env python3
import time



def type_print(text, speed=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)
    print()



def show_banner():
    print(r"""
                    .-'''-.                                                                                                            
                   '   _    \                                                              _______                                     
 __  __   ___    /   /` '.   \                                _..._                        \  ___ `'.                         _..._    
|  |/  `.'   `. .   |     \  '           .--./)             .'     '.                       ' |--.\  \              _     _ .'     '.  
|   .-.  .-.   '|   '      |  '.-,.--.  /.''\\             .   .-.   .                      | |    \  '       /\    \\   //.   .-.   . 
|  |  |  |  |  |\    \     / / |  .-. || |  | |      __    |  '   '  |                      | |     |  '    __`\\  //\\ // |  '   '  | 
|  |  |  |  |  | `.   ` ..' /  | |  | | \`-' /    .:--.'.  |  |   |  |       _              | |     |  | .:--.'.\`//  \'/  |  |   |  | 
|  |  |  |  |  |    '-...-'`   | |  | | /("'`    / |   \ | |  |   |  |     .' |             | |     ' .'/ |   \ |\|   |/   |  |   |  | 
|  |  |  |  |  |               | |  '-  \ '---.  `" __ | | |  |   |  |    .   | /           | |___.' /' `" __ | | '        |  |   |  | 
|__|  |__|  |__|               | |       /'""'.\  .'.''| | |  |   |  |  .'.'| |//          /_______.'/   .'.''| |          |  |   |  | 
                               | |      ||     ||/ /   | |_|  |   |  |.'.'.-'  /           \_______|/   / /   | |_         |  |   |  | 
                               |_|      \'. __// \ \._,\ '/|  |   |  |.'   \_.'                         \ \._,\ '/         |  |   |  | 
                                         `'---'   `--'  `" '--'   '--'                                   `--'  `"          '--'   '--'  
    """)


def main():
    print("[1] Start Game")
    print("[2] Quit Game")

    while True:
        command = input(">>> ")

        if command == "1":
            start_game()

        elif command == "2":
            print("Quit Game!")
            break
        
        else:
            print('Error')


def start_game():
    print("Game start")
    chapter1()


def chapter1():
    type_print("""
To az khab dar otagat bidar shodi
          
1) be samt dar boro
2) be samt laptop boro 
""")    
    choice = input(">>> ")

    if choice == "1":
        samt_dar()

    elif choice == "2":
        samt_laptop()

    else:
        print('Error')
        chapter1()


def samt_dar():
    type_print("""
To dar ra baz kardi 
          
1) be samt right rahro boro (ashpazkhane)
2) be samt left rahro boro (bathroom)
""")
    
    choice = input(">>> ")

    if choice == "1":
        samt_right_rahro()

    elif choice == "2":
        samt_left_rahro()

    else:
        print('Error')
        samt_dar()    

def samt_right_rahro():
    type_print("""
To be samt right rahro rafti (ashpazkhane)
1) yek livan ab bokhor
""")
    
    choice = input(">>> ")

    if choice == "1":
        type_print("to ab ra khordi va mordi :)")
        quit()

    else:
        print('Error')
        samt_right_rahro()
    
    

def samt_left_rahro():
    type_print("""
To be samt left rahro rafti (bathroom)
1) Dar ra baz kon
""")   

    choice = input(">>> ")

    if choice == '1':
        type_print('to dar bathroom ra baz kardi va ba kale be zamin khordi va mordi :)')
        quit()

    else:
        print('Error')
        samt_left_rahro()    

def samt_laptop():
    type_print("""
To be samt laptop rafti va laptop ra baz kardi
          
1) app vscode ro baz kon
2) chrome ro baz kon
3) email haye ersal shode ra check kon
""")

    choice = input('>>> ')

    if choice == "1":
        type_print('to app vscode ra baz kardi va bug ha be to hamle kardand va mordi :)')

    elif choice == "2":
        type_print('to chrome ra baz kardi va ba didan history search sekte kardi va mordi :)')
        quit()

    elif choice == "3":
        type_print("to email haye ersal shode ra baz kardi va pashmat rikht va mordi :)")
        quit()

    else:
        print('Error')
        samt_laptop()



show_banner()
main()