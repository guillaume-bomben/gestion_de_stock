from Database import Database

class product:
    def __init__(self,host,user,password,database):
        self.data = Database(host,user,password,database)
    
    def create(self,name,description,price,quantity,id_category):
        query = "INSERT INTO product (name,description,price,quantity,id_category) VALUES (%s,%s,%s,%s,%s)"
        param = (name,description,price,quantity,id_category)
        self.data.executeQuery(query,param)
    
    def read(self):
        query = "SELECT * FROM product"
        for line in self.data.fetch(query):
            print(f"id : {line[0]}")
            print(f"name : {line[1]}")
            print(f"description : {line[2]}")
            print(f"price : {line[3]}")
            print(f"quantity : {line[4]}")
            print(f"id_category : {line[5]}")
    
    def update_name(self,id,name):
        query = "UPDATE product SET name = %s WHERE id = %s"
        param = (name,id)
        self.data.executeQuery(query,param)
    
    def update_description(self,id,description):
        query = "UPDATE product SET description = %s WHERE id = %s"
        param = (description,id)
        self.data.executeQuery(query,param)
    
    def update_price(self,id,price):
        query = "UPDATE product SET price = %s WHERE id = %s"
        param = (price,id)
        self.data.executeQuery(query,param)
    
    def update_quantity(self,id,quantity):
        query = "UPDATE product SET quantity = %s WHERE id = %s"
        param = (quantity,id)
        self.data.executeQuery(query,param)
    
    def update_id_category(self,id,id_category):
        query = "UPDATE product SET id_category = %s WHERE id = %s"
        param = (id_category,id)
        self.data.executeQuery(query,param)
    
    def delete(self,id):
        query = "DELETE FROM product WHERE id = %s"
        param = (id,)
        self.data.executeQuery(query,param)