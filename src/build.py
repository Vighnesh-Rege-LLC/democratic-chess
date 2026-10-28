import os
HERE=os.path.dirname(os.path.abspath(__file__))
ROOT=os.path.dirname(HERE)
game=open(os.path.join(HERE,'game.html')).read()
reel=open(os.path.join(HERE,'intro-reel.html')).read()
assert '<!--' not in reel
esc=reel.replace('</script','<\\/script')
page=game.replace('__INTRO__',esc,1)
head='''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta property="og:title" content="Democratic Chess">
<meta property="og:description" content="The monarchy is abolished. The Citizens have opinions. Play it.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://chess.apps.vighneshrege.com/">
<meta name="theme-color" content="#1C2333">
'''
os.makedirs(os.path.join(ROOT,'public'),exist_ok=True)
open(os.path.join(ROOT,'public','index.html'),'w').write(head+page+'\n</html>\n')
print('built public/index.html',len(page))
