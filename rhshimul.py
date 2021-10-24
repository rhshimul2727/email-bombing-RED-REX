import smtplib
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login("doubleaech1@gmail.com","11223344$")
for i in range(50):
    server.sendmail("yourmaul@gmail.com","doubleaech3@gmail.com","Tor mare chudi")
    print 'email = raw_input('Attacker Gmail Address : ')
   
    print 'massage has been send'


    print 'REDREX-----########'
