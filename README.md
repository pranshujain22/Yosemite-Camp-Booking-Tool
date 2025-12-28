# Yosemite Camp 4 Booking Tool 🌲🏕️

An automated Python script designed to monitor and book campsites at **Camp 4 in Yosemite National Park** via
Recreation.gov. Given the high demand for Camp 4, this tool automates the process of checking for availability and
adding a site to your cart the moment it becomes available.

## 🚀 Features

* **Automated Monitoring:** Checks the Camp 4 availability grid at set intervals.
* **Auto-Login:** Automatically logs into your Recreation.gov account using Selenium.
* **Immediate Booking:** Attempts to add available slots to your cart to "lock" the reservation.
* **Headless Browser:** Can be configured to run in the background.

---

## 🛠️ Prerequisites

Before running the script, ensure you have the following installed:

* **Python 3.8+**
* **Google Chrome** (latest version)
* **ChromeDriver** (The script uses `webdriver-manager` to handle this automatically)

---

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/pranshujain22/Yosemite-Camp-Booking-Tool.git](https://github.com/pranshujain22/Yosemite-Camp-Booking-Tool.git)
   cd Yosemite-Camp-Booking-Tool
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
---

## ⚙️ Configuration

To use the tool, you need to provide your details. It is recommended to use a configuration file to avoid hardcoding
credentials.

1. Create a `config.json` file in the root directory:

```json
{
  "email": "your_email@example.com",
  "password": "your_secure_password",
  "date": "Sep 13, 2025",
  "polling_interval_seconds": 30,
  "group_size": 3,
  "group_details": [
    {
      "first_name": "firstname_1",
      "last_name": "lastname_1",
      "postal_code": 12345
    },
    {
      "first_name": "firstname_2",
      "last_name": "lastname_2",
      "postal_code": 12345
    },
    {
      "first_name": "firstname_3",
      "last_name": "lastname_3",
      "postal_code": 12345
    }
  ],
  "vehicle_details": {
    "make":"Nissan",
    "model": "Rogue",
    "color": "Silver",
    "license": "9XXX788",
    "state":  "CA"
  }
}
```

2. Ensure the script is pointed to the **Camp 4 Facility ID**: `10004152`.

---

## 🖥️ Usage

Run the script from your terminal:

```bash
python Yosemite-Camp4.py

```

### What happens next?

1. **Login:** A Chrome window will open and log into your account.
2. **Scan:** The script will navigate to the Camp 4 page and scan for the "Available" (A) status.
3. **Carting:** If a site is found, it will be added to your cart.
4. **Manual Checkout:** You must manually complete the payment on the website within 15 minutes to confirm your stay.

---

## ⚠️ Important Disclaimer

* **Terms of Service:** Using automation scripts on Recreation.gov may violate their Terms of Service. Use this tool at
  your own risk.
* **IP Blocking:** Refreshing too frequently may lead to your IP being temporarily blocked.
* **Security:** Never share your `config.json` or scripts containing your password publicly. Add `config.json` to your
  `.gitignore` file.

---

## 📜 License

This project is licensed under the MIT License.
