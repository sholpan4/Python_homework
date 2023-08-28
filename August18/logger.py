
class Logger:
    ERROR = 0
    INFO = 0
    WARNING = 0
    DEBUG = 0
    TRACE = 0

log = Logger(Logger.DEBUG, file='myapp.log')


log.w("Это warning сообщение", 1, 2, 3)
log.t("Это trace сообщение", 4, 5, 6)
log.e("Это error сообщение", 7, 8, 9, end='\n\n')