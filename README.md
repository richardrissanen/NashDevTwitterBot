# NashDev Twitter Bot

Automate posting events from cal.nashvl.org to Twitter

## Proposed Solution
![overview](https://user-images.githubusercontent.com/501822/27800820-96c16a6e-5fe0-11e7-919d-b7786bd35471.png)

## ToDo
* [X] Get a Github Repo
* [X] Write a readme
* [X] Answer Questions
* [X] Scope work
* [X] Add scoped work to ToDo
* [ ] Write docs
* [ ] Write tests
* [ ] Implement
  * [X] Parse Feed
  * [X] Define Structure
  * [X] Filter listings
  * [ ] Truncate for Twitter
  * [X] Authorize via Tweepy
  * [X] Tweet via Tweepy

## Installation on Heroku
> Prerequisites: Heroku Account, Heroku CLI is installed, you are logged into Heroku via Heroku CLI

1. Pull down nashDevTwitterBot
2. cd into nashDevTwitterBot
3. Ensure nashDevTwitterBot is initialized as a git repo. If not run `git init` within nashDevTwitterBot
4. Login into Heroku via a browser and create a new app
5. Add a git remote for the Heroku app within nashDevTwitterBot **Example:** `heroku git:remote -a nash-dev-twitter-bot`
6. Push source to Heroku `git push heroku master`
