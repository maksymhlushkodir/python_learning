class Device:
    def __init__(self, name: str, status: bool=False):
        self.name = name
        self.status = status

    def turn_on(self):
        print(f'Device {self.name} turned on')
        self.status = True

    def turn_off(self):
        print(f'Device {self.name} turned off')
        self.status = False

    def operate(self):
        raise NotImplementedError

    def changes(self):
        raise NotImplementedError

    @staticmethod
    def info():
        return f'Smart Home System v1.0. Developed by Maksym'


class Light(Device):
    def __init__(self, name: str, status: bool=False, brightness: int=0):
        super().__init__(name, status)
        self.brightness = brightness

    def changes(self):
        if self.status == True:
            change_brightness = True
            while change_brightness:
                print(f'select brightness (0 - 100)')
                new_brightness = int(input('your choice: '))
                if new_brightness < 0 or new_brightness > 100:
                    print('Error: number must be in the range 0 to 100')
                else:
                    self.brightness = new_brightness
                    change_brightness = False

    def operate(self):
        print(f'Shining with {self.brightness}% brightness')


class Thermostat(Device):
    def __init__(self, name: str, status: bool=False, temperature: float=0):
        super().__init__(name, status)
        self.temperature = temperature

    def changes(self):
        if self.status == True:
            change_temperature = True
            while change_temperature:
                print(f'Select temperature')
                new_temperature = float(input('temperature: '))
                self.temperature = new_temperature
                change_temperature = False

    def operate(self):
        print(f'Setting the house temperature to {self.temperature}°C')


class HomeManager:
    def __init__(self, device: list=None):
        self.device = device
        if device is None:
            self.device = []

    def add_device(self, new_device: Device):
        self.device.append(new_device)

    def all_on(self):
        for i in self.device:
            if i.status == False:
                i.turn_on()

    def show_status(self):
        on_devices = []
        for i in self.device:
            if i.status == True:
                on_devices.append(i)
        for i in on_devices:
            i.operate()

# Call the static method directly from the class
print(Device.info())

manager = HomeManager()

living_room_light = Light("Living Room Light")
kitchen_thermostat = Thermostat("Kitchen Stat")

living_room_light.turn_on()
kitchen_thermostat.turn_on()

living_room_light.changes()
kitchen_thermostat.changes()

kitchen_thermostat.turn_off()

manager.add_device(living_room_light)
manager.add_device(kitchen_thermostat)

manager.all_on()
manager.show_status()