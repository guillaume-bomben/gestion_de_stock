class Product:
    def __init__(self,database):
        self.data = database
        self.data_list = []
        self.read()
    
    def create(self,name,description,price,quantity,id_category):
        query = "INSERT INTO product (name,description,price,quantity,id_category) VALUES (%s,%s,%s,%s,%s)"
        param = (name,description,price,quantity,id_category)
        self.data.executeQuery(query,param)
    
    def read(self):
        query = "SELECT * FROM product"
        self.data_list = []
        for line in self.data.fetch(query):
            self.data_list.append(line)
    
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