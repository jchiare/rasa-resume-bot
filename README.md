# Rosemary; the resume explainer bot

Bot which explains the details of a (currently my) resume. Mainly created to learn about [rasa 2.x](https://rasa.com), chatbots, and very basic NLP (intents, entities, tokenizer etc)

## Installation

**Requirements:**
* Python 3.7.6 (I use [pyenv](https://github.com/pyenv/pyenv) as the python version manager)
* Install rasa requirements with `pip install -r requirements.txt`

## Run the bot

Use `rasa train` to train a model.

Then, to run, first set up your action server in one terminal window:
```
rasa run actions
```
To talk to the bot in your terminal , run:
```
rasa shell --debug
```
Note that --debug mode will produce a lot of output meant to help you understand how the bot is working under the hood. To simply talk to the bot, you can remove this flag.

You can also try out your bot locally using Rasa X by running
```
rasa x
```

More documentation about rasa here: https://rasa.com/docs/
