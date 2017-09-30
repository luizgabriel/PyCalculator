class BasePresenter:

    def __init__(self, view):
        self.view = view

    def on_create(self):
        raise NotImplemented()
