# onRobot


![](./UOY-logo.svg)

Developed at The University of York

A simple gripper library to use a Universal Robot with an onRobot gripper, no onrobot compute box needed.


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
import onRobot.gripper as gripper

rg_id = 0
ip = "192.168.56.101"
rg_gripper = gripper.RG2(ip,rg_id)

rg_width = rg_gripper.get_rg_width()
print("rg_width: ",rg_width)

target_force = 40.00

rg_gripper.rg_grip(100.0, target_force)



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
