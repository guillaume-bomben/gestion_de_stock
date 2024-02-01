class Category:
    def __init__(self,database):
        self.data = database
    
    def create(self,category):
        query = "INSERT INTO category (name) VALUES (%s)"
        param = (category,)
        self.data.executeQuery(query,param)
    
    def read(self):
        query = "SELECT * FROM category"
        for line in self.data.fetch(query):
            print(f"id : {line[0]}")
            print(f"category : {line[1]}")
    
    def update(self,id,new_category):
        query = "UPDATE category SET name = %s WHERE id = %s"
        param = (new_category,id)
        self.data.executeQuery(query,param)
    
    def delete(self,id):
        query = "DELETE FROM category WHERE id = %s"
        param = (id,)
        self.data.executeQuery(query,param)