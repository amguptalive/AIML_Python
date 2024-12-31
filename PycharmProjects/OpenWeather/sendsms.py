from twilio.rest import Client

account_sid = "ACf4cdf1702ab028ceb2cacf74bbbdc739"
auth_token = "251be7f74026db6860b12a0c66fef83e"
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+18558287490',
  body='Hello from Twilio',
  to='+18777804236'
)

print(message.sid)