def DecodeBlog(doc) -> dict:
    return {
        "_id": str(doc["_id"]),
        "title": doc["title"],
        "sub_title": doc["sub_title"],
        "content": doc["content"],
        "author": doc["author"],
        "tags": doc["tags"],
        "comments": doc["comments"],
    }

def DecodeComment(comment) -> dict:
    return {
        "_id": str(comment["_id"]),
        "text": comment["text"],
        "author": comment["author"],
    }

def DecodePostLike(post_like) -> dict:
    return {
        "_id": str(post_like["_id"]),
        "post_id": post_like["post_id"],
        "user_id": post_like["user_id"],
        "is_liked": post_like["is_liked"],
    }

#all blogs
def DecodeBlogs(docs) -> list:
    return[DecodeBlog(doc) for doc in docs]