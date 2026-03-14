**README FILE**



Security Analysis and Vulnerability Detection in MQTT-Based IoT Systems (Beyond Plaintext Risks)



**PROJECT OVERVIEW**



This project focuses on analyzing security vulnerabilities in MQTT based IoT systems. While many implementations secure communication using encryption, several attacks such as device impersonation, message injection, wildcard topic abuse, and distributed denial-of-service (DDoS) can still occur.

The proposed system monitors MQTT traffic in real time and detects suspicious activities using a security analysis engine and displays alerts through an IDS dashboard.





**WORKFLOW**



1. Traffic Monitoring Module – Captures MQTT messages, topics, and device IDs.
2. Security Analysis Engine – Analyzes message patterns to detect suspicious behavior.
3. Vulnerability Detection – Compares device activity with predefined security rules.
4. Alert Generation – Generates alerts with threat type, vulnerability, and remedy.
5. IDS Dashboard – Displays connected devices and detected threats in real time.







**FEATURES**



* Real-time MQTT traffic monitoring
* Detection of device impersonation
* Detection of message injection attacks
* Detection of topic wildcard abuse
* Detection of DoS / message flooding attacks
* Real-time alert generation with vulnerability and remedy suggestions
* IDS dashboard for monitoring IoT network activity
* Vulnerability distribution visualization (shows types of vulnerabilities detected)
* Threats over time analysis (graph showing attacks detected over time)





**TECH STACK**



* **Protocol**: MQTT
* **Broker**: Mosquitto
* **Programming Language**: Python
* **MQTT** **Library**: Eclipse Paho
* **Backend**: Node.js
* **Frontend**: React.js , CSS , Tailwind
* **Database**: MongoDB





**THREATS DETECTED**



* Device impersonation
* Message injection
* Topic wildcard abuse
* Distributed Denial of Service (DDoS) attack







**SETUP INSTRUCTIONS**



**1. Install MQTT Broker**



**Install Mosquitto.**

**Example (Linux):**



**sudo apt update**

**sudo apt install mosquitto mosquitto-clients**



**2. Install Python Dependencies**



**pip install paho-mqtt flask**



**3. Start the MQTT Broker**



**mosquito**



**4. Run the Monitoring System**



**python monitor.py**



**5. Open the Dashboard**

**Open your browser and go to:**



**http://localhost:5000**



**You will see:**



* **Connected devices**
* **Detected threats**
* **Vulnerability distribution**
* **Threats over time graphs**





**NOVELTY**



Unlike traditional approaches that focus only on encrypting MQTT communication, this system detects behavioral attacks beyond plaintext risks by monitoring device activity and message patterns.





**EXPECTED OUTCOME**



The system helps administrators monitor IoT networks, detect suspicious activity early, and apply recommended security measures to prevent attacks.

