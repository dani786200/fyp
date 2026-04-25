# UniGO — A Smart University Transport Platform
# 🚀 Complete Implementation Plan

## 📋 Project Understanding (From Proposal)

**University:** Mirpur University of Science and Technology (MUST)
**Department:** CS & IT — Final Year Project
**Team:** Abdul Rehman Saqib (FA22-BIT-072) & Danish Zia-ur-Rehman (FA22-BIT-075)

**Core Problem:** The university transport system is manual — paper challans, verbal coordination, no real-time tracking, unauthorized passengers, overcrowding, and poor record-keeping.

**UniGO Solution:** A smart web platform with:
- Student registration & route selection
- QR-based travel pass verification
- Real-time bus tracking
- Online fee challan generation & payment
- Admin dashboard with analytics
- Driver verification interface

---

## 🛠️ Technology Stack

| Layer | Technology |
|---|---|
| **Frontend Structure** | HTML5 (Semantic) |
| **Styling** | Tailwind CSS v3 + Custom CSS |
| **Interactivity** | Vanilla JavaScript (ES6+) |
| **Backend** | PHP 8+ (MVC Architecture) |
| **Database** | MySQL 8 |
| **QR Codes** | `phpqrcode` library (server-side generation) + `html5-qrcode` (client-side scanning) |
| **PDF Generation** | `TCPDF` or `Dompdf` (for fee challans) |
| **Maps/Tracking** | Leaflet.js + OpenStreetMap (free, no API key) |
| **Charts/Analytics** | Chart.js |
| **Server** | XAMPP / WAMP for local dev, Apache + PHP on production |
| **Version Control** | Git + GitHub |

---

## 🗂️ Project Folder Structure

```
Unigo/
├── index.php                    # Landing page / login router
├── .htaccess                    # URL rewriting & security
├── tailwind.config.js           # Tailwind configuration
├── package.json                 # npm for Tailwind build
│
├── config/
│   ├── database.php             # MySQL connection (PDO)
│   ├── constants.php            # App-wide constants
│   └── session.php              # Session management
│
├── core/
│   ├── Router.php               # Simple MVC router
│   ├── Controller.php           # Base controller class
│   ├── Model.php                # Base model class (PDO wrapper)
│   └── Middleware.php           # Auth & role middleware
│
├── controllers/
│   ├── AuthController.php       # Login, Register, Logout, Password Reset
│   ├── StudentController.php    # Student dashboard actions
│   ├── DriverController.php     # Driver dashboard actions
│   ├── AdminController.php      # Admin dashboard actions
│   ├── QRController.php         # QR generation & verification
│   ├── ChallanController.php    # Fee challan CRUD & PDF
│   ├── RouteController.php      # Bus route management
│   ├── TrackingController.php   # Live bus location updates
│   └── ReportController.php     # Analytics & report generation
│
├── models/
│   ├── User.php                 # Users table model
│   ├── Student.php              # Students table model
│   ├── Driver.php               # Drivers table model
│   ├── Bus.php                  # Buses table model
│   ├── Route.php                # Routes table model
│   ├── QRPass.php               # QR passes table model
│   ├── Challan.php              # Fee challans table model
│   ├── Attendance.php           # Travel attendance logs
│   ├── BusLocation.php          # Real-time bus locations
│   └── ActivityLog.php          # Admin activity logs
│
├── views/
│   ├── layouts/
│   │   ├── app.php              # Main layout wrapper
│   │   ├── header.php           # Navigation bar
│   │   ├── footer.php           # Footer
│   │   └── sidebar.php          # Dashboard sidebar
│   │
│   ├── auth/
│   │   ├── login.php            # Login page
│   │   ├── register.php         # Student registration
│   │   └── forgot-password.php  # Password reset
│   │
│   ├── student/
│   │   ├── dashboard.php        # Student home
│   │   ├── profile.php          # Edit profile
│   │   ├── routes.php           # Browse & select routes
│   │   ├── qr-pass.php          # View/download QR pass
│   │   ├── challans.php         # View fee challans
│   │   └── tracking.php         # Live bus tracking map
│   │
│   ├── driver/
│   │   ├── dashboard.php        # Driver home
│   │   ├── scan-qr.php          # QR scanner interface
│   │   ├── passengers.php       # Today's verified passengers
│   │   └── route-info.php       # Assigned route details
│   │
│   ├── admin/
│   │   ├── dashboard.php        # Admin overview with charts
│   │   ├── students.php         # Manage students (CRUD)
│   │   ├── drivers.php          # Manage drivers (CRUD)
│   │   ├── buses.php            # Manage buses (CRUD)
│   │   ├── routes.php           # Manage routes (CRUD)
│   │   ├── challans.php         # Generate & manage challans
│   │   ├── qr-logs.php          # QR verification history
│   │   ├── reports.php          # Analytics & reports page
│   │   ├── tracking.php         # Live bus tracking (all buses)
│   │   └── activity-logs.php    # Admin action logs
│   │
│   ├── components/
│   │   ├── alert.php            # Reusable alert/toast
│   │   ├── modal.php            # Reusable modal dialog
│   │   ├── table.php            # Data table component
│   │   ├── card.php             # Stat/info card
│   │   └── chart.php            # Chart wrapper
│   │
│   └── errors/
│       ├── 404.php
│       └── 403.php
│
├── public/
│   ├── css/
│   │   ├── output.css           # Tailwind compiled output
│   │   └── custom.css           # Custom animations & overrides
│   ├── js/
│   │   ├── app.js               # Global JS (sidebar, modals, toasts)
│   │   ├── qr-scanner.js        # QR scanning logic (html5-qrcode)
│   │   ├── tracking.js          # Leaflet map & live tracking
│   │   ├── charts.js            # Chart.js initialization
│   │   └── form-validation.js   # Client-side form validation
│   ├── images/
│   │   ├── logo.png
│   │   └── hero-bg.jpg
│   └── vendor/
│       ├── chart.min.js
│       ├── leaflet/
│       └── html5-qrcode.min.js
│
├── libraries/
│   ├── phpqrcode/               # QR code generation library
│   └── dompdf/                  # PDF generation library
│
├── storage/
│   ├── qrcodes/                 # Generated QR code images
│   ├── challans/                # Generated challan PDFs
│   └── logs/                    # Application logs
│
├── database/
│   ├── schema.sql               # Full database creation script
│   ├── seed.sql                 # Sample data for testing
│   └── migrations/              # Incremental DB changes
│
└── docs/
    ├── user-manual.md           # End user documentation
    └── admin-guide.md           # Admin documentation
```

