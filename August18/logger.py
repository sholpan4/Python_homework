import sys

class Logger:
    ERROR = 0
    INFO = 1
    WARNING = 2
    DEBUG = 3
    TRACE = 4

    colors = {
        ERROR:   "\033[91m", #red
        INFO:    "\033[94m", #blue
        WARNING: "\033[93m", # yellow
        DEBUG:   "\033[92m", #green
        TRACE:   "\033[90m" #gray
    }

    endc = "\033[0m"

    def __init__(self, level, stdout=True, file=None):
        self.level = level
        self.stdout = stdout
        self.file = file

    def set_level(self, level):
        self.level = level

    def log(self, message, *args, level, end='\n'):
        if level <= self.level:
            log_message = f"[{level}] {message} {' '.join(map(str, args))}"
            if self.stdout:
                print(f"{self.colors.get(level, '')}{log_message}{self.endc}", end=end)
                if self.file:
                    with open(self.file, 'a') as f:
                        f.write(log_message + end)

    def e(self, message, *args, end='\n'):
        self.log(message, *args, level=self.ERROR, end=end)
    
    def i(self, message, *args, end='\n'):
        self.log(message, *args, level=self.INFO, end=end)

    def w(self, message, *args, end='\n'):
        self.log(message, *args, level=self.WARNING, end=end)

    def d(self, message, *args, end='\n'):
        self.log(message, *args, level=self.DEBUG, end=end)

    def t(self, message, *args, end='\n'):
        self.log(message, *args, level=self.TRACE, end=end)

if __name__ == '__main__':
    log = Logger(Logger.DEBUG, file='myapp.log')
    log.i("This in INFO message", 1, 2, 3)
    log.t("This in TRACE message", 4, 5, 6)
    log.e("This in ERROR message", 7, 8, 9, end='\n\n')

    log.set_level(Logger.WARNING)

    log.i("This in INFO message, invisible")
    log.w("This in WARNING message", 1, 2, 3)   

    log.set_level(Logger.DEBUG)

    log.d("This in DEBUG message", 4, 5, 6)
    log.t("This in TRACE message", 7, 8, 9, end='\n\n') 