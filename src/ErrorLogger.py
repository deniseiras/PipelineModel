import os
import datetime


class ErrorLoggerSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ErrorLoggerSingleton, cls).__new__(cls)

        return cls._instance

    def __init__(self, log_dir="logs") -> None:
        os.makedirs(log_dir, exist_ok=True)
        self.log_dump_path = f"{log_dir}/failure.log"
        self.log_file = open(self.log_dump_path, "a")

    def log_failure(self, e):
        fail_str = f"{datetime.datetime.now()} - Failure: %s\n" % (str(e))
        print(fail_str)
        self.log_file.write(fail_str)

log_error = ErrorLoggerSingleton()

def log_failure(e):
    log_error.log_failure(e)


