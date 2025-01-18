class Catalog:
    def __init__(self, CatalogId, Name):
        self.CataLogId = CatalogId
        self.Name = Name
    def __str__(self):
        info = f"ID: {self.CataLogId} - Name: {self.Name}"
        return info