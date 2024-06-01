# Kali Linux Security Lab using Raspberry Pi

## Table of Contents
1. [Introduction](#introduction)
2. [Hardware Requirements](#hardware-requirements)
3. [Software Requirements](#software-requirements)
4. [Initial Setup](#initial-setup)
    - [Flashing Kali Linux](#flashing-kali-linux)
    - [Booting and Initial Configuration](#booting-and-initial-configuration)
5. [Network Configuration](#network-configuration)
6. [Installing Essential Tools](#installing-essential-tools)
7. [Setting Up Services](#setting-up-services)
    - [Web Server](#web-server)
    - [Database Server](#database-server)
8. [Security Tools and Testing](#security-tools-and-testing)
    - [Metasploit Framework](#metasploit-framework)
    - [Wireshark](#wireshark)
9. [Usage Scenarios](#usage-scenarios)
10. [Troubleshooting](#troubleshooting)
11. [Additional Resources](#additional-resources)

## Introduction
This document outlines the steps I took to build and configure a home Kali Linux security lab using a Raspberry Pi. 
The lab is intended for practicing security engineering skills, including penetration testing, network security, and vulnerability assessment.

## Hardware Requirements
- Raspberry Pi 4 Model B (4GB or 8GB RAM recommended)
- MicroSD Card (minimum 32GB, Class 10)
- Official Raspberry Pi power supply
- HDMI cable
- Keyboard and mouse
- Monitor
- Ethernet cable (optional for Wi-Fi)
- Raspberry Pi case

## Software Requirements
- Kali Linux ARM image for Raspberry Pi
- Balena Etcher (or similar flashing tool)
- SSH client (optional, for remote access)

## Initial Setup

### Flashing Kali Linux
1. **Download Kali Linux Image**:
   - Get the ARM image from the [official Kali Linux website](https://www.kali.org/downloads/).
2. **Flash the Image**:
   - Use [Balena Etcher](https://www.balena.io/etcher/) to flash the image to the microSD card.
   - Insert the microSD card into your Raspberry Pi.

### Booting and Initial Configuration
1. **Connect Peripherals**:
   - Attach the keyboard, mouse, monitor, and Ethernet cable (if using wired connection).
2. **Power On**:
   - Connect the power supply to the Raspberry Pi.
   - Follow the on-screen instructions to complete the initial setup, including setting up the username and password.

## Network Configuration
- **Static IP Configuration**:
  - Edit the network configuration file to set a static IP if needed.
  ```bash
  sudo nano /etc/dhcpcd.conf
  ```
  - Add the following lines:
  ```plaintext
  interface eth0
  static ip_address=192.168.1.100/24
  static routers=192.168.1.1
  static domain_name_servers=192.168.1.1
  ```

## Installing Essential Tools
- **Update and Upgrade**:
  ```bash
  sudo apt update
  sudo apt upgrade -y
  ```
- **Install Kali Tools**:
  ```bash
  sudo apt install kali-linux-default
  ```

## Setting Up Services

### Web Server
- **Install Apache**:
  ```bash
  sudo apt install apache2
  sudo systemctl start apache2
  sudo systemctl enable apache2
  ```

### Database Server
- **Install MySQL**:
  ```bash
  sudo apt install mysql-server
  sudo systemctl start mysql
  sudo systemctl enable mysql
  ```

## Security Tools and Testing

### Metasploit Framework
- **Start Metasploit**:
  ```bash
  sudo systemctl start postgresql
  msfdb init
  msfconsole
  ```

### Wireshark
- **Install Wireshark**:
  ```bash
  sudo apt install wireshark
  ```

## Usage Scenarios

### Web Application Testing
- **Set Up Vulnerable Web Application**:
  - Deploy DVWA (Damn Vulnerable Web Application) or another vulnerable web app.
  - Test using tools like OWASP ZAP.

### Network Sniffing
- **Capture and Analyze Traffic**:
  - Use Wireshark to capture network traffic.
  - Simulate attacks and defenses.

## Troubleshooting
- **Common Issues**:
  - Network connectivity problems: Check cables, IP settings.
  - Service not starting: Check logs in `/var/log/`.

## Additional Resources
- [Kali Linux Documentation](https://www.kali.org/docs/)
- [Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/)
- [Metasploit Documentation](https://docs.rapid7.com/metasploit/)

---

This template provides a structured format for documenting your Kali Linux security lab setup on GitHub. Adjust the sections as needed to fit your specific configuration and usage scenarios.
