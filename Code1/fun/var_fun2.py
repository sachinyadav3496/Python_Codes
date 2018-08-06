

def my(**kwargs):

    for key in kwargs:

        print(key, "=", kwargs[key])



my()
my(name='sachin')
my(name='sachin',age=21)
my(name='sachin',age=21,language='python')

