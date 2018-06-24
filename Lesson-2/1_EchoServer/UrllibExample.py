from urllib.parse import urlparse, parse_qs, quote, quote_plus, unquote

address = 'https://www.google.com/search?q=gray+squirrel&tbm=isch'
parts = urlparse(address)
# print(parts)
# print(parts.query)
query = parse_qs(parts.query)
print(query)
example = parse_qs('texture=fuzzy&animal=gray+squirrel')
print(example)
quoting = quote('/El Niño/')
print('quoting:' + quoting)
quoteplus = quote_plus('/El Niño/')
print('quote_plus: ' + quoteplus)
unquote = unquote('%0ap') #\n p
print('unquote: ' + unquote)