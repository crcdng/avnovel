# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Aoki", color="#c8ffc8")
define n = Character("Namura", color="#c8c8ff")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg club
    with fade

    "You've created a new Ren'Py game."

    "Once you add a story, pictures, and music, you can release it to the world!"
    
    show aoki neutral at left

    a "Hi there! How was class?"

    show namura smile at right

    n "Good..."

    "I can't bring myself to admit that it all went in one ear and out the other."

    a "Are you going home now? Wanna walk back with me?"

    n "Sure!"
    
    # This ends the game.

    return
