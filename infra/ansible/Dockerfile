FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        openssl \
        curl \
        unzip \
        git \
        gnupg \
    && update-ca-certificates \
    && curl -fsSL "https://releases.hashicorp.com/terraform/1.9.8/terraform_1.9.8_linux_amd64.zip" \
       -o terraform.zip \
    && unzip terraform.zip -d /usr/local/bin \
    && rm terraform.zip \
    && rm -rf /var/lib/apt/lists/*

# Copy Python requirements
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Install Ansible collections
RUN ansible-galaxy collection install \
        community.docker \
        community.general

WORKDIR /infra/ansible