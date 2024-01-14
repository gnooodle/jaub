# jaub
Just Another Useful (Discord) Bot

The basic foundations for a general purpose Discord Bot, easily expandable.
To get it up and running, a few changes need to be made.
* Create a python venv (any name as long as it is the same in `start.bat`)
* Install the requirements in the venv: `pip install -r requirements.txt`
* Create a `.env` to ideally store the `BOT_TOKEN`
* Find the desired `CHANNEL_ID` for startup message(s) to be sent to (this does not apply to general use, it can be used in any server/channel it has permissions in.)
* Add the path to the bot directory in `start.bat`

To start simply run the `start.bat` which will automatically use the venv created.
