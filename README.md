# Motion_sensor

1. mkdir sensor ( in root of pi user)
2. Clone the repo to your Raspberry Pi
3. run 'pip install smtplib'
4. run 'python sensor.py' in the clone dir
5. sudo cp motion_detect.service /etc/systemd/system
6. sudo systemctl daemon-reload
7. sudo systemctl start motion_detect.service
8. sudo systemctl enable motion_detect.service
