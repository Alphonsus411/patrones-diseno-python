

class LegacyDatabase:
    def insert_data(self, data):
        print(f"Inserted data into legacy database: {data}")

    def get_data(self):
        return "Data from legacy database"


class DataBaseAdapter:
    def __init__(self, legacy_database):
        self.legacy_database = legacy_database

    def add(self, data):
        self.legacy_database.insert_data(data)

    def retrieve(self):
        return self.legacy_database.get_data()


class NewSystem:
    def __init__(self, database):
        self.database = database

    def save_data(self, data):
        self.database.add(data)
        print("Data saved in the new system.")

    def  load_data(self):
        data = self.database.retrieve()
        print(f"Data loaded from the new system: {data}")


legacy_database = LegacyDatabase()
adapter = DataBaseAdapter(legacy_database)

new_system = NewSystem(adapter)
new_system.save_data("Import data")
new_system.load_data()


