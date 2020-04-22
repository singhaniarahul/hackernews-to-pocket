# hackernews-to-pocket
A python program to save the top posts from hackernews to the pocket reading application

Steps to run the application:
  1. Generate the consumer key and access token from the pocket's website [here](https://getpocket.com/developer/apps/new)
  2. Replace the consumer key and access token in the pocket.properties file
  3. Modify your preferences about max items to save, max pages to surf and minimum vote count in config.properties
  4. Run save_to_pocket.py

Prerequisites:
  1. A pocket account
  2. beautifulsoup4,requests and configparser installed on your system
