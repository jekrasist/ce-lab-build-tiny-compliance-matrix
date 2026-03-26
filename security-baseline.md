# AWS Security Baseline — Verification Report

**Date:** 2026-03-26T14:12:48Z
**Engineer:** Ahmet Erdogan
**Account ID:** 741429964627
**Region:** us-east-1

---

## Controls Implemented

| Control | Description | Status | Command to Verify |
|---|---|---|---|
| Least-privilege SG | SSH from 87.210.201.57/32 only | ✅ Active | `aws ec2 describe-security-groups --group-ids sg-0bc6960cc80f4f3db` |
| VPC Flow Logs | ALL traffic captured to CloudWatch | ✅ Active | `aws ec2 describe-flow-logs` |
| EBS encryption by default | New volumes auto-encrypted | ✅ Enabled | `aws ec2 get-ebs-encryption-by-default` |
| CloudTrail | All API calls logged to S3 | ✅ Logging | `aws cloudtrail get-trail-status --name lab-m8-08-security-trail` |

---

## Resources Created
- **Security Group:** sg-0bc6960cc80f4f3db
- **VPC Flow Logs:** /aws/vpc/flow-logs (CloudWatch)
- **CloudTrail Bucket:** cloudtrail-logs-741429964627-1774533681
- **EC2 Instance:** i-03721bf55e871f15a (54.209.156.206)

---

## Test Results
- SSH connection to EC2 instance: ✅ Successful
- EBS volume on instance is encrypted: ✅ Confirmed (vol-0209417be326e386c)
- RunInstances event visible in CloudTrail: ✅ Confirmed

---

## Security Design Decisions
- **SSH restricted to /32:** Implements Least Privilege by denying the entire internet.
- **T3.Micro over T2:** Better performance and full Free Tier support in us-east-1.
- **EBS Encryption:** Ensures data-at-rest protection is a baseline standard, not an option.
