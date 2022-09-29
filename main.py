'''A Basic Beginner Dealership Project where you can sell/publish/buy your cars.
Using abilities such as superclass, subclass, inheritance, Methods, Conditions, Default Arguments, Tuples, Dictonaries, Lists, F-Strings, etc etc...'''
#TODO Add Prices for each company and 

import random

class Car:
    '''A Basic class for the Car, the SuperClass of all the Company Classes which are the Subclasses'''
    car_companies = (
        'Tesla', 'Mazda', 'KIA', 'Chevrolet', 'Hyundai', 'BMW', ' Toyota', ' Honda', 'Audi', ' Nissan', 'Mercedes')

    def __init__(self, color='White', year=2022, company=None):
        self.color = color
        self.year = year
        self.company = company

    def buy_car(self, company, model, color, year):
        print(f'''Congratulations! You bought a car! Order number {random.randint(1, 1000)} is completed!\nCar details:\n\tCompany: {company}\n\tModel: {model}\n\tColor: {color}\n\tYear: {year}\nHave a safe drive!''')

class Tesla(Car):
    '''Tesla Subclass of Car. Used to present the Company Tesla. Class has all the models of Tesla saved inside'''
    models = ('Model S', 'Model 3', 'Model Y', 'CyberTruck', 'Tesla')

    def __init__(self, color='White', year=2022, company=None, model=None):
        Car.__init__(self, color='White', year=2022, company=None)
        self.model = model

        if model in Tesla.models:
            self.model = model
            super().buy_car(company, model, color, year)
        else:
            print(f'Model was not found. Please choose a model from {Tesla.models}')


class Mazda(Car):
    '''Mazda Subclass of Car. Used to present the Company Mazda. Class has all the models of Mazda saved inside'''
    models = ('Mazda 3', 'Mazda 6', 'Mazda CX-5', 'Mazda CX-3', 'Mazda CX-30')

    def __init__(self, color='White', year=2022, company=None, model=None):
        Car.__init__(self, color='White', year=2022, company=None)
        self.model = model

        if model in Mazda.models:
            self.model = model
            super().buy_car(company, model, color, year)
        else:
            print(f'Model was not found. Please choose a model from {Mazda.models}')

class KIA(Car):
    '''KIA Subclass of Car. Used to present the Company KIA. Class has all the models of KIA saved inside'''
    models = ('Sorento', 'Sportage', 'K5', 'Stinger', 'Rio')

    def __init__(self, color='White', year=2022, company=None, model=None):
        Car.__init__(self, color='White', year=2022, company=None)
        self.model = model

        if model in KIA.models:
            self.model = model
            super().buy_car(company, model, color, year)
        else:
            print(f'Model was not found. Please choose a model from {KIA.models}')

class Chevrolet(Car):
    '''Chevrolet Subclass of Car. Used to present the Company Chevrolet. Class has all the models of Chevrolet saved inside'''
    models = ('Camro', 'Cruze', 'Colorado', 'Traverse', 'Impala')

    def __init__(self, color='White', year=2022, company=None, model=None):
        Car.__init__(self, color='White', year=2022, company=None)
        self.model = model
        if model in Chevrolet.models:
            self.model = model
            super().buy_car(company, model, color, year)
        else:
            print(f'Model was not found. Please choose a model from {Chevrolet.models}')

class Hyundai(Car):
    '''Hyundai Subclass of Car. Used to present the Company Hyundai. Class has all the models of Hyundai saved inside'''
    models = ('Elantra', 'Accent', 'Tucson', 'Aura', 'i20')

    def __init__(self, color='White', year=2022, company=None, model=None):
        Car.__init__(self, color='White', year=2022, company=None)
        self.model = model

        if model in Hyundai.models:
            self.model = model
            super().buy_car(company, model, color, year)
        else:
            print(f'Model was not found. Please choose a model from {Hyundai.models}')

class BMW(Car):
    '''BMW Subclass of Car. Used to present the Company BMW. Class has all the models of BMW saved inside'''
    models = ('M5', '5 Series', 'M3', 'M3 Series', '8 Series')

    def __init__(self, color='White', year=2022, company=None, model=None):
        Car.__init__(self, color='White', year=2022, company=None)
        self.model = model

        if model in BMW.models:
            self.model = model
            super().buy_car(company, model, color, year)
        else:
            print(f'Model was not found. Please choose a model from {BMW.models}')

class Toyota(Car):
    '''Toyota Subclass of Car. Used to present the Company Toyota. Class has all the models of Toyota saved inside'''
    models = ('Camry', 'Corolla', 'Prius', 'Hilux', 'Supra')

    def __init__(self, color='White', year=2022, company=None, model=None):
        Car.__init__(self, color='White', year=2022, company=None)
        self.model = model

        if model in Toyota.models:
            self.model = model
            super().buy_car(company, model, color, year)
        else:
            print(f'Model was not found. Please choose a model from {Toyota.models}')

