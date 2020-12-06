# bildserver
Simple Django server for uploading pictures

# Windows:

## open cmd and run:
git clone https://github.com/knivdanne/bildserver

cd bildserver <br>
env\Scripts\activate.bat <br>
python manage.py runserver <br>


## open webbrowser and navigate to:
http://127.0.0.1:8000/bilder/ <br>
Choose picture and put name (later version will be select multiple pictures and no name) <br>
press Upload. <br>

## The picture should appear here:
bildserver\media\pictures

## To run server accessible by other devices on network, run ipconfig and check your ipv4 address
add your address to ALLOWED_HOSTS in bildserver/mysite/settings.py <br>
then run <br>
python manage.py runserver YOUR_IP_ADDRESS:80 <br>
you should now be able to access from other devices on YOUR_IP_ADDRESS/bilder

