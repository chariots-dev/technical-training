{
    "name": "Estate",  # The name that will appear in the App list
    "version": "1.0.0",  # Version
    "application": True,  # This line says the module is an App, and not a module
    "depends": ["base"],  # dependencies
    "data": [
        # views
        "views/estate_menus.xml",
        "views/real_estate_views.xml",

        # security
        "security/res_groups.xml",
        "security/ir.model.access.csv",
    ],
    "demo": [
        "demo/demo.xml",
    ],
    "installable": True,
    'license': 'LGPL-3',
}
