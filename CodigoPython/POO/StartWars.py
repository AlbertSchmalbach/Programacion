class Droid:

    obeys_onwer = True
    count = 0
    def __init__(self, name: str):
        Droid.count += 1
        print('Running __init__')
        self.obeys_owner = Droid.obeys_onwer
        self.__name = name
        self.covered_distance = 0

    def move_up(self, steps: int) -> None:
        self.covered_distance += steps
        print(f'Moving {steps} steps')
        
    @classmethod
    def get_total_droids(cls) -> None:
        print(f'{cls.count} droids built so far!')

    @staticmethod
    def get_droid_categories() -> tuple[str]:
        return ('MESSENGER', 'ASTROMECH', 'POWER', 'PROTOCOL')

    def switch_on(self):
        self.power_on = True
        print("Hi! I'm a droid. Can I help you?")

    def switch_off(self):
        self.power_on = False
        print("Bye! I'm going to sleep")

class AstromechDroid:
    def __init__(self, name: str, height: float):
        self.name = name
        self.height = height

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, height: float) -> None:
        self._height = height
        self._periscope_height = None

    @property
    def periscope_height(self) -> float:
        if self._periscope_height is None:
            print('Calculating periscope height...')
            self._periscope_height = 0.3 * self.height
        return self._periscope_height

Droid.obeys_onwer = False

bb8 = Droid('BB-8')
# bb8.obeys_onwer = False
print(f"Obedencia a su amo: {bb8.obeys_onwer}")
# print(f"{bb8._Droid__name}")

droid = Droid('C-3PO')
print(f"Obedencia a su amo: {droid.obeys_onwer}")
# print(droid._Droid__name)
droid.__name = 'waka-waka'
print(f"Nuevo nombre: {droid._Droid__name}")

droid.manufacturer = 'Cybot Galactica'
droid.height = 1.77

droid.move_up(10)
droid.get_total_droids()
print(droid.get_droid_categories())