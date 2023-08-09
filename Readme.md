# Audio-Visual Novel Demo

*This code is licensed under GPL for noncommercial use. For commercial use / custom game engine integration contact me at [crcdng.com](crcdng.com)*
<br>
<br>
<br>

This is a demo for an audiovisual novel system, integrating [ElevenLabs](https://elevenlabs.io/) text-to-speech synthesis with the [Ren'Py](https://www.renpy.org/) visual novel engine. Made in 48 hours during the [LabLab](https://lablab.ai/) [ElevenLabs AI hackathon](https://lablab.ai/event/eleven-labs-ai-hackathon).

A visual novel is a form of interactive fiction, one that combines text, images and animations. Ren'Py is a popular and open source visual novel engine based on Python. It has been used to create thousands of interactive stories, visual novels and games, including [Andromeda Six](https://store.steampowered.com/app/1642870/Andromeda_Six/), [Highway Blossoms](https://store.steampowered.com/app/451760/Highway_Blossoms/) and [Doki Doki Literature Club](https://store.steampowered.com/app/698780/Doki_Doki_Literature_Club/). 

I am using the [Ren'Py automatic voice feature](https://www.renpy.org/doc/html/voice.html#automatic-voice) to demonstrate adding ElevenLabs voices to a visual novel. There are two Python scripts (for now) that do the job: [generate_voices.py](generate_voices.py) and [wav_to_ogg.py](wav_to_ogg.py). 

You can check out the folder `avdemo` for the demo. The web demo is at https://github.com/crcdng/avnovel_demo
You can play it live here: https://crcdng.github.io/avnovel_demo/

To try out the integration for yourself, follow these steps: 

### What you need

* An editor such as [VSCode](https://code.visualstudio.com/) with the [Ren'Py extension](https://marketplace.visualstudio.com/items?itemName=LuqueDaniel.languague-renpy)
* [Ren'Py](https://www.renpy.org/)
* A Python 3 environment - I recommend using [conda](https://docs.conda.io/en/latest/miniconda.html) 
* The ElevenLabs Python API. Add it to your Python enviroment with `pip install elevenlabs`
* [ffmpeg](https://www.ffmpeg.org/) to convert audio from `.wav` to `.ogg`

### Prepare the dialogue

1. Prepare a game / interactive fiction / visual novel in Ren'Py
2. Extract the dialogue data via the Ren'Py menu `Extract Dialogue`. This creates a file `dialogue.tab` in your project directory.
3. Open this file in your editor. Note the entries in column "Character". The characters that are listed here, are defined in your script, e.g. `define a = Character("Aoki")`. An empty entry stands for the narrator. Add a "-" in each line that you don't wan't to generate. Also go through the `Dialogue` column and clean up any markup that might be there. You will send these strings to the ElevenLabs API.
4. Open `generate_voices.py`. Provide your ElevenLabs API key via the environment variable ELEVEN_API_KEY or via the argument `api_key` in the `generate()` function (optional). Edit the character-to-voice mapping in function `getVoice()` according to step 3. You have to use ElevenLabs voices that are available for your access level. If you don't have an API key, use voices included the free tier. You can check this by running `python list_voices.py`. Test the voices here: https://elevenlabs.io/speech-synthesis
5. Configure Ren'Py to use the automatic voice system by adding the line `define config.auto_voice = "voice/{id}.ogg"` in the Ren'Py file `options.rpy`

### Generate the voices

6. Run `python generate_voices.py [your Ren'Py project directory]`. This will create a subdirectory `voice` inside of the `game` dirctory, call the Elevenlabs API to generate the audio files and store them with the identifier names from `dialogue.tab`.

### Postprocess the voices

7. Run `python wav_to_ogg.py [your Ren'Py game directory]/voice` to convert the audio files from `.wav` to `.ogg` format. You can choose to keep the original files (default) or delete them bz adding the `-d` switch. 

### Test

8. In Ren'Py, reload the scripts with `Shift-R` and restart your visual novel. You should now hear the voices automatically added to the lines spoken by the characters and the narrator ✅

---------

Note these scripts, demo and accompanying materials were made in 48 hours in the LabLab hackathon while listening to techno (Tommorrowland). 

Possible code improvements / Next steps:

* eliminate some of the manual steps above
* add more features, e.g multilingual support
* add a UI 
* improve the code quality 
* add tests

### Credits:

Characters for the demo project: [kid-blue](kid-blue.deviantart.com)
Backgrounds for the demo project: Ren'Py example backgrounds

Ren'Py license: https://www.renpy.org/doc/html/license.html


