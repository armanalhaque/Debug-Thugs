from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Course Model
class Course(db.Model):
    __tablename__ = 'courses'
    code = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    dept = db.Column(db.String(50), nullable=False)
    credits = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'code': self.code,
            'name': self.name,
            'dept': self.dept,
            'credits': self.credits
        }

# Faculty Model
class Faculty(db.Model):
    __tablename__ = 'faculty'
    id = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    dept = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(15), nullable=True)
    email = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'dept': self.dept,
            'phone': self.phone,
            'email': self.email
        }

# Student Model
class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    dept = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'dept': self.dept,
            'email': self.email
        }
