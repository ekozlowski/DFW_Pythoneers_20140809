
def my_decorator(function):
    def inner(*args, **kwargs):
        print "pre decoration"
        function(*args, **kwargs)
        print "post decoration"
    return inner

@my_decorator
def foo():
    print "foo"

@my_decorator
def bar():
    print "bar"

if __name__ == "__main__":
    foo()
    bar()