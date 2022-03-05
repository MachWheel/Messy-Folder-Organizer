from .names import log_name

class Log:
    def __init__(self, working_folder):
        self.working_folder = working_folder
        self.log_file = f"{self.working_folder}/{log_name}.txt"

    def msg(self, message):
        with open(self.log_file, 'a') as log_file:
            log_file.write(message)
            print(message)
