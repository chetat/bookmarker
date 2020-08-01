# bookmarker
Bookmarker is social application, which let users interact with each other by sharing images that they find on the Internet. 
The app has features such as:

- User Management(Registreation and Authentication, Password Reset, and Social Authentication)
- A follow system that allows users to follow each other on the website
- Ability to display shared images by other users
- A bookmark button to enable users to share images from any website
- An activity stream that allows users to see the content uploaded by the people that they follow

## Getting Started

### Installing Dependencie


#### Virtual Enviornment

It is recommended to work within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip3 install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

## Running the server
### Set environment variables

Set the environments variables by exporting(pass your own values) the following: 
```
export SECRET_KEY=xxxxxxx
export EMAIL_HOST_PASSWORD=xxxxx
export SOCIAL_AUTH_TWITTER_SECRET=xxxxxx
export SOCIAL_AUTH_TWITTER_KEY=xxxxx
export SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=xxxxx
export SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=xxxxxx
export SOCIAL_AUTH_FACEBOOK_KEY=xxxxx
export SOCIAL_AUTH_FACEBOOK_SECRET=xxxxxxx
```
*NB: This is valid for unix like systems. For windows CMD you should use SET instead of export*

### Run the server
To run the server, simply issue the commands:
`python manage.py runserver`

