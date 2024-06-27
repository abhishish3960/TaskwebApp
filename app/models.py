from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entityname = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    taskType = db.Column(db.String(50), nullable=False)
    contactNumber = db.Column(db.String(20))  # Optional, since it's not always required
    contactperson = db.Column(db.String(100), nullable=False)
    notes = db.Column(db.Text)
    status = db.Column(db.Boolean, default=True)  # Optional boolean field with default value

    def __repr__(self):
        return f'<Task {self.id}>'

    def serialize(self):
        return {
            'id': self.id,
            'entityname': self.entityname,
            'date': self.date.isoformat() if self.date else None,
            'time': self.time.isoformat() if self.time else None,
            'taskType': self.taskType,
            'contactNumber': self.contactNumber,
            'contactperson': self.contactperson,
            'notes': self.notes,
            'status': self.status
        }
