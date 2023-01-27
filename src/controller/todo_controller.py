from models.todo_model import Todo
from Connection.Connection import new_session

def create_todo(todo,date):
    try:
        session = new_session()
        session.add(Todo(todo_entry=todo, date=date))
        session.commit()
        session.close()
        msg = "New Todo Entry created."
        return (None, msg)
    except Exception as e:
        return (e, None)

def get_all_Todos():
    try:
        session = new_session()
        all_todos = session.query(Todo).all()
        session.expunge_all()
        session.commit()
        session.close()
        return (None, all_todos)
    except Exception as e:
        return (e, None)

def delete_todo_by_id(id):
    try:
        session = new_session()
        todo_to_delete = session.query(Todo).filter(Todo.id==id).first()
        session.delete(todo_to_delete)
        session.commit()
        session.close()
        msg = "Successfully deleted Todo Entry."
        return (None, msg)
    except Exception as e:
        return (e, None)
    
def update_todo_by_id(id, todo, date):
    try:
        session = new_session()
        todo_to_update = session.query(Todo).filter(Todo.id==id).update({"todo_entry":todo, "date": date})
        session.commit()
        session.close()
        msg = "Successfully updated Todo Entry."
        return (None, msg)
    except Exception as e:
        return (e, None)
