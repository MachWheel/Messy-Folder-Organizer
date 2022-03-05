from .names import log_name

class Logger:
    def __init__(self, working_folder):
        self.working_folder = working_folder

    def log(self, message):
        with open(f"{self.working_folder}/{log_name}.txt", 'a') as log_file:
            log_file.write(message)
            print(message)
