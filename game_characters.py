from abc import ABC, abstractmethod


class Character(ABC):
    GAME_TITLE: str = "Fantasy Realm"
    total_characters: int = 0

    def __init__(self, name: str = "Unknown Hero", level: int = 1) -> None:
        cleaned_name = name.strip()
        self.name = cleaned_name if cleaned_name else "Unknown Hero"
        if level < 1:
            self.level = 1
        elif level > 100:
            self.level = 100
        else:
            self.level = level

        Character.total_characters += 1

    @abstractmethod
    def calculate_power(self) -> float:
        pass

    @abstractmethod
    def get_status(self) -> str:
        pass


class MagicCapability:
    def cast_spell(self, spell_name: str) -> str:
        return f"Casting {spell_name} with magical force!"


class WeaponCapability:
    def swing_weapon(self, weapon_name: str) -> str:
        return f"Swinging {weapon_name} for physical damage!"


class Wizard(Character, MagicCapability):
    def __init__(self, name: str, level: int, mana: int = 0) -> None:
        super().__init__(name, level)
        if mana < 1:
            self.mana = 0
        elif mana > 1000:
            self.mana = 1000
        else:
            self.mana = mana

    def calculate_power(self) -> float:
        return self.level * 10.0 + self.mana * 0.5

    def get_status(self) -> str:
        return f"Wizard: {self.name} | Level: {self.level} | Mana: {self.mana} | Power: {self.calculate_power()}"


class Warrior(Character, WeaponCapability):
    def __init__(self, name: str, level: int, stamina: int = 0) -> None:
        super().__init__(name, level)
        if stamina < 1:
            self.stamina = 0
        elif stamina > 500:
            self.stamina = 500
        else:
            self.stamina = stamina

    def calculate_power(self) -> float:
        return self.level * 12.0 + self.stamina * 0.8

    def get_status(self) -> str:
        return f"Warrior: {self.name} | Level: {self.level} | Stamina: {self.stamina} | Power: {self.calculate_power()}"


class Paladin(Character, MagicCapability, WeaponCapability):
    def __init__(self, name: str, level: int) -> None:
        super().__init__(name, level)

    def calculate_power(self) -> float:
        return self.level * 15.0

    def get_status(self) -> str:
        return f"Paladin: {self.name} | Level: {self.level} | Power: {self.calculate_power()} [Hybrid Class]"


def main() -> None:
    wizard = Wizard(" ", -5, 1500)
    warrior = Warrior("Conan", 10, 200)
    paladin = Paladin("Uther", 15)

    print(wizard.get_status())
    print(warrior.get_status())
    print(paladin.get_status())
    print(wizard.cast_spell("Fireball"))
    print(warrior.swing_weapon("Excalibur"))
    print(paladin.cast_spell("Holy Light"))
    print(paladin.swing_weapon("Warhammer"))
    print(f"Total Characters Created: {Character.total_characters}")


if __name__ == "__main__":
    main()