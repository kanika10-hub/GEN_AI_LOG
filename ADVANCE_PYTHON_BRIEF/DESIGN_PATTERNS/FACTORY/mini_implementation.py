class GPT:

    def generate(self):
        print("Using GPT")


class Claude:

    def generate(self):
        print("Using Claude")


class ModelFactory:

    @staticmethod
    def create(model):

        if model == "gpt":
            return GPT()

        return Claude()


model = ModelFactory.create("gpt")

model.generate()


#using MOdelFactory instead of using the 2 classes seperatly
