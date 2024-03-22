class Patient:
    def __init__(self, patientId=None, firstName=None, lastName=None, dateOfBirth=None, gender=None, contactNumber=None, address=None):
        self.__patientId = patientId
        self.__firstName = firstName
        self.__lastName = lastName
        self.__dateOfBirth = dateOfBirth
        self.__gender = gender
        self.__contactNumber = contactNumber
        self.__address = address

    def get_patientId(self):
        return self.__patientId

    def get_firstName(self):
        return self.__firstName

    def get_lastName(self):
        return self.__lastName

    def get_dateOfBirth(self):
        return self.__dateOfBirth

    def get_gender(self):
        return self.__gender

    def get_contactNumber(self):
        return self.__contactNumber

    def get_address(self):
        return self.__address

    def set_patientId(self, patientId):
        self.__patientId = patientId

    def set_firstName(self, firstName):
        self.__firstName = firstName

    def set_lastName(self, lastName):
        self.__lastName = lastName

    def set_dateOfBirth(self, dateOfBirth):
        self.__dateOfBirth = dateOfBirth

    def set_gender(self, gender):
        self.__gender = gender

    def set_contactNumber(self, contactNumber):
        self.__contactNumber = contactNumber

    def set_address(self, address):
        self.__address = address

    def __str__(self):
        return f"Patient ID: {self.__patientId}, Name: {self.__firstName} {self.__lastName}, DOB: {self.__dateOfBirth}, Gender: {self.__gender}, Contact: {self.__contactNumber}, Address: {self.__address}"
