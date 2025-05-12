from flask import Flask

# Create Flask app instance
app = Flask(__name__)

# The existing models list is already defined
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

# Default route
@app.route('/')
def index():
    """Default route that welcomes users to Flatiron Cars"""
    return "Welcome to Flatiron Cars"  # Removed exclamation mark

# Model-specific route
@app.route('/<model>')
def check_model(model):
    """
    Route for checking if a specific car model exists
    
    Args:
        model (str): The car model name from the URL
        
    Returns:
        str: A message indicating whether the model exists in the fleet
    """
    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"  # Added "Flatiron" before model name
    else:
        return f"No models called {model} exists in our catalog"  # Changed to "catalog" (American spelling)

# This allows the app to run directly with 'python app.py'
if __name__ == '__main__':
    app.run(debug=True)