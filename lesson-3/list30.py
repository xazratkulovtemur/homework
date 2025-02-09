def check_sorted_fruits():
    fruits=['banana','apple', 'cherry']
    sorted_fruits=sorted(fruits)
    if sorted_fruits==fruits:
        return True
    return False

result = check_sorted_fruits()
print(result)
