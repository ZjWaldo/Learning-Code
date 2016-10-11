def p_decorate(func):
    def func_wrapper(name):
        print id(name)
        return "<p>{0}</p>".format(func(name))
    return func_wrapper

def div_decorate(func):
    def func_wrapper(name):
        return "<div>{0}</div>".format(func(name))
    return func_wrapper

def get_text(name):
    return "Hi, my name is {0}.".format(name)

text = get_text("John")
my_get_text = p_decorate(get_text)
my_get_text2 = p_decorate(text)

x = "ho"

print(text)
print get_text("Richard")
print my_get_text(x)
print id(x)
print my_get_text("Richard")
print my_get_text2
print p_decorate(text)

@p_decorate
@div_decorate
def get_name(name):
    return name

print get_name("Caitlyn")
