#!/bin/bash
yum update -y
yum install -y stress amazon-cloudwatch-agent
# Start stress: 2 CPUs for 1200 seconds (20 mins)
stress --cpu 2 --timeout 1200 &
# Start CW Agent
/opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -s
