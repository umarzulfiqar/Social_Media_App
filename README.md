<h1>Social_Media_App</h1>
Step 1: User Management <br>
Step 2: Posts <br>
Step 3: News Feed <br>
Step 4: Comments <br>
Step 4: Like or Unlike Post <br>
<hr>
<h2 >Step 1 Explaination:</h2>
I used Django default with some additional fields like (bio,avatar) and make OnetoOnefield with defult user.
Use JWT Authencation when user loged in.<br>
-> User registration (sign up) <br>
-> User login (token obtain) <br>
-> User profile retrieval and update <br>
<h3>Follow Unfollow User:</h3>
User can follow and unfollow other user and can not follow him/her self
<h3>Follow Model:</h3>
id (uuid) <br>
follower (ForeginKey with user) <br>
following (ForeginKey with user) <br>
created_at (DateandTimestamp) <br>
<hr>
<h2>Step 2 Explaination:</h2>
<h3>Post Model Design:</h3>
Post's content (text) <br>
Images upload (Image Field) <br>
Post author(Foregin  key) <br>
Timestamp fields (created_at) <br>
<hr>
<h2>Step 3 Explaination:</h2>
User can see only followed user's post <br>
Uses "Follow" model and check following of curret loged in user in the following column <br>
<hr>
<h2>Step 4 Explaination:</h2>
<h3>Comments Model Design:</h3>
id (uuid) <br>
post (ForeignKey with Post) <br>
user (ForeignKey User) <br>
content (Text) <br>
created_at (DateTimeField) <br>
Only that user can delete comment which is current loged in nd owner of comment. <br>
Anyone can add comment of anyone's post <br>
<hr>
<h2>Step 4 Explaination:</h2>
I use post and logedin user as a ForeginKey in the model <br>
If the use already like the post it will toggle the change (delete to unlike)<br>
I use simple post method of APIView to get data from user <br>