class Parent():
    def __init__(self, last_name, eye_color):
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("last name: " + self.last_name)
        print("eye color: " + self.eye_color)

class Child(Parent) :
    def __init__(self,last_name,eye_color,num_toys):
        Parent.__init__(self,last_name,eye_color)
        self.num_toys = num_toys

    def show_info(self):
        print("last name: " + self.last_name)
        print("eye color: " + self.eye_color)
        print("num toys: " + str(self.num_toys))

billy_cyrus = Parent("Cyrus","blue")
billy_cyrus.show_info()
miley_cyrus = Child("Cyrus", "Blue", 5)
miley_cyrus.show_info()
# print miley_cyrus.num_toys
# print miley_cyrus.last_name