#run the following commands in command prompt with the hashes to install and setup django

#pip install django
#django-admin startproject my_project
#cd_ my project
#python manage.py startapp my_app

from abc import ABC, abstractclassmethod
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import Signal
from django.http import receiver 
from django.views import View
from django.decorators import method_decorator
from django.contrib.auth.decorators import login_required

#behavioural pattern: observer pattern

export_completed_signal = Signal()

@receiver(export_completed_signal)
def log_export_metrics(sender, **kwargs):
    username = kwargs.get('username')
    format_type = kwargs.get('format_type')
    print(f"User {'username'} has succesfully generated a {'format_type'} report.") 

#creational pattern: dynamic object assembly 

class dataformat(ABC):
    @abstractclassmethod
    def format_data(self, dataset: list) -> dict:
        pass

class jsonformat(dataformat):
    def format_data(self, dataset: list) -> dict:
        return {"format": "JSON", "payload": dataset}
    
class xmlformat(dataformat):
    def format_data(self, dataset: list) -> dict:
        return {"format": "XML", "payload": f"<root>{dataset}</root>"}
    
class format:
    @staticmethod
    def get_formatter(requested_format: str) -> dataformat:
        format_map = {
            'json': jsonformat
            'xml': xmlformat
        }

concrete_class = format_map.get(requested_format.lower(), jsonformat)
return concrete_class

#structural pattern: decorator and django view

@method_decorator(login_required, name='dispatch')

class reportview(View):
    def get (self, request):
        user_format_choice = request.GET.get('export_type', 'json')
        mock_database_records = [{"id": 101, "item": "laptop"}, {"id": 102, "item": "monitor"}]

        formatter = format.get_formatter(user_format_choice)
        processed_output = format.format_data(mock_database_records)

        export_completed_signal.send(
            sender=self.__class__,
            username=request.user.username,
            format_type = user_format_choice
        )

        return jsonformat({
            "status": "Export complete",
            "data": processed_output
        })