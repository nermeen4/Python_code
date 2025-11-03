# Vehicle Rental System
class Vehicle:
    #class variable:
    total_vehicles = 0
    
    def __init__(self, v_id, brand, model, rent_p_per_day):
        
        self.v_id = v_id
        self.brand = brand
        self.model= model
        self.rent_p_per_day= rent_p_per_day
        self.is_rented = False
        Vehicle.total_vehicles+=1
            
    # is rented or not. 
    def rent(self):
        if self.is_rented:
            print("Vehicle is already rented")
        else:
            self.is_rented = True
            print("Vehicle rented successfully")
    
    # is it avaliable or not based on rent
    def return_vehicle(self):
        if not self.is_rented:
            print("vehicle wasn't rented")
        else:
            self.is_rented = False
            print("vehicle rented successfully.")
            
    # calculate cost of rent per day
    def calculate_rental_cost(self, days):
        return self.rent_p_per_day * days 
    
    # get info about vehicle
    def get_details(self):
        status = "Rented" if self.is_rented else "Available"
        return (f"{self.brand} {self.model} - "
                f"ID: {self.v_id} - "
                f"${self.rent_p_per_day}/day - {status}")
        #return {f"vehicle_id: {self.v_id}, vehicle_brand: {self.brand}, vehicle_model: {self.model}, vehicle_price_rent: {self.rent_p_per_day}"}
    
    
    #child class car inherit from parent class vehicle
class Car(Vehicle):
    def __init__(self, v_id, brand, model, rent_p_per_day, num_doors):
        super().__init__(v_id, brand, model, rent_p_per_day)
        self.num_doors = num_doors
        self.multiplier = 1.0

#override from base class (same name different implementation)
def calculate_rental_cost(self, days):
        return super().calculate_rental_cost(days) * self.multiplier
    
    
#child class motorcycle inherit from parent class vehicle
class Motorcycle(Vehicle):
    def __init__(self, vehicle_id, brand, model, rent_p_per_day, engine_cc):
        super().__init__(vehicle_id, brand, model, rent_p_per_day)
        self.engine_cc = engine_cc
        self.multiplier = 0.7

#override from base class (same name different implementation) with different value of attribute multiplier
    def calculate_rental_cost(self, days):
        return super().calculate_rental_cost(days) * self.multiplier
    
# ovveride method get_details from parent class with new attribute engine_cc
    def get_details(self):
            status = "Rented" if self.is_rented else "Available"
            return (f"Motorcycle - {self.brand} {self.model} ({self.engine_cc}cc) - "
                    f"ID: {self.v_id} - "
                    f"${self.rent_p_per_day}/day - {status}")
            
            
#child class trunk inherit from parent class vehicle
class Truck(Vehicle):
    def __init__(self, vehicle_id, brand, model, rent_p_per_day, cargo_capacity_tons):
        super().__init__(vehicle_id, brand, model, rent_p_per_day)
        self.cargo_capacity_tons = cargo_capacity_tons
        self.multiplier = 1.5

#override from base class (same name different implementation) with different value of attribute multiplier
    def calculate_rental_cost(self, days):
        return super().calculate_rental_cost(days) * self.multiplier


################### creating objects and access data ################################
car = Car("V001", "Toyota", "Camry", 50, 4)
motorcycle = Motorcycle("V002", "Harley", "Street 750", 40, 750)
truck = Truck("V003", "Ford", "F-150", 80, 2.5)

car.rent()
print(car.is_rented)  

cost = car.calculate_rental_cost(5)
print(f"Rental cost for 5 days: ${cost}")

print(motorcycle.get_details())
car.rent()  

car.return_vehicle()
print(car.is_rented)  

print(f"Total vehicles: {Vehicle.total_vehicles}")