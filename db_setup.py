from main import get_db_ref

db = get_db_ref()

class User(db.Document):
    username = db.StringField()

    def to_json(self):
        return {"name": self.name,
                "email": self.email}

class Project(db.Document):
    title = db.StringField(max_length=50)
    description = db.StringField()
    supportedRobots = db.ListField(db.StringField(max_length=50))