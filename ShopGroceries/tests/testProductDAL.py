from ShopGroceries.data_access_layer.ProductDAL import ProductDAL

product_dal = ProductDAL()
product_dal.connect()
products = product_dal.get_list_products()
for product in products:
    print(product)