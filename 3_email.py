class Emal:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        return self.is_sent is True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


command = input()
while not command == 'Stop':
    self.sender, self.receiver, self.content = command.split()
    

