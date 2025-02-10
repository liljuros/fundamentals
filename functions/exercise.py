# def var_func(first, *args):
#     return first + sum(args)
# print(var_func(1, 5, 3, 10))

# def seperator(data, item_sep=',', rep=10):
#         output = item_sep.join(str(data) for i in range(rep))
#
#         return output
#
#     # for row in data:
#     #     row_str = item_sep.join(str(el) for el in row)
#     #     output += row_str + line_sep
#
#
# print(seperator('abc', item_sep="-", rep=20))

# unique_elements_count = lambda iterable: len(set(iterable)) if iterable else 0
# print(unique_elements_count("hello"))
import re


def arg_func(a="", sep=" ,."):
    pattern = f"[{re.escape(sep)}]"
    words = re.split(pattern, a)

    word_count = {}
    for word in words:
        if word:  # Ignorera tomma strängar
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    return word_count


print(arg_func(
    "This is the first sentence. This is the second sentence. This is not the fourth sentence, it is the third sentence."))