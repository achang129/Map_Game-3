class coin_tracker():
        def __init__(self):
            self.total = 0

        def add(self, input):
            self.total += input

        def return_total(self):
            return self.total