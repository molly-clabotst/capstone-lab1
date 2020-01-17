class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def publish(self, title):
        self.books.append(title)

    def __str__(self):
        titles = ', '.join(self.books) or 'No published books'
        return f'{self.name}, Books: {titles}'

def main():

    orwell = Author('George Orwell')
    orwell.publish('1984')
    orwell.publish('Homage to Catalonia')

    print(orwell)

main()