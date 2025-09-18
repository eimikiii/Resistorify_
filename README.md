# Resistorify_
<img width="1292" height="638" alt="titleeee" src="https://github.com/user-attachments/assets/965d0052-484f-4db6-a7e6-fe3906f7c060" />
Resistorify is a simple **Flask web app** that helps users calculate the resistance of electronic resistors based on their color bands.   It supports **3-band, 4-band, 5-band, and 6-band resistors**, giving quick and accurate resistance values with tolerance and ppm information.
---

##  Features
- 🖥️ **Interactive UI** – Intuitive design for selecting resistor color bands.  
- 🎨 **Supports 3, 4, 5, and 6 bands** – From basic to precision resistors.  
- ⚡ **Instant Calculations** – Get resistance value, tolerance, and ppm in real time.  
- 📱 **Responsive Design** – Works seamlessly across devices.  
- 🔧 **Powered by Flask** – Lightweight, efficient, and easy to run locally.  

---

## Preview  
<img width="1299" height="293" alt="image" src="https://github.com/user-attachments/assets/55d0a1fe-8bf3-4f51-bcfb-f22755f04fed" />
<img width="1301" height="534" alt="image" src="https://github.com/user-attachments/assets/2c7b93f8-ac11-4ece-beee-2e0e042b1032" />

---
## Installation & Setup  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/YOUR-USERNAME/Resistorify_.git
   cd Resistorify_

2. **Create and Activate a Virtual Environment**  
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On Mac/Linux
3. **Installl Dependencies**  
   ```bash
   pip install -r requirements.txt
4. **Run the Flask App**  
   ```bash
   .venv\Scripts\activate  # On Windows
   # On Windows (PowerShell)
   $env:FLASK_APP="main.py"
   $env:FLASK_ENV="development"
   flask run
   # On Mac/Linux
   export FLASK_APP=main.py
   export FLASK_ENV=development
   flask run
 
