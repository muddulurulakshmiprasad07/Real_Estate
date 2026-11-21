
#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
git add .
git commit -m "Prepare DreamHomes for deployment"
git push origin main