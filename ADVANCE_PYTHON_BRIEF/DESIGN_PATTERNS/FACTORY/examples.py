class Dog:

    def speak(self):
        return "Woof"


class Cat:

    def speak(self):
        return "Meow"


class AnimalFactory:

    @staticmethod
    def create(animal):

        if animal == "dog":
            return Dog()

        return Cat()


pet = AnimalFactory.create("dog")

print(pet.speak())


#here instead of typing dog and cat seperatly , the person will use AnimalFactory class for every animal usecase 
