{
	"name" : "Ex1",
	"version" : "1.0",
	"author" : "Watcharapon Hongthong",
	"description": "This is a simple module used for testing",
	"init_xml" : [
	],
    'depends': ['base_setup', 'jasper_reports'],
	"demo_xml" : [],
    "data": [
        'view.xml',
        'report.xml',
        'security/ir.model.access.csv',
        'wizards/wizard_ex1.xml',
        ],
	"active": False,
	"installable": True
}
