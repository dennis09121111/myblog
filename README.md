![sample screenshot](https://i.imgur.com/fTIWIWc.png)

---

To run the code please use the following commends
```
git clone https://github.com/dennis09121111/myblog.git
OR
git clone git@github.com:dennis09121111/myblog.git

cd myblog

python manage.py runserver
```
Open bowser and go to http://localhost:8000/


---


1. Post
- Users are able to modify their own posts (title, content, ?date_modified)
- title
- author: User
- date_posted
- content

2. User
- Users are able to modify their own info
- name
- email
- bio
- image

3. Profile
- Users are able to modify their own profile
- name
- email
- password
- bio
- image

3. Review
- post: Post
- author: User
- content
- date_posted
- date_modified

4. Like
- post: Post
- author: User
- value (1:like, 0:dislike)
- date_voted

5. API
- Post
- User
- Profile
- Review
- Like
