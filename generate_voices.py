
import csv, os
from argparse import ArgumentParser
from elevenlabs import generate, play, save

parser = ArgumentParser()
parser.add_argument("projectpath", help="the full path to the Ren\'Py game project")
parser.add_argument("-i", "--input-file", dest="infile", default="dialogue.tab", help="name of the dialogue file generated in Ren\'Py (default dialogue.tab) ")
parser.add_argument("-o", "--output-path", dest="outpath", default="game/voice", help="relative path to the voice files directory (default: 'voice' inside the 'game' directory). will be created if it does not exist. must be configured in Ren\'Py")
args = parser.parse_args()

projectPath = args.projectpath
inFile = args.infile
if args.outpath == "game/voice":
    outPath = os.path.join('game', 'voice')

def getVoice(character):
    match character:
        case "a":
            return "Jeremy"
        case "n":
            return "Matilda " # Bug in ElevenLabs API https://github.com/elevenlabs/elevenlabs-python/issues/68 
        case "":
            return "Michael " # Bug in ElevenLabs API
        case _:
            raise Exception("Unidentified character. Check input and retry.")  

os.chdir(projectPath)

if not os.path.isdir(outPath):
    os.mkdir(outPath)

# Identifier    Character   Dialogue    Filename    Line Number     Ren'Py Script

print("calling the ElevenLabs API to generate audio files, might take a while...")

with open(inFile, "r", encoding="utf8") as dialogueFile:
    dialogueReader = csv.DictReader(dialogueFile, delimiter="\t")
    for dialogueData in dialogueReader:
        identifier = dialogueData["Identifier"]
        character = dialogueData["Character"]
        dialogue = dialogueData["Dialogue"]
        if character == "-": # special meaning: do not create voice audio 
            continue
        voicefile = generate(text = dialogue, api_key = None, voice = getVoice(character), model = "eleven_monolingual_v1", stream = False)
        voicefilePath = os.path.join(projectPath, outPath, identifier + '.' + "wav")
        save(voicefile, voicefilePath) 

print("done")

# play(audio)

