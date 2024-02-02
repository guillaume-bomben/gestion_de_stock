import tkinter
from tkinter import simpledialog
from tkinter import ttk
from tkinter.ttk import *
from Product import Product
from Category import Category
from Database import Database


class dashboard:
    def __init__(self):
        self.data = None
        self.category = None
        self.product = None
        self.windows = tkinter.Tk()
        self.windows.minsize(600,400)
        self.windows.withdraw()
        self.input_mdp()
        tkinter.Button(self.windows, text="Ajouter produit", command=self.add_product).grid(row=0, column=0, padx=10, pady=10)
        tkinter.Button(self.windows, text="Modifier", command=self.update).grid(row=0, column=1, padx=10, pady=10)
        tkinter.Button(self.windows, text="Supprimer", command=self.delete).grid(row=0, column=2, padx=10, pady=10)
        tkinter.Button(self.windows, text="Ajouter category", command=self.add_category).grid(row=0, column=3, padx=10, pady=10)
        
        ##########################################
        #---------------tableau------------------#
        ##########################################
        self.tableau = Treeview(self.windows, columns=("id","nom","description","prix","quantiter","category"))
        self.tableau.heading("id", text="ID")
        self.tableau.column("id", width=40)
        
        self.tableau.heading("nom", text="Nom")
        self.tableau.column("nom", width=100)
        
        self.tableau.heading("description", text="Description")
        self.tableau.column("description", width=200)
        
        self.tableau.heading("prix", text="Prix")
        self.tableau.column("prix", width=100)
        
        self.tableau.heading("quantiter", text="Quantiter")
        self.tableau.column("quantiter", width=100)
        
        self.tableau.heading("category", text="Category")
        self.tableau.column("category", width=100)
        
        self.tableau['show'] = 'headings'
        self.tableau.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        self.list_product()
        self.windows.mainloop()


    def input_mdp(self):
        mot_de_passe = simpledialog.askstring("Mot de passe", "Veuillez entrer votre mot de passe", show='*')        
        if mot_de_passe:
            print("Mot de passe saisi")
            self.data = Database("localhost","root",mot_de_passe,"store")
            print(self.data.connect_posible)
            if self.data.connect_posible == True:
                self.category = Category(self.data)
                self.product = Product(self.data)
                self.windows.deiconify()
            else:
                self.input_mdp()
        else:
            print("Aucun mot de passe saisi.")


    def add_product(self):
        popup = tkinter.Toplevel(self.windows)
        popup.minsize(300,350)
        list_category = []
        for line in self.category.data_list:
            list_category.append(line[1])
        
        ##########################################
        #-----------------input------------------#
        ##########################################
        tkinter.Label(popup, text="Nom").pack()
        saisie_name = tkinter.Entry(popup)
        saisie_name.pack(pady=10)
        
        tkinter.Label(popup, text="Description").pack()
        saisie_description = tkinter.Entry(popup)
        saisie_description.pack(pady=10)

        tkinter.Label(popup, text="Prix").pack()
        saisie_price = tkinter.Entry(popup)
        saisie_price.pack(pady=10)
        
        tkinter.Label(popup, text="Quantité").pack()
        saisie_quantity = tkinter.Entry(popup)
        saisie_quantity.pack(pady=10)
        
        tkinter.Label(popup, text="ID Category").pack()
        saisie_category = ttk.Combobox(popup,values=list_category)
        saisie_category.pack(pady=10)

        
        tkinter.Button(popup, text="Valider", command=lambda: self.create_product(saisie_name.get(),saisie_description.get(),int(saisie_price.get()),int(saisie_quantity.get()),self.category.get_id(saisie_category.get()))).pack()


    def create_product(self, name, description, price, quantity, id_category):
        self.product.create(name,description, price, quantity, id_category)
        self.product.read()
        self.list_product()


    def list_product(self):
        for child in self.tableau.get_children():
            self.tableau.delete(child)
        for line in self.product.data_list:
            self.tableau.insert('', 'end', iid=line[0], values=(line[0], line[1], line[2], line[3], line[4], self.category.get_category(line[5])), tag="centered")
        for col in self.tableau["columns"]:
            self.tableau.tag_configure("centered", anchor="center")
            self.tableau.column(col, anchor="center")



    def update(self):
        popup = tkinter.Toplevel(self.windows)
        popup.minsize(300,350)
        if not self.tableau.selection():
            tkinter.messagebox.showwarning("Avertissement", "Veuillez sélectionner un produit à modifier.")
            return
        
        list_category = []
        for line in self.category.data_list:
            list_category.append(line[1])
        info = self.tableau.item(self.tableau.selection())['values']
        id = info[0]
        
        ##########################################
        #-----------------input------------------#
        ##########################################
        tkinter.Label(popup, text="Nom").pack()
        saisie_name = tkinter.Entry(popup)
        saisie_name.insert(0,info[1])
        saisie_name.pack(pady=10)
        
        tkinter.Label(popup, text="Description").pack() 
        saisie_description = tkinter.Entry(popup)
        saisie_description.insert(0,info[2])
        saisie_description.pack(pady=10)

        tkinter.Label(popup, text="Prix").pack()
        saisie_price = tkinter.Entry(popup)
        saisie_price.insert(0,info[3])
        saisie_price.pack(pady=10)

        tkinter.Label(popup, text="Quantité").pack()
        saisie_quantity = tkinter.Entry(popup)
        saisie_quantity.insert(0,info[4])
        saisie_quantity.pack(pady=10)
        
        tkinter.Label(popup, text="ID Category").pack()
        saisie_category = ttk.Combobox(popup,values=list_category)
        saisie_category.insert(0,info[5])
        saisie_category.pack(pady=10)
        
        tkinter.Button(popup, text="Valider", command=lambda: self.update_product(id,saisie_name.get(),saisie_description.get(),int(saisie_price.get()),int(saisie_quantity.get()),self.category.get_id(saisie_category.get()))).pack()


    def update_product(self,id, name, description, price, quantity, id_category):
        self.product.update_name(id,name)
        self.product.update_description(id,description)
        self.product.update_price(id,price)
        self.product.update_quantity(id,quantity)
        self.product.update_id_category(id,id_category)
        self.product.read()
        self.list_product()
        
    
    def delete(self):
        if not self.tableau.selection():
            tkinter.messagebox.showwarning("Avertissement", "Veuillez sélectionner un produit à supprimer.")
            return
        info = self.tableau.item(self.tableau.selection())['values']
        id = info[0]
        self.product.delete(id)
        self.product.read()
        self.list_product()

    def add_category(self):
        popup = tkinter.Toplevel(self.windows)
        popup.minsize(300,150)
        
        ##########################################
        #-----------------input------------------#
        ##########################################
        tkinter.Label(popup, text="Nom").pack()
        saisie_name = tkinter.Entry(popup)
        saisie_name.pack(pady=10)
        
        tkinter.Button(popup, text="Valider", command=lambda: self.category.create(saisie_name.get())).pack()
        