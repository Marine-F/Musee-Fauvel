from flask import render_template
from app import app


@app.route('/')
@app.route('/accueil')
def accueil():
    '''
    Route permettant d'afficher la page d'accueil
    '''
    user = {'username': 'Marine'}
    return render_template('accueil.html', title='Accueil', user=user)

@app.route('/catalogue')
def catalogue():
    '''
    Route permettant d'afficher les id des objets + leur type + la matière
    '''

@app.route('/objets/<int:id_objet>')
def objets():
    '''
    Route permettant d'afficher une fiche-objet sur laquelle figure les informations concernant cet objet
    '''

@app.route('')

@app.route('/bibliographie')
def bibliographie():
    '''
    Route permettant d'afficher la bibliographie du projet
    '''