# TwitterBot without API
A couple of Python scripts to follow, unfollow and drop likes and retweets automathicaly without API, just with a chrome dirver and the Selenium-python library.
## What do you need to start using the TwitterBot?
### - Twitter account
[Create a new account](https://twitter.com/i/flow/signup) or use your own
### - [Python](https://www.python.org/)
### - Selenium-python library
```
pip install selenium
```
### - time-python library
```
pip install time
```
### - random-python library
```
pip install random
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
