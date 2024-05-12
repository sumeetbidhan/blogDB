
# FastAPI Blog API

This is a FastAPI-based RESTful API for managing a blog system. It allows users to create, read, update, and delete blog posts, comment on posts, and like/dislike them. The data is stored in a MongoDB database.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [API Endpoints](#api-endpoints)
- [Models](#models)
- [Serializers](#serializers)
- [Contributing](#contributing)


## Features

- Create, read, update, and delete blog posts
- Add comments to blog posts
- Like or dislike blog posts
- Retrieve all blog posts

## Technologies Used

- FastAPI: Python web framework for building APIs quickly
- MongoDB: NoSQL database for data storage
- Pydantic: Data validation and serialization library
- Docker: Containerization for easy deployment
- Git/GitHub: Version control and collaboration

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/sumeetbidhan/blogDB.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up MongoDB:
   - Install MongoDB locally or use a cloud-based service.
   - Update the MongoDB connection string in `config/config.py`.

4. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints

- `POST /new/blog`: Create a new blog post
- `POST /new/comment`: Add a comment to a blog post
- `POST /post/like`: Like or dislike a blog post
- `GET /all/blogs`: Retrieve all blog posts
- `PATCH /update/{_id}`: Update a blog post by ID
- `DELETE /delete/{_id}`: Delete a blog post by ID

For detailed API documentation, visit `http://localhost:8000/docs`.

## Models

- `BlogModel`: Represents a blog post with title, subtitle, content, author, and tags.
- `CommentModel`: Represents a comment with text and author.
- `PostLikeModel`: Represents a like or dislike action on a blog post.

## Serializers

- `DecodeBlog`: Serialize blog data for response
- `DecodeBlogs`: Serialize list of blogs for response
- `DecodeComment`: Serialize comment data for response
- `DecodePostLike`: Serialize like/dislike data for response

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

1. Fork the repository (`https://github.com/sumeetbidhan/blogDB/fork`)
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Create a new Pull Request



Feel free to modify and expand upon this template as needed to suit your project's specific details and requirements.

