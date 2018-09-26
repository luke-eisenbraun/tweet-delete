##Delete your tweets

Original script by [Mathew Inkson](http://www.mathewinkson.com/2015/03/delete-old-tweets-selectively-using-python-and-tweepy)

This python script cleans up after you.


**note:** This script only deletes from the 200 most recent tweets, so it
won't clear your timeline all at once (at least not as-is). However, if you schedule
it to run regularly, it will eventually work it's way back through your timeline,
assuming you schedule it to run more frequently than you post 200 tweets.

##Requirements

In order to use this script, you need:

 *  Python3
 *  Tweepy
 *  Twitter credentials
 *  A way to schedule the script (eg. cron)


##Setup
Get Twitter credentials:

  * Login to Twitter.
  * Visit [http://apps.twitter.com](https://apps.twitter.com).
  * Click "Create New App".
  * Give it a name, like "Delete my tweets," a description and URL.
    Then agree to the terms and conditions.
  * Click on the "Keys and Access Tokens" tab.
  * Copy the `Consumer Key` and `Consumer Secret` strings into the
    `config.py` file.
  * Click on the "Create my access token" button.
  * Copy the `Access Token` and `Access Token Secret` strings into
    the `config.py` file.

##Usage
Install Python libs:

    pip install -r requirements.txt

Copy the `config-template.py` file to `config.py`:

    cp config-template.py config.py

Set values in `config.py`


Run the script:

    python delete_tweets.py

## License
Apache License (2.0)
