# Singleton Pattern demo: Logger
class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.logs = []
        return cls._instance

    def log(self, msg):
        self.logs.append(msg)
        print("LOG:", msg)

# Test
a = Logger()
b = Logger()
a.log("App started")
b.log("User logged in")
print("Same instance?", a is b)
