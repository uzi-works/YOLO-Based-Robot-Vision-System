def robot_decision(objects):

    for obj in objects:

        if obj == "person":
            print("Robot: Hello human!")

        elif obj == "bottle":
            print("Robot: Bottle detected.")

        elif obj == "cup":
            print("Robot: Cup detected.")

        elif obj == "cell phone":
            print("Robot: Phone detected.")