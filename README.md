# CRYPOGRAPHYLAB

This repository contains the cryptography laboratory work, experiments, and security assignments completed by Group 5.

## Current Project: Drone Mission Control System

The current application is a small Python-based console application that simulates basic drone mission-control functionality.

The application demonstrates:

* Drone login/authentication
* Drone registration
* Drone status management
* Drone takeoff and landing
* Location updates
* Waypoint upload
* Mission execution
* Telemetry display
* Drone activity log storage
* Drone command execution

The application is designed for educational and security-analysis purposes. It simulates drone operations and does not control real-world drone hardware.

## Project Structure

```text
CRYPOGRAPHYLAB/
│
├── classical/
├── modern/
├── hashing/
├── attacks/
├── analysis/
├── docs/
│
├── secure_application/
│   ├── src/
│   │   ├── authentication.py
│   │   ├── config.py
│   │   ├── drone.py
│   │   └── main.py
│   │
│   ├── reports/
│   ├── screenshots/
│   ├── sast/
│   ├── outputs/
│   ├── testcases/
│   └── README.md
│
└── README.md
```

## Application Functionality

### 1. Authentication

The application provides a login mechanism before allowing access to the Drone Mission Control System.

### 2. Drone Management

Users can register drones and view their basic information, including:

* Drone ID
* Model
* Owner
* Battery level
* Current location
* Drone status

### 3. Waypoint Upload

Users can upload multiple latitude and longitude waypoints for a drone mission.

Example:

```text
Waypoint 1:
Latitude: 26.9124
Longitude: 75.7873

Waypoint 2:
Latitude: 26.9200
Longitude: 75.8000
```

### 4. Mission Execution

A drone can be taken airborne and a previously uploaded waypoint mission can be executed.

The application simulates movement through the configured waypoints and reports mission completion.

### 5. Telemetry

The application displays simulated drone telemetry such as:

* Battery percentage
* Current location
* Drone status
* Altitude
* Speed
* Mission status
* Number of waypoints

### 6. Log Storage

Important application activities are recorded in the application's output/log files for demonstration and analysis purposes.

## Security Assignment

The Drone Mission Control System is being developed as part of the security laboratory assignments.

The vulnerable version intentionally contains three security weaknesses for SAST analysis:

1. **Hardcoded Secret**

   * A sensitive API key is stored directly in the source code.

2. **Unsafe Dynamic Code Execution**

   * User-controlled command input is processed using `eval()`.

3. **Weak Authorization**

   * Authentication is implemented without proper role-based authorization restrictions.

These vulnerabilities are intentionally present in the Assignment 3 version so that they can be analyzed using a SAST tool in Assignment 4.

## Assignment 4: SAST-Based Security Analysis

The next phase of the project will perform Static Application Security Testing (SAST) on:

```text
secure_application/src/
```

The analysis will include:

* Initial SAST scan
* Vulnerability identification
* Severity analysis
* True Positive / False Positive analysis
* Missed vulnerability analysis
* Manual verification
* Vulnerability remediation
* Second SAST scan
* Before-and-after comparison

## Programming Language

**Python 3**

## How to Run

Create and activate a virtual environment if required:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Run the Drone Mission Control System:

```bash
python3 secure_application/src/main.py
```

## Application Login

For the current laboratory demonstration, use the configured application credentials provided in the assignment/test setup.

Do not use these demonstration credentials for real systems.

## Team / Project Information

* **Repository:** CRYPOGRAPHYLAB
* **Group:** 5
* **Topic:** Drone
* **Application:** Drone Mission Control System
* **Language:** Python
* **Class:** CSE A
* **Year:** 4

### Members

* **Jayant Singh** — 2024ucp1806
* **Jatin Kadamanchi** — 2024ucp1903

## Educational Disclaimer

This project is developed strictly for academic and laboratory purposes. The drone functionality is simulated in software and is not intended to control or interact with real-world drone hardware.
