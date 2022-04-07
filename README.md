# SOCIAL MEDIA - LIKE BLOG
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Demo](#demo)
* [Who we Are?](#who-we-are)

## General info
This project contains normal and admin users. Each user has his features
with categories, posts, likes, comments, and CRUD operations.
Normal users can add, edit, delete posts, view others posts, leave
comments, likes, dislikes, subscribe to categories. An admin panel to
CRUD over the blog, adding forbidden words to appear as asterisks,
block, unblock users, promote others to be admins

## Technologies
- HTML
- CSS 
- BOOTSTRAP
- Django
- Django Rest
- MYSQL

## Setup
Required to install in yout system:
- Github Desktop / Git Bash

Then in yout terminal
```
$ git clone https://github.com/RahmaRamadan/Django-Blog.git
```
- Install python version ‘3.8.6’ from https://www.python.org/downloads/release/python-386/
- Create virtual environment
```
$ python -m venv venv
```
- Activate the virtual environment
```
$ source env/bin/activate
```
- Install requirements packages for the project
```
$ pip install -r requirements.txt
```
- Install postgres from “https://www.postgresql.org/download/”.
- Install pgAdmin from “https://www.pgadmin.org/download/” then open it.
	##### Create new Database 
	* user: postgres
  * password: admin 
  * name: Blog-DB
  
- open settings.py add this in database section
 ```
DATABASES = 
  {
  'default': {
  'ENGINE': 'django.db.backends.postgresql_psycopg2',
  'NAME': 'Blog-DB',
  'USER':'postgres',
  'PASSWORD': 'admin',
  },
}  
```
- python manage.py migrate
- python manage.py runserver

## Features
### This project is a responsive web application that contains:
### 1- Register page 
- It contains fields with validations:
  * Username
  * Email
  * First name
  * Last name 
  * Password
  * Confirm password
  
 ### 2- Login Page 
- It contains fields with validations:
  * Username
  * Password
  
### 3- Home Page 
- Navbar 
  * It contains links Login/Register
  * If the user is already logged in, then the link will be Logout
  * Current username
  * If the logged-in user is an admin, then there will be another link called Manage Blog that will redirect the admin to the administration page to make the admin CRUD Operations plus he can use normal users' features.
  * The user can find posts by tags 
  
- Sidebar
  * It contains all the available categories. (example: Sports, News, Politics, ...) with a button beside them be subscribe or unsubscribe if the user is already   subscribed to this category
  * When a category is chosen it will be redirected to a page that contains all the posts belonging to this category
  * The posts are sorted by date of publish
  
- Body 
   * It has the top posts sorted by publish date
   * When clicking on the image of a post, it will redirect to the post’s page
   * If the user is logged in as a normal user, then he can like or comment on the post and subscribe/unsubscribe category.
   * If post is chosen its details will be displayed with all comments and likes.

### 4- Post Page Content
- Title
- Author name
- Post Picture
- Content of the post
- The category that this post is under
- Tags related
- Comments section
- Like button
- How many likes on this post

### 5- Post Page Features 
- Each comment shows the time of the comment and the username who wrote the comment
- User must be signed in to be able to submit a comment (enter the text and a submit button to submit the comment)
- If the comment contains inappropriate words, it will show like ******** with the length of the undesired word. 
  * *For example:
  * [ ‘stupid’ → ****** ]
  * [ ‘fool’ → **** ]
- Like and dislike counter on the posts
- A reply to each comment

### 6- What Can Normal User DO?
- He can see posts and categories
- Search by tag name
- If logged in he can like, dislike, comment or reply to another user comment on a post
- If blocked, he cannot log into the system on the login page (Your account is locked, please contact an admin)

### 7- What Can Admin User DO?
- Admin users can make CRUD on posts
- Admin users can make CRUD on categories
- Admin users can block or unblock users
- Admin users can promote a normal user to an admin user so that he will be able to log into the admin screen
- Admin users can CRUD on forbidden words
- The Admin page contains links: users, posts, categories, forbidden
- When Admin clicks on the Posts Link, it would list all posts, with links to edit, delete and create
- The same will be applied to categories, forbidden words
- When Admin clicks on Users Link, it would list all the users
- For normal users, there should be a button that enables the admin to either lock or unlock this user from logging into the system and for the Admin users, this button is not available So, an admin cannot lock another admin

### TO DO
- Improve website styling
- Enhance Admin dashboard

## Demo
https://user-images.githubusercontent.com/36454500/162214565-698691ea-159b-45ea-a0c5-139cf3a31f90.mp4

## Who we Are?
- Intensive Code Camp (ICC) - Information Technology Institute (ITI) - The Egyptian Ministry of Communications and Information Technology (MCIT) Students & Teammates
- We are a Full Stack Web Development Graduates from ITI - Python Stack Track
- We are introducing a Django Blog with many features using Django Templates as a front-end and mysql as a database manager

### - Team members
| Name | Email 📧| 
| :-----: | :-: |
| Rahma Ramadan | rahmaramadan23@gmail.com |
| Yousef Ahmed | yousefa.mohamed12@gmail.com |
| Shrouk Hussien | rahmaramadan23@gmail.com |
| Sherif Elshafaey | sherifelshaf3y@yahoo.com |
| Nehal Mohamed | nehalhdev@outlook.com |