---

## 🗄️ Database Schema Design (MySQL)

### Entity Relationship Overview

```
USERS ──1:1──> STUDENTS ──1:N──> QR_PASSES ──1:N──> ATTENDANCE_LOGS
USERS ──1:1──> DRIVERS ──N:1──> BUSES ──N:1──> ROUTES
STUDENTS ──N:1──> ROUTES
STUDENTS ──1:N──> CHALLANS
BUSES ──1:N──> BUS_LOCATIONS
ROUTES ──1:N──> ROUTE_STOPS
USERS ──1:N──> ACTIVITY_LOGS
USERS ──1:N──> NOTIFICATIONS
```

### Table Definitions

```sql
-- =============================================
-- UniGO Database Schema
-- =============================================

CREATE DATABASE IF NOT EXISTS unigo_db
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE unigo_db;

-- 1. USERS (unified auth table)
CREATE TABLE users (
    id              INT PRIMARY KEY AUTO_INCREMENT,
    email           VARCHAR(255) UNIQUE NOT NULL,
    password_hash   VARCHAR(255) NOT NULL,
    role            ENUM('student', 'driver', 'admin') NOT NULL,
    full_name       VARCHAR(100) NOT NULL,
    phone           VARCHAR(20),
    avatar_url      VARCHAR(255) DEFAULT NULL,
    is_active       BOOLEAN DEFAULT TRUE,
    last_login      DATETIME DEFAULT NULL,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 2. STUDENTS
CREATE TABLE students (
    id              INT PRIMARY KEY AUTO_INCREMENT,
    user_id         INT UNIQUE NOT NULL,
    reg_number      VARCHAR(20) UNIQUE NOT NULL,
    program         VARCHAR(50) NOT NULL,
    semester        TINYINT NOT NULL,
    route_id        INT DEFAULT NULL,
    fee_status      ENUM('paid', 'unpaid', 'partial') DEFAULT 'unpaid',
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (route_id) REFERENCES routes(id) ON DELETE SET NULL
);

-- 3. DRIVERS
CREATE TABLE drivers (
    id              INT PRIMARY KEY AUTO_INCREMENT,
    user_id         INT UNIQUE NOT NULL,
    license_number  VARCHAR(30) UNIQUE NOT NULL,
    bus_id          INT DEFAULT NULL,
    status          ENUM('active', 'on_leave', 'inactive') DEFAULT 'active',
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (bus_id) REFERENCES buses(id) ON DELETE SET NULL
);

-- 4. BUSES
CREATE TABLE buses (
    id              INT PRIMARY KEY AUTO_INCREMENT,
    bus_number      VARCHAR(20) UNIQUE NOT NULL,
    capacity        INT NOT NULL DEFAULT 50,
    current_occupancy INT DEFAULT 0,
    route_id        INT DEFAULT NULL,
    status          ENUM('active', 'maintenance', 'retired') DEFAULT 'active',
    FOREIGN KEY (route_id) REFERENCES routes(id) ON DELETE SET NULL
);

-- 5. ROUTES
CREATE TABLE routes (
    id              INT PRIMARY KEY AUTO_INCREMENT,
    route_name      VARCHAR(100) NOT NULL,
    route_code      VARCHAR(10) UNIQUE NOT NULL,
    origin          VARCHAR(100) NOT NULL,
    destination     VARCHAR(100) NOT NULL,
    distance_km     DECIMAL(5,2),
    estimated_time  INT,
    fare_amount     DECIMAL(10,2) NOT NULL,
    is_active       BOOLEAN DEFAULT TRUE,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 6. ROUTE STOPS
CREATE TABLE route_stops (
    id              INT PRIMARY KEY AUTO_INCREMENT,
    route_id        INT NOT NULL,
    stop_name       VARCHAR(100) NOT NULL,
    stop_order      INT NOT NULL,
    latitude        DECIMAL(10,7),
    longitude       DECIMAL(10,7),
    FOREIGN KEY (route_id) REFERENCES routes(id) ON DELETE CASCADE
);

-- 7. QR PASSES
CREATE TABLE qr_passes (
    id              INT PRIMARY KEY AUTO_INCREMENT,
    student_id      INT NOT NULL,
    qr_token        VARCHAR(64) UNIQUE NOT NULL,
    qr_image_path   VARCHAR(255),
    semester        VARCHAR(20) NOT NULL,
    valid_from      DATE NOT NULL,
    valid_until     DATE NOT NULL,
    is_active       BOOLEAN DEFAULT TRUE,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE
);

-- 8. ATTENDANCE LOGS
CREATE TABLE attendance_logs (
    id              INT PRIMARY KEY AUTO_INCREMENT,
    qr_pass_id      INT NOT NULL,
    student_id      INT NOT NULL,
    driver_id       INT NOT NULL,
    bus_id          INT,
    route_id        INT,
    scan_type       ENUM('boarding', 'alighting') DEFAULT 'boarding',
    scan_result     ENUM('valid', 'invalid', 'expired') NOT NULL,
    scanned_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    latitude        DECIMAL(10,7),
    longitude       DECIMAL(10,7),
    FOREIGN KEY (qr_pass_id) REFERENCES qr_passes(id),
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (driver_id) REFERENCES drivers(id),
    FOREIGN KEY (bus_id) REFERENCES buses(id),
    FOREIGN KEY (route_id) REFERENCES routes(id)
);

-- 9. CHALLANS
CREATE TABLE challans (
    id              INT PRIMARY KEY AUTO_INCREMENT,
    challan_number  VARCHAR(20) UNIQUE NOT NULL,
    student_id      INT NOT NULL,
    route_id        INT NOT NULL,
    amount          DECIMAL(10,2) NOT NULL,
    semester        VARCHAR(20) NOT NULL,
    due_date        DATE NOT NULL,
    paid_date       DATE DEFAULT NULL,
    status          ENUM('pending', 'paid', 'overdue', 'cancelled') DEFAULT 'pending',
    payment_method  VARCHAR(50) DEFAULT NULL,
    pdf_path        VARCHAR(255) DEFAULT NULL,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
    FOREIGN KEY (route_id) REFERENCES routes(id)
);

-- 10. BUS LOCATIONS
CREATE TABLE bus_locations (
    id              INT PRIMARY KEY AUTO_INCREMENT,
    bus_id          INT NOT NULL,
    latitude        DECIMAL(10,7) NOT NULL,
    longitude       DECIMAL(10,7) NOT NULL,
    speed_kmh       DECIMAL(5,2) DEFAULT 0,
    heading         DECIMAL(5,2),
    recorded_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (bus_id) REFERENCES buses(id) ON DELETE CASCADE,
    INDEX idx_bus_time (bus_id, recorded_at DESC)
);

-- 11. ACTIVITY LOGS
CREATE TABLE activity_logs (
    id              INT PRIMARY KEY AUTO_INCREMENT,
    user_id         INT NOT NULL,
    action          VARCHAR(100) NOT NULL,
    description     TEXT,
    ip_address      VARCHAR(45),
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- 12. NOTIFICATIONS
CREATE TABLE notifications (
    id              INT PRIMARY KEY AUTO_INCREMENT,
    user_id         INT NOT NULL,
    title           VARCHAR(200) NOT NULL,
    message         TEXT NOT NULL,
    type            ENUM('info', 'warning', 'success', 'danger') DEFAULT 'info',
    is_read         BOOLEAN DEFAULT FALSE,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

---

## 🏗️ Module-by-Module Implementation Plan

### Phase 1: Foundation & Auth (Days 1–5)

#### config/database.php
- PDO connection to MySQL with error handling, character set `utf8mb4`
- Singleton pattern for reuse across controllers

#### config/constants.php
- `BASE_URL`, `APP_NAME`, `UPLOAD_DIR`, role constants

#### config/session.php
- Secure session start, CSRF token generation, session timeout

#### core/Router.php
- Simple URL router: parses `?page=student/dashboard` style routes
- Maps URL → Controller → Method
- Applies middleware (auth check, role check)

#### core/Controller.php & core/Model.php
- Base controller with `view()`, `redirect()`, `json()` helpers
- Base model with PDO CRUD wrappers: `find()`, `findAll()`, `create()`, `update()`, `delete()`

#### core/Middleware.php
- `isAuthenticated()` — checks valid session
- `hasRole($role)` — checks user role (student/driver/admin)

#### controllers/AuthController.php
- `login()` — email/password validation, bcrypt verify, session creation
- `register()` — student self-registration with validation
- `logout()` — session destroy, redirect
- `forgotPassword()` — password reset flow

#### views/auth/login.php & register.php
- Beautiful Tailwind login form with glassmorphism card, gradient background
- Form validation with JavaScript
- Responsive design (mobile-first)

#### views/layouts/app.php, header.php, sidebar.php, footer.php
- Dark/light theme toggle
- Responsive sidebar navigation with role-based menu items
- Animated transitions

---

### Phase 2: Student Module (Days 6–12)

#### controllers/StudentController.php
- `dashboard()` — overview stats (route, QR status, fee status)
- `profile()` — view/edit profile
- `routes()` — browse available routes, request route assignment
- `qrPass()` — view & download QR pass image
- `challans()` — view fee challans, download PDFs
- `tracking()` — real-time bus location map

#### views/student/*.php
- **Dashboard**: Stat cards (route info, fee status, next bus ETA), recent activity feed
- **Profile**: Editable form with avatar upload
- **Routes**: Route cards with origin → destination, stops, fare, map preview
- **QR Pass**: Large QR code display with download button, validity period indicator
- **Challans**: Table of challans with status badges (paid/pending/overdue), PDF download
- **Tracking**: Full-screen Leaflet map with bus marker, route polyline, ETA countdown

---

### Phase 3: Driver Module (Days 13–17)

#### controllers/DriverController.php
- `dashboard()` — today's stats (scans, passengers, route)
- `scanQR()` — process QR scan, validate token, log attendance
- `passengers()` — list of today's verified passengers
- `routeInfo()` — assigned route details with stops

#### views/driver/*.php
- **Dashboard**: Today's boarding count, bus capacity gauge, route card
- **Scan QR**: Camera viewfinder using `html5-qrcode`, instant verification result (green ✓ / red ✗ overlay), sound feedback
- **Passengers**: Sortable table of verified students with timestamps
- **Route Info**: Map of route with all stops highlighted

#### public/js/qr-scanner.js
- Initialize `html5-qrcode` library
- On scan success → AJAX POST to `QRController::verify()`
- Display animated success/failure feedback
- Auto-log attendance

---

### Phase 4: QR Code & Challan System (Days 18–23)

#### controllers/QRController.php
- `generate($studentId)` — create unique token (SHA-256 of student_id + semester + secret), generate QR image via `phpqrcode`, store in `storage/qrcodes/`
- `verify($token)` — lookup token, check expiry, check fee status, return JSON result
- `revoke($passId)` — deactivate a QR pass (admin)

#### controllers/ChallanController.php
- `generate($studentId)` — create challan record with auto-number (e.g., `CH-2026-0001`), calculate amount from route fare
- `generatePDF($challanId)` — render challan as PDF using Dompdf (university header, student info, amount, barcode, due date)
- `bulkGenerate()` — admin generates challans for all students of a route/semester
- `markPaid($challanId)` — update status to paid
- `list()` — filterable list with status

---

### Phase 5: Admin Module (Days 24–32)

#### controllers/AdminController.php
- `dashboard()` — aggregate stats (total students, active buses, revenue, today's boardings)
- `students()` — CRUD with search, filter by route/program/fee-status
- `drivers()` — CRUD with bus assignment
- `buses()` — CRUD with route assignment, capacity management
- `routes()` — CRUD with stops management (add/remove/reorder stops)
- `challans()` — bulk generation, payment tracking
- `qrLogs()` — searchable QR verification history
- `reports()` — analytics dashboard
- `activityLogs()` — audit trail viewer

#### views/admin/*.php
- **Dashboard**: 
  - Stat cards with animated counters (total students, active buses, revenue, today's scans)
  - Chart.js: Line chart (daily boardings trend), Doughnut chart (fee status distribution), Bar chart (route-wise usage)
  - Recent activity feed
  - Quick action buttons

- **CRUD Pages** (students, drivers, buses, routes):
  - Searchable/sortable data tables with pagination
  - Create/Edit modals with form validation
  - Bulk actions (delete, export CSV)
  - Status toggle switches

- **Reports Page**:
  - Date range picker
  - Transport usage reports (route-wise, day-wise)
  - QR verification reports (valid vs invalid scans)
  - Fee collection reports (paid vs pending vs overdue)
  - Export to CSV/PDF

- **Live Tracking**:
  - Full-screen map showing all active buses
  - Bus markers with popups (bus number, driver, occupancy, speed)
  - Route polylines color-coded

#### public/js/charts.js
- Chart.js initialization with UniGO color palette
- Functions to render: line, bar, doughnut, pie charts
- Auto-refresh via AJAX polling

---

### Phase 6: Real-Time Tracking (Days 33–36)

#### controllers/TrackingController.php
- `updateLocation()` — receives GPS coordinates from driver's device, stores in `bus_locations`
- `getLocations()` — returns latest location of all active buses (JSON)
- `getBusHistory($busId)` — returns location trail for a bus

#### public/js/tracking.js
- Initialize Leaflet map centered on MUST campus coordinates
- Poll `/tracking/locations` every 10 seconds
- Animate bus markers moving on map
- Show route polylines, stops as circle markers
- ETA calculation based on distance & average speed

---

### Phase 7: Polish, Testing & Documentation (Days 37–42)

#### Testing Strategy
- **Functional Testing**: Every form submission, CRUD operation, QR scan flow
- **Integration Testing**: QR generation → scan → attendance log → dashboard update
- **Security Testing**: SQL injection, XSS, CSRF, session hijacking
- **Performance Testing**: Page load times, concurrent QR scans
- **Responsive Testing**: Mobile, tablet, desktop breakpoints

#### Documentation
- End-user manual (student guide, driver guide)
- Admin guide
- System admin documentation (server setup, DB backup)

---

## 🎨 UI/UX Design Principles

| Aspect | Approach |
|---|---|
| **Color Palette** | Primary: `#6366F1` (Indigo-500), Secondary: `#10B981` (Emerald-500), Dark BG: `#0F172A`, Cards: `#1E293B` |
| **Typography** | Google Fonts — `Inter` for body, `Outfit` for headings |
| **Theme** | Dark mode default with light mode toggle |
| **Cards** | Glassmorphism with `backdrop-blur`, subtle borders |
| **Animations** | Fade-in on page load, hover scale on cards, smooth sidebar transitions |
| **Responsiveness** | Mobile-first with Tailwind breakpoints (`sm`, `md`, `lg`, `xl`) |
| **Icons** | Heroicons (matches Tailwind ecosystem) |
| **Notifications** | Toast notifications (slide-in from top-right) |

---

## ❓ Questions Before We Start Building

1. **Do you have XAMPP or WAMP installed?** If not, which do you prefer for local PHP + MySQL development?
2. **Tailwind CSS v3 is planned** — is that okay, or do you want v4?
3. **Real GPS tracking or simulated for demo?** True GPS needs driver devices with browser open.
4. **Payment: Real gateway (JazzCash/EasyPaisa) or admin "mark as paid"?** (Admin marking is simpler & recommended for FYP)
5. **Do you have a university logo** to incorporate into the UI?
6. **How many sample routes/buses/students** should we seed for demo?
7. **QR code content**: Just a secure token, or encoded student details?
8. **Driver QR scanner**: Will drivers use phone/tablet or desktop with webcam?
