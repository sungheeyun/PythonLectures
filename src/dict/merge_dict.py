def merge_dict(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)

    return merged_dict


def merge_dict1(dict1, dict2):
    merged_dict = dict()
    for key, value in dict1.items():
        merged_dict[key] = value

    for key, value in dict2.items():
        merged_dict[key] = value

    return merged_dict
