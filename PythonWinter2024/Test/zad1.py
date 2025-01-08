def group_and_sum(data):
    res_dict = {}
    for item in data:
        cat_name = str.lower(item[0])
        if cat_name not in res_dict:
            res_dict[cat_name] = item[1]
        else:
            res_dict[cat_name] += item[1]

    res_lst = sorted(list(res_dict.items()), key=lambda x: x[1], reverse=True)

    return res_dict, res_lst


example1 = [("owoce", 5),
        ("Warzywa", 2),
        ("Owoce", 2),
        ("napoje", 10),
        ("Napoje", 1),
        ("warzywa", 7)]

print(group_and_sum(example1))
