from fastapi import APIRouter, HTTPException
from models.blogModel import BlogModel, CommentModel, PostLikeModel, UpdateBlogModel
from config.config import blogs_collection
import datetime
from datetime import date 
from serializers.blogDataModel import DecodeBlog, DecodeBlogs, DecodeComment, DecodePostLike
from bson import ObjectId



blog_root = APIRouter()

# Create a new blog
@blog_root.post("/blog")
def post_new_blog(doc: BlogModel): 
    doc = dict(doc)
    current_date = datetime.date.today()
    doc["date"] = str(current_date)
    
    res =  blogs_collection.insert_one(doc)

    doc_id = str(res.inserted_id)

    return{
        "status" : "ok",
        "message" : "Blog posted successfully",
        "_id" :  doc_id
    }

# Create a new comment
@blog_root.post("/comment/{post_id}")
def post_new_comment(post_id: str, comment: CommentModel):
    # Check if the blog exists
    blog = blogs_collection.find_one({"_id": ObjectId(post_id)})
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")

    # Create the comment
    comment_data = comment.dict()
    comment_data["timestamp"] = str(date.today())  # Add timestamp

    res = blogs_collection.insert_one(comment_data)
    comment_id = str(res.inserted_id)

    # Update the BlogModel with the new comment ID
    blogs_collection.update_one(
        {"_id": ObjectId(post_id)},
        {"$push": {"comments": comment_id}}
    )

    return {
        "status": "ok",
        "message": "Comment posted successfully",
        "_id": comment_id
    }


# Like or dislike a post
@blog_root.post("/blog/like")
def like_post(like_data: PostLikeModel):
   
    post_id = like_data.post_id
    user_id = like_data.user_id
    like_status = like_data.like_status  # True for like, False for dislike

    # Check if the user has already liked/disliked this post to toggle the status
    existing_like = blogs_collection.find_one({"_id": post_id, "likes.user_id": user_id})

    if existing_like:
        # User already liked/disliked, update the status
        blogs_collection.update_one(
            {"_id": post_id, "likes.user_id": user_id},
            {"$set": {"likes.$.like_status": like_status}}
        )
    else:
        # User is liking/disliking for the first time
        blogs_collection.update_one(
            {"_id": post_id},
            {"$push": {"likes": {"user_id": user_id, "like_status": like_status}}}
        )

    # Fetch the updated post data
    updated_post = blogs_collection.find_one({"_id": post_id})

    return {
        "status": "ok",
        "message": "Post liked/disliked successfully",
        "updated_post": updated_post
    }

#get a blog
@blog_root.get("/blog/{post_id}")
def get_blog(post_id: str):
   # Check if the blog exists
    blog = blogs_collection.find_one({"_id": ObjectId(post_id)})
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")

    decoded_data =  DecodeBlog(blog)

    return {
        "status" : "ok",
        "data" : decoded_data
    }


#getting blogs
@blog_root.get("/blog/")
def get_all_blogs():
    res = blogs_collection.find()    
    decoded_data = DecodeBlogs(res)

    return {
        "status" : "ok",
        "data" : decoded_data
    }


#update blog
@blog_root.patch("/blog/{_id}")
def update_blog(_id: str, doc:UpdateBlogModel):
    req = dict(doc.model_dump(exclude_unset=True))

    blogs_collection.find_one_and_update(
        {
            "_id": ObjectId(_id)
        },
        {
            "$set": req
        },
        upsert=False
    )

    return {
        "status": "ok",
        "message": "blog updated successfully"
    }

#delete blog
@blog_root.delete("/blog/{_id}")
def delete_blog(_id: str):
    result = blogs_collection.find_one_and_delete(
        {
            "_id": ObjectId(_id)
        }
    )

    if result:
        return {"status": "ok", "message": "Blog deleted successfully"}
    else:
        return {"status": "error", "message": "Blog not found for deletion"}
