def make_pizza( *toppings):
    """打印顾客点的所有配料"""
    print(toppings)

make_pizza('a')
make_pizza('a','b','c')

# 形参名*toppings中的型号让Python创建一个名为toppings的空元组(元组看成不可变的数组)

