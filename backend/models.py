from backend.backend_venv.config import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def to_json(self):
        return{
            "id": self.id,
            "firstName": self.first_name, #in JSON use camel case. in python use snakecase. can be confused and mixed up so focus.
            "lastName": self.last_name,
            "email": self.email,
        }