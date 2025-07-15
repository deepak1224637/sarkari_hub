# SarkariHub Project Documentation

## Overview
SarkariHub is a Django-based portal for government job updates, admit cards, and results. It features admin-only posting, user email subscriptions, and a modern, responsive UI.

## Features
- Admin panel for posting jobs, admit cards, and results
- Public home page with categorized sections
- Email subscription for notifications
- Social media floating buttons (Telegram, Twitter, Instagram, Facebook)
- Search bar for posts
- About Us and Subscribe pages
- Add Answer Key 
- Dark mode togal


## How to Run
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
3. Create a superuser for admin:
   ```
   python manage.py createsuperuser
   ```
4. Start the server:
   ```
   python manage.py runserver
   ```
5. Access the site at http://127.0.0.1:8000/

## Email Notifications
- Users can subscribe via the Subscribe page.
- To send emails, configure SMTP settings in `settings.py`.

## Adding Posts
- Log in to the admin panel at `/admin/`.
- Add posts under the Post model, selecting the appropriate category.

## Customization
- Edit templates in the `templates/` folder for UI changes.
- Add more features as needed (see suggestions in chat history).

## Contact
For support, email info@sarkarihub.com
