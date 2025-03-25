import assemblyai as aai

aai.settings.api_key = "f256a97fbb8944859bef065dc1e0290f"
transcriber = aai.Transcriber()

transcript = transcriber.transcribe("https://assembly.ai/news.mp4")
# transcript = transcriber.transcribe("./my-local-audio-file.wav")

print(transcript.text)