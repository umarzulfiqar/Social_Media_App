<h1>Social_media_App</h1>
Step 1: User Management <br>
Step 2: Posts <br>
Step 3: News Feed <br>
Step 4: Comments <br>

<h2>Step 1 Explaination:</h2>
I used Django default with some additional fields like (bio,avatar) and make OnetoOnefield with defult user.
Use JWT Authencation when user loged in.
-> User registration (sign up) <br>
-> User login (token obtain) <br>
-> User profile retrieval and update <br>
<h3>Follow Unfollow User</h3>
User can follow and unfollow other user and can not follow him/her self
<h2>Follow Model</h2>
id (uuid) <br>
follower (ForeginKey with user) <br>
following (ForeginKey with user) <br>
created_at (DateandTimestamp) <br>

<h2>Step 2 Explaination:</h2>
<h4>Post Model Design</h4>
Post's content (text) <br>
Images upload (Image Field) <br>
Post author(Foregin  key) <br>
Timestamp fields (created_at) <br>

<h2>Step 3 Explaination:</h2>
User can see only followed user's post <br>
Uses "Follow" model and check following of curret loged in user in the following column <br>

<h2>Step 4 Explaination:</h2>
<h4>Comments Model Design</h4>
id (uuid) <br>
post (ForeignKey with Post) <br>
user (ForeignKey User) <br>
content (Text) <br>
created_at (DateTimeField) <br>

Only that user can delete comment which is current loged in nd owner of comment. <br>
Anyone can add comment of anyone's post <br>