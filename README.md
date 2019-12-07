# attractor_final_exam

Library application on Django Framework

### Installation
```bash
git clone https://github.com/qwanysh/attractor_final_exam.git
cd attractor_final_exam
virtualenv -p python3 venv  
source venv/bin/activate  
pip3 install -r requirements.txt
cd library
python3 manage.py migrate
python3 manage.py loaddata fixtures.json
unzip fixtures.zip

```

### Run server

```bash
source venv/bin/activate  
cd library   
python3 manage.py runserver  
```
