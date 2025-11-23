# Engineering Documentation - NSWRO Team
This is the GitHub repository of team NSWRO for the WRO 2025 Future Engineers Category
![](/Team/Images/NSWRO.png)

## Content
`Chassis, Motor and Porcessing Unit` This folder includes diagrams and images featuring the components of our robot.
`Programming` This folder includes the programs and their corresponding illustrations.
`Robot` This folder includes images of our robots from all views.
`Team` These are the photos of our team!

Our README consists of:
- <a name="our_team">Our Team</a>
- <a name="hardware">Chassis, Motor and Processing Unit</a>
  - <a name="material">Chassis Material</a>
  - <a name="processor">Processing Unit</a>
  - <a name="motors">Motors</a>
  - <a name="drivetrain">Differential Drivetrain</a>
  - <a name="ackermann_steering">Ackermann Steering</a>
  - <a name="camera">Camera</a>
- <a name="software">Programming</a>
  - <a name="open">Open challenge</a>
  - <a name="obstable">Obstable challenge</a>
- <a name="vehicle_photos">Vehicle Photos</a>
- <a name="video">Videos</a>

## [Our Team](#our-team)
![](/Team/Images//Team%20Photo.jpg)

<h3>Overall:</h3>
   NSWRO is a team composed of three students from Nguyen Sieu High School who collaborate with Thay Phong Stem for the WRO 2025 season. We are the first team from Vietnam to compete in this category. Thus, there are many problems and difficulties, yet there are also many opportunities and experience we can gain from this event.

<h4>Cao Tung Lam (on the right)</h4>
    Lam is the most experienced team member. He has competed in WRO for three seasons. He has won acclaim by finishing 8th in the Junior Robomission category in 2024. This year, looking to enrich and diversify his experience in robotics, he chose Future Engineer to bolster his knowledge with new engineering concepts and new programming experience.

<h3>Do Cong Danh (on the left)</h3>
   This season is not Danh's first season, but it is his first season in such a high skill level environment. His contribution in this team is designing and assemblying the robot, assemblying the field. He also discovered many engineering principles which help our robot develop.

<h3>Nguyen Uyen Nhu (in the middle)</h3>
    Just like Do, this is Nhu's first season in WRO. However, her rich experience with programming and GitHub helped her build this impressive repository. Furthermore, he aided Lam in the programming process, making the programmes more efficient and the algorithms to be more accurate.


## [Chassis, Motor and Processing unit](#hardware)
Here is our hardware documentation.
<h3>Our main goal for the development of our chassis</h3>

Low center of gravity
Lightweight
Minimum Size

<h3>[Chassis material choice: LEGO and PLA](#material)</h3>

We start the development of our robot using LEGO because we have extensive experience with building and assembling LEGO models. Lam participated in WRO 2023 and WRO 2024 in the Junior Category, so he is very familiar with building robots with LEGO as the main material.

We 3D print several parts which does not exist in the current LEGO collection; they can accommodate LEGO just as good as authentic LEGO pieces, and the freedom of customisation helps us with reaching our main design principles with the chassis.

<h3>[Processing Unit: LEGO® Education SPIKE™ Prime](processor)</h3>
   
We choose LEGO processing units, Spike Prime or Mindstorm EV3, over Arduino or Raspberry Pi because our experience shows that we can execute complicated algorithms at an acceptable level.

Between EV3 and Spike Prime, we chose Spike Prime even though the central processing unit of the Spike Prime has a lower clock speed, as the Spike Hub's performance is still adequate for our algorithms. The Spike Prime Hub, including battery, is around 200 grams, almost half as light as the EV3 Hub; the total volume occupied by the Spike Prime Hub is around 0.158L, more than half as small as the EV3 Hub, which occupies 0.388L. These two characteristics of the Spike Hub make it superior to use compared to the EV3 Hub

<div style="display: flex; align-items: center;">
  <div>

|                 | Mindstorm EV3 | Spike Prime |
|-----------------|---------------|--------------|
| CPU Clock Speed (MHz) | 300 | 100 |
| Weight (g) | 385 | 200 |
| Volume Occupied (L) | 0.388 | 0.158 |

  </div>
  <img src="Chassis, Motor and Processing Unit/Images/EV3 vs Spike.png" width="400" style="margin-left: 20px;" />
</div>

<h3>[Motors: Technic™ Large Motor L and XL](#motors)</h3>
   
With a LEGO chassis, we can opt for LEGO motors, which are way lighter than other pervasive, conventional robotics motors such as the GA25 370. Even though the torque figures and RPM are not as impressive, the benefit of having a manageable wiring system and light plastic case definitely outweighs this disadvantage.

For our powertrain, we use the Technic Powered up L motor instead of the Original Spike Motors because it's much higher RPM (315 vs 250) and its smaller size, and the breadth of the mounting hole on its case makes it extremely versatile in case of mounting position.

For our steering compartment, we utilize the Technic Powered up XL motor with a 3:1 gearbox to maximize torque. The stall torque of this motor is higher than the Spike Angular Motor (40Ncm vs 25Ncm). However, after completing our first version of the robot, we found out that such impressive torque figures are still not satisfactory for the turning compartment
<p align="center">
  <img src="Chassis, Motor and Processing Unit/Images/Powered Up Motors.png" width="600">
</p>


<h3>[Differential drivetrain](#drivetrain)</h3>

During cornering scenarios, the two rear wheels must rotate at different angular velocities to maintain the difference between the radius of the two circles accommodated by the inner wheel and outer wheel. Therefore, we implement a differential system.

<p align="center">
  <img src="Chassis, Motor and Processing Unit/Images/Differential.png" width="600">
</p>

<h3>[Ackermann Steering](#ackermann_steering)</h3>

Upon steering, the inner side of the robot facing the center of the rotation aligns with a circle of a smaller radius, which has a tangent of a different angle compared to the outer circle. In order to achieve the maximum turning effect, the wheel need to steer at a different angle in order to accommodate the tangents, and we will use ackermann steering to achieve this.
<p align="center">
  <img src="Chassis, Motor and Processing Unit/Images/Ackermann.png" width="350">
  <img src="Chassis, Motor and Processing Unit/Images/Ackermann_2.png" width="350">
</p>

<h3>[Camera: Matrix Robotics M-Vision Cam with Type-C Cable Pack](#camera)</h3>

We use Matrix Robotics's M-Vision Cam over other cameras because it has a processing unit inside the camera itself. Consequently, the LEGO Spike Prime Hub does not have to execute extra image processing algorithms, prolonging the battery life and maintaining a healthy load on the processing unit
<p align="center">
  <img src="Chassis, Motor and Processing Unit/Images/M Vision Cam.jpg" width="400">
</p>

## [Programming](#software)
Here is our software documentation
<h3>[Open Challenge:](#open)</h3>
   
We draw two boxes on two sides. We set a threshold, and if a pixel has RGB value within the threshold, it will be counted as "black". In order for the robot at the middle of the path, the fill of the two boxes must be equal. Therefore, our algorithm compare the fill ratio of the two boxes and use PID turning for the steering.

We also have a box at the center of the frame. When a color between orange or blue touches this box, it will know when to start turning. If the box detects the blue line first, it can be inferred that the robot is running in the counterclockwise direction and vice versa.

In addition to the main boxes, we include two small boxes at the bottom of the frame. These bottom boxes only turn black when the robot has moved into a position where the front boxes can no longer see the black line and the robot is very close to the wall. When both bottom boxes detect black, the robot enters a priority correction mode, where steering decisions rely on the bottom boxes instead of the main ones. This prevents the robot from hugging the wall or losing the track when the front sensors no longer provide reliable data.

![](/Programming/Images/Open%201)
![](/Programming/Images/Open%202.png)



<h3>[Obstacle Challenge:](#obstable)</h3>

Scenario 1: Traffic signs visible
The camera detects a region of high density of either red or green in the field. It will draw a rectangle box around the block. For the robot to avoid the sign in the desired direction, the boxes must align with the two lines. Therefore, by measuring the distance between the base of the rectangles and the lines, an error value can be calculated and used for PID steering.

<p align="center">
  <img src="Programming/Images/Obstacle%20Diagram.png" width="600">
</p>

Scenario 2: Passed all traffic signs
When no color of red or green is visible, the robot will infer that it has passed all traffic signs.  Now, a box is drawn on the left side of the camera, and the robot will attempt to drive relatively close to the wall, filling the box with 70% black color. The difference between the black color fill of the box and the 70% threshold is used for PID turning. Another box is drawn in the middle, and when the blue line touches that block, it will know that it needs to start turning. By doing so, the robot will be given the maximum possible turning angle, and when it completes turning, the distance from it to the incoming sign will be far, allowing it to make a lot of changes in course before executing a  maneuver around the line

<p align="center">
  <img src="Programming/Images/Scenario 2.png" width="600">
</p>

After the robot completes 3 laps, the robot will align with the same method used with the blocks. When the robot aligns with the wall of the parking lot, it will run until the magenta color reaches a particular x coordinate on the camera. After this, we program a sequence of actions for the robot to execute. The reason why we choose such a rudimentary method rather than using computer vision for parking is that the distance travelled by the robot during this short task is really short, so the error margin of using the encoder is acceptable. Furthermore, our skill in handling computer vision data is not thorough enough to program such a difficult task using values extrapolated from the camera.

<p align="center">
  <img src="Programming/Images/Parking%20Diagram.png" width="600">
</p>

## [Vehicle Images](#vehicle_photos)
![Front view](/Robot/Images/ver2/front_view.png)
![Left view](/Robot/Images/ver2/left_view.png)
![Right view](/Robot/Images/ver2/right_view.png)
![Back view](/Robot/Images/ver2/back_view.png)
![Top view](/Robot/Images/ver2/top_view.png)
![Bottom view](/Robot/Images/ver2/bottom_view.png)

## [Video](#video)
This is our video for the open challenge!
[Click here!](https://youtu.be/54i8wre7FL8)