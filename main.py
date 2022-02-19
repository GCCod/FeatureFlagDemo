import random
# Import the LaunchDarkly client.
import ldclient
from ldclient.config import Config

# Initialize the ldclient with your environment-specific SDK key.

ldclient.set_config(Config("sdk-a4ffb164-6f96-4593-94ef-715434d4806b"))

ld_client = ldclient.get()

# The SDK starts up the first time ldclient.get() is called.
if ldclient.get().is_initialized():
  print("SDK successfully initialized!")
else:
  print("SDK failed to initialize")
  exit()

user = {
      "key": "anon",
      "anonymous": True
    }

# Call LaunchDarkly with the feature flag key you want to evaluate.
# The flag that was created in LaunchDarkly is "total-quotes".
# This flag was configured to have multiple values, numbers, from 3 to 5

# The two lines below are used as a control to check that the application is receiving the value from LaunchDarkly

flag_value = ldclient.get().variation("total-quotes", user, False)
print("Feature flag 'total-quotes' is %s for this user" % (flag_value))



# This is the basic code with the app that will make use of the feature flag
# Based on the number returned by the flag configured with LaunchDarkly, the app will include 3 to 5 possible options as Movie quotes
max_quotes = ''

if flag_value == 3:
  max_quotes = 3
if flag_value == 4:
  max_quotes = 4
if flag_value == 5:
  max_quotes = 5

quote_number = random.randint(1,max_quotes)

movie_quote = ''


if quote_number == 1:
  movie_quote = 'May the Force be with you - From Star Wars'
if quote_number == 2:
  movie_quote = 'This is the way - From The Mandalorian'
if quote_number == 3:
  movie_quote = "I don't go looking for trouble. Troble usually finds me - From Harry Potter"
if quote_number == 4:
  movie_quote = "Always - From Harry Potter" 
if quote_number == 5:
  movie_quote = "My philosophy is that worrying means you suffer twice - From Fantastic Beasts"

print(f'\n Your favorite movie quote is: \n \"{movie_quote}\"')

# Here we ensure that the SDK shuts down cleanly and has a chance to deliver analytics
# events to LaunchDarkly before the program exits. 

ldclient.get().close()