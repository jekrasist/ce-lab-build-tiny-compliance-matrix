# Lab M7.03 - Rightsizing EC2 Instances

## Project Overview
This lab demonstrates the process of identifying, analyzing, and rightsizing over-provisioned EC2 instances to optimize cloud costs.

## Technical Tasks Completed
- **Fleet Launch:** Deployed a mix of T3-family instances.
- **Metric Collection:** Configured IAM roles and installed the CloudWatch Agent to capture memory utilization.
- **Load Simulation:** Executed synthetic CPU load tests using `stress` to simulate production traffic.
- **Analysis:** Evaluated CloudWatch Metrics to identify underutilized resources.
- **Optimization:** Performed a live resize of an idle instance to a smaller tier.

## Troubleshooting & Pivot
During the lab, account-level restrictions prevented the use of M5 instances. I successfully pivoted the lab to use the T3 family, maintaining the learning objectives by comparing the utilization ratios between micro and small tiers.

## Verification
Final fleet state shows all instances successfully rightsized to the `t3.micro` tier based on <1% utilization data.
