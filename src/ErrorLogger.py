import os
import datetime


class ErrorLoggerSingleton:
    _instance = None

    def __new__(cls, log_dir="logs"):
        if cls._instance is None:
            cls._instance = super(ErrorLoggerSingleton, cls).__new__(cls, log_dir)
            os.makedirs(log_dir, exist_ok=True)
            cls._instance.log_dump_path = f"{log_dir}/failure.log"
            cls._instance.log_file = open(cls._instance.log_dump_path, "a")
            
        return cls._instance
        

log_error = ErrorLoggerSingleton()

def log_failure(self, e):
    self.log_error.write(f"{datetime.datetime.now()} - Failure: %s\n" % (str(e)))
