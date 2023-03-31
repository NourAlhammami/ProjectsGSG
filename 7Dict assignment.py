while True:
    while True:
        total_num_products = int(input("Enter the Total Number of Products: "))
        products_data = []
        if total_num_products < 0:
            print("Invalid Input")
        else:
            break
    for i in range(total_num_products):
        product_name = str(input(f"Enter the {i + 1 } Product Name: "))
        product_quantity = int(input(f"Enter the {i + 1 } Product Quantity: "))
        product_price = float(input(f"Enter the {i + 1 } Product Price: "))
        enter_product_data = {
            "product_name" : product_name,
            "product_quantity" : product_quantity,
            "product_price" : product_price
        }
        products_data.append(enter_product_data)
    print("Products have been added successfully")
    # print(products_data)

    while True:
        selected_number = int(input("""Select 1. For Add New Product
Select 2. Search using Product Name
Select 3. Exit
"""))
        if selected_number == 1:
            break
        elif selected_number == 2:
            searched_name = str(input("Enter the name to search for: "))
            for i in products_data:
                names = i["product_name"]
                if searched_name not in names:
                    continue
                else:
                    print(i)
                    break
            continue
        else:
            print("Goodbye")
            break
        break

# __________________________________________________________________________________________
#
# products_list = []
#
#
# def find_product(items_list, key, value):
#     result_list = []
#     for item in items_list:
#         if value in item.get(key):
#             result_list.append(item)
#     return result_list
#
#
# while True:
#     t = int(input("Select 1.Enter new Product\nSelect 2.Search using product name"
#                   "\nSelect 3.Exit"))
#     if t == 1:
#         products_number = int(input("Enter Total Products Number"))
#         if products_number <= 0:
#             exit()
#         for i in range(products_number):
#             product_name = input(f"Enter Product {i + 1} Name : ")
#             product_price = float(input(f"Enter Product {i + 1} Price : "))
#             product_qty = int(input(f"Enter Product {i + 1} Quantity : "))
#             product = {
#                 "name": product_name,
#                 "price": product_price,
#                 "qty": product_qty
#             }
#             products_list.append(product)
#             print(f"{product_name} has been added successfully")
#     elif t == 2:
#         text = input("Enter Product Name")
#         result = find_product(products_list, "name", text)
#         if len(result) == 0:
#             print("Product Not Exist")
#         else:
#             print(result)
#     else:
#         exit()
