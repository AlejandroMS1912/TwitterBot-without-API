# TwitterBot without API

A few of scripts that use an inputed hashtag or username as an index to execute the ordered action (Follow, unfollow, like or retweet) using random and customizable time intervals to avoid the Twitter's ban systems.

**It works just with a chrome driver and his python library *Selenium-python*.**

**Without API/Tweepy**

## What do you need to start using the TwitterBot?
### - Twitter account
[Create a new account](https://twitter.com/i/flow/signup) or use your own
### - [Python](https://www.python.org/)
### - [Selenium-python library](https://pypi.org/project/selenium/)
```
pip install selenium
```
### - [Python-time library](https://pypi.org/project/python-time/)
```
pip install python-time
```
### - [Random-python library](https://pypi.org/project/random2/)
```
pip install random2
```
### - [Chrome driver](https://chromedriver.chromium.org/downloads)
- Check your Chrome version

First step             |  Second step
:-------------------------:|:-------------------------:
![](https://user-images.githubusercontent.com/110389988/199535024-4404c8a1-d73a-48ba-9d77-8e65fa04453e.jpg)  |  ![](https://user-images.githubusercontent.com/110389988/199537114-e23bf8ac-9a95-4a78-aff4-cdf843b5ccce.jpg)
- [CLICK HERE](https://chromedriver.chromium.org/downloads) and download the Chromedriver with the corresponding version

First step             |  Second step
:-------------------------:|:-------------------------:
![](https://user-images.githubusercontent.com/110389988/199540825-4c5c5cae-b8c9-4d15-9251-40f5818bc3b8.jpg)  |  ![](https://user-images.githubusercontent.com/110389988/199542285-37d11d45-f4b5-4af4-8d56-58c74f340513.png)

**When you have already installed the chromedriver.exe copy it to the TwitterBot scripts folder in Visual Studio Code and you can start running it**

> **Warning**
> REMEMBER THAT YOU HAVE TO SPECIFY THE PATH OF THE chromedriver.exe IN EACH OF THE SCRIPTS

## How do it works?

This repository is divided into 4 folders ([FollowScripts](https://github.com/AlejandroMS1912/TwitterBot-without-API/tree/main/FollowScripts), [UnfollowScript](https://github.com/AlejandroMS1912/TwitterBot-without-API/tree/main/UnfollowScript), [LikeScripts](https://github.com/AlejandroMS1912/TwitterBot-without-API/tree/main/LikeScripts) and [RetweetScripts](https://github.com/AlejandroMS1912/TwitterBot-without-API/tree/main/RetweetScripts)) but the idea of all of them is the same, execute their action according to their input parameters.


We can introduce a username (ex. 'elonmusk') so that the bot goes directly to his profile and starts executing the action (Follow his followers or like and retweet his tweets) or we can also introduce a hashtag/keyword (ex. 'drop handles') as an index to execute the action (Like and retweet the tweets founded in that hashtag or start following the followers of each of the users who have tweeted that hashtag/keyword)

> **Note**
> *Obiusly the UnfollowScript only can use as input your own username*

## Here you have 4 YT videos to exemplify the operation of each script:
### - [TwitterBot to FOLLOW automatically without API](https://www.youtube.com/watch?v=nc2t4aSK0rU&t=0s)
### - [TwitterBot to UNFOLLOW automatically without API](https://www.youtube.com/watch?v=gcVIfo9Z_6o&t=0s)
### - [TwitterBot to RETWEET automatically without API](https://www.youtube.com/watch?v=1Cyi6Zy5CQ4&t=0s)
### - [TwitterBot to LIKE tweets automatically without API](https://www.youtube.com/watch?v=XoR1Ak_FxAA&t=0s)


## How to avoid Twitter bans?

### Follows and unfollows limits:

According to the [Twitter privacy policy](https://help.twitter.com/en/using-twitter/twitter-follow-limit), the number of accounts you can follow is not limitited in fact, but there are some conditions about the pace as wich you can do so:
- **The maximum number of accounts you can follow in a day is 400**. Verified Twitter accounts are able to follow up to 1,000 accounts per day.
- **You can only follow 5000 accounts**. Once you reach that number, you may need to wait until your account has more followers before you can follow additional accounts.
- You should not spam constantly follows or unfollows. The number of follows/unfollows that you can do continuosly is limited and it is recommended make an step of a few seconds between each follow/unfollow. The cooldowns that are usually been used are **series of 20/30 follows with a break of 10 minutes each one of them and a interval of 3/15 seconds between each follow/unfollow.**

### Tweet/Retweet limits:

- According to the [Twitter privacy policy](https://help.twitter.com/es/rules-and-policies/twitter-limits), **the maximum number of tweets you can post in a day is 2400**. The daily update limit is subdivided into smaller limits with half-hour intervals. Retweets are counted as Tweets.

### Liking limits: 

It seems that there is not any limit for liking tweets


> **Note**
> **This bot uses random intervals of time each follow with the goal of appearing as natural as possible against Twitter's ban systems. You can modify all of these intervals to fit your needs.**


## Conclusion


In resume, this bot uses an inputed hashtag or username as an index to execute the ordered action (Follow, unfollow, like or retweet) using random and customizable time intervals to avoid the Twitter's ban systems. This is very useful because you can get interactions back from your target keyword.

The fact of not using the Twitter API makes the bot's actions much more difficult to detect for the application's tracking systems.

## Future Projects

This is just a tiny sample of what could be achieved by following this working method. In this repository I have shown how to develop the basic functions of Twitter as a starting point but there is a universe of possibilities beyond this.
- If you have a custom phone cases shop, for example, I could make a script that replies with a custom text (even with a link to your shop) to every person who has ever tweeted "phone case". Or interact with each tweet published by the main mobile phone brands. Or block anyone who interacts with you with the "she/her he/him" in their bio... the possibilities are endless
- I could also do something similar on any other social network like Instagram, Facebook, Reddit, TikTok... (with a few of time to understand its html structure)

If you are interested in something like this, I'm here to help with whatever is needed
