Chassis and Drivetrain Design
The robot is built around a two-part mechanical structure consisting of the main chassis and a modular drivetrain unit. The main chassis houses the Raspberry Pi, motor driver, sensors, and battery. Meanwhile, the drivetrain unit is responsible for delivering power to the wheels and handling steering. This modular separation allows for easier assembly, maintenance, and mechanical tuning.

From LEGO to Fusion 360
We began prototyping the chassis using LEGO to experiment with proportions and component placement. Once the layout was validated, we transitioned to Fusion 360 for precise 3D modeling. This allowed us to fine-tune the design and reduce unnecessary material, keeping the total weight low without sacrificing rigidity. The final chassis dimensions are 223 mm (L) × 180 mm (W) × 124 mm (H).

Integrated Mounts & Chassis Optimization
To save material and avoid unnecessary weight, we designed the motor mounts directly into the chassis, eliminating the need for separate brackets. The sides of the chassis are narrowed to shorten wire lengths and improve internal cable routing. In contrast, the front and rear ends are wider, offering strong attachment points for the drivetrain and more space to mount other mechanical components. 
[](motor_mount_1.png)
[](motor_mount_2.png)
[](motor_mount_.png)

From a physics perspective, the design prioritizes minimizing rotational inertia. According to Newton’s First Law, mass resists changes in velocity. A heavier or taller robot would be harder to control during fast cornering due to inertia. To counter this, we kept the center of mass low and distributed mass symmetrically. The result is a more stable robot with sharper turning capability and improved dynamic control.

Motor & Drivetrain Rework
Initially, we used JGB37-520 motors, but we found them too powerful and bulky for our ~1.5 kg robot. They caused the undercarriage to be too tall, which raised the center of gravity and made the robot less stable. We replaced them with GA25 motors, which are lighter, more compact, and easier to integrate. This change also required modifying axle connectors from 6mm to 4mm.

We manually redesigned the frame for the differential system, reducing its size to better fit the compact chassis. During the process, we found enough space to align the steering system and drivetrain motor on a straight axis, so we moved the motor to the center of the chassis. This centralized layout improves torque distribution between the rear wheels, enhancing straight-line acceleration and corner balance.

Mounting & Modularity
We designed several camera mounts with different viewing angles to evaluate visibility during testing. These modular designs allow flexibility in adjusting the field of view depending on track conditions or processing needs.
[](angles.png)

