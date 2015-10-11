# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

class candidat(osv.Model):
	_name='hr_rec.candidat'
	_description="Informations du Candidat"

	
	_columns = {
		'name': fields.many2one('res.partner', 'Nom', required=True),#related
		'situation': fields.selection([('Nouveau','Nouveau'), ('RDV Thechnique','RDV Technique'), ('RDV RH','RDV RH'), ('Disqualifie','Disqualifie'), ('Annulation','Annulationn'), ('Recrut sur mission','Recrut sur mission'), ('Proposition faite','Proposition faite'), ('Contrat signe','Contrat signe')],string='Situation'),
		'fonction': fields.selection(string="Fonctions", selection=[('Consultant','Consultant'),('CP','CP'),('IED','IED')]),
		'mobilite': fields.selection(string="Mobilité", selection=[('local','Local'),('Region','Region'),('Pays','Pays'),('Continent','Continent'),('Monde','Monde')]),
		'date_disp': fields.date(string="Disponibilité"),
		'permet_cond': fields.selection(string="Permet de conduite", selection=[('Aucun','Aucun'),('Categorie A','Categorie A'),('Categorie B','Categorie B')]),
		'cand_cont_id': fields.many2one('hr_rec.contrat', 'Contrat'),
		'cand_dom_ids': fields.many2many('hr_rec.cand_dom', 'hr_rec_cand_dom_rel','cand_id', 'dom_id', 'Domaines'),
		'cand_log_ids': fields.many2many('hr_rec.cand_log', 'hr_rec_cand_log_rel','cand_id', 'log_id', 'Logiciels'),#essayer one2many
		'cand_lang_ids': fields.many2many('hr_rec.cand_lang', 'hr_rec_cand_lang_rel','cand_id', 'lang_id', 'Langues'),
		'cand_lang_prog_ids': fields.many2many('hr_rec.cand_lang_prog', 'hr_rec_cand_lang_prog_rel','cand_id', 'lang_prog_id', 'Langages de programmation'),
	}
	

class contrat(osv.Model):
	_name='hr_rec.contrat'
	_description='cette classe contient les differents types contrats'

	_columns={
		'name': fields.char(string="Type de contrat", size=50, required=True),
		'description': fields.text(string='Description'),
	}
	
	_sql_constraints = [
	('uniq_name','unique(name)','Ce type de contrat existe déja ! ')
	]

class domaine(osv.Model):
	_name='hr_rec.domaine'
	_description='Les domaines '

	_columns = {
		'name': fields.char(string='Domaine', size=100, required=True),
		
	}

	_sql_constraints = [
	('uniq_name','unique(name)','Le domaine existe déja ! ')
	]

class cand_dom(osv.Model):
	_name='hr_rec.cand_dom'
	_description='relation entre un candidta et ses domaines'
	_rec_name='domaine'

	_columns = {

		'domaine': fields.many2one('hr_rec.domaine', 'Domaines'),#changer a many2many
		'niveau': fields.selection(string="Niveau", selection=[('Theorie','Theorie'),('Connaissances','Connaissances'),('Pratique','Pratique'),('Maitrise','Maitrise'),('Expert','Expert')]),	
		'annee_exp': fields.integer(string='Annees d\'experience', digits=(,), required=False),
		
	}

class logiciel(osv.Model):
	_name='hr_rec.logiciel'
	_description='Les logiciels '

	_columns = {
		'name': fields.char(string='Logiciels', size=100, required=True),
		
	}

	_sql_constraints = [
	('uniq_name','unique(name)','Le logiciel existe déja ! ')
	]

class cand_log(osv.Model):
	_name='hr_rec.cand_log'
	_description='relation entre un candidat et ses logiciels'
	_rec_name='logiciel'

	_columns = {

		'logiciel': fields.many2one('hr_rec.logiciel', 'Logiciel'),
		'niveau': fields.selection(string="Niveau", selection=[('Theorie','Theorie'),('Connaissances','Connaissances'),('Pratique','Pratique'),('Maitrise','Maitrise'),('Expert','Expert')]),
	}
class langue(osv.Model):
	_name='hr_rec.langue'
	_description='Les langues '

	_columns = {
		'name': fields.char(string='Langues', size=100, required=True),
		
	}

	_sql_constraints = [
	('uniq_name','unique(name)','Cette Langue existe déja ! ')
	]

class cand_lang(osv.Model):
	_name='hr_rec.cand_lang'
	_description='relation entre un candidat et les langues'
	_rec_name='langue'

	_columns = {

		'langue': fields.many2one('hr_rec.langue', 'Langue'),
		'niveau': fields.selection(string="Niveau", selection=[('Scolaire', 'Scolaire'), ('Debutant', 'Débutant'), ('Avancé','Avancé'), ('Courant','Courant'), ('Bilingue','Bilingue')] ),
	}
class langage_prog(osv.Model):
	_name='hr_rec.langage_prog'
	_description='Les langages de programmation'

	_columns = {
		'name': fields.char(string='Langages de programmation', size=100, required=True),
		
	}

	_sql_constraints = [
	('uniq_name','unique(name)','Cette Langue existe déja ! ')
	]

class cand_lang_prog(osv.Model):
	_name='hr_rec.cand_lang_prog'
	_description='relation entre un candidat et les langage de programmation'
	_rec_name='lang_prog'

	_columns = {

		'lang_prog': fields.many2one('hr_rec.langage_prog', 'Langage de programmation'),
		'niveau': fields.selection(string="Niveau", selection=[('Theorie','Theorie'),('Connaissances','Connaissances'),('Pratique','Pratique'),('Maitrise','Maitrise'),('Expert','Expert')]),
	}