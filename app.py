blogs = dict()


def menu():
    # Show the user the available blogs
    # Let the user make a choice
    # do something with that choice
    # Eventually exit

    print_blogs()

def print_blogs():
    # print the available blogs
    for key, blog in blogs.items():
        print('- {}'.format(blog))