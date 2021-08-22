from flask import Flask, jsonify, request
app = Flask(__name__)


contacts = [
    {
        'id': 1,
        'Name': u'Papa',
        'Contact': u'959385973',
'done': False

    },
    {
              'id': 2,
        'Name': u'Mummy',
        'Contact': u'4924424',
'done': False
    }
] 


@app.route("/add-data", methods = ["POST"])
def addContact():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data",
        
        }, 400)
    contact = {
        "id": task[-1]['id']+1,
        "Name": request.json["name"],
        "Contact": request.json.get("contact", ""),
        'done': False
    }
    contacts.append(contact)
    return jsonify({
        "status": "success",
        "message": "Task added succesully"
    })




if __name__ == '__main__':
    app.run(debug=True)
