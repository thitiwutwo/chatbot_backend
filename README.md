# chatbot_backend
ทีม 7 
# เริ่มต้น
### ติดตั้ง
1. สร้างโฟล์เดอร์สำหรับการ Clone Project
2. Clone repository ไปที่เครื่อง.
    ``````````
    git clone https://github.com/thitiwutwo/chatbot_backend.git
    ``````````
3. เปิด command line เพื่อเข้าสู่โฟล์เดอร์ของ project ที่โคลนมา
    ``````````
    // command line
    cd your/clone/project
    ``````````
4. ใช้คำสั่งเพื่อติดตั้ง virtual environment ของ python
    ``````````
    // command line
    python -m venv venv
    ``````````
5. เปิด virtual environment
    ``````````
    // command line
    venv\Script\active
    ``````````
6. ติดตั้ง django และ rest api
    ``````````
    // command line
    pip install django djangorestframework
    ``````````
7. สร้างฐานข้อมูล และ import ข้อมูล
    ``````````
    // command line
    cd chatbot_backend
    python manage.py migrate
    python manage.py makemigrations
    python manage.py createsuperuser
    //จะมีให้กรอก username email(สามารถข้ามได้โดยกด enter ไปเลย) password
    python manage.py loaddata db.json
    ``````````
8. เริ่มต้นโปรแกรม
    ``````````
    // command line
    python manage.py runserver
    ``````````
### การ export ข้อมูล
##### สำหรับต้องการเก็บข้อมูลไว้เป็นข้อมูลเริ่มต้นเช่น บัญชี admin
    ``````````
    // command line
    python manage.py dumpdata > db.json
    ``````````
### การ commit code
1. สร้าง branch สำหรับ push งาน (หรือจะใช้ git desktop ก็ได้)
    ``````````
    git checkout -b <branch-name>
    ``````````
2. เพิ่มไฟล์ที่จะ push เข้า git
    ``````````
    git add .
    ``````````
3. เพิ่ม comment
    ``````````
    git commit -m "this is a comment"
    ``````````
4. push งาน
    ``````````
    git push origin <branch-name>
    ``````````

# Authors
Thitiwut Wongsa - Initial work