from elevenlabs import voices, generate
voices = voices()
audio = generate(text="Hello there!", voice=voices[0])
print(voices)