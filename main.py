'''A Basic Beginner Dealership Project where you can sell/publish/buy your cars.
Using abilities such as superclass, subclass, inheritance, Methods, Conditions, Default Arguments, Tuples, Dictonaries, Lists, F-Strings, etc etc...'''

import random

class Car:
    '''A Basic class for the Car, the SuperClass of all the Company Classes which are the Subclasses'''
    car_companies = (
        'Tesla', 'Mazda', 'KIA', 'Chevrolet', 'Hyundai', 'BMW', ' Toyota', ' Honda', 'Audi', ' Nissan', 'Mercedes')

    def __init__(self, color='White', year=2022, company=None):
        self.color = color
        self.year = year
        self.company = company

    def buy_car(self, company, model, color, year, price):
        '''Buying the car and ticketing the order of the car including all the details the user chose for his/her car
        :param self: self variable, used to present the instance -> Instance of the class Car type
        :param company: presents the company the user chose -> str type
        :param model: presents the model of the car the user chose -> str type
        :param color: presents the color of the car -> str type
        :param year: presents the car year -> int type
        :param price: The price of the specific model the user chose -> int type
        :return: A string including all the details according the the user's choices
        :rtype: type -> str
        '''
        print(f'''Congratulations! You bought a car! Order number {random.randint(1, 1000)} is completed!\nCar details:\n\tCompany: {company}\n\tModel: {model}\n\tColor: {color}\n\tYear: {year}\n\tPrice: {price}₪\nHave a safe drive!''')

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
    models = {'Mazda 3': 65000, 'Mazda 6': 85000, 'Mazda CX-5': 150000, 'Mazda CX-3': 125000, 'Mazda CX-30': 170000}

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
    models = {'Sorento': 150000, 'Sportage': 120000, 'K5': 100000, 'Stinger': 95000, 'Rio': 125000}

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
    models = {'Camro': 65000, 'Cruze': 80000, 'Colorado': 95000, 'Traverse': 115000, 'Impala': 100000}

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
    models = {'Elantra': 80000, 'Accent': 120000, 'Tucson': 150000, 'Aura': 115000, 'i20': 65000}

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
    models = {'M5': 200000, '5 Series': 215000, 'M3': 225000, 'M3 Series': 275000, '8 Series': 180000}

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
    models = {'Camry': 95000, 'Corolla': 100000, 'Prius': 125000, 'Hilux': 115000, 'Supra': 115000}

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
    models = {'Civic': 110000, 'CR-V': 120000, 'Accord': 155000, 'Fit': 165000, 'Insight': 175000}

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
    models = {'Q5': 115000, 'Q7': 120000, 'E-Tron': 155000, 'A8': 175000, 'A4': 175000}

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
    models = {'Altima': 125000, 'Juke': 150000, 'Sentra': 115000, 'Maxima': 100000, 'Leaf': 85000}

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
    models = {'C-Class': 100000, 'A-Class': 150000, 'GLE': 250000, 'AMG GT': 300000}

    def __init__(self, color='White', year=2022, company=None, model=None):
        Car.__init__(self, color='White', year=2022, company=None)
        self.model = model

        if model in Mercedes.models:
            self.model = model
            super().buy_car(company, model, color, year)

        else:
            print(f'Model was not found. Please choose a model from {Mercedes.models}')

def main():
    '''Main function of the program, where the instance of the decided car is presented and the main loop of the program runs including conditions and flow control'''
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
                                requested_car = companies_dict[car_company_decision](car_color_decision, car_year_decision, car_model_decision)
                                requested_car.buy_car(car_company_decision, car_model_decision, car_color_decision, car_year_decision, requested_car.models[car_model_decision])
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