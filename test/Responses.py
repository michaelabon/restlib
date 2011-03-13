class Responses:
    def __init__(self):
        self.GET = dict()
        self.GET['/'] = ('{ "isRoot": true }', {'isRoot': True})
        self.GET['/sgml'] = \
            ("""{ "glossary": { "title": "example glossary", "GlossDiv": {  
            "title": "S","GlossList": {   "GlossEntry":{"ID": "SGML", "SortAs":
            "SGML",        "GlossTerm": "Standard Generalized Markup Language",
            "Acronym": "SGML",                    "Abbrev": "ISO 8879:1986",    
            "GlossDef":{"para": "A meta-markup language, used to create markup
            languages such as DocBook.", "GlossSeeAlso": ["GML", "XML"]},
            "GlossSee": "markup"}}}}}""",
            {'glossary': {'GlossDiv': {'GlossList': {'GlossEntry': {
            'GlossDef': {'GlossSeeAlso': ['GML', 'XML'], 'para'
                         : 'A meta-markup language, used to create markup languages such as DocBook.'
                         },
            'GlossSee': 'markup',
            'Acronym': 'SGML',
            'GlossTerm': 'Standard Generalized Markup Language',
            'Abbrev': 'ISO 8879:1986',
            'SortAs': 'SGML',
            'ID': 'SGML',
            }}, 'title': 'S'}, 'title': 'example glossary'}})
