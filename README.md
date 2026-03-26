# AWS GDPR Data Protection & Right to Erasure Workflow

This repository demonstrates a technically compliant infrastructure for handling Personal Identifiable Information (PII) of EU residents under the General Data Protection Regulation (GDPR).

## 🎯 Objectives
* **Data Residency:** Ensure data remains in the EU (`eu-west-1`).
* **Technical Safeguards:** Implement AES-256 encryption and Block Public Access (Article 32).
* **Storage Limitation:** Automate a 30-day retention policy via S3 Lifecycle Rules (Article 5).
* **Right to Erasure:** Execute a verified Article 17 deletion workflow including version history purging.

## 🛠️ Tech Stack
* **Cloud Provider:** AWS (S3, IAM, CloudTrail)
* **Tools:** AWS CLI v2, Git
* **Compliance Framework:** GDPR (Articles 4, 5, 17, 32)

## 🏗️ Implementation Details

### 1. Data Protection by Design
The S3 bucket was provisioned with a "Hardened" configuration:
* **Region:** `eu-west-1` (Ireland) to meet data residency requirements.
* **Encryption:** Default AES-256 enabled with a bucket policy denying unencrypted uploads.
* **Privacy:** All four "Block Public Access" settings enabled to prevent accidental data leaks.
* **Versioning:** Enabled to provide an audit trail and protect against accidental data loss.

### 2. Automated Retention (Article 5)
A lifecycle policy was applied to any object tagged with `DataClassification=PersonalData`. Objects are automatically expired after 30 days, and non-current versions are purged after 7 days, ensuring we do not store data longer than necessary.

### 3. Right to Erasure Workflow (Article 17)
To fulfill a "Right to be Forgotten" request for user `U003` (Clara Rossi):
1. **Data Portability:** Exported the user's specific record before deletion (Article 20).
2. **Sanitization:** Re-uploaded the dataset without the user's record.
3. **Hard Deletion:** Identified and permanently deleted the specific S3 `VersionId` containing the historical PII to ensure it cannot be recovered.

## 📂 Project Structure
* `personal-data.csv`: The initial dataset containing PII.
* `personal-data-cleaned.csv`: The sanitized dataset post-erasure request.
* `clara-rossi-export.csv`: The data extract provided to the user (Right to Access/Portability).
* `gdpr-evidence.md`: Comprehensive audit document for the Data Protection Officer (DPO).

## ⚖️ Verification
Erasure was verified using the following CLI check:
```bash
grep "U003" personal-data-cleaned.csv && echo "ERROR: Record still exists" || echo "SUCCESS: Record removed"
