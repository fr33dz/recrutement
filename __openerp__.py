# -*- coding: utf-8 -*-
{
    'name': "Recrutement_mlm",

    'summary': """
        gerer le recrutement facilement""",

    'description': """
        Ce module permet de gerer l'activité de recrutement ....
    """,

    'author': "MLMConseil",
    'website': "http://www.mlmconseil.fr",
    'sequence': 3,

    'category': 'HUMAN RESSOURCES',
    'version': '0.1',

    'depends': ['base','hr'],

    
    'data': [
        # 'security/ir.model.access.csv',
        'Recrutement_mlm.xml',
		
    ],
    
    'demo': [
        'demo.xml',
    ],
    'installable': True,
    #'application': False,
    'auto_install': False,
}