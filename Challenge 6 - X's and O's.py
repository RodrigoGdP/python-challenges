def countxo(string):
    x = string.count("x")
    o = string.count("o")
    equal = x == o
    return equal

text = "Python is an interpreted high-level general-purpose " \
       "programming language. Its design philosophy emphasizes " \
       "code readability with its use of significant indentation. " \
       "Its language constructs as well as its object-oriented " \
       "approach aim to help programmers write clear, logical code " \
       "for small and large-scale projects."
print(countxo(text))