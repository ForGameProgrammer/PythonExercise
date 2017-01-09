from SMS.pytextbelt import Textbelt

Recipient = Textbelt.Recipient("+905433972004", "intl")
reponse = Recipient.send("Hello World!")
print(reponse)