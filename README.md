# Setup for my small Todo list

### First clone the repo:
```bash
git clone https://github.com/laurin-notemann/todo_list_learn
```
### Go into the directory and run the following commands:
```bash
python -m venv venv
```
## Active the venv:
### MacOS Linux: 
```bash
source venv/bin/activate
```
### Windows User:
```bash
path\to\venv\Scripts\activate.bat
```
### Install dependecies:
```bash
pip install
```

## Now create a .env file in the project directory. 
##### Paste the contents of the .env.example contents into the .env file and swap the placeholder with your own Secrets

### Run the program locally with:
```bash
python3 src/main.py
```

This will start the server and now enter the URL: http://127.0.0.1:5000 or http://localhost:5000 into your browser and now you can add new entries (it will take the current date as your date), delete them and you can also change the Todo entry by clicking on one of them and changing the value and then clicking somewhere else on the screen.
