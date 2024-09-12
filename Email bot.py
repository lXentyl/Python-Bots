import smtplib 
toaddrs = 'arosabg1@gmail.com'
fromaddrs = 'gutipedro915@gmail.com'
message = 'Gregori'
with smtplib.SMTP('smtp.gmail.com', '587') as smtperver:
    smtperver.ehlo()
    smtperver.starttls()
    smtperver.ehlo()
    smtperver.login('arosabg1@gmail.com', 'ooyj optu ojzy lxwl')
    for i in range(100):
        smtperver.sendmail(fromaddrs, toaddrs, message)
        print(i)
