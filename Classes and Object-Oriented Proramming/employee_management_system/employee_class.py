#employee class
class Employee:
    def __init__(self, name, id_number, department, job_title):
        self.__name = name
        self.__id = id_number
        self.__department = department
        self.__job = job_title
    def set_name(self, name):
        self.__name = name
    def set_id(self, id_number):
        self.__id = id_number
    def set_department(self, department):
        self.__department = department
    def set_job(self, job_title):
        self.__job = job_title
    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
    def get_department(self):
        return self.__department
    def get_job(self):
        return self.__job
