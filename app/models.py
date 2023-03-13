from . import db

from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property
import datetime

NUM_BOXES = 5
BOXES = range(1, NUM_BOXES + 1)


class Card(db.Model):
    __tablename__ = "cards"
    name = db.Column(db.String(64), unique=True, primary_key=True)
    description = db.Column(db.Text)
    example = db.Column(db.Text)
    _box = db.Column(db.Integer, default=BOXES[0])
    timestamp = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)

    @hybrid_property
    def box(self):
        return self._box

    @box.setter
    def box(self, value):
        if value < BOXES[0]:
            self._box = BOXES[0]
        elif value > BOXES[-1]:
            self._box = BOXES[-1]
        else:
            self._box = value

