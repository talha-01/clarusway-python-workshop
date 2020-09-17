from flask import Flask, jsonify, abort, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo-list.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

def init_todo_db():
    drop_table = 'DROP TABLE IF EXISTS todos;'
    todos_table = """
    CREATE TABLE todos(
        task_id INTEGER PRIMARY KEY,
        title VARCHAR NOT NULL,
        description VARCHAR,
        is_done BOOLEAN NOT NULL DEFAULT 0 CHECK(is_done IN(0,1))
    );
    """
    data = '''
    INSERT INTO todos (title, description, is_done)
    VALUES
    ('Project 2', 'Work on project 2 with teammates', 1);
    '''
    db.session.execute(drop_table)
    db.session.execute(todos_table)
    db.session.execute(data)
    db.session.commit()

def get_all_tasks():
    query = '''
    SELECT * FROM todos;
    '''
    result = db.session.execute(query)
    tasks = [{'task_id':row[0], 'title':row[1], 'description':row[2], 'is_done':bool(row[3])} for row in result]
    return tasks

def find_tasks(id):
    query = '''
    SELECT * FROM todos;
    '''
    row = db.session.execute(query).first()
    task = None
    if row is not None:
        task = {'task_id':row[0], 'title':row[1], 'description':row[2], 'is_done':bool(row[3])}
    return task
    

def insert_task(title, description):
    insert = f'''
    INSERT INTO todos (title, description)
    VALUES ('{title}', '{description}');
    '''
    result = db.session.execute(insert)
    db.session.commit()

    query =f'''
    SELECT * FROM todos WHERE task_id={result.lastrowid};
    '''
    row =db.session.execute(query).first()
    return {'task_id':row[0], 'title':row[1], 'description':row[2], 'is_done':bool(row[3])}


def change_task(task):
    update = f'''
    UPDATE todos
    SET title="{task['title']}, description="{task['description']}, is_done={task['is_done']}
    WHERE task_id={task['task_id']};
    '''
    result = db.session.execute(update)
    db.session.commit()
    query =f'''
    SELECT * FROM todos WHERE task_id={task['task_id']};
    '''
    row =db.session.execute(query).first()
    return {'task_id':row[0], 'title':row[1], 'description':row[2], 'is_done':bool(row[3])}    

def remove_task(task):
    delete = f'''
    DELETE FROM todos
    WHERE task_id={task['task_id']};
    '''
    result = db.session.execute(delete)
    db.session.commit()
    query =f'''
    SELECT * FROM todos WHERE task_id={task['task_id']};
    '''
    row =db.session.execute(query).first()
    return True if row is None else False


@app.route('/')
def home():
    return "Welcome to Talha's to-do API service"

@app.route('/todos', methods=['GET'])
def get_tasks():
    return jsonify({'tasks':get_all_tasks()})

@app.route('/todos/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = find_task(task_id)
    if task == None:
        abort(404)
    return jsonify({'task foud': task})

@app.route('/todos', methods = ['POST'])
def add_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    return jsonify({'new added task':insert_task(request.json['title'], request.json.get('description', ''))}), 201

@app.route('/todos/<int:task_id>', methods = ['PUT'])
def update_task(task_id):
    task = find_tasks(task_id)
    if task == None:
        abort(404)
    if not request.json:
        abort(400)
    task['title'] = request.json.get('title', task['title'])
    task['description'] = request.json.get('description', task['description'])
    task['is_done'] = int(request.json.get('is_done', task['is_done']))
    return jsonify({'updated task': change_task(task)})

@app.route('/todos/<int:task_id>', methods = ['DELETE'])
def delete_task(task_id):
    task = find_tasks(task_id)
    if task == None:
        abort(404)
    return jsonify({'result':remove_task(task)})


if __name__ == '__main__':
    init_todo_db()
    app.run(debug = True)
