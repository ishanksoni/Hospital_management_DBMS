from Home.options import action

def Context(request):
    actions = action(request)
    context = {'actions':actions}

    return context