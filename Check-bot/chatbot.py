from chatterbot import ChatBot
from chatterbot import logic
from chatterbot import filters
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from give_answer_google import answer_question
import json
import os
import glob
# import spacy
# nlp = spacy.load('en')


def init_bot():
    global bot
    bot = ChatBot(
        "Health-assist-chatbot",
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri='sqlite:///db.sqlite3',
        logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch',
                # 'maximum_similarity_threshold': 0.1
            },
            'chatterbot.logic.MathematicalEvaluation',
            'chatterbot.logic.UnitConversion',
            'chatterbot.logic.SpecificResponseAdapter'

        ],
        filters=['chatterbot.filters.RepetitiveResponseFilter']
    )


def train_bot():
    trainer = ListTrainer(bot)
    # trainer = ChatterBotCorpusTrainer(bot)
    trainer.train('chatterbot.corpus')

    # Code for training from  JSON files
    convArray = []
    with open('./Dataset/WHO_data.json', encoding="utf-8") as json_file:
        data = json.load(json_file)
        for p in data:
            convArray.append(p['Context'])
            convArray.append(p['Answer'])
    trainer.train(convArray)

    # code for training from text files
    path = 'textfiles/'
    # for filename in os.listdir(path):
    # for filename in glob.glob(os.path.join(path, '*.txt')):
        # print("fileName : ", filename)
        # conv = open(filename, 'r').readlines()
        # trainer = ListTrainer(bot)
        # trainer.train(conv)


def get_response(query):
    response = bot.get_response(query)
    print("conf", response.confidence)
    if not response.confidence > 0.5:
        response = answer_question(query)
    return response