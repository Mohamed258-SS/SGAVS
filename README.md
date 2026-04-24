# SwiftGuard Antivirus System (SGAVS) 🛡️

[![Project Logo](image-url)](image-url)  

---

Developed by: **Mohamed Khaled Nassar**  
Course: **Network Security (CSE 231)** | Instructor: **Dr. Aida Nasr**  
Academic Email: [mohamednassar@el-eng.menofia.edu.eg](mailto:mohamednassar@el-eng.menofia.edu.eg)  

---

## 📝 Description

**SwiftGuard Antivirus Scanner (SGAVS)** is a Python-based desktop application designed to detect and protect against malware and malicious threats. 

The antivirus system provides an easy-to-use graphical interface with comprehensive features, such as:  
- File scanning for malicious code.
- Full system scan to identify potential threats.
- URL scanning for harmful links using VirusTotal API.
- Update mechanism to ensure prompt detection of the latest threats.

Utilizing modern libraries such as Scapy, `hashlib`, and VirusTotal API integrations, it empowers the user to detect malware in files and analyze links for threats.

---

## 🚀 Features

- **File Scanning**:
  - Scan individual files for malicious content.
  - Detect malware using a signature-based detection method.  

- **Full System Scan**:
  - Scan all drives on your computer for malicious files.
  - Delete any detected threats during the scan.  

- **URL Scanning**:
  - Integrates with VirusTotal API to analyze submitted URLs for malicious activity.
  - Retrieves online reports of scanned links and displays any detected threats.  

- **Update Feature**:
  - Updates the system to ensure the virus definitions and scanner are current.   

- **User-Friendly Interface**:
  - Includes an intuitive GUI and detailed logging.
  - Gradient-styled title bar for aesthetics and easy navigation.
  - Log details are provided for every scan, update, and action.  

---

## 🛠️ Setup Instructions

1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```

2. Navigate to the project directory:
    ```bash
    cd <project-directory>
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

   > **Note**: The required Python libraries will be installed automatically.  
   > Python 3.x is required to run the program.

4. Execute the application:
    ```bash
    python SGAVS.py
    ```

---

## 🧰 Dependencies and Libraries

The following libraries are required for this project:  
- `tkinter`: Provides graphical user interface (GUI) elements. (Included in standard Python distributions.)
- `requests`: For API requests to VirusTotal.
- `hashlib`: For hashing the files to check for malware signatures.
- `time`: To implement time-based operations and delays.
- `threading`: For non-blocking processes and multitasking.

Use the following commands to install external libraries:
```bash
pip install requests
python3 -m pip install requests
pip install hashlib
pip install python-time
pip install auto-py-to-exe
```

You can find additional resources and tools used in the project from the following sites:

- [Create AI Images](https://deepai.org/machine-learning-model/text2img)  
- [Resize Images](https://www.iloveimg.com/resize-image)  
- [Create ICO Files](https://image.online-convert.com/convert-to-ico)  
- [Gradient Tools](https://www.b3multimedia.ie/beautiful-color-gradients-for-your-next-design-project/)  
- [VirusTotal](https://www.virustotal.com/gui/home/upload)

---

## 🖥️ User Guide

### 1. Launching the Application
- Run the command `python SGAVS.py` to open the SGAVS application.

### 2. Main Features
Upon launching the app, you will see an interactive window with the following main options:  
- **Update**: Perform an update for the application and virus definitions.  
- **Scan File**: Perform a quick scan of individual files for malware detection.  
- **Full Scan**: Scan all available drives for malicious files and threats.  
- **Scan Link**: Analyze a URL using the VirusTotal API and generate a detailed report.  
- **Exit**: Close the application securely.

---

## ⚙️ How It Works

### File Scanning
- Hashes the file using MD5 and compares it against known malware signatures.
- Verifies if the file matches any threat in a locally stored virus signature list.

### Full System Scanning
- Automatically scans all connected drives. 
- Identifies files with potential threats; provides the option to delete malicious files.

### Link Scanning
- Integrates with the VirusTotal API to ensure links are analyzed for malicious threats.
- Retrieves detailed reports of scanned links, including the number of antivirus engines that flagged the link.

### Updating Virus Definitions
- Updates SGAVS to keep your system protected from new and emerging threats.

---

## 🛡️ Security and Privacy

- **Local Scans**: Ensure your data privacy by scanning files directly on your system without uploading them online.
- **Cloud Scan Integration**: Securely communicate with the VirusTotal API for link scanning. No data is shared without user consent.

---

## ⚠️ Disclaimer

This tool is intended **solely for educational purposes** and ethical usage. Scanning systems or devices without authorization is illegal. The project team and developers are not responsible for any misuse of this tool. Always use this software responsibly.

---

## 📁 Project Structure

```
Project Directory/
│
├── Network&Port Scanner.py     # Main script for the Network and Port Scanner tool
├── SGAVS.py                     # Main script for the SwiftGuard Antivirus System
├── viruses.txt                  # Text file containing predefined known malware signatures
├── websites and libraries.txt   # Resource links and required library documentation
├── README.md                    # Project documentation (this file)
└── requirements.txt             # List of required Python libraries
```

---

## Contributions

Contributions are welcome! Feel free to submit a pull request or open an issue for suggestions or feature requests.

---

## ✉️ Contact

For further details or troubleshooting, please contact:  
📧 Email: [mohamednassar@el-eng.menofia.edu.eg](mailto:mohamednassar@el-eng.menofia.edu.eg)

---

© 2026 Mohamed Khaled Nassar. All rights reserved.
