from flask import Flask, render_template, request
from google_trans_new import google_translator
import WHO_data as dataset
import utils as utils
import chatbot
# import speech_recognition as sr

botApp = Flask(__name__)
translator = google_translator()
chatbot.init_bot()
chatbot.train_bot()


def translate(text):
    if not dataset.s_lang == "en":
        #print(translator.translate(text, lang_tgt=dataset.s_lang))
        return translator.translate(text, lang_tgt=dataset.s_lang)
        # return translator.translate(text, "fr").text
    else:
        return text


# def init_speech_recogition():
#     r = sr.Recognizer()
#
#     with sr.Microphone() as source:
#         audio = r.listen(source)
#
#     try:
#         text = r.recognize_google(audio)
#         return str(text)
#     except:
#         return "Sorry. I didnt understand"


@botApp.route("/")
def home():
    return render_template("index.html")


@botApp.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')

    if utils.chatbot_enabled:
        if user_text.lower() == "quit":
            utils.chatbot_enabled =False
            return translate("Bye")
        else:
            respo = translate(str(chatbot.get_response(translate(user_text))))
            if respo == "":
                respo = "sorry, Data Not found."
            print("response: ", respo)
            return respo
    elif (user_text.strip() == "Help") or (user_text.strip() == "help") or (user_text.strip() == "Help!"):
        return str('Ok, here is a link to search more: <a href=\'https://www.google.com\'>www.google.com</a>')
    elif user_text.isnumeric():
        if int(user_text) == 7:
            utils.chatbot_enabled = True
            return translate("Hi, ask any question relate to Covid.<br> \n For Quiting this chatbot Enter 'Quit'")
        # elif int(user_text) == 8:
            # return init_speech_recogition()
            # utils.chatbot_enabled = True
            # return translate("Hi, ask any question relate to Covid. For Quiting this chatbot Enter 'Quit'")
        elif (int(user_text) <= len(dataset.data)) and (int(user_text) > -1):
            return translate(str(utils.remove_breakline(dataset.data[int(user_text)])))
        else:
            return translate(str(utils.remove_breakline(dataset.wrong_input)))
    elif user_text.lower() in (name.lower() for name in dataset.languages):
        dataset.s_lang = dataset.languages_code[[name.lower() for name in dataset.languages].index(user_text.lower())]
        return translate(dataset.lang_changed_text)
    else:
        return str("Wrong input.")


if __name__ == "__main__":
    botApp.run()
