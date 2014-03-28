cd /d ./emotionExtract/jieba
python setup.py install

cd ../../
cls
python manage.py runserver 127.0.0.1:80

pause