from variable import Variable

class DATETIME(Variable):
    def get_display_size(self, precision, scale, char_size, internal_size):
        return 23