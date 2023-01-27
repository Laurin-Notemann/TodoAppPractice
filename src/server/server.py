from flask import Flask, request, Response, jsonify, render_template
from controller.todo_controller import get_all_Todos, create_todo, delete_todo_by_id, update_todo_by_id
from flask_cors import CORS

app = Flask(__name__, static_url_path='/static')
CORS(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.get("/api/todo")
def todo_get_all():
    try:
        (error, content) = get_all_Todos()
        if error != None:
            return error, 400

        return jsonify(content), 200
    except Exception as e:
        print(e)
        return f"Could not get all entries: {e}", 400


@app.post("/api/todo")
def todo_post():
    try:
        todo_entry = request.json["todo_entry"]
        date = request.json["date"]
        (error, msg) = create_todo(todo_entry, date)
        if error != None:
            return error, 400

        return msg, 201
    except Exception as e:
        print(e)
        return f"Could not create a new Todo: {e}", 400


@app.delete("/api/todo/<id>")
def todo_delete(id):
    try:
        id = id
        (error, msg) = delete_todo_by_id(id)
        if error != None:
            return error, 400

        return msg
    except Exception as e:
        print(e)
        return f"Could not delete entry: {e}", 400


@app.put("/api/todo/<id>")
def todo_update(id):
    try:
        id = id
        todo_entry = request.json["todo_entry"]
        date = request.json["date"]
        (error, msg) = update_todo_by_id(id, todo_entry, date)

        if error != None:
            return error, 400
        return msg
    except Exception as e:
        print(e)
        return f"Could not update Entry: {e}", 400
