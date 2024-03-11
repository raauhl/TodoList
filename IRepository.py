from abc import ABC, abstractmethod


class IRepository(ABC):
    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def read(self, id):
        pass

    @abstractmethod
    def read_all(self):
        pass

    @abstractmethod
    def update(self, id, data):
        pass

    @abstractmethod
    def delete(self, id):
        pass
