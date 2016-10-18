
def tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator

#@tags("p")
def get_text(name):
    return "Hello "+name

get_text1 = tags("p")
get_text2 = get_text1(get_text)
print get_text2("ho")