from abc import ABC, abstractmethod

class Pass(ABC):
    def __init__(self, pass_id, name, date_purchased):
        self._pass_id = pass_id
        self._name = name
        self._date_purchased = date_purchased

    def get_pass_id(self):
        return self._pass_id

    def get_name(self):
        return self._name

    def get_date_purchased(self):
        return self._date_purchased

    def set_pass_id(self, pass_id):
        self._pass_id = pass_id

    def set_name(self, name):
        self._name = name

    def set_date_purchased(self, date_purchased):
        self._date_purchased = date_purchased

    @abstractmethod
    def print_pass(self):
        pass

class Day(Pass):
    def __init__(self, pass_id, name, date_purchased):
        self._pass_id = pass_id
        self._name = name
        self._date_purchased = date_purchased

    def print_pass(self):
        print("Pass ID: {}".format(self._pass_id), " {}".format(self._name))

