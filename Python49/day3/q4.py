#Here we get the Product details like product Id and order amount.
#Then we check and show the product name and net amount(after discount).

pro_id = int(input("Enter Product_id :"))
ord_amt = int(input("Enter Order Amount :"))

des_amt = 0

if pro_id == 1 and ord_amt > 1000:
    des_amt = ord_amt * 10 / 100
    net_amt = ord_amt - des_amt
    print("Product Name is Transistors.")
    print("Total Amount =",net_amt)

if pro_id == 2 and ord_amt > 100:
    des_amt = ord_amt * 5 / 100
    net_amt = ord_amt - des_amt
    print("Product Name is Resisters.")
    print("Total Amount =",net_amt)

if pro_id == 3 and ord_amt > 500:
    des_amt = ord_amt * 10 / 100
    net_amt = ord_amt - des_amt
    print("Product Name is Capacitors.")
    print("Total Amount =",net_amt)

if pro_id > 3:
    print("Enter Proper Product id!!!")