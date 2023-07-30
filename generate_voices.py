
import csv, os
from argparse import ArgumentParser
from elevenlabs import generate, play, save

parser = ArgumentParser()
parser.add_argument("gamepath", help="the full path to the Ren\'Py game")
parser.add_argument("-i", "--input-file", dest="infile", default="dialogue.tab", help="name of the dialogue file generated in Ren\'Py (default dialogue.tab) ")
parser.add_argument("-o", "--output-path", dest="outpath", default="voice", help="relative path to the voice files directory (default: 'voice' inside the game directory). will be created if it does not exist. must be configured in Ren\'Py")
args = parser.parse_args()

gamePath = args.gamepath
inFile = args.infile
outPath = args.outpath

def getVoice(character):
    match character:
        case "a":
            return "Josh"
        case "n":
            return "Rachel"
        case "":
            return "Bella"
        case _:
            raise Exception("Unidentified character. Check input and retry.")  

os.chdir(gamePath)

if not os.path.isdir(outPath):
    os.mkdir(outPath)

# Identifier    Character   Dialogue    Filename    Line Number     Ren'Py Script

print("calling the elevenlabs API to generate audio files, might take a while...")

with open(inFile, "r", encoding="utf8") as dialogueFile:
    dialogueReader = csv.DictReader(dialogueFile, delimiter="\t")
    for dialogueData in dialogueReader:
        identifier = dialogueData["Identifier"]
        character = dialogueData["Character"]
        dialogue = dialogueData["Dialogue"]
        if character == "-": # special meaning: do not create voice audio 
            continue
        voicefile = generate(text = dialogue, api_key = None, voice = getVoice(character), model = "eleven_monolingual_v1", stream = False)
        voicefilePath = os.path.join(gamePath, outPath, identifier + '.' + "wav")
        save(voicefile, voicefilePath) 

print("done")

# play(audio)

