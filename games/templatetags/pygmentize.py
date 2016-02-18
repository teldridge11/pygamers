from pygments import highlight
from pygments.lexers import get_lexer_by_name
from django import template
from pygments.formatters.other import NullFormatter

register = template.Library()

@register.tag(name='code')
def do_code(parser,token):
    code = token.split_contents()[-1]
    nodelist = parser.parse(('endcode',))
    parser.delete_first_token()
    return CodeNode(code,nodelist)
    
class CodeNode(template.Node):
    def __init__(self,lang,code):
        self.lang = lang
        self.nodelist = code
        
    def render(self,context):
        code = self.nodelist.render(context)
        lexer = get_lexer_by_name('python')
        return highlight(code,lexer,NullFormatter())