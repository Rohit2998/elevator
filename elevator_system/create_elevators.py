from .models import Elevator
'''
  Function to create elevators inside an elevator system
'''

def create_elevators(number_of_elevators : int,system_id : int):

  for i in range(number_of_elevators):
    elevator_object = Elevator.objects.create(
      elevator_system_id = system_id,
      elevator_number = i+1,
    )

    elevator_object.save()