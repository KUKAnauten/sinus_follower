#Sinus_follower 

1. roslaunch iimoveit run_movegroup.launch **or** roslaunch iiwa_moveit moveit_planning_execution.launch
2. rosrun sinus_follower sinus.py /freq /rate <!-- freq zB 0.1 Hz, rate zB 100-->
3. roslaunch sinus_follower sinus_follower.launch
