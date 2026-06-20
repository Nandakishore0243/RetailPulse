
# AWS Deployment Guide

1. Create EC2 Instance
2. Install Docker
3. Pull RetailPulse Image
4. Run Container
5. Open Port 8501
6. Access Application

Example:

docker build -t retailpulse .
docker run -p 8501:8501 retailpulse
