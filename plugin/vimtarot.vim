if !has("python3")
  echo "vim has to be compiled with +python3 to run this"
  finish
endif

if exists('g:sample_python_plugin_loaded')
  finish
endif

let s:plugin_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')

python3 << EOF
import sys
from os.path import normpath, join
import vim
plugin_root_dir = vim.eval('s:plugin_root_dir')
python_root_dir = normpath(join(plugin_root_dir, '..', 'python'))
sys.path.insert(0, python_root_dir)
import vimtarot
EOF

let g:sample_python_plugin_loaded = 1

function! TarotCelticCross()
  python3 vimtarot.TarotCelticCross()
endfunction

function! TarotCelticCrossQuestion()
  python3 vimtarot.TarotCelticCrossQuestion() 
endfunction

function! TarotCharacter()
  python3 vimtarot.TarotCharacter() 
endfunction

function! TarotCharacterQuestion()
  python3 vimtarot.TarotCharacterQuestion() 
endfunction

function! TarotSimpleBeat()
  python3 vimtarot.TarotSimpleBeat() 
endfunction

function! TarotSimpleBeatQuestion()
  python3 vimtarot.TarotSimpleBeatQuestion() 
endfunction

function! TarotComplexBeat()
  python3 vimtarot.TarotComplexBeat() 
endfunction

function! TarotComplexBeatQuestion()
  python3 vimtarot.TarotComplexBeatQuestion() 
endfunction

function! TarotHeroJourney()
  python3 vimtarot.TarotHeroJourney() 
endfunction

function! TarotHeroJourneyQuestion()
  python3 vimtarot.TarotHeroJourneyQuestion() 
endfunction

function! TarotDeck()
  python3 vimtarot.TarotDeck() 
endfunction

function! TarotDeckSingle()
  python3 vimtarot.TarotDeckSingle() 
endfunction

function! TarotMajor()
  python3 vimtarot.TarotMajor() 
endfunction

function! TarotMajorSingle()
  python3 vimtarot.TarotMajorSingle() 
endfunction

function! TarotMinor()
  python3 vimtarot.TarotMinor() 
endfunction

function! TarotMinorSingle()
  python3 vimtarot.TarotMinorSingle() 
endfunction

function! TarotCourt()
  python3 vimtarot.TarotCourt() 
endfunction

function! TarotCourtSingle()
  python3 vimtarot.TarotCourtSingle() 
endfunction

function! TarotCups()
  python3 vimtarot.TarotCups() 
endfunction

function! TarotCupsRandom()
  python3 vimtarot.TarotCupsRandom() 
endfunction

function! TarotWands()
  python3 vimtarot.TarotWands() 
endfunction

function! TarotWandsRandom()
  python3 vimtarot.TarotWandsRandom() 
endfunction

function! TarotSwords()
  python3 vimtarot.TarotSwords() 
endfunction

function! TarotSwordsRandom()
  python3 vimtarot.TarotSwordsRandom() 
endfunction

function! TarotPentacles()
  python3 vimtarot.TarotPentacles() 
endfunction

function! TarotPentaclesRandom()
  python3 vimtarot.TarotPentaclesRandom() 
endfunction

function! TarotFool()
  python3 vimtarot.TarotFool() 
endfunction

function! TarotFoolRandom()
  python3 vimtarot.TarotFoolRandom() 
endfunction

command! -nargs=0 TarotCelticCross call TarotCelticCross()
command! -nargs=0 TarotCeltQuestion call TarotCelticCrossQuestion()
command! -nargs=0 TarotCharacter call TarotCharacter()
command! -nargs=0 TarotCharacterQuestion call TarotCharacterQuestion()
command! -nargs=0 TarotSimple call TarotSimpleBeat()
command! -nargs=0 TarotSimpleQuestion call TarotSimpleBeatQuestion()
command! -nargs=0 TarotComplex call TarotComplexBeat()
command! -nargs=0 TarotComplexQuestion call TarotComplexBeatQuestion()
command! -nargs=0 TarotHero call TarotHeroJourney()
command! -nargs=0 TarotHeroQuestion call TarotHeroJourneyQuestion()
command! -nargs=0 TarotDeck call TarotDeck()
command! -nargs=0 TarotDeckSingle call TarotDeckSingle()
command! -nargs=0 TarotMajor call TarotMajor()
command! -nargs=0 TarotMajorSingle call TarotMajorSingle()
command! -nargs=0 TarotMinor call TarotMinor()
command! -nargs=0 TarotMinorSingle call TarotMinorSingle()
command! -nargs=0 TarotCourt call TarotCourt()
command! -nargs=0 TarotCourtSingle call TarotCourtSingle()
command! -nargs=0 TarotCups call TarotCups()
command! -nargs=0 TarotCupsRandom call TarotCupsRandom()
command! -nargs=0 TarotWands call TarotWands()
command! -nargs=0 TarotWandsRandom call TarotWandsRandom()
command! -nargs=0 TarotSwords call TarotSwords()
command! -nargs=0 TarotSwordsRandom call TarotSwordsRandom()
command! -nargs=0 TarotPentacles call TarotPentacles()
command! -nargs=0 TarotPentaclesRandom call TarotPentaclesRandom()
command! -nargs=0 TarotFool call TarotFool()
command! -nargs=0 TarotFoolRandom call TarotFoolRandom()

