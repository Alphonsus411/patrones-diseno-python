import uuid

class MySingleton:
    _instance = None
    id = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating new singleton instance")
            cls._instance = super(MySingleton, cls).__new__(cls)
            cls.id = uuid.uuid4()

        return cls._instance


instance1 = MySingleton()
print(f"Instance 1 id: {instance1.id}")

instance2 = MySingleton()
print(f"Instance 2 id: {instance2.id}")

instance3 = MySingleton()
print(f"Instance 3 id: {instance3.id}")