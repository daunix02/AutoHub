# AutoHub — DevOps Learning Project

## Project Overview

AutoHub is a simple second-hand luxury car marketplace that will gradually evolve into a containerized web application.

The purpose of this project is to learn DevOps concepts through building, packaging, deploying, and troubleshooting a real application.

The application will eventually include:
- Used luxury car listings.
- Spare parts inventory and availability.
- Spare parts booking and order management.
- Mock payment and order confirmation.
- Delivery status tracking.

## Day 1 — Python Environment and Flask Setup

### Objective

Create and run a basic Python web application locally using Flask.

### Technology Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Flask | Backend web framework |
| VS Code | Code editor |
| macOS | Development environment |

### Implementation Completed

1. Created the AutoHub project directory.
2. Created a Python virtual environment using `venv`.
3. Activated the virtual environment.
4. Installed Flask inside the virtual environment.
5. Created the Flask application instance.
6. Defined the homepage route (`/`).
7. Started the Flask development server.
8. Successfully accessed the application through the browser.

### Current Application

The application currently returns:

`Welcome to AutoHub`

Local development URL:

`http://127.0.0.1:5001`

### Concepts Learned

**1. Python virtual environments**
- Isolate project-specific Python packages.
- Use a separate package installation directory.
- Activation modifies the shell's PATH.
- Do not provide complete operating-system isolation.

**2. Flask**
- Flask is a Python web framework.
- Routes map URLs to Python functions.
- The application returns HTTP responses to browsers.
- `app.run()` starts the development server.

**3. Networking fundamentals**
- `127.0.0.1` is the loopback IP address.
- `localhost` is a hostname that resolves to a loopback address.
- IP addresses identify network destinations.
- Port numbers identify application endpoints.
- Multiple applications can listen on different ports.

**4. Troubleshooting**
- Used `lsof` to investigate listening processes.
- Identified a macOS Control Center process occupying port 5000.
- Changed the Flask development port to 5001.
- Verified the application was running successfully.

### Current Project Status

- [x] Python environment configured
- [x] Virtual environment created
- [x] Flask installed
- [x] Basic Flask application created
- [x] Homepage route working
- [x] Application accessible locally
- [ ] HTML homepage
- [ ] CSS styling
- [ ] Car inventory
- [ ] Spare parts inventory
- [ ] Docker packaging
- [ ] VM deployment

### Engineering Lessons

- Inspect the environment before making changes.
- Understand what commands change on the machine.
- Distinguish configuration from actual runtime behaviour.
- Investigate port conflicts rather than randomly terminating processes.
- Understand application networking before containerizing applications.

---

## Next Session — Day 2

### Objective
Convert the plain-text Flask application into a basic AutoHub website.

### Planned work
1. Introduce Flask templates.
2. Create `templates/index.html`.
3. Create `static/style.css`.
4. Build the AutoHub homepage.
5. Display three sample luxury cars.
6. Test the application locally.

### Future DevOps Direction

The same application will progressively be extended to learn:

Python → Flask → Docker → Docker Compose → Linux VM deployment → CI/CD → Kubernetes → Monitoring.

**Learning principle:** Build, understand, troubleshoot, document, and then move forward.


### Day 2 — Project Structure

- Created `templates/` directory for Flask HTML templates.
- Created `static/` directory for CSS and static assets.
- Created `static/images/` for application images.
- Prepared the project structure for frontend integration.

**Next:** Connect Flask with HTML templates using `render_template()` and build the AutoHub homepage.

### Day 3 ##
Added the index.hmtl and routed the index.html in flask
next python list in html doc and routing it in flask.py

## Day4 ##
Added jinja2 in html now I am able to display all three cars which I want to show on my website