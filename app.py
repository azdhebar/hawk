from datetime import datetime
from flask_cors import CORS
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import bcrypt
from flask import Flask, render_template, request, redirect, session,jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
import spacy
nlp = spacy.load("en_core_web_sm")

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
englishBot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(englishBot)
trainer.train("chatterbot.corpus.english")  # train the chatter bot for english

@app.route("/")
def chat():
    return render_template("chatbot.html")

@app.route("/get")

def get_bot_response():
    userText = request.args.get('msg')
    return str(englishBot.get_response(userText))


@app.route("/api/v1/users")
def api_msg():
    userText = request.args.get('msg')
    res=str(englishBot.get_response(userText))
    return jsonify(
      msg=res
    )

