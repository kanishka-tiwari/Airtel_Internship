#run the following commands in command prompt with the hashes to install and setup django

#pip install django
#django-admin startproject my_project
#cd_ my project
#python manage.py startapp my_app

from importlib import reload
import os
from abc import ABC, abstractclassmethod 
from django.db import models
from django.http import JsonResponse
from django.views import View

#implementing ISP and DIP
#abtractions 

class actioninterface(ABC):
    @abstractclassmethod
    def excecute_action(self, data: dict) -> None:
        pass

class alterinterface(ABC):
    @abstractclassmethod
    def send_alert(self, message: str) -> None: 
        pass

#implementing OCP and LSP
#engine

class coreactionengine(actioninterface):
    def execute_action(self, data: dict) -> bool:
        print(f"Action executed with data: {data}")
        return True
    
class corealertengine(alterinterface):
    def send_alert(self, data: str) -> None:
        print(f"Alter dispatched: {message}")
    
#implementing SRP
#django model

class corerecord(models.Model):
    status = models.CharField(max_length=20, default="pending")
    meta_data = models.JSONField(default=dict)

class meta:
    abstract = True

#implementing SRP and DIP
#orchestrator

class workflow:
    def __init__(self, action_engine: actioninterface, context_data: dict) -> bool:
        success = self.action_engine.execute_action(context_data)
        
        if success:
            reload.status = "processed"
            self.alert_engine.send_alert("Workflow completed sucessfully")

        return False
    
#implementing SRP 
#django view

class coreview(View):
    def post(self, request, record_id):
        record = corerecord()

        orchestrator = workflow(
            action_engine=coreactionengine()
            alterinterface=corealertengine()
        )

        if orchestrator.run_workflow(record, request.POST.dict()):
            return JsonResponse({"status": "sucess"})
        else:
            return JsonResponse({"status": "failed"}, status = 400) 