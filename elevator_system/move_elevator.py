from .models import Elevator,ElevatorRequest,ElevatorSystem
from threading import Thread

class RunThread(Thread):

  def run(self):
    while True:
      final_run()



def move_elevator(elevator_object : Elevator,elevator_system : ElevatorSystem):
  requests_pending = ElevatorRequest.objects.filter(
    elevator = elevator_object,
    is_active = True,
  ).order_by('request_time')

  for elev_request in requests_pending:
    request_start = elev_request.requested_floor
    request_destination = elev_request.destination_floor
    curr_elev_location = elevator_object.current_floor
    if request_destination < 0 or  request_destination > elevator_system.max_floor or request_start < 0 or  request_start > elevator_system.max_floor:
      elev_request.is_active = False
      elev_request.save()
      continue
    if request_destination == request_start:
      elev_request.is_active = False
      elev_request.save()
      continue

    # Close the door
    elevator_object.is_door_open = False

    if request_start > curr_elev_location:  
      # Start going up
      elevator_object.running_status = 1
    elif request_start < curr_elev_location:
      # Start going down
      elevator_object.running_status = -1
    elevator_object.save()

    elevator_object.current_floor = request_start
    elevator_object.running_status = 0
    elevator_object.is_door_open = True
    elevator_object.save()

    # Let people get in, Close the door
    elevator_object.is_door_open = False
    if request_destination > curr_elev_location:
      # Start going up
      elevator_object.running_status = 1
    elif request_destination < curr_elev_location:
      # Start going down
      elevator_object.running_status = -1
    elevator_object.save()

    # Open the door
    elevator_object.current_floor = request_destination
    elevator_object.running_status = 0
    elevator_object.is_door_open = True
    elevator_object.save()
    
    elev_request.is_active = False
    elev_request.save()


def check_elevator_system(elevator_system : ElevatorSystem):

  elevators_running = Elevator.objects.filter(
    elevator_system = elevator_system,
    is_operational = True,
  )

  for elevator in elevators_running:
    move_elevator(elevator_object = elevator,elevator_system = elevator_system)


def final_run():
  '''
  Run the process for all elevator systems
  '''
  elevator_systems = ElevatorSystem.objects.all().order_by('id')

  for elevator_system in elevator_systems:
    check_elevator_system(elevator_system = elevator_system)