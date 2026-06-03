class Logger:

    _instance = None

    def __new__(cls):

        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def log(self, message):
        print(f"[LOG] {message}")


logger1 = Logger()
logger2 = Logger()

logger1.log("Application Started")

print(logger1 is logger2)

## Logger

##Entire application writes through one logger.
