from twilio.rest import Client 
 
account_sid = 'AC5211cc1cc90014631d6637de01293461' 
auth_token = 'd673cef687b45b9c65b669c5c870a25f' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='+12513255848',  
                              body='HEYyyy',      
                              to='+918939245810' 
                          ) 
 
print(message.sid)