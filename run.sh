cd ./Vue/ || exit
concurrently "npm run dev" "python ../Django/manage.py runserver"