# onRobot

A simple gripper library to use a Universal Robot with an onRobot gripper, no onrobot compute box needed!

**See further down for usage examples**

- Simple and easy to use!
- No onRobot compute box needed!
- Communicates with XML-RPC interface so is compatible with ROS driver!
- Supports RG2 only, more coming soon!

# Install instructions

```bash

pip install onrobot


```
# Example Usage

```python
from onRobot import RG2

# Default id is zero, if you have multiple grippers, 
# see logs in UR Teach Pendant to know which is which :)
rg_id = 0
rg_gripper = RG2(rg_id)

rg_width = rg_gripper.get_rg_width()
pregrasp_width = 100

# force and width units described in onRobot RG2 Manual
target_width = 15.66
target_force = 40.00

if (rg_wdith == pregrasp_width):
    rg_gripper.rg_grip(target_width, target_force)

epsilon = 0.05 # Just an example of reasonable error may not be realistic. 
grip_success = abs(rg_gripper.get_rg_width() - target_width) < epsilon

```


# Functions to be implemented for the RG2

- [ ] rg_stop
- [x] rg_grip
- [ ] rg_calibration
- [ ] rg_get_all_variables
- [ ] rg_get_all_double_variables
- [ ] rg_get_all_integer_variable>
- [ ] rg_get_all_boolean_variable>
- [ ] rg_get_speed
- [ ] rg_get_depth
- [ ] rg_get_relative_depth
- [ ] rg_get_angle
- [ ] rg_get_angle_speed
- [x] rg_get_width
- [ ] rg_get_fingertip_offset
- [ ] rg_get_status
- [ ] rg_get_busy
- [ ] rg_get_grip_detected
- [ ] rg_get_s1_pushed
- [ ] rg_get_s1_triggered
- [ ] rg_get_s2_pushed
- [ ] rg_get_s2_triggered
- [ ] rg_get_safety_failed
- [ ] rg_set_fingertip_offset