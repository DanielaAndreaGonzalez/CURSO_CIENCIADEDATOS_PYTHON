from twilio.rest import Client

#Debemos agregar nuestras credenciales
account = "AC49a1e648c983605c3f7f9a3a3087f15c"
token = "8f860afcfce7acee4b05151eb0e651e3"
client = Client(account, token)

call = client.calls.create(to="9991231234",
                           from_="9991231234",
                           url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
print(call.sid)
