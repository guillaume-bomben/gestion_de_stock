import getpass
from category import category

password = getpass.getpass("Entrez un mdp : ")
data = category("localhost","root",password,"store")


data.create("test")


