# 🎓 Django Student Portal

A modern, professional student management system built with Django and PostgreSQL. Features a clean UI, advanced calendar interface, and full CRUD operations - all deployable for FREE with 24/7 uptime!

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.1.2-green.svg)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## ✨ Features

### 🎨 Modern UI/UX
- **Professional Design System**: Royal blue theme with clean, modern aesthetics
- **Responsive Layout**: Works perfectly on desktop, tablet, and mobile devices
- **Dark Mode Ready**: Consistent color palette optimized for all screen sizes
- **Custom Icons**: SVG icons for intuitive navigation

### 📅 Advanced Calendar Interface
- **Flatpickr Integration**: Professional JavaScript date picker
- **Material Blue Theme**: Matches the app's design system
- **Mobile Optimized**: Touch-friendly calendar on all devices
- **User-Friendly Dates**: Displays dates like "March 25, 2007" instead of raw formats

### 📊 Student Management (Full CRUD)
- **Create**: Add new students with a beautiful form layout
- **Read**: View all students with powerful search (by name or email)
- **Update**: Edit student details with pre-filled forms
- **Delete**: Safe deletion with professional confirmation page

### 🔍 Smart Search
- **Multi-field Search**: Search by name OR email
- **Real-time Filtering**: Instant results as you type
- **No Results Handling**: Helpful messages when no students found

### 📈 Dashboard Overview
- **Live Statistics**: Total student count at a glance
- **Status Cards**: Active/inactive student tracking
- **Data Grid**: Clean, sortable table of all students

### 🔒 Security & Production-Ready
- **Environment Variables**: Secure configuration with `.env` files
- **PostgreSQL Database**: Production-grade database (Supabase)
- **Row-Level Security (RLS)**: Enhanced data protection
- **HTTPS Support**: SSL certificate included with Render deployment

---

## 🛠️ Tech Stack

### Backend
- **Django 5.1.2**: Python web framework
- **PostgreSQL**: (via Supabase) Production database
- **Gunicorn**: WSGI HTTP server for deployment
- **WhiteNoise**: Static file serving

### Frontend
- **Vanilla CSS**: Custom design system (no frameworks)
- **Flatpickr**: Professional calendar UI
- **SVG Icons**: Heroicons for crisp, scalable graphics
- **Google Fonts**: Inter font family

### Deployment & DevOps
- **Render.com**: Free hosting platform
- **GitHub**: Version control
- **APScheduler**: Keep-alive cron jobs
- **UptimeRobot**: (Optional) External monitoring

---

## 📸 Screenshots

### Home Page
Clean, welcoming interface with clear call-to-action buttons.

### Add Student Form
Two-column grid layout with input icons and professional calendar picker.

### Manage Students Dashboard
Live stats, search bar, and data table with Edit/Delete actions.

### Delete Confirmation
Safety-first approach with detailed confirmation before deletion.

---

## 🚀 Quick Start (Local Development)

### Prerequisites
- Python 3.11+
- PostgreSQL (or Supabase account)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sravanshetty06/DJANGO_studentportal.git
   cd DJANGO_studentportal
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Mac/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=your_supabase_connection_string
   SECRET_KEY=your_secret_key_here
   DJANGO_DEBUG=True
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Collect static files**
   ```bash
   python manage.py collectstatic --no-input
   ```

7. **Start development server**
   ```bash
   python manage.py runserver
   ```

8. **Visit the app**
   
   Open your browser to: `http://127.0.0.1:8000/`

---

## 🌐 Deployment (Free 24/7 on Render)

### Method 1: One-Click Deploy

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

### Method 2: Manual Deployment

#### Step 1: Prepare Your Repository
```bash
# Ensure all files are committed
git add .
git commit -m "Prepare for deployment"
git push origin main
```

