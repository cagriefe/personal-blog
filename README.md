# Personal Blog

This is a personal blog application built with Django. It allows users to create, read, update, and delete blog posts. Users can also leave comments on posts.

## Features

- User authentication (login, logout, register)
- Create, read, update, and delete blog posts
- Comment on blog posts
- Categorize and tag blog posts
- Responsive design
- Docker

### Prerequisites

- Docker
- Docker Compose

### Steps

1. Clone the repository:

```sh
git clone https://github.com/yourusername/personal-blog.git
cd personal-blog

docker-compose up --build

docker-compose run web python [manage.py](http://_vscodecontentref_/5) migrate

docker-compose run web python [manage.py](http://_vscodecontentref_/6) createsuperuser

docker-compose run web python [manage.py](http://_vscodecontentref_/7) collectstatic


Contributions are welcome! Please open an issue or submit a pull request.

This project is licensed under the GNU General Public License v3.0. See the LICENSE file for details.