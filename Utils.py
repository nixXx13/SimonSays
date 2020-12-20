def singleton(cls):

    instances = {}

    def create_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return create_instance
