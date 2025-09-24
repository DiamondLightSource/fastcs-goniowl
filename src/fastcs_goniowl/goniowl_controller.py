from fastcs.controller import Controller


class GoniOwlController(Controller):
    def __init__(self) -> None:
        # Create a Jungfrau detector object
        # and initialise it with a config file
        print("controller!")

        super().__init__()
