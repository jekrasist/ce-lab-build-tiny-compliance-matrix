# EC2 Rightsizing Report

## Analysis Period
- **Date:** March 26, 2026
- **Duration:** 30 minutes of monitoring
- **Method:** CloudWatch metrics + synthetic load testing (stress)

## Instance Analysis
| Instance Name | Current Type | vCPUs | RAM (GB) | Avg CPU % | Avg Mem % | Recommended Type | Status |
|---------------|-------------|-------|----------|-----------|-----------|-----------------|---------|
| web-server-v2 | t3.micro    | 2     | 1        | 99.9%     | 15%       | t3.micro (keep) | Sized   |
| api-server    | t3.micro    | 2     | 1        | 0.48%     | 10%       | t3.nano         | Oversized |
| data-processor| t3.small    | 2     | 2        | 0.53%     | 8%        | t3.micro        | Oversized |

## Implementation Results
- **Action:** Successfully resized `rightsizing-data-processor` from **t3.small** to **t3.micro**.
- **Post-Resize Verification:** Instance is running stably as a t3.micro.

## Key Takeaways
1. Even "small" instances can be over-provisioned.
2. CloudWatch memory metrics (CWAgent) are essential for safe rightsizing to avoid OOM (Out of Memory) errors.
3. Automated stress testing helps distinguish between baseline "idle" noise and actual production workload.
