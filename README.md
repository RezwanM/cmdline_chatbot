# cmdline_chatbot

The goal of this project was to build a chatbot that could be accessed from the terminal. It uses Google Gemini's API for accessing the Gemini models.

## Requirements

- Python 3.12.9
- google-genai 1.28.0
- python-dotenv 1.1.0

## Setup
The following instructions assume the user has Ubuntu as their local machine's OS. Most instructions should work for other Linux distributions as well, though mileage may vary.

### Step 1: Install Python3
Set up Python3 (v3.12.9) on the local machine.

    sudo apt update 
    sudp apt install python3.12
    
### Step 2: Clone the project
Clone this GitHub repository into the local machine.
    
    git clone --single-branch -b main <project_repo_url> <project_root> 
    
### Step 3: Set up a virtual environment
To resolve project dependencies, install Python3 and the required packages for this project inside a virtual environment. 
    
    cd <project_root> 
    python3 -m venv .venv 
    source .venv/bin/activate
    pip install -r requirements.txt

### Step 4: Obtain the API key
Create a Google account if one is not available or accessible. Then, while logged in, click the link below and then click the "Get API key" button to generate a private API key. 
https://aistudio.google.com/apikey

Note: DO NOT share this API key with anyone!

### Step 5: Store the API key
Create a file inside the project root directory and store the private API key in the file.
    
    touch .env 
    echo "GEMINI_API_KEY=<private_api_key>" > .env

Note: The script will specifically look for the "GEMINI_API_KEY" environment variable, so make sure to write it exactly as shown above.

### Step 6: Run the application
Run the application from the command-line. For quitting the application, press Ctrl+C (keyboard interrupt), or simply type "quit", "exit", or "bye" in the prompt. 

## Usage
    
    cd <project_root>
    python3 ./main.py
