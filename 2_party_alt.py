class Party:
    def __init__(self):
        self.people = []


party = Party()

command = input()
while not command == 'End':
    person = command
    party.people.append(person)
    command = input()

print(f"Going: {', '.join(party.people)}")
print(f'Total: {len(party.people)}')
