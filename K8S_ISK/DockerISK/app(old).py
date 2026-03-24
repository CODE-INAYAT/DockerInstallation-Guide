from flask import Flask
from colorama import Fore, init

init(autoreset=True) # Initialize Colorama
app = Flask(__name__)

@app.route('/')
def home():
    print(Fore.GREEN + ">>> [DOCKERISK] Web request received!")
    return """
    <div style="background-color: #ffffff; padding: 100px; text-align: center; border: 1px solid #eee; min-height: 100vh; display: flex; flex-direction: column; justify-content: center;">
      <h1 style="font-family: 'Didot', 'Bodoni MT', 'Times New Roman', serif; font-weight: bold; font-size: 3.5rem; color: #111; letter-spacing: 0.25em; text-transform: uppercase; margin: 0;">
        Docker is <span style="font-weight: 400; color: #333;">Absolute Cinema</span>
      </h1>
      <p style="font-family: 'Futura', 'Helvetica', sans-serif; font-weight: 300; font-size: 1rem; color: #777; letter-spacing: 0.3em; text-transform: uppercase; margin-top: 30px; border-top: 1px solid #ddd; display: inline-block; padding-top: 10px;">
        Interstellar Python <span style="color: #0077b6; font-weight: 500;">Containerization</span>
      </p>
    </div>
    """

if __name__ == '__main__':
    # host='0.0.0.0' is required for Docker to listen correctly
    app.run(host='0.0.0.0', port=5000)