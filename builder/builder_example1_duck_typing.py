from builder.builder_example1 import Robot


class RobotBuilder:
    def __init__(self):
        self.robot = Robot()

    def build_head(self, head):
        self.robot.head = head

    def build_body(self, body):
        self.robot.body = body

    def build_arms(self, arms):
        self.robot.arms = arms

    def build_legs(self, legs):
        self.robot.legs = legs

    def get_robot(self):
        return self.robot


class RobotDirector:
    def __init__(self, robot_builder):
        self.robot_builder = robot_builder

    def construct_robot(self):
        self.robot_builder.build_head("Round")
        self.robot_builder.build_body("Metal")
        self.robot_builder.build_arms("Claws")
        self.robot_builder.build_legs("Wheels")


class Robot:
    def display_robot_info(self):
        print("Robot Info: ")
        print(f"Head: {self.head}")
        print(f"Body: {self.body}")
        print(f"Arms: {self.arms}")
        print(f"Legs: {self.legs}")


robot_builder = RobotBuilder()
robot_director = RobotDirector(robot_builder)

robot_director.construct_robot()
robot = robot_builder.get_robot()

robot.display_robot_info()
