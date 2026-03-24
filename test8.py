original_str = "www.moe.gov.cn"

first_char = original_str[0]
print("第一个字符：", first_char)

first_three_chars = original_str[:3]
print("前三个字符：", first_three_chars)

last_three_chars = original_str[-3:]
print("后三个字符：", last_three_chars)

str_length = len(original_str)
print("字符串总长度：", str_length)

first_o_index = original_str.index('o')
print("字符'o'第一个位置的索引：", first_o_index)

o_count = original_str.count('o')
print("字符'o'出现的总次数：", o_count)

replaced_str = original_str.replace('.', '-')
print("替换'.'为'-'后的字符串：", replaced_str)

upper_str = original_str.upper()
print("转换为大写后的字符串：", upper_str)

split_str_list = original_str.split('.')
print("删除标点并拆分后的四个字符串：", split_str_list)

