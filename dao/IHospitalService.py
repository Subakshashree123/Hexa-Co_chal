import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from abc import ABC, abstractmethod
from Models.Appointment import Appointment
from typing import List

class IHospitalService(ABC):
    @abstractmethod
    def get_appointment_by_id(self, appointment_id):
        pass

    @abstractmethod
    def get_appointments_for_patient(self, patient_id):
        pass

    @abstractmethod
    def get_appointments_for_doctor(self, doctor_id):
        pass

    @abstractmethod
    def schedule_appointment(self, appointment):
        pass

    @abstractmethod
    def update_appointment(self, appointment):
        pass

    @abstractmethod
    def cancel_appointment(self, appointment_id):
        pass