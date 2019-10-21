wait-for-it -h redis.service -p 6379 -t 60 -- echo 'Redis is UP'
wait-for-it -h mysql.service -p 3306 -t 60 -- echo 'MySQL is UP'
pipenv run  python dev.py migrate
pipenv run  python dev.py runserver 0.0.0.0:8000