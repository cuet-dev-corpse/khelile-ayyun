# খেলিলি আইয়ুন

## Setting up the bot

Firstly Download Python and Git. Then follow the following instructions
### For Linux:
```bash
# Clone GitHub repository, and move into the folder
git clone https://github.com/cuet-dev-corpse/khelile-ayyun
cd khelile-ayyun

# Create and activate a virtual environment
python3 -m venv bot-env
source bot-env/bin/activate

# Install required packages
pip install -r requirements.txt

# Make a file for environment variables
echo "TOKEN = {Put your token here}" > .env-var

# Run the bot
python main.py
```
### For Windows:
```batch
:: Clone GitHub repository, and move into the folder
git clone https://github.com/cuet-dev-corpse/khelile-ayyun
cd khelile-ayyun

:: Create and activate a virtual environment
python -m venv bot-env
.\bot-env\Scripts\activate.bat

:: Install required packages
pip install -r requirements.txt

:: Make a file for environment variables
echo "TOKEN = {Put your token here}" > .env-var

:: Run the bot
python main.py
```