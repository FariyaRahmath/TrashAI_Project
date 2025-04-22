# TrashAI_Project

## Installation and File Download
1. Uninstall all the Python IDLE, Jupyter, any local servers (like WampServer) if it is already installed in your system/ laptop.
2. Then, install the Python IDLE and WampServer that I have given in the main branch.
3. There are 2 more branches in addition to the main branch - Training and Testing branches.
4. Download all the files and folders of the Training and Testing branches as well.
5. Keep 2 separate folders in your systems for the Training and Testing branches' files and folders.

## Project Execution
1. Click Start -> Start WampServer
2. There will be an up arrow in the right corner of the taskbar. Click it and then click on the WampServer symbol. Then click "Start All Services".
3. Then open Chrome browser and type "localhost".
4. After that, open the main.py file of Training folder. You should see a message in it called "Debugger is now active".
5. Then in a new tab in Chrome, type "localhost:5000".
6. Then you will be prompted to enter the Admin username and password. Both the username and password is "admin".
7. After entering the credentials, start the training process by uploading the images from the "static" or "upload" folder.
8. After completing the training process, close the main.py file of Training folder.
9. After completing the training process, click logout.
10. Now, open the main.py file of Testing folder.
11. After opening it, refresh the chrome tab. Then, click on start testing. You will be prompted to enter Mobile Number and Email ID (for sending alerts).
12. After entering it, click start testing. It will repeat the training process before testing, please wait.
13. Then the model will prompt open the camera, and you'll have to place a trash object in front of the camera and the model will detect it and send alert (SMS and Email).
14. After being done with the detection, close the chrome tabs, main.py file and WampServer.
