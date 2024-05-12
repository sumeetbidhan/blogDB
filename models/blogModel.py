from pydantic import BaseModel



class BlogModel(BaseModel):
    title: str
    sub_title: str
    content: str
    author: str
    tags: list[str] = []
    comments: list[str] = []



class CommentModel(BaseModel):
    text: str
    author: str


class PostLikeModel(BaseModel):
    post_id: str
    user_id: str
    is_liked: bool

class UpdateBlogModel(BaseModel):
    title: str = None
    sub_title: str = None
    content: str = None
    author: str = None
    tags: list[str] = []
