# config.py

import os

class Config:
    SECRET_KEY = '1234567890'  
    # Replace with a random secret key
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
   # or 'postgresql://ashish:aaaaa3960@localhost:5433/tasklistdb'
     
    # postgresql://tasklist_96z4_user:nGAzQs8qbzQwnpEDCXCjRu1fgkC9v81y@dpg-cpukosmehbks73ejkr80-a.oregon-postgres.render.com/tasklist_96z4
    # postgresql://tasklist_96z4_user:nGAzQs8qbzQwnpEDCXCjRu1fgkC9v81y@dpg-cpukosmehbks73ejkr80-a.oregon-postgres.render.com/tasklist_96z4
    SQLALCHEMY_TRACK_MODIFICATIONS = False





'postgresql://taskuser:taskpassword@localhost/tasklistdb'