# Compliance Gap Analysis

## Critical Gaps (Immediate Action)
1. **[CIS 5.1] Security groups allow SSH from 0.0.0.0/0**
   - **Resources:** sg-0b6298d77b3a22a93, sg-093711db3c322f573, sg-0f8d6c2a3def8bd76, sg-04caf01536cba05e3
   - **Risk:** Potential for brute-force attacks and unauthorized remote access.
   - **Remediation:** Restrict to specific IP ranges or use SSM.
   - **Timeline:** 4 hours.

## High Priority Gaps
2. **[CIS 1.22] IAM Password Policy Not Defined**
   - **Remediation:** Set minimum length to 14.
   - **Timeline:** 1 day.
