import json

class Resource:
    def __init__(self, id, title, author, year):
        self.id = id
        self.title = title
        self.author = author
        self.year = year

class ResourceManager:
    def __init__(self):
        self.resources = []

    def create_resource(self, resource):
        self.resources.append(resource)

    def find_resources(self, attribute, value):
        return [res for res in self.resources if getattr(res, attribute, None) == value]

    def update_resource(self, id, new_attributes):
        resource = next((r for r in self.resources if r.id == id), None)
        if resource:
            for key, value in new_attributes.items():
                if key != 'id':  # Ensure ID is not modified
                    setattr(resource, key, value)

    def delete_resource(self, id):
        self.resources = [res for res in self.resources if res.id != id]

class DataPersistenceManager:
    @staticmethod
    def save_data(resources, filename):
        data = [{"id": res.id, "title": res.title, "author": res.author, "year": res.year} for res in resources]
        try:
            with open(filename, 'w') as file:
                json.dump(data, file)
        except Exception as e:
            print(f"Error saving data: {e}")

    @staticmethod
    def load_data(filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
            return [Resource(**item) for item in data]
        except FileNotFoundError:
            print("Data file not found. Starting with an empty collection.")
            return []
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return []

class UI:
    @staticmethod
    def input_resource_details():
        while True:
            try:
                id = int(input("Enter ID: "))
                title = input("Enter Title: ")
                author = input("Enter Author: ")
                year = int(input("Enter Year: "))
                return Resource(id, title, author, year)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    @staticmethod
    def display_resources(resources):
        for res in resources:
            print(f"ID: {res.id}, Title: {res.title}, Author: {res.author}, Year: {res.year}")

if __name__ == "__main__":
    data_file = "resources.json"
    resource_manager = ResourceManager()
    resource_manager.resources = DataPersistenceManager.load_data(data_file)

    running = True
    try:
        while running:
            print("\n1. Create\n2. Read/Search\n3. Edit\n4. Delete\n5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                new_resource = UI.input_resource_details()
                resource_manager.create_resource(new_resource)

            elif choice == "2":
                attribute = input("Enter attribute to search (e.g., title): ")
                value = input(f"Enter {attribute} value: ")
                found_resources = resource_manager.find_resources(attribute, value)
                UI.display_resources(found_resources)

            elif choice == "3":
                id = input("Enter ID to edit: ")
                new_attributes = UI.input_resource_details()
                resource_manager.update_resource(id, vars(new_attributes))

            elif choice == "4":
                id = input("Enter ID to delete: ")
                resource_manager.delete_resource(id)

            elif choice == "5":
                DataPersistenceManager.save_data(resource_manager.resources, data_file)
                running = False

    except Exception as e:
        print(f"An error occurred: {e}")
        DataPersistenceManager.save_data(resource_manager.resources, data_file)
