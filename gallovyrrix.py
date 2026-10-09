import curses,random,string
from ui import put,run
WORDS=('planet','circuit','window','tunnel','orchard','lantern','bicycle','volcano','penguin','puzzle','compass','blanket','harbor','rocket','garden','silver','mystery','thunder','castle','forest')
class Game:
 def __init__(self,word):
  word=word.strip().lower()
  if not 3<=len(word)<=24 or any(c not in string.ascii_lowercase for c in word):raise ValueError('Use 3-24 English letters, no spaces.')
  self.word=word;self.guesses=set()
 @property
 def wrong(self):return sorted(self.guesses-set(self.word))
 @property
 def won(self):return set(self.word)<=self.guesses
 @property
 def lost(self):return len(self.wrong)>=6
 def guess(self,c):
  c=c.lower()
  if len(c)!=1 or c not in string.ascii_lowercase or self.won or self.lost:return False
  if c in self.guesses:return False
  self.guesses.add(c);return True
 def shown(self):return ' '.join(c.upper() if c in self.guesses else '_' for c in self.word)
def word_entry(s):
 value='';error=''
 while True:
  s.erase();h,w=s.getmaxyx();put(s,1,2,'SECOND PLAYER: guesser must look away',curses.A_BOLD);put(s,3,2,'Secret word: '+'*'*len(value));put(s,5,2,'3-24 letters. Enter accepts; Esc cancels.');put(s,7,2,error);s.refresh();k=s.get_wch()
  if k=='\x1b':return None
  if k in ('\n','\r'):
   try:Game(value);s.erase();s.refresh();return value
   except ValueError as e:error=str(e)
  elif k in ('\x7f','\b',curses.KEY_BACKSPACE):value=value[:-1]
  elif isinstance(k,str) and k.lower() in string.ascii_lowercase and len(k)==1 and len(value)<24:value+=k.lower()
def draw(s,g):
 s.erase();h,w=s.getmaxyx()
 if h<20 or w<58:put(s,0,0,'Resize to at least 58x20. Esc exits.');s.refresh();return
 put(s,1,2,'G A L L O V Y R R I X',curses.A_BOLD);put(s,3,2,'Guess letters | F2 new round | Esc quit')
 n=len(g.wrong);cx=w//2;cy=6
 for y in range(cy,cy+9):put(s,y,cx-10,'██')
 put(s,cy,cx-10,'██████████████');put(s,cy+1,cx+2,'██');put(s,cy+9,cx-14,'████████████████████')
 if n>=1:put(s,cy+2,cx+1,'(O)',curses.color_pair(3))
 if n>=2:put(s,cy+3,cx+2,'█',curses.color_pair(3));put(s,cy+4,cx+2,'█',curses.color_pair(3))
 if n>=3:put(s,cy+3,cx,'/',curses.color_pair(3))
 if n>=4:put(s,cy+3,cx+4,'\\',curses.color_pair(3))
 if n>=5:put(s,cy+5,cx+1,'/',curses.color_pair(3))
 if n>=6:put(s,cy+5,cx+3,'\\',curses.color_pair(3))
 word=g.shown();put(s,h-4,max(2,(w-len(word))//2),word,curses.A_BOLD)
 put(s,h-3,2,'Wrong: '+' '.join(g.wrong).upper()+'  |  '+str(6-n)+' chances left')
 put(s,h-2,2,'You won! F2 for another round.' if g.won else 'Word: '+g.word.upper()+'. F2 for another round.' if g.lost else 'Type one letter. Repeated guesses cost nothing.');s.refresh()
def loop(s):
 while True:
  s.erase();put(s,2,2,'G A L L O V Y R R I X',curses.A_BOLD);put(s,5,2,'1 Random offline word');put(s,7,2,'2 Another person chooses (hidden input)');put(s,9,2,'Q Quit');s.refresh();k=s.get_wch()
  if k in ('q','Q'):return
  if k not in ('1','2'):continue
  word=random.choice(WORDS) if k=='1' else word_entry(s)
  if not word:continue
  if k=='2':
   s.erase();put(s,4,2,'Word is hidden. Pass the terminal to the guesser.');put(s,6,2,'Press Enter when ready.');s.refresh()
   while s.get_wch() not in ('\n','\r'):pass
  g=Game(word)
  while True:
   draw(s,g);k=s.get_wch()
   if k=='\x1b':return
   if k==curses.KEY_F2:break
   h,w=s.getmaxyx()
   if h>=20 and w>=58 and isinstance(k,str):g.guess(k)
if __name__=='__main__':raise SystemExit(run(loop))
