# BMEAS-wa
BMEAS Web App Resources.

To run this website on localhost // MacOS X or Linux:

1. Install __Python 3.7.6__ (or a newer version) and set up __pip__: In terminal, type 

`python3.7 get-pip.py`

3. Create virtual environment __in the directory of application.py__ (navigate there with `cd /dir/...`: In terminal, type

  `python3.7 -m venv .env`
  
   `source .env/bin/activate`
   
3. Install __requirements.txt__: In terminal, type

`pip install -r requirements.txt`

4. Run flask with `flask run`

5. View web app in announced address on terminal (typically [http://127.0.0.1:5000/](http://127.0.0.1:5000/))

6. `CTRL C` in terminal to quit flask 

HTML files extend from __aa_layout.html__ (with Jinja, these define the left bar of the website). HTML files can be found in __/templates__ directory. 
