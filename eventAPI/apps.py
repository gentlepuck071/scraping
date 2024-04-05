from django.apps import AppConfig
import sys
sys.path.insert(0, '../eventscraping')

class eventAPIConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'eventAPI'

    print('---11===------------')

    def ready(self):
        if not getattr(self, '_already_called', False):
            self._already_called = True
        
