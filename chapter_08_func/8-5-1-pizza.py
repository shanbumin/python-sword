def make_pizza( size,*args):
    """概述要制作的披萨"""
    print(f"\n制作{size}英寸披萨使用了下面的配料:")
    for topping in args:
        print(f"-{topping}")

make_pizza(12,'a','b','c')


# 你经常会看到通用形参名*args,用来收集任务数量的位置实参

