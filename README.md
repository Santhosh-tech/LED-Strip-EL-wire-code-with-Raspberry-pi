# LED Dance code for Raspberry pi

This above code controls the LED strip or EL wires by connecting it to Raspberry pi. The installation of the code is so simple. The code makes the Lights blink fast, blink medium, glow, dim and much more according to needed timings. I have made this code for Dance performance using LED strip but it also works well with EL wire. The code can be edited for required timings.

STEP 1: Wire the shirt and Pant

Paste the LED Strip or EL wire in your shirt and pant by making four connections such as right hand, left hand, right leg and left leg. For any shapes or formations Red and Green color LED is used in my case.

STEP 2: Make the required circuit

Make a circuit by connecting NPN transistors (three pin) in my case. To connect LED strip NPN transistor 122 can be used. Connect the positive and negative to the transistor pins in the circuit. The circuit can be designed as per your needs. Connect a switch in circuit.

STEP 3: Connect to raspberry pi

Now, connect the center pin from the transistor to the pins in Raspberry pi as per the following.

Right Hand = 7

Left Hand = 24

Right leg = 18

Left leg = 23

Red color = 12

Green color = 8

Refer Raspberry pi pin diagram to identify pin numbers.

STEP 4: Copy the Above code in Raspberry pi

Copy the above code in raspberry pi desktop and run the program by typing the following commands in terminal:

cd Desktop

sudo python suitecode.py
