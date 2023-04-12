#!/usr/bin/python3

import flask
import app_tasques
import tasca
import json

app = flask.Flask(__name__)
core_app = app_tasques.App_tasques()

@app.route("/tasks", methods=["POST", "GET"])
def tasks():
    if flask.request.method == "POST":
        info_body = flask.request.get_data()                   #info body = '{"title": "hola"}' _> str
        tasca_nova = json.loads(info_body)                     #tasca nova = '{"title": "hola"}' ->str
        objecte_tasca = tasca.Tasca(None, tasca_nova["title"]) # Objecte.Tasca _> tasca.Tasca
        resultat = core_app.afegeix_tasca(objecte_tasca)
        return "", 201
    elif flask.request.method == "GET":
        llista_jsons = []
        llista_tasques = core_app.llegir_tasques()
        for t in llista_tasques:
            tasca_json = str(t)                          # tasca_json -> str
            tasca_diccionary = json.loads(tasca_json)    #tasca_diccionary -> dictionary
            llista_jsons.append(tasca_diccionary)     #array de dictionaries
        return flask.jsonify(llista_jsons), 200   #retorna json + Content_type: application/json

app.run(host="0.0.0.0")