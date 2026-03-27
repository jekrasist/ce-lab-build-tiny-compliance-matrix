import csv
from datetime import datetime

# Data gathered from your manual CLI audit
data = [
    ['CIS 1.4', 'Root Access Keys', '✅ COMPLIANT', 'Low'],
    ['CIS 1.5', 'Root MFA', '✅ COMPLIANT', 'Low'],
    ['CIS 1.22', 'Password Policy', '❌ FAILED', 'Medium'],
    ['CIS 3.1', 'CloudTrail Enabled', '✅ COMPLIANT', 'Low'],
    ['CIS 5.1', 'SSH Restrictions', '❌ 3 VIOLATIONS REMAINING', 'Critical'],
    ['CIS 3.2', 'Log Validation', '✅ COMPLIANT', 'Low'],
    ['CIS 2.2.1', 'EBS Encryption', '✅ COMPLIANT', 'Low'],
]

filename = f'compliance-report-{datetime.now().strftime("%Y-%m-%d")}.csv'

with open(filename, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Control ID', 'Control Name', 'Status', 'Severity'])
    writer.writerows(data)

print(f"Report generated: {filename}")
