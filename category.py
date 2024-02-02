class Category:
    def __init__(self,database):
        self.data = database
        self.data_list = []
        self.read()
    
    def create(self,category):
        query = "INSERT INTO category (name) VALUES (%s)"
        param = (category,)
        self.data.executeQuery(query,param)
    
    def read(self):
        query = "SELECT * FROM category"
        self.data_list = []
        for line in self.data.fetch(query):
            self.data_list.append(line)
    
    def update(self,id,new_category):
        query = "UPDATE category SET name = %s WHERE id = %s"
        param = (new_category,id)
        self.data.executeQuery(query,param)
    
    def delete(self,id):
        query = "DELETE FROM category WHERE id = %s"
        param = (id,)
        self.data.executeQuery(query,param)
    
    def get_category(self,id):
        query = "SELECT name FROM category WHERE id = %s"
        param = (id,)
        return self.data.fetch(query,param)[0][0]
    
    def get_id(self,category):
        query = "SELECT id FROM category WHERE name = %s"
        param = (category,)
        return self.data.fetch(query,param)[0][0]