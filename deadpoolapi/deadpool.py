from flask import Flask, jsonify, request, abort, render_template_string
import random

app = Flask(__name__)

# Expanded data about Deadpool and his associates, including quotes and images from Wikipedia
characters = {
    "Deadpool": {
        "real_name": "Wade Wilson",
        "alias": "Merc with a Mouth",
        "abilities": ["Regeneration", "Skilled in martial arts", "Expert marksman"],
        "description": "An anti-hero known for his humor and breaking the fourth wall.",
        "quotes": [
            "I'm touching myself tonight.",
            "Maximum effort!",
            "You look like an avocado had sex with an older, more disgusting avocado.",
            "Fourth wall? What fourth wall?",
        ],
        "image_url": "https://static.wikia.nocookie.net/superheroes/images/b/b9/Deadpool.jpg/",
    },
    "Cable": {
        "real_name": "Nathan Summers",
        "alias": "Time-traveling soldier",
        "abilities": ["Superhuman strength", "Telepathy", "Telekinesis"],
        "description": "A mutant with a cybernetic arm, often works with or against Deadpool.",
        "quotes": [
            "I’m Cable, and I’m from the future.",
            "You're not a hero. You're just an annoying clown.",
            "Sometimes, you have to fight dirty."
        ],
        "image_url": "https://static.wikia.nocookie.net/superheroes/images/0/0a/Cable_X-Men.jpg",
    },
    "Domino": {
        "real_name": "Neena Thurman",
        "alias": "Luck Manipulator",
        "abilities": ["Probability manipulation", "Expert markswoman", "Hand-to-hand combat"],
        "description": "A mercenary with the ability to manipulate luck in her favor.",
        "quotes": [
            "Luck isn't a superpower. It's a skill.",
            "I make my own luck.",
            "Just stay out of my way and I'll stay out of yours.",
        ],
        "image_url": "https://upload.wikimedia.org/wikipedia/en/8/8a/Domino_X-Force_Vol_3_8.png",
    },
    "Weasel": {
        "real_name": "Jack Hammer",
        "alias": "The Informant",
        "abilities": ["Intelligence", "Weapon supplier", "Tactical support"],
        "description": "Deadpool's friend and weapons supplier, often reluctantly involved in his schemes.",
        "quotes": [
            "I’m not your sidekick, I’m your supplier.",
            "I'm really more of a behind-the-scenes guy.",
            "This is the last time I help you, Wade. Really.",
        ],
        "image_url": "https://upload.wikimedia.org/wikipedia/en/6/68/Weasel2.jpg",
    },
    "Blind Al": {
        "real_name": "Althea",
        "alias": "Blind Al",
        "abilities": ["Sharp wit", "Survival skills"],
        "description": "Deadpool's roommate and friend, despite their chaotic relationship.",
        "quotes": [
            "I may be blind, but I see right through you, Wade.",
            "You're the worst roommate ever.",
            "Put the knife away, Wade. Not today."
        ],
        "image_url": "https://upload.wikimedia.org/wikipedia/en/a/ad/Blind_Al_%28Deadpool_character%29.png",
    },
    "Vanessa": {
        "real_name": "Vanessa Carlysle",
        "alias": "Copycat",
        "abilities": ["Shapeshifting", "Enhanced agility"],
        "description": "Deadpool's love interest with the ability to shapeshift.",
        "quotes": [
            "I’ll always love you, Wade.",
            "Life is better with a little danger.",
            "You’re crazy, but you’re my kind of crazy."
        ],
        "image_url": "https://static.wikia.nocookie.net/marveldatabase/images/0/00/Vanessa_Carlysle_%28Earth-616%29_from_Deadpool_Vol_5_27_001.jpg",
    },
    "Hydra Bob": {
        "real_name": "Bob",
        "alias": "Hydra Bob",
        "abilities": ["Loyalty to Deadpool", "Knows Hydra secrets"],
        "description": "Deadpool's friend and occasional sidekick, formerly a Hydra agent.",
        "quotes": [
            "I really don’t want to do this, Wade.",
            "Can we talk about this?",
            "I’m not even supposed to be here today!"
        ],
        "image_url": "https://upload.wikimedia.org/wikipedia/en/e/ea/Hydra_Bob.jpg",
    },
    "Agent X": {
        "real_name": "Nijo Minamiyori",
        "alias": "Agent X",
        "abilities": ["Healing factor", "Hand-to-hand combat", "Expert tactician"],
        "description": "A mercenary with abilities similar to Deadpool's, often rivals but sometimes allies.",
        "quotes": [
            "I’m the real deal, not a cheap knock-off.",
            "We could make a great team, if you stopped talking.",
            "You're not as funny as you think, Wade."
        ],
        "image_url": "https://upload.wikimedia.org/wikipedia/en/1/14/Agentx.png",
    },
    "Taskmaster": {
        "real_name": "Tony Masters",
        "alias": "Taskmaster",
        "abilities": ["Photographic reflexes", "Master martial artist", "Weapon proficiency"],
        "description": "A mercenary who can mimic any physical movement, sometimes works with Deadpool.",
        "quotes": [
            "I don’t need to learn; I just watch.",
            "You’re predictable, Wade.",
            "Let’s make this quick. I’ve got other jobs."
        ],
        "image_url": "https://upload.wikimedia.org/wikipedia/en/7/76/Taskmaster_%28Marvel_Comics_character%29.jpg",
    },
    "Outlaw": {
        "real_name": "Inez Temple",
        "alias": "Outlaw",
        "abilities": ["Enhanced strength", "Marksmanship", "Regeneration"],
        "description": "A mutant mercenary with a friendly rivalry with Deadpool.",
        "quotes": [
            "Don’t get in my way, Wade.",
            "I fight for the thrill of it.",
            "Try to keep up."
        ],
        "image_url": "https://upload.wikimedia.org/wikipedia/en/1/10/Outlaw_Marvel_Comics.jpg",
    },
}

