# coding: utf-8


BASIC_CONFIG = """
set fileencodings=utf-8,ucs-bom,gb18030,gbk,gb2312,cp936
set termencoding=utf-8
set encoding=utf-8
set fenc=utf-8

" 设置 vimrc 修改保存后立刻生效，不用在重新打开
" 建议配置完成后将这个关闭
autocmd BufWritePost $MYVIMRC source $MYVIMRC

set nocompatible " 关闭兼容模式
filetype off

set nu              " 设置行号
set cursorline      "突出显示当前行
" set cursorcolumn  " 突出显示当前列
set showmatch       " 显示括号匹配

set tabstop=4       " 设置Tab长度为4空格
set shiftwidth=4    " 设置自动缩进长度为4空格
set autoindent      " 继承前一行的缩进方式，适用于多行注释
set expandtab

let mapleader=";"   " 定义快捷键的前缀，即<Leader>

" v 模式下复制内容到系统剪切板
vmap <Leader>c "+yy
" n 模式下复制一行到系统剪切板
nmap <Leader>c "+yy
" n 模式下粘贴系统剪切板的内容
nmap <Leader>v "+p

" buffer切换
nmap <Leader>[ :bn<CR>
nmap <Leader>] :bp<CR>

nmap <Leader>nu :set nu<CR>
nmap <leader>NU :set nonu<CR>

" 自动保存
let g:auto_save = 1
let g:auto_save_events = ["InsertLeave", "TextChanged", "TextChangedI", "CursorHoldI", "CompleteDone"]

set incsearch   " 开启实时搜索
set ignorecase  " 搜索时大小写不敏感

syntax enable
syntax on                    " 开启文件类型侦测
filetype plugin indent on    " 启用自动补全

" 退出插入模式指定类型的文件自动保存
au InsertLeave *.go,*.sh,*.php write

" for python
let python_highlight_all=1
au Filetype python set tabstop=4
au Filetype python set softtabstop=4
au Filetype python set shiftwidth=4
au Filetype python set textwidth=79
au Filetype python set expandtab
au Filetype python set autoindent
au Filetype python set fileformat=unix
autocmd Filetype python set foldmethod=indent
autocmd Filetype python set foldlevel=99

" 开启折叠
setlocal foldmethod=syntax
autocmd FileType c setlocal foldmethod=syntax
"""