class Honda(Car):
    '''Honda Subclass of Car. Used to present the Company Honda. Class has all the models of Honda saved inside'''
    models = ('Civic', 'CR-V', 'Accord', 'Fit', 'Insight')

    def __init__(self, color='White', year=2022, company=None, model=None):
        Car.__init__(self, color='White', year=2022, company=None)
        self.model = model

        if model in Honda.models:
            self.model = model
            super().buy_car(company, model, color, year)
        else:
            print(f'Model was not found. Please choose a model from {Honda.models}')

class Audi(Car):
    '''Audi Subclass of Car. Used to present the Company Audi. Class has all the models of Audi saved inside'''
    models = ('Q5', 'Q7', 'E-Tron', 'A8', 'A4')

    def __init__(self, color='White', year=2022, company=None, model=None):
        Car.__init__(self, color='White', year=2022, company=None)
        self.model = model

        if model in Audi.models:
            self.model = model
            super().buy_car(company, model, color, year)

        else:
            print(f'Model was not found. Please choose a model from {Audi.models}')

class Nissan(Car):
    '''Nissan Subclass of Car. Used to present the Company Nissan. Class has all the models of Nissan saved inside'''
    models = ('Altima', 'Juke', 'Sentra', 'Maxima', 'Leaf')

    def __init__(self, color='White', year=2022, company=None, model=None):
        Car.__init__(self, color='White', year=2022, company=None)
        self.model = model

        if model in Nissan.models:
            self.model = model
            super().buy_car(company, model, color, year)

        else:
            print(f'Model was not found. Please choose a model from {Nissan.models}')

class Mercedes(Car):
    '''Mercedes Subclass of Car. Used to present the Company Mercedes. Class has all the models of Mercedes saved inside'''
    models = ('C-Class', 'A-Class', 'GLE', 'AMG GT', 'Tesla')

    def __init__(self, color='White', year=2022, company=None, model=None):
        Car.__init__(self, color='White', year=2022, company=None)
        self.model = model

        if model in Mercedes.models:
            self.model = model
            super().buy_car(company, model, color, year)

        else:
            print(f'Model was not found. Please choose a model from {Mercedes.models}')

def main():
    models_dict = {'Tesla': Tesla.models, 'Mazda': Mazda.models, 'KIA': KIA.models, 'Chevrolet': Chevrolet.models,
                   'Hyundai': Hyundai.models, 'BMW': BMW.models, 'Toyota': Toyota.models,
                   'Honda': Honda.models, 'Audi': Audi.models, 'Nissan': Nissan.models, 'Mercedes': Mercedes.models}

    companies_dict = {'Tesla': Tesla, 'Mazda': Mazda, 'KIA': KIA, 'Chevrolet': Chevrolet,
                      'Hyundai': Hyundai, 'BMW': BMW, 'Toyota': Toyota,
                      'Honda': Honda, 'Audi': Audi, 'Nissan': Nissan, 'Mercedes': Mercedes}

    colors_tup = ('White', 'Black', 'Blue', 'Yellow', 'Red', 'Green', 'Orange', 'Purple', 'Pink')

    while True:
        user_action_decision = input(f'Welcome to the Car Dealearship, Type buy_car to start the process: ')

        if user_action_decision.lower() == 'buy_car':
            car_company_decision = input('What company would you like to buy from? ')

            if car_company_decision in Car.car_companies:
                car_model_decision = input(f'What model from {car_company_decision} would you like to have? ')
                car_color_decision = input(f'What color would you like to have (Default = White)\nPick a color from the list {colors_tup}: ')

                try:
                    car_year_decision = int(input(f'What year of the car would you like?: (Year above 2010, Default = 2022 ): '))
                    if car_model_decision in models_dict[car_company_decision]:
                        if car_color_decision in colors_tup or car_color_decision == '':
                            if car_year_decision == '' or car_year_decision > 2010:
                                requested_car = companies_dict[car_company_decision](car_color_decision,
                                                                                     car_year_decision,
                                                                                     car_model_decision)
                                requested_car.buy_car(car_company_decision, car_model_decision, car_color_decision,
                                                      car_year_decision)
                                quit_input = input('Would you like quit the prorgam? [Yes/No]: ')
                                if quit_input.lower() == 'yes':
                                    print(f'Thank you for coming. Have a nice day!')
                                    quit()

                            else:
                                print(f'Year is invalid. Pick a valid year')
                                continue

                        else:
                            print(f'Color is invalid. Please pick a valid color')
                            continue

                    else:
                        print(f'Model was not found. Please choose one of the company\'s models next time\n{car_company_decision}\'s Models --> {models_dict[car_company_decision]}')
                        continue


                except ValueError:
                    print(f'Error! Please enter an intenger for the year argument')

            else:
                print(f'Could not find the company. Please type one of the {list(companies_dict.keys())}')

        else:
            print(f"Could not find the action you typed. Please type the required action")
            continue

if __name__ == '__main__':
    main()