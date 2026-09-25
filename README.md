# 🏋️ Training Manager

A simple console-based application for managing workouts with user authentication and SQLite storage.

## 📌 Features

- User registration and login  
- Password hashing (SHA‑512 + salt)  
- Create, view, and delete workouts  
- Workouts grouped by muscle group  
- Clean table formatting using `prettytable`  
- Auto‑creates database on first run  

## 🛠️ Tech Stack

- **Python 3**
- **SQLite3** — local database
- **PrettyTable** — formatted console output
- **Hashlib** + **UUID** — hashing and unique IDs

🔐 Security

· Passwords are never stored in plain text
· Each password is hashed with SHA‑512 and a unique salt
· Workout deletion is allowed only for the logged‑in user

👤 Usage

1. Create an account – choose a username and password
2. Log in – use your credentials
3. Manage your workouts:
   · Add new workouts (muscle group, weight, sets, reps)
   · View your complete workout list
   · Delete workouts by ID

🧠 Author

This project was built as part of a self‑taught programming journey.
The author is a beginner developer exploring Python, SQL, and application architecture.

📄 License

MIT — free to use, modify, and distribute.