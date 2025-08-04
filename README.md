# Lost & Found Django Application

A Django web application for posting and managing lost and found items. Users can create accounts, post lost or found items with images, search through posts, and manage their own posts.

## Features

- **User Authentication**: Sign up, login, and logout functionality
- **Post Items**: Create posts for lost or found items with images
- **View Items**: Browse all posts on the homepage with search functionality
- **Item Details**: Detailed view of individual items
- **Manage Posts**: Users can view and delete their own posts
- **Search**: Search items by title, description, or location
- **Responsive Design**: Modern UI with Tailwind CSS

## Technology Stack

- **Backend**: Django 5.2.4
- **Database**: SQLite (default)
- **Frontend**: HTML with Tailwind CSS
- **Image Handling**: Pillow for image processing

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone or navigate to the project directory**
   ```bash
   cd lostfound_pro
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Open your browser and go to `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## Usage

### For Users

1. **Sign Up**: Create a new account to start posting
2. **Post Items**: 
   - Click "Post Lost Item" to report something you lost
   - Click "Post Found Item" to report something you found
3. **Browse**: View all posts on the homepage
4. **Search**: Use the search bar to find specific items
5. **Manage**: View and delete your own posts from "My Posts"

### For Administrators

- Access the admin panel at `/admin/` to manage all posts and users
- View, edit, or delete any post
- Manage user accounts

## Project Structure

```
lostfound_pro/
├── lostfound_app/          # Main application
│   ├── models.py           # Database models
│   ├── views.py            # View functions
│   ├── forms.py            # Form classes
│   ├── urls.py             # URL patterns
│   ├── admin.py            # Admin configuration
│   └── templates/          # HTML templates
│       └── lostfound_app/
│           ├── base.html   # Base template
│           ├── home.html   # Homepage
│           ├── signup.html # Registration
│           ├── login.html  # Login
│           ├── post_lost.html   # Post lost item
│           ├── post_found.html  # Post found item
│           ├── item_detail.html # Item details
│           ├── my_posts.html    # User's posts
│           └── delete_confirm.html # Delete confirmation
├── lostfound_pro/          # Project settings
│   ├── settings.py         # Django settings
│   └── urls.py             # Main URL configuration
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Database Models

### Item Model
- `user`: Foreign key to User (who posted)
- `post_type`: Choice field ('lost' or 'found')
- `title`: Item title
- `description`: Detailed description
- `location`: Where item was lost/found
- `date`: Date when item was lost/found
- `image`: Optional image upload
- `created_at`: When post was created
- `updated_at`: When post was last updated

## Features in Detail

### User Authentication
- Session-based authentication
- User registration and login
- Secure password handling

### Post Management
- Create posts for lost or found items
- Upload images with posts
- Edit and delete own posts
- View all posts on homepage

### Search Functionality
- Search by title, description, or location
- Real-time search results
- Case-insensitive search

### Responsive Design
- Mobile-friendly interface
- Modern UI with Tailwind CSS
- Intuitive navigation

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please create an issue in the repository or contact the development team. 