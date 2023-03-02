# Auto Push

Automatically push the changes of a local Git repository to remote on system startup

## Usage

```bash
vim ~/.push-config 	# Add the absolute path of the Repositories/Directories. One per Line

# As a Service
cd /etc/systemd/system
touch auto-push.service

# Service File (auto-push.service)
[Unit]
Description=Automatically push changes to Remote on System Startup 

[Service]
ExecStart=/usr/bin/python3 /path/to/program /path/to/config
User=user

[Install]
WantedBy=multi-user.target

```

