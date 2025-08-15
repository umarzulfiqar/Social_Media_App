<h1>Social_media_App</h1>
Step 1: User Management
Step 2: Posts
Step 3: News Feed
Step 4: Comments

<h2>Step 1 Explaination:</h2>
I used Django default with some additional fields like (bio,avatar) and make OnetoOnefield with defult user.
Use JWT Authencation when user loged in.
-> User registration (sign up)
-> User login (token obtain)
-> User profile retrieval and update
<h3>Follow Unfollow User</h3>
User can follow and unfollow other user and can not follow him/her self
<h2>Follow Model</h2>
id (uuid)
follower (ForeginKey with user)
following (ForeginKey with user)
created_at (DateandTimestamp)

<h2>Step 2 Explaination:</h2>
<h4>Post Model Design</h4>
Post's content (text)
Images upload (Image Field)
Post author(Foregin  key)
Timestamp fields (created_at)

<h2>Step 3 Explaination:</h2>
User can see only followed user's post
Uses "Follow" model and check following of curret loged in user in the following column

<h2>Step 4 Explaination:</h2>
<h4>Comments Model Design</h4>
id (uuid)
post (ForeignKey with Post)
user (ForeignKey User)
content (Text)
created_at (DateTimeField)

Only that user can delete comment which is current loged in nd owner of comment.
Anyone can add comment of anyone's post