Movie App - README 🎬
Overview 🌟
This Django-based web application allows users to explore movies, register, log in, and leave comments on movie details.
Users can filter movies by categories and easily search for films using titles. The app provides authentication features for logging in, registering, and logging out. 
Admin users have the ability to manage the app, while regular users can interact with movie details and share their comments. 🎥🍿

Features ✨
User Authentication: Users can register, log in, and log out 🔑
Movie List: Movies are displayed in a paginated list 📜
Categories: Movies can be filtered by genre 🎬
Movie Details: View detailed information about each movie 📚
Comments: Logged-in users can leave comments on movies 💬
Search: Search movies by their title 🔍
Admin Panel: Admins can manage movies, categories, and comments 🛠️

Technologies 🛠️
Django - Web framework 🕸️
HTML/CSS - For user interface styling 🎨
Python - Backend programming language 🐍
SQLite (or another database) - Database storage 💾

Installation & Setup 🖥️
Install required dependencies:
pip install -r requirements.txt

Create the database and apply migrations:
python manage.py migrate

Run the development server:
python manage.py runserver

Then navigate to http://127.0.0.1:8000/ in your browser to access the app 🌐

Usage 📱
Register: To create a new user, visit the register page and fill in the necessary details ✍️
Login: Access the login page and log in with your credentials 🔐
View Movies: Browse through movies displayed in a paginated format on the movies page 🎞️
Filter by Category: Select a category to view movies related to that genre 🎬
View Movie Details: Click on a movie to see more details and comments 📜
Add Comments: Only logged-in users can add comments to movies ✏️
Search: Use the search bar to find movies by title 🔎

Notes ⚠️
Admin users can manage movies, categories, and comments from the admin panel 🏠
Only authenticated users can post comments 💬
Movies and comments are stored in the database and can be viewed by all users 🌍
Recommendations 📋
If you're new to Django, we recommend reading the official documentation: Django Documentation 📖
Feel free to explore, leave comments, and enjoy your movie experience! 🎉🎬
