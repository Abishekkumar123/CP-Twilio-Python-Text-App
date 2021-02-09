from twilio.rest import TwilioRestClient
from credentials import account_sid, auth_token, my_cell, my_twilio

# Find these values at https://twilio.com/user/account
client = TwilioRestClient(account_sid, auth_token)

my_msg = "669575 is your SECRET one time password (OTP) for payment of Rs. 990.00 via GOOGLEPLAYMASTERM via Netbanking. Do not share it with anyone."

message = client.messages.create(to=my_cell, from_=my_twilio,
                                     body=my_msg)
