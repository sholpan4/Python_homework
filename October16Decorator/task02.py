#Задание 2
#Напишите один-два примера использования декоратора `@lru_cache` 
#для методов класса. Например, для запросов к базе данных TynyDB.

from functools import lru_cache
from tinydb import TinyDB, Query


class DatabaseHandler:
    def __init__(self, db_path):
        self.db = TinyDB(db_path)
        self.query = Query()
        
    @lru_cache(maxsize=None)
    def get_user_data(self, user_id):
        print(f"User data for user_id {user_id}")
        result = self.db.get(self.query.user_id == user_id) #как работать с query?
        return result
    
db_handler = DatabaseHandler('my_database.json')
user_data = db_handler.get_user_data(1)
print(user_data)

user_data = db_handler.get_user_data(1)
print(user_data)