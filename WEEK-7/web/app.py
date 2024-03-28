from flask import Flask, jsonify, render_template

app = Flask(__name__)

data = [
          {
        "name": "Abyssinian",
        "origin": "Egypt",
        "description": "The Abyssinian is easy to care for, and a joy to have in your home. They’re affectionate cats and love both people and other animals."
    },
    {
        "name": "Aegean",
        "origin": "Greece",
        "description": "Native to the Greek islands known as the Cyclades in the Aegean Sea, these are natural cats, meaning they developed without humans getting involved in their breeding. As a breed, Aegean Cats are rare, although they are numerous on their home islands. They are generally friendly toward people and can be excellent cats for families with children."
    },
    {
        "name": "American Bobtail",
        "origin": "United States",
        "description": "American Bobtails are loving and incredibly intelligent cats possessing a distinctive wild appearance. They are extremely interactive cats that bond with their human family with great devotion."
    },
    {
        "name": "American Curl",
        "origin": "United States",
        "description": "Distinguished by truly unique ears that curl back in a graceful arc, offering an alert, perky, happily surprised expression, they cause people to break out into a big smile when viewing their first Curl. Curls are very people-oriented, faithful, affectionate soulmates, adjusting remarkably fast to other pets, children, and new situations."
    },
    {
        "name": "American Shorthair",
        "origin": "United States",
        "description": "The American Shorthair is known for its longevity, robust health, good looks, sweet personality, and amiability with children, dogs, and other pets."
    },
    {
        "name": "American Wirehair",
        "origin": "United States",
        "description": "The American Wirehair tends to be a calm and tolerant cat who takes life as it comes. His favorite hobby is bird-watching from a sunny windowsill, and his hunting ability will stand you in good stead if insects enter the house."
    },
    {
        "name": "Arabian Mau",
        "origin": "United Arab Emirates",
        "description": "Arabian Mau cats are social and energetic. Due to their energy levels, these cats do best in homes where their owners will be able to provide them with plenty of playtime, attention and interaction from their owners. These kitties are friendly, intelligent, and adaptable, and will even get along well with other pets and children."
    },
    ]

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    first_name= "Asabeneh"
    last_name = 'Yetayeh'
    return render_template('about.html', first_name = first_name, last_name= last_name, data = data)

@app.route('/cats')
def cats():
    return jsonify(data)

@app.route('/cats/<name>')
def cat(name):
    return jsonify([item for item in data if item['name'] == name])
    

if __name__ == '__main__':
    app.run(debug=True, host ='0.0.0.0', port=5000)

