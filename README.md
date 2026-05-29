# ✈️ TravelGuard AI

TravelGuard AI is a real-time travel assistance application powered by Google's Gemma model. It helps travelers quickly solve travel-related issues such as lost passports, flight delays, taxi scams, medical emergencies, hotel problems, and travel safety concerns.

## 🚀 Features

### 🛂 Lost Passport Assistance
- Immediate action steps
- Embassy guidance
- Travel document recommendations

### ✈️ Flight Delay Support
- Alternative travel suggestions
- Airport waiting tips
- Compensation guidance

### 🚕 Scam Detection
- Identify potential travel scams
- Safety recommendations
- Next-step actions

### 🏥 Medical Emergency Guidance
- Emergency response steps
- Important medical precautions
- Healthcare assistance recommendations

### 🌍 Multi-Language Support
- English
- Hindi
- Telugu

### 📄 PDF Report Generation
- Download AI-generated travel guidance
- Save travel assistance reports

### ⚡ Real-Time AI Assistance
- Powered by Google's Gemma model
- Fast response generation
- Practical travel recommendations

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Google GenAI (Gemma)
- FPDF
- Python Dotenv

---

## 📂 Project Structure

```text
TravelGuardAI/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
└── assets/
```

---

## 📦 Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/TravelGuardAI.git

cd TravelGuardAI
```

### Create Virtual Environment

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### Linux / Mac

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure API Key

Create a file named:

```text
.env
```

Add your Google API key:

```env
GOOGLE_API_KEY=YOUR_API_KEY_HERE
```

Get API Key from:

https://aistudio.google.com/

---

## ▶️ Run Application

```bash
streamlit run app.py
```

Application will open automatically in your browser:

```text
http://localhost:8501
```

---

## 💡 Example Use Cases

### Example 1

Input:

```text
My passport is lost at Hyderabad Airport.
```

Output:

- Immediate reporting steps
- Embassy recommendations
- Safety guidance
- Recovery process

---

### Example 2

Input:

```text
My flight has been delayed by 6 hours.
```

Output:

- Alternative travel options
- Passenger rights information
- Airport assistance recommendations

---

### Example 3

Input:

```text
A taxi driver is charging me an unusually high fare.
```

Output:

- Scam risk assessment
- Negotiation tips
- Safety recommendations

---

## 🎯 Buildathon Theme

TravelGuard AI addresses real-world travel challenges using AI-powered decision support.

Instead of searching multiple websites during stressful situations, travelers receive:

- Actionable guidance
- Safety recommendations
- Emergency assistance information
- Alternative travel solutions

---

## 🔮 Future Enhancements

- Voice Input
- Speech Output
- Offline Travel Guide
- Live Maps Integration
- Currency Converter
- Emergency Contact Finder
- Nearby Hospital Finder
- Travel Risk Prediction
- Travel Itinerary Generator


---

## 👨‍💻 Author

Developed for Build with Gemma Hackathon

Powered by:
- Google Gemma
- Streamlit
- Python

---

## 📜 License

This project is open-source and available under the MIT License.
