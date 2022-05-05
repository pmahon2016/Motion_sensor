# Motion_sensor

1. mkdir sensor in root(home directory) of pi user
2. Clone the repo in the sensor dir. 'git clone https://github.com/pmahon2016/Motion_sensor.git'
3. run 'python sensor.py' in the clone dir

# Run as a process / service
1. From the clone dir type 'sudo cp motion_detect.service /etc/systemd/system'
2. sudo systemctl daemon-reload
3. sudo systemctl start motion_detect.service
4. sudo systemctl enable motion_detect.service ( to run at system startup)
