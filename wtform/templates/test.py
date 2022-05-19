class Test:
    def __call__(self, **kwargs):
        print("wow")
        print(kwargs)

    def __str__(self):
        return "yahoo"


def func(test: Test, **kwargs):
    print("test:" + str(test))
    print(kwargs)
    test(kwargs)


test = Test()
func(test, a=2)
