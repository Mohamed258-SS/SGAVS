import tkinter as tk
from tkinter import filedialog, messagebox, Toplevel
from tkinter.ttk import Progressbar
import os
import hashlib
import threading
import requests
import time

def generate_gradient(start_color, end_color, steps):
    def hex_to_rgb(hex_color):
        return tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))
    
    def rgb_to_hex(rgb_color):
        return f"#{rgb_color[0]:02x}{rgb_color[1]:02x}{rgb_color[2]:02x}"

    start_rgb = hex_to_rgb(start_color)
    end_rgb = hex_to_rgb(end_color)
    gradient = [
        rgb_to_hex((
            int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * i / (steps - 1)),
            int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * i / (steps - 1)),
            int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * i / (steps - 1))
        ))
        for i in range(steps)
    ]
    return gradient

class AntivirusApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SGAVS")
        self.root.geometry("1080x520")
        self.root.iconbitmap(r'C:/Users/NASSAR/Desktop/SGAVS/icons_and_images/icon/icon_program.ico')
        self.root.configure(bg="#0B2F3A")
        self.root.resizable(False, False)

        self.malware_signatures = {
            "e99a18c428cb38d5f260853678922e03": "Test Virus",
            "098f6bcd4621d373cade4e832627b4f6": "Sample Malware"
        }

        self.virus_names = self.load_virus_names(r"C:\Users\NASSAR\Desktop\SGAVS\viruses.txt")
        
        # Load icons first
        self.load_icons() 
        
        # Setup GUI
        self.setup_gui()  

    def load_virus_names(self, filepath):
        """Load virus names from a file."""
        virus_names = []
        try:
            with open(filepath, "r") as f:
                for line in f:
                    virus_names.append(line.strip())
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load virus names: {e}")
        return virus_names

    def load_icons(self):
        """Load icons for buttons and title."""
        try:
            self.title_icon = tk.PhotoImage(file=r"C:/Users/NASSAR/Desktop/SGAVS/icons_and_images/images/imageprogram.png")
            self.update_icon = tk.PhotoImage(file=r"C:/Users/NASSAR/Desktop/SGAVS/icons_and_images/images/Update.png")
            self.scan_file_icon = tk.PhotoImage(file=r"C:/Users/NASSAR/Desktop/SGAVS/icons_and_images/images/Scan_File.png")
            self.full_scan_icon = tk.PhotoImage(file=r"C:/Users/NASSAR/Desktop/SGAVS/icons_and_images/images/Full_scan.png")
            self.scan_link_icon = tk.PhotoImage(file=r"C:/Users/NASSAR/Desktop/SGAVS/icons_and_images/images/Link_Scan.png")
            self.exit_icon = tk.PhotoImage(file=r"C:/Users/NASSAR/Desktop/SGAVS/icons_and_images/images/Exit.png")
        except Exception as e:
            print(f"Error loading icons: {e}")
            self.title_icon = None
            self.update_icon = self.scan_file_icon = self.full_scan_icon = self.scan_link_icon = self.exit_icon = None

    def draw_gradient_text(self, canvas, text, font, x, y, gradient):
        """Draws text with a gradient effect and white shadow."""
        
        # Shadow offset
        shadow_offset = 3
        shadow_x = x + shadow_offset
        shadow_y = y + shadow_offset

        # Draw shadow
        for idx, char in enumerate(text):
            char_id = canvas.create_text(shadow_x, shadow_y, text=char, font=font, fill="white", anchor="nw")
            bbox = canvas.bbox(char_id)
            shadow_x += bbox[2] - bbox[0]  # Increment x by character width

        # Draw gradient text on top
        x_offset = x
        for idx, char in enumerate(text):
            color = gradient[idx % len(gradient)]
            char_id = canvas.create_text(x_offset, y, text=char, font=font, fill=color, anchor="nw")
            bbox = canvas.bbox(char_id)
            x_offset += bbox[2] - bbox[0]  # Increment x by character width
    

    def setup_gui(self):
        """Set up the graphical user interface."""
        # Title Canvas
        title_canvas = tk.Canvas(self.root, bg="#0B2F3A", highlightthickness=0)
        title_canvas.place(x=0, y=0, width=1080, height=100)

        # Display program image next to the text
        if self.title_icon:
            title_canvas.create_image(50, 50, image=self.title_icon, anchor="center")  # Adjust position as needed

        # Generate gradient colors
        gradient = generate_gradient(start_color="#2E3192", end_color="#ED1E79", steps=len("SwiftGuard Antivirus Scanner"))

        # Draw gradient text
        font = ("tajawal", 50, "bold")
        self.draw_gradient_text(title_canvas, "SwiftGuard Antivirus Scanner", font, x=100, y=1, gradient=gradient)

        # Buttons and other GUI elements
        button_frame = tk.Frame(self.root, bg="#1A6691")
        button_frame.place(x=10, y=100, width=200, height=350)

        tk.Button(button_frame, text="Update", image=self.update_icon, compound=tk.LEFT,font=("tajawal", 14, "bold"), bg="#DBA901", command=self.update_program, width=150, padx=10).pack(pady=10)
        tk.Button(button_frame, text="Scan File", image=self.scan_file_icon, compound=tk.LEFT,font=("tajawal", 14, "bold"), bg="#DBA901", command=self.scan_file, width=150, padx=10).pack(pady=10)
        tk.Button(button_frame, text="Full Scan", image=self.full_scan_icon, compound=tk.LEFT,font=("tajawal", 14, "bold"), bg="#DBA901", command=self.full_scan, width=150, padx=10).pack(pady=10)
        tk.Button(button_frame, text="Scan Link", image=self.scan_link_icon, compound=tk.LEFT,font=("tajawal", 14, "bold"), bg="#DBA901", command=self.scan_link, width=150, padx=10).pack(pady=10)
        tk.Button(button_frame, text="Exit", image=self.exit_icon, compound=tk.LEFT,font=("tajawal", 14, "bold"), bg="#DBA901", command=self.root.destroy, width=150, padx=10).pack(pady=10)

        # Details Panel with Scrollbar
        details_frame = tk.Frame(self.root, bg="#0B4C5F")
        details_frame.place(x=220, y=100, width=850, height=350)

        details_scrollbar = tk.Scrollbar(details_frame)
        details_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.details_text = tk.Text(details_frame, wrap=tk.WORD, font=("courier", 13), bg="white", fg="black",yscrollcommand=details_scrollbar.set)
        self.details_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        details_scrollbar.config(command=self.details_text.yview)

        # Progress Bar and Label
        self.progress_bar = Progressbar(self.root, orient="horizontal", mode="determinate", length=850)
        self.progress_bar.place(x=220, y=480, width=850, height=15)

        self.progress_label = tk.Label(self.root, text="Progress: 0%", bg="#0B2F3A", fg="white", font=("Arial", 10, "bold"))
        self.progress_label.place(x=1080 - 180, y=450)

        # Footer Label
        designer_label = tk.Label(self.root, text="Designed by Mohamed Khaled Nassar", bg="#0B2F3A", fg="white",font=("tajawal", 9, "italic", "bold"))
        designer_label.place(x=10, y=470, width=200, height=30)

    def log_details(self, message):
        """Log details to the details panel."""
        self.details_text.insert(tk.END, message + "\n")
        self.details_text.see(tk.END)

    def reset_progress(self):
        """Reset the progress bar and label to 0% after a delay."""
        time.sleep(3)
        self.progress_bar["value"] = 0
        self.progress_label["text"] = "Progress: 0%"
        self.root.update_idletasks()

    def calculate_file_hash(self, file_path):
        """Calculate the hash of a file."""
        hash_func = hashlib.md5()
        try:
            with open(file_path, "rb") as f:
                while chunk := f.read(4096):
                    hash_func.update(chunk)
            return hash_func.hexdigest()
        except Exception as e:
            return f"Error: {str(e)}"

    def update_program(self):
        threading.Thread(target=self._update_program).start()

    def _update_program(self):
        self.log_details("Starting update process...")
        self.progress_bar["value"] = 0
        self.progress_label["text"] = "Progress: 0%"
        self.root.update_idletasks()

        for i in range(101):
            time.sleep(0.02)
            self.progress_bar["value"] = i
            self.progress_label["text"] = f"Progress: {i}%"
            self.root.update_idletasks()

        self.log_details("Update completed successfully!")
        self.reset_progress()

    def scan_file(self):
        file_path = filedialog.askopenfilename(title="Select a File to Scan")
        if not file_path:
            messagebox.showwarning("No File Selected", "Please select a file to scan.")
            return
        threading.Thread(target=self._scan_file, args=(file_path,)).start()

    def _scan_file(self, file_path):
        self.log_details(f"Scanning file: {file_path}")
        self.progress_bar["value"] = 0
        self.progress_label["text"] = "Progress: 0%"
        self.root.update_idletasks()

        # Check if the file is an executable or library
        if file_path.lower().endswith(('.exe', '.dll', '.bat')):
            # Check against the list of virus names
            with open(file_path, 'r', errors='ignore') as f:
                file_content = f.read()
                for virus_name in self.virus_names:
                    if virus_name in file_content:
                        self.log_details(f"Threat detected: {virus_name} in {file_path}")
                        if messagebox.askyesno("Threat Detected", f"The file '{file_path}' contains a known threat: {virus_name}.\nDo you want to delete it?"):
                            try:
                                os.remove(file_path)
                                self.log_details(f"File '{file_path}' has been deleted.")
                            except Exception as e:
                                self.log_details(f"Error deleting file '{file_path}': {e}")
                        return  # Stop scanning after finding a threat

        self.progress_bar["value"] = 100
        self.progress_label["text"] = "Progress: 100%"
        self.root.update_idletasks()
        self.log_details("No threats detected!\n")
        self.reset_progress()

    def full_scan(self):
        threading.Thread(target=self._full_scan).start()

    def _full_scan(self):
        self.log_details("Starting full scan of all drives...")
        self.progress_bar["value"] = 0
        self.progress_label["text"] = "Progress: 0%"
        self.root.update_idletasks()

        drives = self.get_all_drives()
        total_files = 0
        scanned_files = 0

        # Precompute total files for progress bar setup
        file_paths = []
        for drive in drives:
            for root, dirs, files in os.walk(drive):
                file_paths.extend([os.path.join(root, file) for file in files if file.lower().endswith((".exe", ".dll", ".bat"))])

        total_files = len(file_paths)
        self.log_details(f"Total files to scan: {total_files}")
        self.progress_bar["maximum"] = total_files

        for file_path in file_paths:
            scanned_files += 1
            self.progress_bar["value"] = scanned_files
            self.progress_label["text"] = f"Progress: {int((scanned_files / total_files) * 100)}%"
            self.log_details(f"Scanning file: {file_path}")
            self.root.update_idletasks()

            try:
                with open(file_path, 'r', errors='ignore') as f:
                    file_content = f.read()
                    for virus_name in self.virus_names:
                        if virus_name in file_content:
                            self.log_details(f"Threat detected: {virus_name} in {file_path}")
                            if messagebox.askyesno("Threat Detected", f"The file '{file_path}' contains a known threat: {virus_name}.\nDo you want to delete it?"):
                                try:
                                    os.remove(file_path)
                                    self.log_details(f"File '{file_path}' has been deleted.")
                                except Exception as e:
                                    self.log_details(f"Error deleting file '{file_path}': {e}")
                            break
            except Exception as e:
                self.log_details(f"Error reading file '{file_path}': {e}")

        self.log_details("Full scan completed!")
        self.progress_bar["value"] = 100
        self.progress_label["text"] = "Progress: 100%"
        self.root.update_idletasks()

        self.reset_progress()

    def get_all_drives(self):
        if os.name == 'nt':
            from string import ascii_uppercase
            return [f"{drive}:\\" for drive in ascii_uppercase if os.path.exists(f"{drive}:\\")]
        else:
            return ["/"]

    def scan_link(self):
        """Enhanced Scan Link process with a pop-up window."""
        def start_link_scan():
            link = link_entry.get()
            if not link:
                messagebox.showwarning("No Link Entered", "Please enter a valid link to scan.")
                return
            if not link.startswith("http://") and not link.startswith("https://"):
                messagebox.showerror("Invalid Link", "Please enter a valid URL starting with http:// or https://")
                return
            threading.Thread(target=self._scan_link, args=(link,)).start()
            link_window.destroy()

        # Create a new Toplevel window for scanning links
        link_window = Toplevel(self.root)
        link_window.title("Scan Link")
        link_window.geometry("800x250")  
        link_window.iconbitmap(r'C:/Users/NASSAR/Desktop/SGAVS/icons_and_images/icon/icon_program.ico')
        link_window.configure(bg="#0B4C5F")
        link_window.resizable(False, False)

        # Add label, entry box, and button
        tk.Label(link_window,text="Enter the link to scan:",bg="#0B4C5F",fg="white",font=("tajawal", 30, "bold")).pack(pady=30)
        link_entry = tk.Entry(link_window, font=("Arial", 14), width=70)
        link_entry.pack(pady=10)
        tk.Button(link_window,text="Start Scan",font=("tajawal", 14, "bold"),bg="#DBA901",command=start_link_scan).pack(pady=20)

    def _scan_link(self, link):
        """Scan a link using the VirusTotal API."""
        self.log_details(f"Scanning link: {link}")
        self.progress_bar["value"] = 10
        self.root.update_idletasks()

        api_key = '3406fa884f80d97c3af758033ade3bddda9fd79983a0ff0668e92a8de280aa81' 
        url = "https://www.virustotal.com/vtapi/v2/url/scan"
        params = {"apikey": api_key, "url": link}

        try:
            self.log_details("Submitting link to VirusTotal for scanning...")
            response = requests.post(url, data=params)
            self.progress_bar["value"] = 50
            self.root.update_idletasks()

            if response.status_code == 200:
                result = response.json()
                scan_id = result.get("scan_id", "N/A")
                self.log_details(f"Scan submitted successfully! Scan ID: {scan_id}")
                self.log_details("Fetching scan report...")

                report_url = "https://www.virustotal.com/vtapi/v2/url/report"
                report_params = {"apikey": api_key, "resource": scan_id}
                report_response = requests.get(report_url, params=report_params)

                if report_response.status_code == 200:
                    report = report_response.json()
                    positives = report.get("positives", 0)
                    total = report.get("total", 0)
                    self.log_details(f"Scan Results: {positives}/{total} engines detected a threat.")
                else:
                    self.log_details("Failed to fetch scan report.")
            else:
                self.log_details("Error submitting URL for scanning.")
        except Exception as e:
            self.log_details(f"Error during scanning: {e}")
        finally:
            self.progress_bar["value"] = 100
            self.progress_label["text"] = "Progress: 100%"
            self.root.update_idletasks()
            self.reset_progress()

if __name__ == "__main__":
    root = tk.Tk()
    app = AntivirusApp(root)
    root.mainloop()
