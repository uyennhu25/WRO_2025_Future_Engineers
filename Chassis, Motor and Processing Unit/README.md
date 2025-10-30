Chassis development:

We develop the chassis with three principles in mind:
Low center of gravity
Lightweight
Minimum Size 

Chassis material choice: LEGO & PLA

We start the development our robot using LEGO because we have very rigorous experience with building and essemblying LEGO models. Lam parcipitated in WRO 2023 and WRO 2024 in Junior Category so he is very familiar with building robot with LEGO as the main material.

We 3D print several parts which does not exist in the current LEGO collection; they can accomodate LEGO just as good as authentic LEGO pieces, and the freedom of customisation help us with reaching our main design principles with the chassis. 

Processing Unit: LEGO® Education SPIKE™ Prime
    
We choose LEGO processing units, Spike Prime or Mindstorm EV3, over adruino or raspberry pi because our past experience shows that we can execute complicated algorithms at an acceptable level.

Between EV3 and Spike Prime, we choose Spike Prime despite the fact that the central processing unit of the Spike Prime has a lower clock speed, as the Spike Hub's performance is still adequate for our algorithms. The Spike Prime Hub including battery is around 200 grams, almost half as light as the EV3 Hub; the total volume occupied by the Spike Prime Hub is around 0.158L, more than half as small as the EV3 Hub, which occupies 0.388L. These two characteristics of the Spike Hub make its superiorly favorable to use compared to the EV3 Hub 

Motors: Technic™ Large Motor L and XL
    
With a LEGO chassis, we can opt for LEGO motors, which are way lighter than other pervasive,conventional robotics motors such as the GA25 370. Even though the torque figures and RPM are not as impressive, the benefit of having a manageable wiring system and light plastic case defenitely outweight this disadvantage. 

For our powertrain, we use the Technic Powered up L motor instead of the Original Spike Motors because its much higher RPM (315 vs 250) and its smaller size, and the breadth of the mounting hole on its case makes it extremely versatile in case of mounting position.

For our steering compartment, we utilize the Technic Powered up XL motor with a 3:1 gearbox to maximize torque. The stall torque of this motor is higher than the Spike Angular Motor (40Ncm vs 25Ncm). However, after completing our first version of the robot, we found out that such impressive torque figures are still not satisfactory for the turning compartment
<p align="center">
  <img src="Images/Powered%20Up%20Motors.png" width="600">
</p>


Differential drivetrain: 

During cornering scenarios, the two rear wheels must rotate at diffent angular velocity in order to maintain the difference between the radius of the two circles accomodated by the inner wheel and outer wheel. Therefore, we implement a differential system. 

<p align="center">
  <img src="Images/Differential.png" width="600">
</p>

Ackermann Steering:

Upon steering, the inner side of the robot facing the center of the rotation aligns with a circle of smaller radius, which has a tangent of different angle compared to the outer circle. In order to achieve the maximum turning effect, the wheel need to steer at different angle in order to accomodate the tangents, and we will use ackermann steering to achieve this.
<p align="center">
  <img src="Images/Ackermann.png" width="350">
  <img src="Images/Ackermann_2.png" width="350">
</p>

Camera: Matrix Robotics M-Vision Cam with Type-C Cable Pack

We use Matrix Robotics's M-Vision Cam over other cameras because it has a processing unit inside the camera itself. Consequently, the LEGO Spike Prime Hub does not have to execute extra image processing algorithms, prolonging the battery life and maintain a healthy load on the processing unit
<p align="center">
  <img src="M%20Vision%20Cam" width="600">
</p>
