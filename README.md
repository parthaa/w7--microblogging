# W7 -- Build a Microblogging Platform

## Description

For this project, you will build an application with an API that works like Twitter and other microblogging applications. The application will allow users to create and share short posts. _Yes, the posts are tweets. But please find another name to call them in your app._

## Project details

Your application has users, posts, likes, and follows. "Follows" are relationships between two users -- a user can follow another user to see updates from that user.

Your application has both a front-end in Django and a REST API. You should create standard Django views and templates for registration, login, and updating a user's account (like changing passwords or the user's username). You should also create Django views for the home page and individual user pages.

**Home page**: The home page should show the last 20 posts from all users in reverse chronological order if the user is not logged in. If a user is logged in, it should show the last 20 posts from users they follow (as well as their own posts). If a user is logged in, this page should also have a place to make a new post.

**User profile pages**: Each user has a page with a unique URL (like `/users/bocephus`) that shows their posts. On that page, you should show the last 20 posts they have made.

### The API

Design your API to support a service like Twitter, allowing users to create and share microposts and to favolikerite other users' microposts. **Your Django front-end should use this API as much as possible.** Liking a post, adding a new post, getting the next 20 posts, and any other in-page interaction that should not cause a page reload should use JavaScript + the API to perform that interaction.

Begin by thinking about the resources that you need to create. If a front-end team wanted to recreate Twitter, what data would they need from you in order to do it?

Map the endpoints your application will expose, decide which will require authentication, and design the data structures you will return.

Please provide documentation for how to use your API in your project's README. In the documentation, you should list the available endpoints and any query parameters you can accept. Think about the documentation that's been helpful to you, and include any information that will make it easier to consume your api (for your fellow developers!).

### Requirements

- Posts have a text body and belong to a user.
- Posts should not be valid if they are less than 2 characters or greater than 280 characters.
- Only authenticated users can create, delete, or like posts.
  - Posts are not editable. They can only be created or destroyed.
  - Only the user that created a post should be able to delete it.
- Any user should have the ability to "follow" other users.
  - Your application should have an authenticated endpoint that returns a list of users that the current user is following and an endpoint that will return all the posts from users that the current user follows.
- Your application should have seed data to populate the database with 100 users and 10-50 posts per user.
- Your application should be deployed to Heroku.
  
### Extra challenges

- Add the ability to re-post another user's posts.
- Add the ability to "unfollow" users you have followed.
- Add the ability to "unlike" posts you have liked.
- The root url of the site shows a list of the top users (ordered by who has the most posts) in a sidebar.
- Display all the users that a user is following and who is following them on their profile.
