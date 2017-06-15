from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "############"
# Your Auth Token from twilio.com/console
auth_token  = "############"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+1xxxxxxxxxx", # verified recipient phone number here
    from_="+1xxxxxxxxxx ", # your twilio number here
    body="A nice text message! :)")

print(message.sid)

