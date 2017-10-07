
from fbchat import log, Client
from fbchat.models import *

Contact = "You can call him with this phone number:\n01662228388"
CheckID = "Your ID: "
Handsome = "Even God knows that :)"
defaultAnswer = "I'm a chatbot working for my boss VKing34.\n(Be still updated)\nNow he is busy\nI can answer some questions:\n1. How to contact with my boss?\n2. Check your ID/the group's ID ?\n3. Is my boss f**king handsome? 8) \nPlease choose one number:"


def contact(self, author_id, thread_id, thread_type):
    if author_id != self.uid:
        self.sendMessage(Contact, thread_id=thread_id, thread_type=thread_type)


def checkID(self, author_id, thread_id, thread_type):
    if author_id != self.uid:
        self.sendMessage(CheckID, thread_id=thread_id, thread_type=thread_type)
        self.sendMessage(self.uid, thread_id=thread_id, thread_type=thread_type)

def handsome(self, author_id, thread_id, thread_type):
    if author_id != self.uid:
        self.sendMessage(Handsome, thread_id=thread_id, thread_type=thread_type)
        self.sendTypingStatus(TypingStatus.TYPING, thread_id=thread_id, thread_type=thread_type)
        self.sendEmoji(emoji=None, size=EmojiSize.MEDIUM, thread_id=thread_id, thread_type=thread_type)


#def photo(self, author_id, threat_id, thread_type):
#    if author_id != self.uid:
#        self.sendRemoteImage('https://scontent.fhan2-2.fna.fbcdn.net/v/t1.0-9/18881746_1293811270738264_6446055320898986059_n.jpg?oh=7064456ca35ed7d234068fcb7507fe2d&oe=5A2E7241', thread_id=threat_id, thread_type=thread_type)

def other(self, author_id, thread_id, thread_type):
    if author_id != self.uid:
        self.sendMessage(defaultAnswer, thread_id=thread_id, thread_type=thread_type)

def group(self, author_id, thread_id, thread_type):
    if author_id != self.uid:
        self.sendEmoji(emoji=None, size=EmojiSize.SMALL, thread_id=thread_id, thread_type=thread_type)

class EchoBot(Client):

    def onMessage(self, author_id, message, thread_id, thread_type, **kwargs):
        self.markAsDelivered(author_id, thread_id)  # Mark an already received message
        self.markAsRead(author_id)                  # Mark an already seen message

        # Show the message
        log.info("Message from {} in {} ({}): {} .".format(author_id, thread_id, thread_type.name, message))

        # For groups:
        if thread_type == ThreadType.GROUP:
            group(self, author_id, thread_id, thread_type)

        # For individuals:
        else:
            function = choices.get(message, other)
            function(self, author_id, thread_id, thread_type)


if __name__ == '__main__':
    choices = {'1': contact, '2': checkID, '3': handsome}   # choose a particular funciton

    #Login and listen
    client = EchoBot("lzzvkingzzl@gmail.com", "Vking34100%6789")
    client.listen()
