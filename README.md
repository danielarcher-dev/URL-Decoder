# URL-Decoder

Because I can't remember how to do things, I create sample projects for my future self.

This repo unquotes URLs:
unquote(encoded_string)

eg. turn quoted URL:
  https%3A%2F%2Fgithub.com%2Fdanielarcher-dev%2FURL-Decoder%2Fblob%2Fmain%2Furldecode.py

into unquoted URL:
  https://github.com/danielarcher-dev/URL-Decoder/blob/main/urldecode.py

Sample usage:
PS E:\Develop\URL-Decoder> python.exe .\urldecode.py -a "https%3A%2F%2Fgithub.com%2Fdanielarcher-dev%2FURL-Decoder%2Fblob%2Fmain%2Furldecode.py"
https://github.com/danielarcher-dev/URL-Decoder/blob/main/urldecode.py
PS E:\Develop\URL-Decoder>
 
