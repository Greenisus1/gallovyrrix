import unittest
from gallovyrrix import Game
class Tests(unittest.TestCase):
 def test_hidden(self):self.assertEqual(Game('planet').shown(),'_ _ _ _ _ _')
 def test_case(self):g=Game('planet');g.guess('P');self.assertTrue(g.shown().startswith('P'))
 def test_repeat(self):g=Game('planet');g.guess('x');g.guess('x');self.assertEqual(len(g.wrong),1)
 def test_win(self):g=Game('planet');[g.guess(c) for c in 'planet'];self.assertTrue(g.won)
 def test_loss(self):g=Game('planet');[g.guess(c) for c in 'bcdfgh'];self.assertTrue(g.lost);self.assertFalse(g.guess('p'))
 def test_bad(self):
  for word in ('hi','two words','abc123','a'*25):
   with self.assertRaises(ValueError):Game(word)
if __name__=='__main__':unittest.main()
