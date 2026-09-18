classes = [["Alice", "Ben"], ["Chloe", "David"]]
CN = 0 # For indexing
for _class in classes:
    CN += 1
    SN = 0 # For indexing
    print(f"CLASS {CN} Names List:")
    for name in _class:
        SN += 1
        print(f"{SN}. {name}")
    print()