#### Step 2: Create Render Account
1. Go to [render.com](https://render.com)
2. Sign up with GitHub
3. Authorize Render to access your repositories

#### Step 3: Create Web Service
1. Click **"New +"** → **"Web Service"**
2. Connect this repository
3. Configure:
   - **Name**: `studentportal` (or your choice)
   - **Runtime**: Python 3
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn studentdata.wsgi:application`
   - **Instance Type**: Free

#### Step 4: Set Environment Variables
In Render dashboard, add:
- `DATABASE_URL`: Your Supabase PostgreSQL connection string
- `SECRET_KEY`: Generate at [djecrety.ir](https://djecrety.ir/)
- `DJANGO_DEBUG`: `False`
- `PYTHON_VERSION`: `3.11.0`

#### Step 5: Keep It Alive 24/7 (Free!)

**Option A: Render Cron Job (Recommended)**
1. In Render, create a new **Cron Job**
2. Set schedule: `*/14 * * * *` (every 14 minutes)
3. Command: `curl https://YOUR_APP_NAME.onrender.com/`

**Option B: Background Worker**
1. Use the included `keepalive.py` management command
2. Deploy it as a separate worker service

**Option C: UptimeRobot**
1. Sign up at [uptimerobot.com](https://uptimerobot.com)
2. Add HTTP monitor for your Render URL
3. Set interval to 5 minutes

### Deployment Architecture
```
┌─────────────────────────────────────┐
│   Your Django App (Render.com)      │
│                                     │
│  ┌──────────┐      ┌─────────────┐ │
│  │   Web    │      │  Keep-Alive │ │
│  │ Service  │◄─────┤    Cron     │ │
│  │  (Free)  │      │   (Free)    │ │
│  └────┬─────┘      └─────────────┘ │
└───────┼─────────────────────────────┘
        │
        ▼
┌───────────────┐
│   Supabase    │
│ PostgreSQL DB │
│    (Free)     │
└───────────────┘
```

### Cost Breakdown
| Service | Plan | Monthly Cost |
|---------|------|--------------|
| Render (Web Service) | Free Tier | $0 |
| Render (Cron Job) | Free | $0 |
| Supabase (Database) | Free Tier | $0 |
| **Total** | | **$0** ✅ |

---

## 📁 Project Structure

```
DJANGO_studentportal/
├── app1/                          # Main Django app
│   ├── management/
│   │   └── commands/
│   │       └── keepalive.py       # Self-ping keep-alive script
│   ├── migrations/                # Database migrations
│   ├── static/
│   │   └── css/
│   │       └── styles.css         # Custom design system
│   ├── models.py                  # Student model
│   ├── views.py                   # CRUD views
│   └── urls.py                    # URL routing
├── templates/
│   └── app1/
│       ├── base.html              # Base layout with navbar/footer
│       ├── home.html              # Landing page
│       ├── addstudent.html        # Add student form
│       ├── update_student.html    # Edit student form
│       ├── manage_students.html   # Dashboard & search
│       ├── delete_confirm.html    # Delete confirmation
│       └── success.html           # Success message
├── studentdata/                   # Project settings
│   ├── settings.py                # Django settings
│   ├── urls.py                    # Root URL config
│   └── wsgi.py                    # WSGI application
├── build.sh                       # Render build script
├── render.yaml                    # Render configuration
├── requirements.txt               # Python dependencies
├── .gitignore                     # Git ignore rules
└── README.md                      # This file
```

---

## 🎯 Key Features Breakdown

### 1. Professional UI Design
- Custom CSS variables for consistent theming
- Responsive grid layouts (mobile-first)
- Input wrappers with SVG icons
- Touch-friendly buttons (48px+ tap targets)
- iOS zoom prevention (16px font size on inputs)

### 2. Advanced Forms
- **Two-column grid** on desktop, stacks on mobile
- **Icon indicators** for each field type
- **Flatpickr calendar** for intuitive date selection
- **Form validation** with helpful error messages
- **Pre-filled forms** for editing

### 3. Data Management
- **Dashboard stats** showing total students
- **Search functionality** across name and email
- **Table view** with sortable columns
- **Action buttons** for Edit and Delete
- **Empty state** messaging when no data

### 4. Safety Features
- **Confirmation pages** for destructive actions
- **CSRF protection** on all forms
- **Row-level security** on database
- **Environment-based** configuration
- **HTTPS enforcement** in production

---

## 🔧 Configuration

### Environment Variables

Create a `.env` file with:

```env
# Database
DATABASE_URL=postgresql://user:password@host:5432/database

# Django
SECRET_KEY=your_secret_key_here
DJANGO_DEBUG=True  # Set to False in production

# Render (only for deployment)
RENDER_EXTERNAL_URL=https://your-app.onrender.com
```

### Database Setup (Supabase)

1. Create a free account at [supabase.com](https://supabase.com)
2. Create a new project
3. Get your PostgreSQL connection string
4. Add it to `.env` as `DATABASE_URL`
5. Enable Row Level Security (RLS) on tables

---

## 🧪 Testing

### Run the application locally
```bash
python manage.py runserver
```

### Test features:
1. ✅ **Add a student** - Try the calendar picker
2. ✅ **Search** - Test name and email search
3. ✅ **Edit** - Verify pre-filled form
4. ✅ **Delete** - Check confirmation page
5. ✅ **Mobile** - Resize browser to 375px width

### Check for issues:
```bash
python manage.py check
python manage.py test  # If you add tests
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Sravan Doniparthi**

- GitHub: [@sravanshetty06](https://github.com/sravanshetty06)
- LinkedIn: [Add your LinkedIn]
- Email: [Add your email]

---

## 🙏 Acknowledgments

- Django Documentation
- Flatpickr by Gregory Petrosyan
- Heroicons by Tailwind Labs
- Render.com for free hosting
- Supabase for free PostgreSQL

---

## 📞 Support

If you have any questions or run into issues:

1. Check the [Deployment Guide](DEPLOYMENT_GUIDE.md)
2. Open an [Issue](https://github.com/sravanshetty06/DJANGO_studentportal/issues)
3. Review [Django Docs](https://docs.djangoproject.com/)

---

## 🚀 What's Next?

Potential enhancements:
- [ ] Photo upload for students
- [ ] Export to Excel/PDF
- [ ] Email notifications
- [ ] Department/Class grouping
- [ ] Student attendance tracking
- [ ] Grade/marks management
- [ ] Authentication system
- [ ] Multi-tenant support

---

**Made with ❤️ by Sravan Doniparthi**

*Last updated: December 2025*
