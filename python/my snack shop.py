snack_name= "chips"
price= 1.50
quantity= 10
is_available= True

print("snack:", snack_name)
print("price:", price)
print("in stock:", quantity)
print("available?:", is_available)

total= price*quantity
print("total value:$", total)
print("sale price:$", price-0.25)
print("double stock:$", price*2)

print("is price under $2?", price < 2)
print("more than 5 in stock?", quantity > 5)
print("is price exactly $1.50?", price==1.50)

shop_name= "Quick","snack","shop"
print("shop name:",shop_name)
print("first letter of shop name:", shop_name[0])
print("letters in snack name:",len(snack_name))

price_a = 1.50
price_b = 3.00
print("before:", price_a, "and", price_b)

temp = price_a
price_a = price_b
price_b = temp
print("after:",price_a, "and", price_b)
