#10.How to create nested dictionary and if it contains list as a value how to append element and modify and remove from that list.

nested_dict = {
    "class1": {
        "students": ["a", "b", "c"],
        "teacher": "abc"
    },
    "class2": {
        "students": ["d", "e", "f"],
        "teacher": "def"
    }
}

# Append element to list in nested dictionary
nested_dict["class1"]["students"].append("g")

# Modify element in list in nested dictionary
nested_dict["class2"]["students"][0] = "d_changed"

# Remove element from list in nested dictionary
nested_dict["class1"]["students"].remove("b")

print(nested_dict)