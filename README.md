# WeatherStat CLI

## 📌 Project Overview
WeatherStat is a Python-based Command-Line Interface (CLI) application for managing and analyzing weather statistics. It allows users to store, retrieve, and manage weather data for different locations using a relational database powered by SQLAlchemy ORM.

## 🚀 Features
- **Database Management:** Uses SQLite with SQLAlchemy ORM.
- **CRUD Operations:** Add, view, and delete locations and weather records.
- **One-to-Many Relationship:** Each location can have multiple weather records.
- **Interactive CLI:** Users can interact with a menu-driven interface.
- **Automatic Data Persistence:** Ensures that records remain stored across sessions.
- **Preloaded Sample Data:** Includes example locations and weather data for easy testing.

## 📂 Project Structure
```
weather_stat/
├── cli.py         # CLI logic for user interaction
├── database.py    # Database connection setup
├── models.py      # ORM models for Locations & WeatherRecords
├── main.py        # Entry point to launch the CLI
├── Pipfile        # (Optional) Dependency management file
├── Pipfile.lock   # (Optional) Lock file for dependencies
├── README.md      # Project documentation (this file)
└── weather_stat.db # SQLite database file (created automatically)
```

## 🛠️ Installation & Setup
### **Step 1: Clone the Repository**
```bash
 git clone <repository-url>
 cd weather_stat
```

### **Step 2: Create a Virtual Environment (Optional but Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### **Step 3: Install Dependencies**
```bash
pip install sqlalchemy tabulate
```

### **Step 4: Run the Application**
```bash
python models.py  # Creates the database and inserts sample data
python cli.py     # Runs the CLI
```

## 🎮 How to Use
Once inside the CLI, follow the on-screen instructions:
1. **Add a location** (City & Country)
2. **Add a weather record** (Temperature, Humidity, Wind Speed)
3. **View locations and weather records**
4. **Delete records if necessary**
5. **Exit the application**

## 🗂️ Database Schema
- **Locations Table**:
  - `id` (Primary Key)
  - `city` (String)
  - `country` (String)

- **Weather Records Table**:
  - `id` (Primary Key)
  - `location_id` (Foreign Key → locations.id)
  - `temperature` (Float)
  - `humidity` (Float)
  - `wind_speed` (Float)
  - `date` (DateTime - Defaults to current timestamp)

## 📊 Sample Data Inserted
When you run `models.py`, the following sample locations and weather records are added:
| ID | City      | Country |
|----|----------|---------|
| 1  | Nairobi  | Kenya   |
| 2  | New York | USA     |
| 3  | Tokyo    | Japan   |

| ID | Location ID | Temperature (°C) | Humidity (%) | Wind Speed (km/h) | Date |
|----|------------|------------------|-------------|-------------------|------|
| 1  | 1          | 25.5              | 60.0        | 12.3              | Now  |
| 2  | 2          | 18.2              | 55.5        | 8.7               | Now  |
| 3  | 3          | 22.1              | 70.0        | 10.2              | Now  |

## 🔄 Running Database Queries
If you want to manually inspect the database, you can use SQLite CLI:
```bash
sqlite3 weather_stat.db
```
Once inside SQLite shell, you can run queries:
```sql
SELECT * FROM locations;
SELECT * FROM weather_records;
```

## 🛠️ Troubleshooting
### **Database Not Created?**
- Ensure `models.py` is executed before running the CLI.
- Verify SQLite is installed: `sqlite3 --version`

### **Tables Empty?**
- Run `python models.py` again to insert sample data.
- Check if the database is created: `ls -lah | grep weather_stat.db`

## 📜 License
This project is open-source and available under the MIT License.

## 📞 Contact & Support
For questions or contributions, open an issue on GitHub or contact the project maintainer.

🚀 **Happy Coding!**

