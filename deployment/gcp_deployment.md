
# GCP Deployment Guide

1. Create Compute Engine VM
2. Install Docker
3. Build RetailPulse Container
4. Run Streamlit Application
5. Configure Firewall Rules

Example:

docker build -t retailpulse .
docker run -p 8501:8501 retailpulse
