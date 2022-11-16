dict_example = {"f": 5, "a": 1, "c": 3, "d": 2, "b": 4}

# sorted 사용 시 리스트가 반환되므로 dict를 사용하여 딕셔너리로 변환함
dict_example_sorted = sorted(dict_example.items())
print(f"dict_example_sorted : {dict_example_sorted}")  # dict_example_sorted : {'a': 1, 'b': 4, 'c': 3, 'd': 2, 'f': 5}
