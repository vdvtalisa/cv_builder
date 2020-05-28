# CV Builder

## Goal

Build a site where a person can fill out their info, which will be rendered into a pre-made cv template.
The user will be able to register and log in to save their info.

## Learning objectives

- Learn how to build a multi-page website with Django and Python

- Familiarise yourself with MVC (or MVT: Model, View, Template) in Django
    - Work with data and databases in models
    - Present the model to the client-side as an HTTP response, via the view
    - Learn how to design your lay-out with templates
    
- Learn how to use the Authentication framework and User model

## Pre-requisites

Install Django globally

Install/update pip installer

Make sure you have the latest version of Python (3.8) or at least 3.x

## Part 1: set-up

Set up your Django project with a virtual environment(make sure you set this up with the right Python version!). Install needed dependencies with pip.

Make your cv builder app within your project and configure it within your settings.

## Must-haves:

### Data handling

What information do you need from a user?

Tip: create a superuser as soon as possible and register your data models in your admin file, so you can access your data from the admin site.

### Form

On the homepage, the user will fill out a form and upload a picture of themselves, should they want to.

Once all the required fields are filled in and the form is validated, the user will be redirected to their cv.

A user should still be able to go back to the form to make changes.

### View

This will contain the data as given by the user.

Since we want a professional looking cv, your template will need styling.

How do you add styling to a Django template?

### Registration/login

Make sure the user registers and logs in so their info and template will be saved.

## Bonus:

### Make your forms dynamic so the user can add multiple work experience and education items

### Allow the user to save their cv as a pdf

# cv_builder
