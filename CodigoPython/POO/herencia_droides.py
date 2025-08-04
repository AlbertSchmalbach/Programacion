class Droid:
    def __init__(self, name: str):
        self.name = name

class ProtocolDroid(Droid):
    def __init__(self, name: str, languages: list[str]):
        super().__init__(name)
        self.languages = languages

droid = ProtocolDroid('C-3PO', ['Ewokese', 'Huttese', 'Jawaese'])
droid.name
droid.languages