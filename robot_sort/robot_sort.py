class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """

        """
            ! UPER !

            -> -- U (Understand) --
            - The robot will have to have the light turned on while sorting. 
                - Then I can turn it off when I have completed sorting, breaking out of the while-loop.
            - The robot is going to have to iterate through each item and compare the values.
                - I will have to check to make sure the robot can move left/right before making the move.
                - I can use the robot's helper function that will return:
                    - -1 (current item is lesser)
                    - 0 (current item is same)
                    - 1 (current item is greater).
                - From the helper function's return value, I can make my determination on whether to swap or not.

            -> -- P (Plan) --
            - I am going to use a while-loop that cross-checks whether the robots light is on/off and subsequently to keep running.
                - While running, the robot can preform it's actions (move left/right and compare/swap).
           
            -> -- E (Execute) --
        """

        # -> Turn the light on first to allow the while-loop to run.
        self.set_light_on()

        # -> Initalize the while loop to run until light is turned off.
        while self.light_is_on():

            # -> Robot starts with an empty hand, we will just pick up the first item it start on.
            self.swap_item()

            # -> This is where we can start iterating through the list of items. 
            # -> We can use the while-loop to make sure that the robot CAN move right before making the move.
            while self.can_move_right():

                # -> We CAN move right, so do so.
                self.move_right()

                # -> We've move one to the right and are above a new item. Compare the current item in hand to the item we're standing above.
                comparison = self.compare_item()

                # -> Check to see if the comparison is 1 (item in hand is greater).
                if comparison == 1:
                    # -> Item in hand is greater than the item that we're standing on. Swap them.
                    self.swap_item()
            
            # -> At the beginning when we did the first swap, we swap our None value with the item.
            # -> So we have to go back to that position by getting the item that is one after it; 
            # -> and move left one the the correct position.
            while self.can_move_left() and self.compare_item() !=None:
                self.move_left()

            #-> Then move swap the item in hand with the None value in place.
            self.swap_item()
            # -> Then move right one so when then next iteration goes around, it will start at the next element.
            self.move_right()

            # -> If the robot can not move right anymore, then shut the light off. Else, continue to next loop iteration.
            if not self.can_move_right():
                self.set_light_off()
            else: continue



if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)