class File:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)


class Folder:

    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, item):
        self.items.append(item)

    def display(self):

        print(f"[Folder] {self.name}")

        for item in self.items:
            item.display()


docs = Folder("Documents")

docs.add(File("resume.pdf"))
docs.add(File("notes.txt"))

docs.display()

