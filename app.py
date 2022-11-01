from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://text:sparta@cluster0.csxr5oe.mongodb.net/@cluster0?retryWrites=true&w=majority')
db = client.minipro


@app.route('/')
def home():
    return render_template('team_first.html')


@app.route("/project", methods=["POST"])
def project_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name': name_receive,
        'comment': comment_receive
    }

    db.minipro.insert_one(doc)

    return jsonify({'msg': '방명록을 남기셨습니다!'})


@app.route("/project", methods=["GET"])
def project_get():
    comment_list = list(db.minipro.find({}, {'_id':False}))
    return jsonify({'comments': comment_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
