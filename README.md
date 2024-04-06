# **Student Record Management App**

**This Flask application manages student records, allowing you to:**

- Add student information
- View a list of all students
- Clear the student database

## **Getting Started**

1. **Install dependencies:**

   - [requirements.txt](requirements.txt)

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**

   ```bash
   flask run
   ```

## **API Endpoints**

### **Add student (/)**

- **Method:** POST
- **Data:**
  - name (string)
  - age (integer)
  - dob (date string in format YYYY-MM-DD)
  - gender (string)
- **Redirects:** To a success page on successful submission

### **View student list (/show_details)**

- **Method:** GET
- **Displays:** A list of all student records

### **Clear database (/clear_database)**

- **Method:** POST
- **Confirms:** Requires confirmation before clearing student records
- **Redirects:** To a success page on successful clearing

## **Additional Information**

- **Database:** SQLite (`students.sqlite3`)
- **Python version:** Tested with Python 3.6 or newer
- **Port:** Runs on port 8081 by default

## **Contributing**

We welcome contributions to this project. Please feel free to suggest improvements or create pull requests.
