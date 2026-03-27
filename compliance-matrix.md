# CIS AWS Foundations Benchmark Compliance Matrix

| ID | Control | Implementation | Evidence | Status | Priority |
|:---|:---|:---|:---|:---|:---|
| 1.4 | No root access keys | Checked IAM Summary | RootDeviceCredentialPresent: null | ✅ Compliant | - |
| 1.5 | MFA for root user | Checked Account Summary | AccountMFAEnabled: 1 | ✅ Compliant | - |
| 1.22| Password Policy (14+ chars) | Custom Policy Check | NoSuchEntity (Default active) | ❌ Failed | Medium |
| 3.1 | CloudTrail Multi-Region | Active Multi-region trail | lab-m8-08-security-trail | ✅ Compliant | - |
| 5.1 | SSH Restricted (Port 22) | Security Group Audit | 4 Violations Found | ❌ Failed | Critical |
| 2.1.1| S3 Public Access Block | Account-level check | s3control query | ⚠️ TODO | High |
| 3.2 | CloudTrail Log Validation | Integrity Check | LogFileValidationEnabled | ✅ Compliant | - |
| 1.16 | IAM Policies on Groups | User Policy Audit | list-user-policies | ✅ Compliant | - |
| 2.2.1| EBS Encryption Default | Regional Setting | EbsEncryptionByDefault | ✅ Compliant | - |
| 5.2 | RDP Restricted (3389) | Security Group Audit | describe-security-groups | ✅ Compliant | - |
