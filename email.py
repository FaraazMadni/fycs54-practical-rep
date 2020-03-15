import smtplib
content='hello,sending mail from python code'
mail=smtplib.SMTP('smtp.gmail.com',25)
mail.ehlo()
mail.starttls()
mail.login('botpro70@gmail.com','ProBot@073208')
mail.sendmail('botpro70@gmail.com','minaytulla@gmail.com',content)
mail.close()
 
