class Character:
    def __init__(self, name: str, current_health: int, max_health: int, attack_power: int):
        self.name = name
        self.current_health = current_health
        self.max_health = max_health
        self.attack_power = attack_power

    def take_damage(self, damage_amount: int):
        print(f'{self.name} is dealt {damage_amount} damage.')
        self.current_health -= damage_amount
        self.is_alive()
        print(f'{self.name} has {self.current_health} health.')

    def is_alive(self):
        if self.current_health <= 0:
            print(f'{self.name} lost')
            self.current_health = 0
            return False
        return True

    def attack(self, target):
        print(f'{self.name} attacks {target.name} for {self.attack_power} damage.')
        target.current_health -= self.attack_power  # ВИПРАВЛЕНО: було target.health
        target.is_alive()

    def get_status(self):
        print(f'Name: {self.name}, current health: {self.current_health}, max health: {self.max_health}, '
              f'attack power: {self.attack_power}')


class Enemy(Character):
    def __init__(self, name: str, current_health: int, max_health: int, attack_power: int, xp_reward: int):
        super().__init__(name, current_health, max_health, attack_power)
        self.xp_reward = xp_reward

    def take_damage(self, damage_amount: int):  # ВИПРАВЛЕНО: було target
        print(f'{self.name} is dealt {damage_amount} damage.')
        self.current_health -= damage_amount
        self.is_alive()
        print(f'{self.name} has {self.current_health} health.')

    def get_status(self):
        print(f'Name: {self.name}, current health: {self.current_health}, max health: {self.max_health}, '
              f'attack power: {self.attack_power}, xp reward: {self.xp_reward}')


class Player(Character):
    def __init__(self, name: str, current_health: int, max_health: int, attack_power: int,
                 level: int = 1, current_xp: int = 0):
        super().__init__(name, current_health, max_health, attack_power)
        self.level = level
        self.current_xp = current_xp

    def gain_xp(self, amount):
        self.current_xp += amount
        print(f'{self.name} has {self.current_xp} XP')
        if self.current_xp >= 100:
            self.current_xp -= 100  # ПОКРАЩЕНО: зберігаємо залишок XP
            self.level += 1
            print(f'{self.name} leveled up to level {self.level}!')

    def attack(self, target):
        print(f'{self.name} attacks {target.name} for {self.attack_power} damage.')
        target.take_damage(self.attack_power)

        if not target.is_alive():
            print(f"Enemy {target.name} was defeated!")
            if isinstance(target, Enemy):
                self.gain_xp(target.xp_reward)
                print(f"{self.name} gained {target.xp_reward} XP.")

    def get_status(self):
        print(f'Name: {self.name}, current health: {self.current_health}, max health: {self.max_health}, '
              f'attack power: {self.attack_power}, current xp: {self.current_xp}, level: {self.level}')


# Створення персонажів
hero = Player('Hero', 100, 100, 10)
goblin = Enemy("Goblin Shaman", 40, 40, 10, 65)
wolf = Enemy("Dire Wolf", 30, 30, 8, 35)

# ВИПРАВЛЕНО: правильна логіка циклу
while (goblin.is_alive() or wolf.is_alive()) and hero.is_alive():
    print("\n" + "=" * 50)
    hero.get_status()

    if goblin.is_alive():
        print("\n--- Hero attacks Goblin ---")
        hero.attack(goblin)
    elif wolf.is_alive():
        print("\n--- Hero attacks Wolf ---")
        hero.attack(wolf)

    # Ворожі атаки
    if goblin.is_alive():
        print("\n--- Goblin attacks Hero ---")
        goblin.attack(hero)

    if wolf.is_alive():
        print("\n--- Wolf attacks Hero ---")
        wolf.attack(hero)

print("\n" + "=" * 50)
print("THE BATTLE IS OVER!")
hero.get_status()