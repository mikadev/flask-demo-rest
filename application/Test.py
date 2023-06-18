class Test:
    @property  # first decorate the getter method
    def attribute(self):  # This getter method name is *the* name
        return self.attribute

    #
    @attribute.setter  # the property decorates with `.setter` now
    def attribute(self, attribute):  # name, e.g. "attribute", is the same
        self.attribute = attribute  # the "value" name isn't special


test = Test()
test.attribute = 'x'
