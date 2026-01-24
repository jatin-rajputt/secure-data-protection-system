# Secure Data Protection System (V1.0)

A cybersecurity-focused file protection system that implements
authentication, password-based encryption, integrity verification,
and security logging using secure software engineering principles.

---

## 🔐 Key Features

- User authentication with hashed passwords
- Password-based key derivation (PBKDF2)
- File encryption and decryption (AES via Fernet)
- Integrity verification using SHA-256 hashing
- Protection against tampered or modified encrypted files
- Security event logging
- Modular and scalable architecture

---

## 🏗️ Project Architecture

SECURE-DATA-PROTECTION-SYSTEM/
│
├── src/
│ ├── auth.py # Authentication & brute-force protection
│ ├── crypto_engine.py # Encryption & decryption engine
│ ├── integrity.py # File integrity verification
│ ├── logger.py # Security logging
│ └── main.py # Application controller
│
├── config/
│ └── salt.bin # Cryptographic salt (runtime-generated)
│
├── data/
│ ├── encrypted/ # Encrypted files
│ └── decrypted/ # Decrypted files
│
├── logs/
│ └── security.log # Security audit logs
│
├── requirements.txt
├── .gitignore
└── README.md


---

## 🔑 Security Concepts Used

- **Confidentiality**: AES-based encryption (Fernet)
- **Integrity**: SHA-256 hash verification
- **Authentication**: Username/password with hashing
- **Access Control**: Encryption and decryption allowed only after login
- **Defense in Depth**: Multiple independent security layers
- **Secure Key Management**: Password-derived keys, no static key storage

---

## ▶️ How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/secure-data-protection-system.git
cd secure-data-protection-system

2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

3. Install dependencies
pip install -r requirements.txt

4. Run the application
python src/main.py
