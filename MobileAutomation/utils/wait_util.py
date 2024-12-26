import time

class WaitUtil:
    def pause(self, milliseconds=2000):
        """
        Pause execution for a few seconds.
        :param milliseconds: Time in milliseconds to pause (default is 2000ms).
        """
        time.sleep(milliseconds / 1000)  # Convert milliseconds to second