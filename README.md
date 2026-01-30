# 🐳 Optimized Docker Installation for Windows (WSL 2)

This guide ensures a clean, stable Docker setup that avoids common issues like system freezing, high RAM consumption, and CPU spikes.

---

### 🟢 Step 1: Verify Hardware Virtualization
Docker requires hardware-level support to run the Linux kernel efficiently.
1.  Open **Task Manager** (`Ctrl + Shift + Esc`).
2.  Go to the **Performance** tab and select **CPU**.
3.  Check the bottom right for **Virtualization: Enabled**.
    *   *If disabled, you must enable it in your BIOS/UEFI (Search for "Intel VT-x" or "AMD-V").*

---

### 🟢 Step 2: Install WSL 2 (Windows Subsystem for Linux)
WSL 2 is the modern backend that makes Docker run natively on Windows.
1.  Search for **PowerShell**, right-click, and select **Run as Administrator**.
2.  Execute the following command:
    ```powershell
    wsl --install
    ```
3.  **Restart your computer** when the process completes.
4.  After the reboot, open PowerShell again and ensure the default version is set:
    ```powershell
    wsl --set-default-version 2
    ```

---

### 🟢 Step 3: Install Docker Desktop
1.  Download the official [Docker Desktop Installer](https://docs.docker.com).
2.  Run the `.exe` file.
3.  **Critical:** Ensure the checkbox **"Use WSL 2 instead of Hyper-V"** is **checked**.
4.  Complete the installation and **Restart** your PC once more.

---

### 🟢 Step 4: The "RAM Fix" (Crucial for Performance)
By default, WSL 2 can consume up to 80% of your system RAM. We will cap it to keep your PC fast.
1.  Press `Win + R`, type `%UserProfile%`, and hit Enter.
2.  Create a new text file and name it precisely `.wslconfig` (ensure there is **no** `.txt` extension).
3.  Open it with Notepad and paste the following:
    ```ini
    [wsl2]
    # Limit RAM usage (e.g., 4GB or 2GB depending on your total RAM)
    memory=4GB   
    # Limit CPU cores to prevent 100% usage spikes
    processors=2 
    ```
4.  Save and close the file.
5.  In PowerShell, run `wsl --shutdown` to apply these limits immediately.

---

### 🟢 Step 5: Enable "Resource Saver" Mode
1.  Open the **Docker Desktop** application.
2.  Click the **Settings** (Gear Icon) at the top right.
3.  Under the **General** tab, check the box for **"Resource Saver"**.
    *   *This feature puts Docker to sleep when no containers are running, saving battery and memory.*

---

### 🟢 Step 6: Verify the Setup
Open your terminal (CMD or PowerShell) and run these commands to confirm everything is perfect:
*   `docker --version` (Should show the installed version).
*   `docker run hello-world` (Should download a tiny image and print a "Hello" message).

---

## 🧹 Maintenance Tip
To prevent Docker from eating your disk space over time, run this command occasionally:
```bash
docker system prune -a
