
class LoggingContext:
    def __enter__(self):
        print("Initializing logging context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Cleaning logging context")
        print("Exception details: {}, {}, {}".format(exc_type, exc_val, exc_tb))
        return

    def info(self, mssg):
        print("INFO - {}".format(mssg))

    def error(self, mssg):
        print("ERROR - {}".format(mssg))
