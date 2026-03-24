# VPC Flow Log Analysis Report

## Project Details
- **VPC ID:** vpc-0ed6d205ee10202e8
- **Account ID:** 741429964627
- **Region:** us-east-1

## Traffic Summary
- **Log Group:** /aws/vpc/flowlogs
- **Detection Method:** CloudWatch Metric Filter (SSHRejectFilter)
- **Status:** Active

## Security Findings
1. **SSH Brute Force Detection**
   - **Pattern:** Monitoring for `REJECT` actions on Destination Port 22.
   - **Target Instance:** 10.0.12.101 (app-server-1)
   - **Action:** Configured CloudWatch Alarm `rejected-ssh-attempts`.

2. **Alarm Configuration**
   - **Threshold:** > 100 rejected attempts within a 5-minute (300s) window.
   - **Notification:** Linked to SNS Topic `security-alerts`.

## Recommendations
- Review Security Group rules for `app-server-1` to ensure only trusted IPs can attempt port 22 access.
- Deploy AWS GuardDuty for advanced threat intelligence and automated IP blocking.
