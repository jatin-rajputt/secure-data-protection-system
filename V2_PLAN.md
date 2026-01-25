# Secure Data Protection System – Version 2 Roadmap

## Objective
Version 2 focuses on transforming the project from a secure functional system
into a hardened cybersecurity platform that can resist real-world attacks.

This version emphasizes attack simulation, access control, and professional
security engineering practices.

---

## V2 Core Security Enhancements

### 1. Secure Key Management
- Per-user cryptographic salt generation
- User-specific key derivation using PBKDF2-HMAC-SHA256
- Increased iteration count to slow brute-force attacks
- No static encryption keys stored on disk
- Cryptographic isolation between users

Status: 🔄 In Progress

---

### 2. Role-Based Access Control (RBAC)
- Defined roles: Admin, User
- Role-based permission enforcement
- Only authorized roles can encrypt/decrypt files
- Admin-only access to logs and audit data

Status: ⏳ Planned

---

### 3. Brute-Force Attack Simulation & Defense
- Controlled brute-force attempts on authentication
- Measurement of attack success before defenses
- Rate limiting after failed login attempts
- Account lockout after threshold violations
- Detailed logging of brute-force behavior

Status: ⏳ Planned

---

### 4. Security Logging & Monitoring Enhancements
- Structured security logs
- Detection of suspicious behavior
- Tamper and anomaly alerts
- Improved forensic traceability

Status: ⏳ Planned

---

## Why Version 2 Matters
Version 2 demonstrates applied cybersecurity knowledge by simulating attacks
and implementing layered defenses. It bridges the gap between theory and
real-world security engineering.

---

## Future Scope
- V3: MFA, database-backed authentication, secure key vaults
- V4: GUI interface, API exposure, advanced audit controls
