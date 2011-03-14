class Responses:
    def __init__(self):
        self.GET = dict()
        self.GET['/'] = ('{ "isRoot": true }', {'isRoot': True})
        self.GET['/widget'] = ('{"widget":{"debug": "on","window": { "title": "Sample Konfabulator Widget",        "name": "main_window",        "width": 500,        "height": 500    },    "image": {        "src": "Images/Sun.png",        "name": "sun1",        "hOffset": 250,        "vOffset": 250,        "alignment": "center"    },    "text": {        "data": "Click Here",        "size": 36,        "style": "bold",        "name": "text1",        "hOffset": 250,        "vOffset": 100,        "alignment": "center",        "onMouseUp": "sun1.opacity = (sun1.opacity / 100) * 90;"    }}}    '
                               , {'widget': {'debug': 'on', 'text': {'vOffset': 100, 'style': 'bold', 'name': 'text1', 'hOffset': 250, 'onMouseUp': 'sun1.opacity = (sun1.opacity / 100) * 90;','data': 'Click Here', 'alignment': 'center', 'size': 36}, 'window': {'width': 500, 'height': 500, 'name': 'main_window', 'title': 'Sample Konfabulator Widget'}, 'image': {'vOffset': 250, 'src': 'Images/Sun.png', 'alignment': 'center', 'name': 'sun1', 'hOffset': 250}}}
                               )
        self.GET['/book'] = ('{ "glossary": { "title": "example glossary", "GlossDiv": { "title": "S", "GlossList": { "GlossEntry": { "ID": "SGML", "SortAs": "SGML", "GlossTerm": "Standard Generalized Markup Language", "Acronym": "SGML", "Abbrev": "ISO 8879:1986", "GlossDef": { "para": "A meta-markup language, used to create markup languages such as DocBook.", "GlossSeeAlso": ["GML", "XML"] }, "GlossSee": "markup" } } } } }'
                             , {'glossary': {'GlossDiv': {'GlossList': {'GlossEntry': {'GlossDef': {'GlossSeeAlso': ['GML', 'XML'], 'para': 'A meta-markup language, used to create markup languages such as DocBook.'}, 'GlossSee': 'markup', 'Acronym': 'SGML', 'GlossTerm':'Standard Generalized Markup Language', 'Abbrev': 'ISO 8879:1986', 'SortAs': 'SGML', 'ID': 'SGML'}}, 'title': 'S'}, 'title': 'example glossary'}} 
                             )
        self.GET['/menu/svg?hasNull=true'] = ('{"menu": { "header": "SVG Viewer", "items": [ {"id": "Open"}, {"id": "OpenNew", "label": "Open New"}, null, {"id": "ZoomIn", "label": "Zoom In"}, {"id": "ZoomOu t", "label": "Zoom Out"}, {"id": "OriginalView", "label": "Original View"}, null , {"id": "Quality"}, {"id": "Pause"}, {"id": "Mute"}, null, {"id": "Find", "label": "Find..."}, {"id": "FindAgain", "label": "Find Again"}, {"id": "Copy"}, {"id": "CopyAgain", "label": "Copy Again"}, {"id": "CopySVG", "label": "Copy SVG"},{"id": "ViewSVG", "label": "View SVG"}, {"id": "ViewSource", "label": "View Source"}, {"id": "SaveAs", "label": "Save As"}, null, {"id": "Help"}, {"id": "About", "label": "About Adobe CVG Viewer..."} ] }}'
                                              , {'menu': {'header': 'SVG Viewer', 'items': [{'id': 'Open'}, {'id': 'OpenNew', 'label': 'Open New'}, None, {'id': 'ZoomIn', 'label': 'Zoom In'}, {'id': 'ZoomOu t', 'label': 'Zoom Out'}, {'id': 'OriginalView', 'label': 'Original View'}, None, {'id': 'Quality'}, {'id': 'Pause'}, {'id': 'Mute'}, None, {'id': 'Find', 'label': 'Find...'}, {'id': 'FindAgain', 'label': 'Find Again'}, {'id': 'Copy'}, {'id': 'CopyAgain', 'label': 'Copy Again'}, {'id': 'CopySVG', 'label': 'Copy SVG'}, {'id': 'ViewSVG', 'label': 'View SVG'}, {'id': 'ViewSource', 'label': 'View Source'}, {'id': 'SaveAs', 'label': 'Save As'}, None, {'id': 'Help'}, {'id': 'About', 'label': 'About Adobe CVG Viewer...'}]}}                                           
                                              )
        
        self.ARGS = dict()
        self.ARGS['{ "one" : True }'] = {'args': {'one': True}}
        self.ARGS['{"one":True, "two":3}'] = {'args': {'two': 3, 'one': True}}
        self.GET['/has/args?one=True'] = ('{ "args": { "one" : true } }', {'args': {'one': True}})
        self.GET['/has/args?one=True&two=3'] = ('{"args":{"one":true, "two":3}}', {'args': {'two': 3, 'one': True}})
        self.GET['/has/args?two=3&one=True'] = ('{"args":{"one":true, "two":3}}', {'args': {'two': 3, 'one': True}})
        
        self.GET_TEST = dict()
        self.GET_TEST['/unterminatedJSON'] = ('{', )
        self.GET_TEST['/overterminatedJSON'] = ('{ "isRoot": true }}', )
        self.GET_TEST['/noJSON'] = ('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"><html xmlns="http://www.w3.org/1999/xhtml"> ', )