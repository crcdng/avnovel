# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Aoki", color="#c8ffc8")
define n = Character("Namura", color="#c8c8ff")

# The game starts here.

label start:

    scene bg club
    with fade
    
    show aoki speak at left
    show namura silent at right

    a "Hi, I am Aoki. This is Namura. We both are characters in visual novels."
    a "Our voices, however, are muted."

    a "Many creators cannot afford professional voices in their interactive novels or games."

    show namura speak at right

    n "I wish we could speak!!"

    scene bg slide05

    "Lets do this. I created automated voice generation for Ren'Py during the LabLab ElevenLabs hackathon in 48 hours"

    scene bg slide06
    with fade

    "The results are breathtaking."

    show aoki speak at left
    show namura silent at right

    a "This enables automatic voice generation for the whole project."
    n "This is super exciting."

    scene bg slide08
 
    a "This opens up new opportunities for creators and for players."
    n "It marks the beginning of a whole new era. The era of the audio-visual novel."

    scene bg slide09

    "And therefore there are significant market opportunities."
    
    scene bg meadow
    with fade
    show aoki smile at left
    show namura smile at right

    a "I am glad we finally found our voices."
    n "Easier than I thought. And the quality is amazing!"
    
    scene bg slide13
    with fade

    show namura smile at right
    
    "But of course there is a lot left to do, adding more features, improving the code quality and creating a couple of audio-visual novels with other creators"

    n "and working on the business model! I could need help with that"

    "Thank you for playing the demo. This is just the beginning for audio-visual Novels."

    # This ends the game.

    return
