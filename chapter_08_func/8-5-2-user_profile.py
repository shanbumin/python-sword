def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('小龙', '李',
                             location='苏州',
                             sex='男')
print(user_profile)

# **user_info中的两个星号让Python创建一个名为user_info的空字典,并将收到的所有名称值对都放到这个字典中。
# 你经常会看到形参名**kwargs,它用于收集任意数量的关键字实参。

