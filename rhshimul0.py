import smtplib
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login("doubleaech1@gmail.com","11223344$")
print '    '
email = raw_input('Attacker Gmail Address : ')
for i in range(50):
    server.sendmail("torbap@gmail.com","doubleaech3@gmail.com","Tor mare chudi")
    print 'massage has been send'
    
  print 'REDREX-RH SHIMUL'