import os

from flask import Flask, session
from flask import Flask, render_template, request
from flask_session import Session



def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    
    
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev",
        # store the database in the instance folder
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )
    Session(app)
    app.config['SESSION_TYPE'] = 'filesystem'

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        session['score'] = 0

        return render_template('index.html')

    #This function is the way you will change your score
    def button_clicking(intro_text, a_text,b_text,c_text, a_score_change, b_score_change, c_score_change, message, go_to_this_html_page):
        if request.method == "POST":
            print("post")
            if request.form.get("submit_a"):
                session['score'] = session['score']+a_score_change
                print('a')

            elif request.form.get("submit_b"):
                session['score'] = session['score']+b_score_change
                print('b')

            elif request.form.get("submit_c"):
                session['score'] = session['score']+c_score_change
                print('c')

            else:
                print("MAJOR ISSUE ARRISING!!")
                pass

            session['intro_text'] = intro_text
            session['choice_a_text'] = a_text
            session['choice_b_text'] = b_text
            session['choice_c_text'] = c_text
            session['go_to_this_html_page'] = go_to_this_html_page
            print('message: ', message)
            print('new score: ', session['score'])
            

        elif request.method == "GET":
            print("Get")



    @app.route("/classic_mode",methods=['GET', 'POST'])
    def original():
        #First Question
        session['intro_text'] = "You fell asleep in the library and you suddenly find yourself late to Miss Misa's class! What are you going to do!?"
        session['choice_a_text'] = 'Start running to class'
        session['choice_b_text'] = 'Keep sleeping'
        session['choice_c_text'] = 'Roam the hallway'
        session['go_to_this_html_page'] = 'classic_mode.html'
        print("Message: Q1")
        
        
        #Change the score depending on whether you clicked a, b, or c using the button_clicking function
        #Change the text when clicked using the button_clicking function
        #Second Question
        new_intro_text =  "Mr. Seney sees you running in the hallway..!!!."
        new_a_text = "Speed up! Hope he doesn't catch me!!"
        new_b_text = 'Stop... slow down and walk'
        new_c_text = 'Wave and smile as you fast walk past him.'
        message = 'Q2'
        html_page = 'classic_mode_r1.html'


        button_clicking(new_intro_text, new_a_text, new_b_text, new_c_text, 1,2,3, message, html_page)
        
        return render_template(session['go_to_this_html_page'], intro = session['intro_text'], a_text = session['choice_a_text'], b_text = session['choice_b_text'], c_text = session['choice_c_text']) 

    @app.route("/classic_mode_2", methods=['GET','POST'])
    def classic_mode2():
        #Change the score depending on whether you clicked a, b, or c using the button_clicking function
        #Change the text when clicked using the button_clicking function
        #Third Question
        new_intro_text =  'Your friends call you asking where you are at...'
        new_a_text = "You tell them to not worry about it!"
        new_b_text = 'Slowly start walking to class'
        new_c_text = 'Try to meet them in the lunch room'
        message = 'Q3'
        html_page = 'classic_mode_r2.html'
        
        button_clicking(new_intro_text, new_a_text, new_b_text, new_c_text, 3,4,5, message,  html_page)

        print(session['intro_text'])
        print(session['go_to_this_html_page'])



        return render_template(session['go_to_this_html_page'], intro = session['intro_text'], a_text = session['choice_a_text'], b_text = session['choice_b_text'], c_text = session['choice_c_text']) 



    @app.route("/classic_mode_3", methods=['GET','POST'])
    def classic_mode3():
    #Change the score depending on whether you clicked a, b, or c using the button_clicking function
    #Change the text when clicked using the button_clicking function
    #Fourth Question
        new_intro_text =  "Mrs. Durbin finds you!? Now what!?"
        new_a_text = 'RUUUNNNN!!!'
        new_b_text = 'Smile and wave????'
        new_c_text = 'Try to make small talk'
        message = 'Q4'
        html_page = 'classic_mode_r3.html'
        
        button_clicking(new_intro_text, new_a_text, new_b_text, new_c_text, 7,9,11, message,  html_page)

        
        
        print(session['intro_text'])
        
        return render_template(session['go_to_this_html_page'], intro = session['intro_text'], a_text = session['choice_a_text'], b_text = session['choice_b_text'], c_text = session['choice_c_text']) 

    @app.route("/classic_mode_4", methods=['GET','POST'])
    def classic_mode4():
        score = session['score']
    #Change the score depending on whether you clicked a, b, or c using the button_clicking function
    #Change the text when clicked using the button_clicking function
    #Third Question
        new_intro_text =  'Someone hands you a squishy and tells you to hide it'
        new_a_text = 'Ignore them and keep heading to class'
        new_b_text = "Run to hide it in Mr. Seney's office"
        new_c_text = 'Take it and head back to the library'
        message = 'Q5'
        html_page = 'end_screen.html'
        
        button_clicking(new_intro_text, new_a_text, new_b_text, new_c_text, 3,4,5, message,  html_page)
        
        print(session['intro_text'])
        
        return render_template(session['go_to_this_html_page'], intro = session['intro_text'], a_text = session['choice_a_text'], b_text = session['choice_b_text'], c_text = session['choice_c_text']) 



    @app.route("/end_screen/", methods=['POST'])
    def ending():  
        score = session['score']
        if score < 14:
            last_scene = render_template('end_screen.html', ending_text = 'Sorry, you got in trouble anyway...')
        elif score == 15 or score == 16 or score == 17:
            last_scene = render_template('end_screen.html', ending_text = 'I have no idea but you escaped!!!!')
        else:
            last_scene = render_template('end_screen.html', ending_text = "Uhhh.. You just got yourself suspended...")

        return last_scene


    


    # register the database commands
    from flaskr import db

    db.init_app(app)

    # apply the blueprints to the app
    from flaskr import auth, blog

    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)

    # make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
   # app.add_url_rule("/", endpoint="index")


    sess = Session()
    sess.init_app(app)

    return app








#helpful websites
#https://stackoverflow.com/questions/15557392/how-do-i-display-images-from-google-drive-on-a-website
#https://unsplash.com/images/stock/blogging
#https://getbootstrap.com/docs/3.3/components/#btn-groups
#https://www.w3schools.com/bootstrap/bootstrap_theme_me.asp
#https://stackoverflow.com/questions/42601478/flask-calling-python-function-on-button-onclick-event