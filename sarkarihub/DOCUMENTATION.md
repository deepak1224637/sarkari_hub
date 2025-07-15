# SarkariHub Project Documentation

## Overview
SarkariHub is a Django-based portal for government job updates, admit cards, and results. It features admin-only posting, user email subscriptions, and a modern, responsive UI.


## Features

- Admin-only posting of jobs, admit cards, results, and answer keys via a secure admin panel
- Public home page with categorized, side-by-side sections for Latest Jobs, Admit Cards, Results
- Dynamic job detail view for every post (clickable from home page)
- Email subscription system: users can subscribe and receive notifications for new posts
- Automatic email notifications sent to all subscribers when a new post is created (admin panel)
- Floating social media buttons: Telegram, Twitter, Instagram, Facebook
- Modern, responsive UI with Bootstrap 5 and custom styles
- Search bar for instant filtering of posts by title
- About Us and Subscribe informational pages
- Documentation page for project usage and setup
- Animated hero section for a professional look
- Floating notification (toast) in hero section for important alerts
- Scrolling marquee (news ticker) for latest updates
- Dark mode toggle with persistent user preference
- Real Tawk.to live chat widget for instant user support
- Category-specific pages for Latest Jobs, Admit Cards, Results
- Admin panel improvements: search, filter, and edit job details easily
- Answer Key category and navigation added
- All code modular and easy to extend

## Recent Improvements

- Added floating notification (toast) for user engagement
- Added scrolling marquee for latest news/alerts
- Integrated Tawk.to real live chat widget
- Improved job detail view and navigation
- Enhanced admin panel with job details and email notification logic
- Added Answer Key as a new post category
- Improved documentation and setup instructions
- Fixed bugs in URL routing and template rendering



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
