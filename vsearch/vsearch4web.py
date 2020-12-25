from flask import Flask, render_template, request, session, copy_current_request_context, redirect, flash
from vsearch import search4letters
from DBcm import UseDatabase, ConnectionError, CredentialsError, SQLError
from checker import check_logged_in
from threading import Thread
from time import sleep

app = Flask(__name__)

app.config['dbconfig'] =  {
            'host' : '127.0.0.1',
            'user' : 'root',
            'password' : 'root',
            'database' : 'vsearchlogdb',
            }

@app.route('/search4', methods = ['POST'])
@check_logged_in
def do_search():
    
    @copy_current_request_context
    def log_request(req: 'flask_request', res: str, phrase: str):
        """Log details of the web request and the results."""
        try:
            sleep(5)
            with UseDatabase(app.config['dbconfig']) as cursor:
                _SQL = """insert into log
                    (phrase, letters, ip, browser_string, results)
                    values
                    (%s, %s, %s, %s, %s)"""
                cursor.execute(_SQL,(
                    phrase,
                    #req.form['phrase'],
                    req.form['letters'],
                    req.remote_addr,
                    req.user_agent.browser,
                    res, ))
            return 'No errors'
        except ConnectionError as err:
            print('Is your database switched on? Error:', str(err))
        except CredentialsError as err:
            print('User-id/Password issues. Error:', str(err))
        except SQLError as err:
            print('Is your query correct? Error:', str(err))
        except Exception as err:
            print('Something went wrong:', str(err))
        return 'Error'

    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results: '
    results = ''
    log_results = ''
    try:
        results = str(search4letters(phrase, letters))
        log_results = results
        t = Thread(target = log_request, args = (request, log_results, phrase))
        t.start()
    except Exception as err:
        log_results = str(err)
        phrase = str(err)
        print('Error:', str(err))
    return render_template('results.html',
                           the_phrase = request.form['phrase'],
                           the_letters = letters,
                           the_title = title,
                           the_results = results,)
                           
@app.route('/')
@app.route('/entry')
@check_logged_in
def entry_page():
    return render_template('entry.html', the_title = 'Welcome to search4letters on the web!')

@app.route('/viewlog')
@check_logged_in
def view_the_log():
    try:
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """select phrase, letters, ip, browser_string, results
            from log"""
            cursor.execute(_SQL)
            contents = cursor.fetchall()
            titles = ('Phrase', 'Letters', 'Remote address', 'User Agent', 'Results')     
            return render_template('viewlog.html',
                                    the_title = 'View log',
                                    the_row_titles = titles,
                                    the_data = contents,)
    except ConnectionError as err:
        print('Is your database switched on? Error:', str(err))
    except CredentialsError as err:
        print('User-id/Password issues. Error:', str(err))
    except SQLError as err:
        print('Is your query correct? Error:', str(err))
    except Exception as err:
        print('Something went wrong:', str(err))
    return 'Error'

app.secret_key = 'YouWillNeverGuessMySecretKey'

@app.route('/login')
def do_login():
    session['logged_in'] = True
    flash('You are now logged in')
    sleep(2)
    return redirect('/')

@app.route('/logout')
def do_logout():
    if 'logged_in' in session:
        session.pop('logged_in')
    return 'You are now logged out'

if __name__ == '__main__':
    app.run(debug = True)