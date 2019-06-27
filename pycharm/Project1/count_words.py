def count_words(lst):
    d = {x: lst.count(x) for x in lst}
    return sorted(d.items(), key=lambda x: x[1], reverse=True)


text = """a a a b b c"""

print(count_words(text.split()))
