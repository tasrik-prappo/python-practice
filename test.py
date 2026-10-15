from abc import ABC,abstractmethod

class DataProcessor(ABC):

    @abstractmethod
    def process_data(self,data: list) -> list:
        pass


class TextCleaner(DataProcessor):

    
    def process_data(self, data: list) -> list:
        return [item.lower() for item in data]


text_cleaner = TextCleaner()
print(text_cleaner.process_data(["HELLO","WORLD"]))
    