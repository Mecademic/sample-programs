# Meca500 - Unitronics PLC Integration

This MecaNetwork example features the Meca500 being used with a Unitronics Samba 3.5" PLC over TCP/IP.

The example program provided can also be adapted to a variety of other Unitronics PLCs.

You can use this program to jog the robot directly from the Samba's HMI and start programs saved on the robot's controller or stream position commands.

---

## Downloads

**User Guide with the setup steps:** [Mecademic Visilogic TCPIP User Guide](Attachments/Mecademic%20VisiLogic%20TCPIP%20User%20Guide.pdf)

**PLC and HMI program:** [Mecademic_VisiLogic_Demo_V0_11_1.vlp](Attachments/Mecademic_VisiLogic_Demo_V0_11_1.vlp)

---

## Requirements

### Hardware Requirements
- **[Meca500 Robot](https://www.mecademic.com/)** 
- **[Unitronics Samba SM35-J-TA22 PLC](http://www.unitronicsplc.com/samba-series-samba35/)**
- **Ethernet network connection** between robot and PLC

### Software Requirements
- **[Unitronics VisiLogic Software](https://www.unitronicsplc.com/software-visilogic-for-programmable-controllers/)**
- **[Meca500 Firmware](https://www.mecademic.com/support/)** (Version 8.1.6 or above)

### Network Requirements
- **TCP/IP communication** enabled on robot
- **Robot and PLC on same network segment** or routed connection
- **Robot IP address** configured and accessible from PLC

---

_Please note that these examples are provided as-is by either Mecademic or it's Partners. These can be used as a starting point for development and testing but Mecademic or it's partners are not under obligation to provide support and are not liable for any errors or unintended behavior caused by the examples. These examples could be updated over time._