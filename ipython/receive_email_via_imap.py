import imaplib

username = 'someuser'
password = 'password'

mail_server = 'mail.somedomain.com';

i = imaplib.IMAP4_SSL(mail_server)

print(i.login(username, password))

print(i.select("INBOX"))

for msg_id in i.search(None, 'ALL')[1][0].split():
    print(msg_id)
    outf = open("%s.eml" % msg_id, 'w')
    outf.write(i.fetch(msg_id,'(UID BODY[TEXT])'))

i.logout()
