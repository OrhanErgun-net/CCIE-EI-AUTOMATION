#!/bin/bash

# -k, --insecure
# This option allows curl to proceed and operate even for server connections otherwise considered insecure.

# Check if RESTCONF is running
curl -k https://192.168.96.121/restconf/ -u "cisco:cisco"

# Get Capabilities
curl -k https://192.168.96.121/restconf/data/netconf-state/capabilities -u "cisco:cisco"

# Discover YANG Module
curl -k https://192.168.96.121/restconf/data/Cisco-IOS-XE-native:native/ -u "cisco:cisco"

# Specify a leaf
curl -k https://192.168.96.121/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=1 -u "cisco:cisco"

# Use JSON
curl -H "Accept: application/yang-data+json" -k https://192.168.96.121/restconf/data/Cisco-IOS-XE-native:native/ -u "cisco:cisco"


