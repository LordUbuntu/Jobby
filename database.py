import pymongo


# NOTE this is a standard template for a database wrapper.
#      this will probably be replaced by a more specialized one, or a
#        specialized extension as the need arises.
class database:
    # default host and port
    host = "localhost"
    port = 27017
    # default collection record object
    collection = "test"
    db = None

    def __init__(self, collection=collection, host=host, port=port):
        self.host = host
        self.port = port
        self.collection = collection
        self.db = pymongo.MongoClient(host, port)[f"{self.collection}"]

    def insert(self, data: list[dict]):
        self.db[f"{self.collection}"].insert_many(data)

    def find(self, attribute: dict):
        # not sure whether this should return an object that can be queried further, or whether this should simply return a list
        return self.db[f"{self.collection}"].find(attribute)

    def count(self, attribute: dict):
        return self.db[f"{self.collection}"].count_documents(attribute)


# this is for testing database functions interactively. Testing for wimps >:[
test = database()
