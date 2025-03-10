
class Employee:
    def __init__ (
            self,
            frontend : bool = False,
            backend : bool = False
    ):
        self.designation = "Developer"
        self.frontend = frontend
        self.backend = backend

    def __repr__ (self):
        return '{}'.format (self.designation, self.frontend, self.backend)

    ### Write the your method over here.
    def verifier (self):
        if ((self.backend) and (self.frontend)):
            return 'Fullstack '
        elif self.backend:
            return 'Backend '
        elif self.frontend:
            return 'Frontend'
        else:
            return 'Not a '


frnt = bool(int(input("Does Employee know Frontend Coding?(Yes->1/No->0)\n")))
bck = bool(int(input("Does Employee know Backend Coding?(Yes->1/No->0)\n")))
firstEmployee = Employee (frontend=frnt, backend=bck)
result = firstEmployee.verifier()
print(result, firstEmployee.designation)
