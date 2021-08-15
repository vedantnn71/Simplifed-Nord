" Note: Skip initialization for vim-tiny or vim-small.
if 0 | endif

if &compatible
  set nocompatible
endif

set runtimepath+=~/.vim/bundle/neobundle.vim/

call neobundle#begin(expand('~/.vim/bundle/'))

NeoBundleFetch 'Shougo/neobundle.vim'

" ############### MY PACKAGEs #################

" ** Look & Customization **
" status bar 
NeoBundle 'itchyny/lightline.vim'
" color scheme
NeoBundle 'arcticicestudio/nord-vim'
" Icons
NeoBundle 'ryanoasis/vim-devicons'
" NERDTree
NeoBundle 'preservim/nerdtree'

" ***************************
" ** Web Development Setup **
" Live Server
NeoBundle 'turbio/bracey.vim'
" Emmet HTML code
NeoBundle 'mattn/emmet-vim'

call neobundle#end()
filetype plugin indent on

NeoBundleCheck

" ############# MY CUSTOMIZATIONs #############
" Set numbers
set number 
set relativenumber

" Look and feel customization
colorscheme nord
" Status Bar Configuration
let g:lightline = {
      \ 'colorscheme': 'nord',
      \ }


" !important make vim detect mouse
set mouse=a

" Get rid of swap shit
set noswapfile
set encoding=UTF-8

" Start NERDTree. If a file is specified, move the cursor to its window.
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * NERDTree | if argc() > 0 || exists("s:std_in") | wincmd p | endif

" Liver Server (bracey) config
g:bracey_server_path = 'http://127.0.0.1:5500/'
