import json

"""id
    name
    sale_price
    qty
    base_price
""" 
class ProductDatabase:
    db = []
    id = 0
    def __init__(self):
        pass
    
    @staticmethod
    def from_json(JSON):
        my_dict = json.loads(JSON)
        record = {"id": 0, "name": "", "sale_price": 0, "qty": 0,  "base_price": 0}
        if 'name' in my_dict:
            record["name"] = my_dict["name"]
        if 'sale_price' in my_dict:
            record["sale_price"] = my_dict["sale_price"]
        if 'base_price' in my_dict:
            record["base_price"] = my_dict["base_price"]
        if 'qty' in my_dict:
            record["qty"] = my_dict["qty"]

        result = ProductDatabase()
        result.add(record)
        
        return result
    
    def add(self, record):
        self.id += 1
        record["id"] = self.id
        self.db.append(record)
        return record["id"]
        
    def get(self, id):
        for a in self.db:
            if id == a["id"]:
                return a
            
    def update(self, id, new_record):
        for a in self.db:
            if id == a["id"]:
                if 'name' in new_record:
                    a["name"] = new_record["name"]
                if 'sale_price' in new_record:
                    a["sale_price"] = new_record["sale_price"]
                if 'base_price' in new_record:
                    a["base_price"] = new_record["base_price"]
                if 'qty' in new_record:
                    a["qty"] = new_record["qty"]
                return True
            
    def delete(self, id):
        for a in self.db:
            if id == a["id"]:
                self.db.remove(a)
                
    def to_json(self):
        result = json.dumps(self.db)
        return result
        
prod = ProductDatabase.from_json('{"name": "apple", "sale_price": 200, "qty": 5,  "base_price": 100}')
prod.add({"name": "apple", "sale_price": 200, "qty": 5,  "base_price": 100})
prod.add({"name": "grape", "sale_price": 200, "qty": 5,  "base_price": 100})
prod.add({"name": "watermelon", "sale_price": 200, "qty": 5,  "base_price": 100})
# print(prod.db)
prod.update(1, {"name": "banana"})
prod.delete(1)
print(prod.db)
print(prod.get(1))

res = prod.to_json()
print(res)

#CRUD create, read, update, delete