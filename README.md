Below is the rewritten response that includes **all the required libraries** for setting up the `instainfo` tool from the GitHub repository [Kgsflink/instainfo](https://github.com/Kgsflink/instainfo) on a Linux system. This response also provides a step-by-step guide for installation and setup.

---

### **Step 1: Install Prerequisites**
Before setting up `instainfo`, ensure you have the following installed on your Linux system:
1. **Python 3.x**: The tool is written in Python, so you need Python installed.
2. **Git**: To clone the repository.
3. **pip**: Python's package manager.

#### **Install Python and Git**
Run the following commands to install Python and Git:
```bash
sudo apt update
sudo apt install python3 python3-pip git
```

---

### **Step 2: Clone the Repository**
Clone the `instainfo` repository from GitHub to your local machine:
```bash
git clone https://github.com/Kgsflink/instainfo.git
cd instainfo
```

---

### **Step 3: Install Python Dependencies**
The tool requires specific Python libraries to function. These libraries are listed in the `requirements.txt` file. Install them using `pip`:
```bash
pip install -r requirements.txt
```

#### **Required Libraries**
The `requirements.txt` file typically includes the following libraries:
- **`requests`**: For making HTTP requests to Instagram's API.
- **`argparse`**: For parsing command-line arguments.
- **`phonenumbers`**: For parsing and formatting phone numbers.
- **`pycountry`**: For country code lookups.

If the `requirements.txt` file is missing, you can manually install the required libraries:
```bash
pip install requests argparse phonenumbers pycountry
```

---

### **Step 4: Set Up Instagram Session ID**
To use `instainfo`, you need an Instagram session ID. Here's how to get it:

1. **Log in to Instagram** in your browser.
2. Open the browser's developer tools (usually `F12` or `Ctrl+Shift+I`).
3. Go to the **Application** tab (in Chrome/Edge) or **Storage** tab (in Firefox).
4. Under **Cookies**, select `https://www.instagram.com`.
5. Look for the `sessionid` cookie and copy its value.

---

### **Step 5: Run the Tool**
Once everything is set up, you can run the tool using the following command:
```bash
python3 instainfo.py -u USERNAME -s SESSION_ID
```

Replace:
- `USERNAME` with the Instagram username you want to look up.
- `SESSION_ID` with the session ID you copied earlier.

---

### **Step 6: Example Usage**
Here’s an example command to fetch information about a user:
```bash
python3 instainfo.py -u selenophile____9 -s 1234567890%3Aabcdef%3A12345
```

---

### **Step 7: Additional Features**
The tool may have additional features or options. Check the repository's README or run the tool with the `--help` flag for more details:
```bash
python3 instainfo.py --help
```

---

### **Step 8: Troubleshooting**
If you encounter issues:
1. **Rate Limits**: Instagram may block your requests if you make too many in a short time. Wait a few minutes and try again.
2. **Invalid Session ID**: Ensure the session ID is correct and not expired.
3. **Dependency Errors**: Make sure all dependencies are installed correctly using `pip install -r requirements.txt`.

---

### **Step 9: Update the Tool**
To update the tool to the latest version, pull the latest changes from the repository:
```bash
cd instainfo
git pull origin main
pip install -r requirements.txt
```

---

### **Step 10: Ethical Use**
- Use the tool responsibly and only on accounts you own or have permission to access.
- Do not use the tool for malicious purposes or to violate Instagram's terms of service.

---

### **Required Libraries Summary**
Here’s a summary of the required libraries and their purposes:
1. **`requests`**: For making HTTP requests to Instagram's API.
2. **`argparse`**: For parsing command-line arguments.
3. **`phonenumbers`**: For parsing and formatting phone numbers.
4. **`pycountry`**: For country code lookups.

You can install all of them using:
```bash
pip install requests argparse phonenumbers pycountry
```

---

By following these steps, you should be able to download, set up, and use the `instainfo` tool on your Linux system. Let me know if you need further assistance!
