# 🎓 Student Management System (CRUD) - Django

A simple **Student Management System** built using **Django**.  
This project allows you to **Add, Display, Update, and Delete** student details easily.  
It also supports **image upload for student profile photos**.

---

## 🚀 Features

- Add new students with details & photo
- Display student list
- Update student information
- Delete students
- Django Class Based Views (GET & POST)
- Bootstrap UI

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| Django | Backend Framework |
| MySQL | Database |
| HTML, CSS, Bootstrap | Frontend UI |

---

---

## 📸 Screenshots

---

### 🔐 Authentication
- **Sign Up Page**
  ![Sign Up](screenshots/sign_up.png)
- **Sign In Page**
  ![Sign In](screenshots/sign_in.png)

---

### ➕ Add Student (Form)
- **Page 1**
  ![Add Student Page 1](screenshots/add_stu_part1.png)
- **Page 2**
  ![Add Student Page 2](screenshots/add_stu_part2.png)

---

### ✏️ Update Student
- **Page 1**
  ![Update Student Page 1](screenshots/update_stu_part1.png)
- **Page 2**
  ![Update Student Page 2](screenshots/update_stu_part2.png)

---

### 📋 Display Student
![Student List](screenshots/display_stu.png)

---

### 🗑️ Delete Student
![Delete Student](screenshots/delete_stu.png)



---

## ▶️ Setup Instructions (Run Locally)

```bash
# Clone the repository
git clone https://github.com/omkarpawar2002/student-management-system-practice-project.git

# Move into project
cd student-management-system-practice-project

# Create virtual environment
python -m venv venv
venv\Scripts\activate 

# Install dependencies
pip install -r requirements.txt

# Run the server
python manage.py runserver
