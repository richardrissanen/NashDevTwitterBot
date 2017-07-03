# NashDev Twitter Bot

Currently the NashDev slack channel's events calendar which is tied integrated with Twitter is posted manually. This is impressive but seems quite unsustainable. Thus an automated solution should be built in order to replace the current method.

## Questions

* Is the Twitter integration with Slack the current solution?
Yes, at the moment, the Twitter integration with Slack fires the Slack post after being manually tweeted from TweetDeck.

* How are events currently sourced?
All events are sourced from cal.nashvl.org. I believe that another one of my coworkers manually loads data from Meetup.com from time to time, but most of the events are manually created by their organizers.

* Where from?
Meetup.com or single organizers or conferences

* Is there a single place that contains all events?
Yes, cal.nashvl.org contains both events from Meetup.com and anyone may contribute.

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
  * [ ] Parse Feed
  * [ ] Define Structure
  * [ ] Filter listings
  * [ ] Truncate for Twitter
  * [ ] Authorize via Tweepy
  * [ ] Tweet via Tweepy
