from flask import (
    render_template,
    redirect,
    url_for,
    abort,
    Response,
    make_response
)
import random
import json

from . import main
from .forms import CardForm, EditCardForm
from .. import db
from ..models import Card, BOXES
from ..tts import text_to_speech


@main.route("/")
def index():
    cards_num = Card.query.count()
    return render_template("index.html", cards_num=cards_num, BOXES=BOXES)


@main.route("/add", methods=["GET", "POST"])
def add_card():
    form = CardForm()
    if form.validate_on_submit():
        card = Card(
            name=form.name.data,
            description=form.description.data,
            example=form.example.data,
            box=form.box.data
        )
        db.session.add(card)
        db.session.commit()
        return redirect(url_for(".add_card"))
    return render_template("card.html", form=form, header="Add new card")


@main.route("/edit/<card>", methods=["GET", "POST"])
def edit_card(card):
    c = Card.query.get(card)
    if not c:
        abort(404)
    form = EditCardForm(c.name)
    if form.validate_on_submit():
        c.name = form.name.data
        c.description = form.description.data
        c.example = form.example.data
        c.box = form.box.data
        db.session.add(c)
        db.session.commit()
        return redirect(url_for(".list_cards"))
    form.name.data = c.name
    form.description.data = c.description
    form.example.data = c.example
    form.box.data = c.box
    return render_template("card.html", form=form, header="Edit")


@main.route("/cards")
def list_cards():
    cards = Card.query.order_by(Card.box)
    return render_template("all_cards.html", cards=cards.all(), count=cards.count())


@main.route("/practice")
def get_card():
    cards = []
    weights = []
    for num in range(1, len(BOXES) + 1):
        box_cards = Card.query.filter_by(box=num).all()
        try:
            card = random.choice(box_cards)
        except IndexError:
            continue
        weight = len(BOXES) / num
        cards.append(card)
        weights.append(weight)
    try:
        card = random.choices(cards, weights, k=1)
    except IndexError:
        abort(404)
    return render_template("practice.html", card=card[0])


@main.route("/move/<card>/<direction>")
def move_card(card, direction):
    card = Card.query.filter_by(name=card).first_or_404()
    if direction == "up":
        card.box += 1
    elif direction == "down":
        card.box -= 1
    db.session.add(card)
    db.session.commit()
    return redirect(url_for("main.get_card"))


@main.route("/db_as_json")
def download_db():
    data = {}
    for card in Card.query.all():
        data[card.name] = card.description
    json_data = json.dumps(data, ensure_ascii=False)
    response = Response(
        json_data,
        mimetype='application/json; charset=utf-8'
    )
    response.headers.set(
        'Content-Disposition',
        'attachment',
        filename='data.json'
    )
    return response


@main.route("/box/<id>/cards")
def list_box_cards(id):
    cards = Card.query.filter_by(box=id)
    return render_template("all_cards.html", cards=cards.all(), count=cards.count())


@main.route("/audio/<text>")
def audio(text):
    audio_data = text_to_speech(text)
    return Response(audio_data, mimetype="audio/mpeg")


