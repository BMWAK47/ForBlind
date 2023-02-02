from gtts import gTTS
from flask import Flask, Response

app=Flask(__name__)


@app.route("/")
def title ():
    return "視障友善用餐系統For Blind"

@app.route("/<lan>/<word>")
def voice(lan,word):
    if lan=="zh":
        tts = gTTS(word,lang='zh')
    elif lan=="en":
        tts = gTTS(word,lang='en')
    tts.save("1.mp3")

#     sound_file = 'TTS.mp3'
#     def generate(): 
#         with open(sound_file, "rb") as fwav:
#             data = fwav.read(1024)
#             while data:
#                 yield data
#                 data = fwav.read(1024)
#     return Response(generate(), mimetype="audio/x-mp3")         


# @app.route("/<name>")
# def home(name):

# #@app.route("")
# #def streamwav():
#     tts = gTTS(name, lang='zh',slow=False)
#     tts.save('1.mp3')
    sound_file = '1.mp3'
    def generate(): 
        with open(sound_file, "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)

#    return f"<h1>你好! {name}</h1>"
    return Response(generate(), mimetype="audio/x-mp3")

if __name__=="__main__":
    app.run()