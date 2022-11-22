from django.apps import AppConfig

class ElevatorSystemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'elevator_system'
    def ready(self):

        from elevator_system.move_elevator import RunThread

        RunThread().start()

