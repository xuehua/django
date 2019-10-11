# Install and Run React

## Install React on windows 
1. Install nvm-windows. 
   The nvm-windows is an open source accesbible at
   https://github.com/coreybutler/nvm-windows. It has an installer at
   https://github.com/coreybutler/nvm-windows/releases.
   Download nvm-setup.zip of release 1.1.7, which is the latest at this time.
   Unzip the file and install the nvm-setup.exe.   
   
2. Install node.js
   At command line, we can run "nvm install latest" to install the latest stable
   version. 
   From the print out of the command, we can see node.js version 12.11.1
   (65-bit) is installed. Run "nvm use 12.11.1" to use this version. 

3. Go to the todo's project directory and run "npx create-react-app frontend"

4. Go to the frontend directory and run "npm start" and we can see
   localhost:3000 is opened in the system default browser.  