# gallovyrrix

Original offline fullscreen hangman. Choose a random word from the bundled English list, or have another person type a word in masked entry. The guesser should look away during setup; the screen is cleared before handoff. Masking is a game mechanic, not encryption or protection against someone reading process memory.

Type letters to guess. Six wrong letters loses; repeated guesses cost nothing. F2 starts a new round, Esc quits. Q and R are valid guesses during play. Word entry accepts 3-24 English letters without spaces. Resize to at least 58x20 to play.

Python 3 and curses, no pip dependencies, desktop, account, or network needed. Installation checks requirements and stops with the real Python error if they are missing; it does not silently install packages.

```sh
bash app-store.sh install
bash app-store.sh run
python3 -m unittest -v
```

Linux tests and actual terminal secret-entry/gameplay/resize/restoration checks pass. Physical Raspberry Pi and non-Linux systems are untested.
