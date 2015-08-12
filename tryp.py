from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

lexer = get_lexer_by_name("haskell", stripall=True)
formatter = HtmlFormatter(linenos=True, cssclass="source")
result = highlight("./github/haskell/first.hs", lexer, formatter)
print result