# HTML template for the dropdown form and character display
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Character Lookup</title>
</head>
<body>
    <h1>Character Lookup</h1>
    <form action="/" method="post">
        <label for="character_name">Select Character:</label>
        <select id="character_name" name="character_name" required>
            {% for character_name in characters.keys() %}
                <option value="{{ character_name }}">{{ character_name }}</option>
            {% endfor %}
        </select>
        <button type="submit">Get Character Info</button>
    </form>
    
    {% if character %}
        <h2>{{ character_name }}</h2>
        {% if character.image_url %}
            <img src="{{ character.image_url }}" alt="{{ character_name }}'s image" width="200">
        {% endif %}
        <p><strong>Real Name:</strong> {{ character.real_name }}</p>
        <p><strong>Alias:</strong> {{ character.alias }}</p>
        <p><strong>Abilities:</strong> {{ character.abilities | join(", ") }}</p>
        <p><strong>Description:</strong> {{ character.description }}</p>
        <h3>Random Quote:</h3>
        <blockquote>{{ quote }}</blockquote>
    {% elif error %}
        <p style="color: red;">{{ error }}</p>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    """Root route with dropdown form to lookup a character and display info and a random quote."""
    if request.method == 'POST':
        character_name = request.form['character_name']
        character = characters.get(character_name)
        if character:
            quote = random.choice(character.get("quotes", ["No quotes available for this character."]))
            return render_template_string(
                html_template, 
                character=character, 
                character_name=character_name, 
                quote=quote, 
                characters=characters
            )
        else:
            error = "Character not found. Please try another name."
            return render_template_string(html_template, error=error, characters=characters)
    
    return render_template_string(html_template, character=None, error=None, characters=characters)

@app.route('/characters', methods=['GET'])
def get_characters():
    """Endpoint to retrieve a list of all characters."""
    return jsonify(list(characters.keys()))

@app.route('/characters/<string:name>', methods=['GET'])
def get_character(name):
    """Endpoint to retrieve information about a specific character."""
    character = characters.get(name)
    if character is None:
        abort(404, description="Character not found")
    return jsonify(character)

@app.route('/characters/<string:name>/quote', methods=['GET'])
def get_character_quote(name):
    """Endpoint to retrieve a random quote from a character."""
    character = characters.get(name)
    if character is None:
        abort(404, description="Character not found")
    
    quotes = character.get("quotes", [])
    if not quotes:
        return jsonify({"quote": "No quotes available for this character."})
    
    return jsonify({"quote": random.choice(quotes)})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=2224, debug=True)
