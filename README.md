#Sinus_follower 

1. roslaunch iimoveit run_movegroup.launch **or** roslaunch iiwa_moveit moveit_planning_execution.launch
2. rosrun sinus_follower sinus.py /freq /pubRate <!-- freq zB 0.1 Hz, pubRate zB 100-->
3. roslaunch sinud_follower sinus_follower.launch