# 🎉 Guest List Manager

A responsive web application to manage event guest lists and track invitation statuses efficiently.

---

## 🚀 Features
- Add, update, and delete guests  
- Track invitation status (Pending, Invited, Accepted, Declined)  
- Search guests by name  
- Filter guests based on status  
- Responsive UI (works on mobile & desktop)  

---

## 🛠️ Tech Stack
- **Backend:** Python (Flask)  
- **Database:** SQLite (.db managed via DB Browser for SQLite)  
- **Frontend:** HTML, CSS, JavaScript  
- **Version Control:** Git & GitHub  

---

## 🗄️ Database Design

### Entities:
- **Guest:** guest_id, name, email, phone, status  
- **Event:** event_id, event_name, event_date, location  
- **Invited_To:** event_id, guest_id, rsvp_date  

---

## 📊 ER Diagram
(Add your ER diagram image here)
