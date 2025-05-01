# Gagan Goyal - Portfolio Website (Python Flask)

A modern, responsive portfolio website built with Python Flask, showcasing professional experience and skills as a Data Engineer.

## Features

- Responsive design that works on all devices
- Modern UI with smooth animations
- Clean and professional layout
- Easy navigation
- Contact information and social links
- Skills showcase
- Experience timeline
- Education section
- Dynamic content management through Python

## Technologies Used

- Python 3.x
- Flask (Web Framework)
- HTML5
- CSS3
- JavaScript (ES6+)
- Font Awesome Icons
- Google Fonts

## Project Structure

```
portfolio/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── static/            # Static files (CSS, JS, images)
│   ├── styles.css
│   └── script.js
└── templates/         # HTML templates
    └── index.html
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd portfolio
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask development server:
```bash
python app.py
```

2. Open your browser and visit:
```
http://localhost:5000
```

## Customization

1. Update personal information in `app.py`:
   - Modify the `portfolio_data` dictionary
   - Add or remove sections as needed

2. Modify styling in `static/styles.css`:
   - Change colors
   - Adjust layout
   - Update responsive breakpoints

3. Add new features in `static/script.js`:
   - Add new animations
   - Implement additional interactivity

## Deployment Options

### Option 1: Python Anywhere (Free)

1. Create a Python Anywhere account
2. Upload your project files
3. Configure the web app
4. Your site will be live at `yourusername.pythonanywhere.com`

### Option 2: Heroku (Free)

1. Create a Heroku account
2. Install Heroku CLI
3. Create a `Procfile`:
```
web: gunicorn app:app
```
4. Deploy using Git:
```bash
git push heroku main
```

### Option 3: DigitalOcean (Paid)

1. Create a DigitalOcean account
2. Create a new droplet
3. Set up Nginx and Gunicorn
4. Deploy your application

### Option 4: Custom Domain

1. Purchase a domain from providers like:
   - GoDaddy
   - Namecheap
   - Google Domains
2. Configure DNS settings
3. Update your hosting provider's settings

## Contact

For any questions or suggestions, feel free to reach out:
- Email: gagangoyal.cs@gmail.com
- LinkedIn: linkedin.com/in/gagan-goyal 