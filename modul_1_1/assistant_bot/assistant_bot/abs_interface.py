from abc import abstractmethod, ABCMeta


class UserOutputInterface(metaclass=ABCMeta):
    @abstractmethod
    def format_income(self):
        pass

    @abstractmethod
    def create_header(self):
        pass

    @abstractmethod
    def create_table(self):
        pass

    @abstractmethod
    def output_table(self):
        pass
