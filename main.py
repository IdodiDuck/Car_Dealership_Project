# Cars Finder Basic Algorithm Program, made by IdoRedid123
class Car:
    car_companies = (
    'Tesla', 'Mazda', 'KIA', 'Chevrolet', 'Hyundai', 'BMW', ' Toyota', ' Honda', 'Audi', ' Nissan', 'Mercedes')
    published_cars = []

    def __init__(self, color='White', year=2022, company=None):
        self.color = color
        self.year = year
        self.company = company

    def buy_car(self):
        print(f'Congratulations! You bought a car! Have a safe drive!')

    def publish_car(self, car_company, car_model, car_color='White', car_year=2022):
        # if car_company.lower() in [car.lower() for car in self.car_companies] & None:
        Car.published_cars.append('Car from company {car_company}\nModel {car_model}\nColor {car_color}\nYear {car_year}')
        print('''Published a car with the next information:
        \nCar from company {car_company}\nModel {car_model}\nColor {car_color}\nYear {car_year}''')

class Tesla(Car):
    models = ('Model S', 'Model 3', 'Model Y', 'CyberTruck', 'Tesla')

    def __init__(self, model):
        Car.__init__(self, color='White', year=2022, company=None)

        if model in Tesla.models:
            self.model = model
        else:
            print(f'Model was not found. Please choose a model from {Tesla.models}')


class Mazda(Car):
    models = ('Mazda 3', 'Mazda 6', 'Mazda CX-5', 'Mazda CX-3', 'Mazda CX-30')

    def __init__(self, model):
        Car.__init__(self, color='White', year=2022, company=None)

        if model in Mazda.models:
            self.model = model
        else:
            print(f'Model was not found. Please choose a model from {Mazda.models}')


class KIA(Car):
    models = ('Sorento', 'Sportage', 'K5', 'Stinger', 'Rio')

    def __init__(self, model):
        Car.__init__(self, color='White', year=2022, company=None)

        if model in KIA.models:
            self.model = model
        else:
            print(f'Model was not found. Please choose a model from {KIA.models}')


class Chevrolet(Car):
    models = ('Camro', 'Cruze', 'Colorado', 'Traverse', 'Impala')

    def __init__(self, model):
        Car.__init__(self, color='White', year=2022, company=None)

        if model in Chevrolet.models:
            self.model = model
        else:
            print(f'Model was not found. Please choose a model from {Chevrolet.models}')


class Hyundai(Car):
    models = ('Elantra', 'Accent', 'Tucson', 'Aura', 'i20')

    def __init__(self, model):
        Car.__init__(self, color='White', year=2022, company=None)

        if model in Hyundai.models:
            self.model = model
        else:
            print(f'Model was not found. Please choose a model from {Hyundai.models}')


class BMW(Car):
    models = ('M5', '5 Series', 'M3', 'M3 Series', '8 Series')

    def __init__(self, model):
        Car.__init__(self, color='White', year=2022, company=None)

        if model in BMW.models:
            self.model = model
        else:
            print(f'Model was not found. Please choose a model from {BMW.models}')


class Toyota(Car):
    models = ('Camry', 'Corolla', 'Prius', 'Hilux', 'Supra')

    def __init__(self, model):
        Car.__init__(self, color='White', year=2022, company=None)

        if model in Toyota.models:
            self.model = model
        else:
            print(f'Model was not found. Please choose a model from {Toyota.models}')


class Honda(Car):
    models = ('Civic', 'CR-V', 'Accord', 'Fit', 'Insight')

    def __init__(self, model):
        Car.__init__(self, color='White', year=2022, company=None)

        if model in Honda.models:
            self.model = model
        else:
            print(f'Model was not found. Please choose a model from {Honda.models}')


class Audi(Car):
    models = ('Q5', 'Q7', 'E-Tron', 'A8', 'A4')

    def __init__(self, model):
        Car.__init__(self, color='White', year=2022, company=None)

        if model in Audi.models:
            self.model = model
        else:
            print(f'Model was not found. Please choose a model from {Audi.models}')


class Nissan(Car):
    models = ('Altima', 'Juke', 'Sentra', 'Maxima', 'Leaf')

    def __init__(self, model):
        Car.__init__(self, color='White', year=2022, company=None)

        if model in Nissan.models:
            self.model = model
        else:
            print(f'Model was not found. Please choose a model from {Nissan.models}')


class Mercedes(Car):
    models = ('C-Class', 'A-Class', 'GLE', 'AMG GT', 'Tesla')

    def __init__(self, model):
        Car.__init__(self, color='White', year=2022, company=None)

        if model in Mercedes.models:
            self.model = model
        else:
            print(f'Model was not found. Please choose a model from {Mercedes.models}')


def main():
    models_dict = {'Tesla': Tesla.models, 'Mazda': Mazda.models, 'KIA': KIA.models, 'Chevrolet': Chevrolet.models,
                   'Hyundai': Hyundai.models, 'BMW': BMW.models, 'Toyota': Toyota.models,
                   'Honda': Honda.models, 'Audi': Audi.models, 'Nissan': Nissan.models, 'Mercedes': Mercedes.models}

    while True:
        user_action_decision = input(f'Welcome to the Car Dealearship, what action would you like to do?\nBuy_Car/Publish_Car ')

        if user_action_decision.lower() == 'buy':
            car_company_decision = input('What company would you like to buy? ')

            if car_company_decision in Car.car_companies:
                car_model_decision = input(f'What model from {car_company_decision} would you like to have? ')

                if car_model_decision in models_dict[car_company_decision]:
                    print()

                else:
                    print(f'Model was not found. Please choose one of the company\'s models next time\n{car_company_decision}\'s Models --> {models_dict[car_company_decision]}')

            else:
                print(f'Car was not found. Please choose a model from the next list:\n{Car.car_companies}')
                continue

        

if __name__ == '__main__':
    main()