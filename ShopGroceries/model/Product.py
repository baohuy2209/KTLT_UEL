class Product:
    def __init__(self, ProductID, Name, Quantity, Price, ProductType):
        self.ProductID = ProductID
        self.Name = Name
        self.Quantity = Quantity
        self.Price = Price
        self.ProductType = ProductType
    def __str__(self):
        info = f"Information about {self.Name}: \n +ProductID: {self.ProductID} \n +Name: {self.Name} \n + Quantity: {self.Quantity} \n +Price: {self.Price} \n+ Type: {self.ProductType}"
        return info