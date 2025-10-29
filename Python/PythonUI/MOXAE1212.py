from pymodbus.client import ModbusTcpClient

class MoxaE1212:
    """Class to interface with the MOXA ioLogik E1212 External IO Module.
    https://www.moxa.com/en/products/industrial-edge-connectivity/controllers-and-ios/universal-controllers-and-i-os/iologik-e1200-series/iologik-e1212

    Attributes
    ----------
    modbusConnection : ModbusTcpClient object
        The Modbus object from the pymodbus library used to communicate with the device.
    outputStatus : list of bool
        The current status of the digital outputs of the MOXA E1212.
    address : string
        The IP address of the device.

    """
    def __init__(self):
        """Constructor for an instance of the MoxaE1212 class."""
        self.address = None

        self.outputStatus = [False, False, False, False, False, False, False, False]


    def _getoutputstatus(self):
        """Private method to get the actual status of the digital outputs. This is done once in the constructor."""
        if not self.modbusConnection.is_socket_open():
            ret = self.connect()
            if not ret:
                return
        rq = self.modbusConnection.read_coils(0, 8)
        if rq.isError():
            print("Could not get the values")
        self.outputStatus = rq.bits
        return

    def connect(self, address):
        """Attempts to connect to the device.
        Return
        ------
        Bool
            True if connected, False otherwise.
        """
        self.address = address
        self.modbusConnection = ModbusTcpClient(address)
        r = self.modbusConnection.connect()
        if not r:
            print("Could not connect to the module.")
            return r
        self._getoutputstatus()
        return r

    def setsingleoutput(self, pos, value):
        """Sets a single output to the desired value.
        Parameters
        ----------
        pos : int
            Number of the output to set.
        value : Bool
            True to set to High, False to set to Low.

        Return
        ------
        Bool
            True if output was set correctly, False otherwise.
        """
        if not self.modbusConnection.is_socket_open():
            ret = self.connect()
            if not ret:
                return False
        try:
            self.outputStatus[pos] = value
        except IndexError:
            print("Index Error: Not a valid output position")
            return False
        rq = self.modbusConnection.write_coils(0, self.outputStatus)
        if rq.isError():
            print("Could not set the value properly")
            return not rq.isError()
        return not rq.isError()

    def readsingleinput(self, pos):
        """Read a single digital input from the MOXA E1212.

        Parameters
        ----------
        pos : number of the IO to read.

        Return
        ------
        Bool or None
            True if High, False if Low, None if an error has occurred.
        """
        if pos > 7:
            print("Not a valid input position")
            return None
        if not self.modbusConnection.is_socket_open():
            ret = self.connect()
            if not ret:
                return None
        rq = self.modbusConnection.read_discrete_inputs(0,8)
        if rq.isError():
            print("Could not read the value")
            return None
        return rq.bits[pos]

    def setalloutputs(self, values):
        """Set the value of all the digital outputs of the MOXA E1212.
        Parameters
        ----------
        values : List of bool.
            A list of 8 elements where True is High and False is Low.
        Return
        ------
        Bool
            True if the values were set correctly, False otherwise.
        """
        if not self.modbusConnection.is_socket_open():
            ret = self.connect()
            if not ret:
                return False
        try:
            self.outputStatus = values
        except IndexError:
            print("Index Error: Not a valid output position")
            return False
        rq = self.modbusConnection.write_coils(0, self.outputStatus)
        if rq.isError():
            print("Could not set the value properly")
            return not rq.isError()
        return not rq.isError()

    def readallinputs(self):
        """Reads all the inputs of the MOXA E1212
        Return
        ------
        List of bool or None
            A list of bool where True is High and False is Low or None if an error has occurred
        """
        if not self.modbusConnection.is_socket_open():
            ret = self.connect()
            if not ret:
                return None
        rq = self.modbusConnection.read_discrete_inputs(0, 8)
        if rq.isError():
            print("Could not read the values")
            return None
        return rq.bits

    def waitforinput(self, pos, state):
        inp = None
        while inp is not state:
            inp = self.readsingleinput(pos)
        return
