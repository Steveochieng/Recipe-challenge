from werkzeug.security import generate_password_hash

userdata = {}


class User:
    """defines the user"""

    def __init__(self, email, password, first_name, last_name):
        global userdata
        user_id = hash(email)
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = generate_password_hash(password)
        userdata[user_id] = {'email': self.email, 'password': self.password,
                             'First Name': self.first_name, 'Last Name': self.last_name}


recipes = {}


class Recipe:
    """Stores the user recipes"""
    recipe_id = 0
    global recipes

    def __init__(self, recipe_name, recipe_type, recipe):
        self.recipe_name = recipe_name
        self.recipe_type = recipe_type
        self.recipe = recipe
        self.recipe_id = Recipe.recipe_id
        Recipe.recipe_id += 1
        recipes[self.recipe_id] = {'Recipe name': self.recipe_name, 'Recipe Type': self.recipe_type,
                                   'Recipe': self.recipe}