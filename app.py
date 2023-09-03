from flask import Flask, render_template, request
from random import sample

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/love')
def love_form():
    return render_template('love.html')


LOVE_STORY = [
    f'Once upon a time in a quaint little town named {{town}}, {{name1}} and {{name2}} met at the local cafe. {{name1}}, a talented pianist, was {{verb}} a soothing melody that resonated with {{name2}}, who was sipping his coffee pensively. He approached her {{adverb}}, his heart racing, and said, "You play beautifully." {{name1}} smiled warmly and replied, "Thank you." As they talked, their connection deepened, and over time, their love for music and each other blossomed, creating a harmonious and enduring love story in {{town}}.', 
    f'Once upon a time in {{town}}, there were two souls named {{name1}} and {{name2}}. They had been friends for years, but one fateful evening, something changed between them. As the rain {{verb}} down {{adverb}} outside, {{name1}} and {{name2}} found themselves sitting in a cozy café, sipping hot chocolate and sharing stories. Suddenly, {{name2}} reached out and gently touched {{name1}}\s hand. Their eyes met, and in that moment, their hearts raced as they realized their true feelings for each other. With trembling hands, {{name2}} whispered adoringly, "{{name1}}, I\'ve loved you silently for so long." {{name1}} smiled warmly and replied, "{{name2}}, I\'ve been waiting for you to say that."In that dimly lit café, amidst the rain\'s soft symphony, {{name2}} and {{name1}}\s friendship blossomed into a deep, passionate love. Their love story unfolded with a tenderness that warmed their hearts, and they lived happily ever after, forever grateful for that rainy evening when their love took flight.'
]
@app.route('/love_story')
def love_story():
    name1 = request.args['name1']
    name2 = request.args['name2']
    town = request.args['town']
    verb = request.args['verb']
    adverb = request.args['adverb']
    story = sample(LOVE_STORY, 1)

    return render_template('love_story.html', name1=name1, name2=name2, town=town, verb=verb, adverb=adverb, loves=story)

@app.route('/action')
def action():
    return render_template('action.html')

@app.route('/action_story')
def action_story():
    name = request.args['name']
    body_part = request.args['body_part']
    adjective = request.args['adjective']
    return render_template('action_story.html', name=name, body_part=body_part, adjective=adjective)

@app.route('/horror')
def horror():
    return render_template('horror.html')

@app.route('/horror_story')
def horror_story():
    name = request.args['name']
    town = request.args['town']
    entity = request.args['entity']
    return render_template('/horror_story.html', name=name, town=town, entity=entity)
