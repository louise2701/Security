
## How to run the application

To run the application, you need to run the following commands, **in the first `fruiticart` directory (the one containing `manage.py`)**:
- `python create_database.py` (to create the database)
- `python manage.py migrate` (to create the tables in the database)
- `python manage.py load_data` (to load the data in the database)
- `python manage.py runserver` (to run the server)

Here an image of the commands to run, with the expected output:
![commands](captures/how_to_run.png)

Then, you can access the application at the following address: `http://127.0.0.1:8000/order/home` (in function of the port used by the server).

## How to use the application

To use the application, you need to create an account. Then, you can login and use the application. You can add products to your cart, and then order them. You can also see your orders and your profile.

There's also some accounts already created, the one to test the application is:
- email: *test@test*
- password: *test*

Don't hesitate to see the demo video to see how to use the application.

If you have any questions, you can contact us at the following address: *loevan.le_quernec@edu.devinci.fr*.

