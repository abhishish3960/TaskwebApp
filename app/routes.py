from flask import Blueprint, jsonify, request, abort
from app.models import Task
from app import db

tasks_bp = Blueprint('tasks', __name__, url_prefix='/api/tasks')

@tasks_bp.route('/', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.serialize() for task in tasks])

@tasks_bp.route('/<int:id>', methods=['GET'])
def get_task(id):
    task = Task.query.get(id)
    if not task:
        abort(404)
    return jsonify(task.serialize())


@tasks_bp.route('/add', methods=['POST'])
def add_task():
    data = request.json
    task = Task(
        entityname=data.get('entityname'),
        date=data.get('date'),
        time=data.get('time'),
        taskType=data.get('taskType'),
        contactNumber=data.get('contactNumber'),
        contactperson=data.get('contactperson'),
        notes=data.get('notes'),
        status=data.get('status')
    )
    db.session.add(task)
    db.session.commit()
    return jsonify(task.serialize()), 201


@tasks_bp.route('/<int:id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get(id)
    if not task:
        abort(404)
    data = request.json
    for key, value in data.items():
        setattr(task, key, value)
    db.session.commit()
    return jsonify(task.serialize())

@tasks_bp.route('/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)
    if not task:
        abort(404)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted'})

@tasks_bp.route('/duplicate/<int:id>', methods=['POST'])
def duplicate_task(id):
    task = Task.query.get(id)
    if not task:
        abort(404)
    new_task = Task(
        entityname=task.entityname,
        date=task.date,
        time=task.time,
        taskType=task.taskType,
        contactperson=task.contactperson,
        notes=task.notes,
        status=task.status
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.serialize()), 201
