def fusionner_dicts(dict1, dict2):
    cop_dict = dict1.copy()  

    for key, value in dict2.items():
        if key in cop_dict:
            cop_dict[key] += value
        else:
            cop_dict[key] = value

    return cop_dict

# Example usage
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
result = fusionner_dicts(dict1, dict2)
print(result)  # {'a': 1, 'b': 5, 'c': 7, 'd': 5}
