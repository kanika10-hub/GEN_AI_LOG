class Database:

    _instance = None

    def __new__(cls):

        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance


db1 = Database()
db2 = Database()

print(db1 is db2)

#ONE OBJECT TO EXIST AT A TIME 
#SO DB1 HAD Database() SEPERATELY AND DB2 HAD Database() SEPERATELY
