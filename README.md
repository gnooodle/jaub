# jaub
Just Another Useful (Discord) Bot

The basic foundations for a general purpose Discord Bot, easily expandable.
To get it up and running, a few changes need to be made.

### Install

Create a python venv (any name as long as it is the same in `start.bat`)

Install the requirements in the venv: `pip install -r requirements.txt` (after starting the venv, of course)

Create a `.env` to ideally store the `BOT_TOKEN` (in the example, it is simply called `token` within the `.env`)

Find the desired `CHANNEL_ID` for startup message(s) to be sent to (this does not apply to general use, it can be used in any server/channel it has permissions in.)

Add the path to the bot directory in `start.bat`

To start simply run the `start.bat` which will automatically use the venv created.

### To come

An install script to make setup quicker/easier.
