import os
import random
# Import the LaunchDarkly client.
import ldclient
from ldclient.config import Config

# Initialize the ldclient with your environment-specific SDK key.
my_secret = os.environ['LD_SDK_KEY']
ldclient.set_config(Config(my_secret))

ld_client = ldclient.get()

# The SDK starts up the first time ldclient.get() is called.

# The following if statement shows if the SDK was successfully initialized
if ldclient.get().is_initialized():
  print("SDK successfully initialized!")
else:
  print("SDK failed to initialize")
  exit()

# Launchdarkly will detect users for which the flag is evaluated, but because this program does not have user inputs, we are usin the following lines to populate users on Launchdarkly side.
  
user = {
    "key": "aa2ceb",
    "email": "tom@abc.com",
    "custom": {
      "groups": ["Customer"]
    }}
    
ldclient.get().identify(user)
    
user = {
    "key": "aa3ceb",
    "email": "andrew@abc.com",
    "custom": {
      "groups": ["Customer"]
    }}
    
ldclient.get().identify(user)
    
user = {
    "key": "aa0ceb",
    "email": "pparker@abc.com",
    "custom": {
      "groups": ["Development"]
    }}

# Call LaunchDarkly with the feature flag key you want to evaluate.
# The flag that was created in LaunchDarkly is "total-quotes".
# This flag was configured to have multiple values, numbers, from 3 to 5

# The two lines below are used as a control to check that the application is receiving the value from LaunchDarkly

flag_value = ldclient.get().variation("total-quotes", user, False)
print("Feature flag 'total-quotes' is %s for this user" % (flag_value))

# This is the basic code with the app that will make use of the feature flag
# Based on the number returned by the flag configured with LaunchDarkly, the app will include 3 to 5 possible options as Movie quotes
max_quotes = ''

quote_number = random.randint(1,flag_value)

movie_quote = ''

if quote_number == 1:
  movie_quote = 'May the Force be with you - From Star Wars'
if quote_number == 2:
  movie_quote = 'This is the way - From The Mandalorian'
if quote_number == 3:
  movie_quote = "I don't go looking for trouble. Trouble usually finds me - From Harry Potter"
if quote_number == 4:
  movie_quote = "Always - From Harry Potter" 
if quote_number == 5:
  movie_quote = "My philosophy is that worrying means you suffer twice - From Fantastic Beasts"

print(f'\n Your favorite movie quote is: \n \"{movie_quote}\"')

# Here we ensure that the SDK shuts down cleanly and has a chance to deliver analytics
# events to LaunchDarkly before the program exits. 

ldclient.get().close()