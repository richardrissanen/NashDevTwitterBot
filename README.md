# NashDev Twitter Bot

Automate posting events from cal.nashvl.org to Twitter

## Proposed Solution

![overview](https://user-images.githubusercontent.com/501822/27800820-96c16a6e-5fe0-11e7-919d-b7786bd35471.png)

## Prerequisites

* Create Twitter App (below)
* Add config variables for CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, and ACCESS_TOKEN_SECRET to your environment. The values of these variables should be copied from the Twitter page you left open in step 6 of "Create Twitter App"

## Run tests

`python3 -m unittest tests/test_timer.py tests/test_twitter.py tests/test_event.py -v`

## Run

`python3 main.py`

## Installation on Heroku

> Prerequisites: Twitter and Heroku Accounts, Heroku CLI is installed, you are logged into Heroku via Heroku CLI

### Create Twitter App

1. Visit [https://apps.twitter.com](https://apps.twitter.com)
2. Login
3. Create a new app
4. Within your app visit the "Keys and Access Tokens" tab
5. Generate your access token and access token secret
6. Leave the page open, you will need it later

### Push to Heroku

1. Pull down nashDevTwitterBot
2. cd into nashDevTwitterBot
3. Ensure nashDevTwitterBot is initialized as a git repo. If not run `git init` within nashDevTwitterBot
4. Login into Heroku via a browser and create a new app
5. Add a git remote for the Heroku app within nashDevTwitterBot **Example:** `heroku git:remote -a nash-dev-twitter-bot`
6. Push source to Heroku `git push heroku master`

### Configure Heroku Settings

1. Visit your Heroku App's "Settings" tab
2. Locate the section "Config Variables"
3. Add config variables for CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, and ACCESS_TOKEN_SECRET. The values of these variables should be copied from the Twitter page you left open in step 6 of "Create Twitter App"

### Add Scheduled Job

1. Go to your Heroku App's "Resources" tab
2. Locate the "Add-ons" section
3. Within the "Add-ons" section search for "Heroku Scheduler"
4. Confirm it as an Add-on
5. Click on "Heroku Scheduler"
6. Click "Add new job"
7. In the textfield paste in `python3 main.py`
8. Adjust "next due" to 14:00 UTC (9:00am CDT)
9. Click save
10. Test that everything is working by running `heorku run python3 main.py`
11. If it worked congrats! If not contact me at email@richardrissanen.com

Cheers.
