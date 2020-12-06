# bildserver
Simple Django server for uploading pictures

# Windows:
git clone https://github.com/knivdanne/bildserver

open cmd and run:
cd bildserver
env\Scripts\activate.bat
python manage.py runserver

open webbrowser and navigate to:
http://127.0.0.1:8000/bilder/
Choose picture and put name (later version will be select multiple pictures and no name)
press Upload.

The picture should appear here:
bildserver\media\pictures

To run server accessible by other devices on network, run ipconfig and check your ipv4 address
add your address to ALLOWED_HOSTS in bildserver/mysite/settings.py
then run
python manage.py runserver YOUR_IP_ADDRESS:80

you should now be able to access from other devices on YOUR_IP_ADDRESS/bilder

