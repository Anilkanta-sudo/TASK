import re


def reduce_string(str_value):
    str_value = str(str_value)
    str_value = [i for i in str_value if re.sub('[a-z]', ' ', i)]
    val_list = []
    for i in str_value:
        if val_list and i == val_list[-1]:
            val_list.pop()
        else:
            val_list.append(i)
    if len(val_list) >= 1:
        return ''.join(val_list)
    else:
        return "EMPTYSTRING"


obj = reduce_string("baab")
print(obj)
