# coding: utf-8
import sys
import inspect

from .vim_plugin_base import VimPluginBase


def get_plugins(manager):
    mod = sys.modules[__name__]

    plugins = list()
    for name, obj in inspect.getmembers(mod):
        if inspect.isclass(obj):
            if not name.startswith("VimPlugin") or name == "VimPluginBase":
                continue

            plugin = obj(manager)
            if not plugin.enable:
                continue

            plugins.append(obj(manager))

    return plugins


class VimPluginAirline(VimPluginBase):
    PLUGIN_NAME = "vim-airline/vim-airline"
    PLUGIN_CONFIG = """
set laststatus=2
let g:airline_powerline_fonts=1
let g:airline#extensions#tabline#enabled=1 " enable tabline
let g:airline#extensions#tabline#buffer_nr_show=1 " 显示buffer行号
let g:airline#extensions#tabline#fnamemod = ':t'
"""
    COMMENT = "状态栏"


class VimPluginClangFormat(VimPluginBase):
    PLUGIN_NAME = "rhysd/vim-clang-format"
    OTHER_PKG = ["clang-format", "[dnf]git-clang-format"]
    COMMENT = "格式化代码"
    PLUGIN_CONFIG = """
let g:clang_format#style_options = {
            \ "AccessModifierOffset" : -4,
            \ "AllowShortIfStatementsOnASingleLine" : "true",
            \ "AlwaysBreakTemplateDeclarations" : "true",
            \ "Standard" : "C++11"}
" map to <Leader>cf in C++ code
autocmd FileType c,cpp,objc nnoremap <buffer><Leader>cf :<C-u>ClangFormat<CR>
autocmd FileType c,cpp,objc vnoremap <buffer><Leader>cf :ClangFormat<CR>
" if you install vim-operator-user
autocmd FileType c,cpp,objc map <buffer><Leader>x <Plug>(operator-clang-format)
" Toggle auto formatting:
nmap <Leader>C :ClangFormatAutoToggle<CR>    
"""


class VimPluginOperatorUser(VimPluginBase):
    PLUGIN_NAME = "kana/vim-operator-user"


class VimPluginFlyGrep(VimPluginBase):
    PLUGIN_NAME = "wsdjeg/FlyGrep.vim"
    COMMENT = "搜索"
    PLUGIN_CONFIG = """
nnoremap <C-F> :FlyGrep<CR>
"""


class VimPluginAle(VimPluginBase):
    PLUGIN_NAME = "dense-analysis/ale"
    COMMENT = "代码检查"
    PLUGIN_CONFIG = """
let g:ale_linters = {
            \ 'cpp': ['cppcheck'],
            \ 'c': ['cppcheck'],
            \ 'python': ['pylint'],
            \}
" normal 模式下文字改变运行 linter
let g:ale_lint_on_text_changed = 'normal'
" 离开 insert 模式的时候运行 linter
let g:ale_lint_on_insert_leave = 1
let g:ale_c_cppcheck_options = '--enable=all'
let g:ale_cpp_cppcheck_options = '--enable=all'
"""
    OTHER_PKG = ["cppcheck", "pylint"]


class VimPluginIndentLine(VimPluginBase):
    PLUGIN_NAME = "Yggdroot/indentLine"
    COMMENT = "缩进线"


class VimPluginDelimitMate(VimPluginBase):
    PLUGIN_NAME = "Raimondi/delimitMate"
    COMMENT = "括号自动补全"


class VimPluginCurtineIncSw(VimPluginBase):
    PLUGIN_NAME = "ericcurtin/CurtineIncSw.vim"
    COMMENT = "头文件源文件切换"
    PLUGIN_CONFIG = """
map <Leader>o :call CurtineIncSw()<CR>
"""


class VimPluginTagbar(VimPluginBase):
    PLUGIN_NAME = "majutsushi/tagbar"
    COMMENT = "大纲视图"
    OTHER_PKG = ["ctags"]
    PLUGIN_CONFIG = """
nmap <F9> :TagbarToggle<CR>
" 启动时自动focus
let g:tagbar_autofocus = 1
"""


class VimPluginNerdTree(VimPluginBase):
    PLUGIN_NAME = "scrooloose/nerdtree"
    COMMENT = "文件浏览"
    PLUGIN_CONFIG = """
nmap <F2> :NERDTreeToggle<CR>
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>
let NERDTreeShowBookmarks=1
let NERDTreeIgnore=['\.py[cd]$', '\~$', '\.swo$', '\.swp$', '^\.git$','^\.hg$', '^\.svn$', '\.bzr$'] " 隐藏这些后缀的文件
let NERDTreeChDirMode=0
let NERDTreeQuitOnOpen=0
let NERDTreeMouseMode=2
let NERDTreeShowHidden=1 "显示隐藏文件
let NERDTreeKeepTreeInNewTab=1
let g:nerdtree_tabs_open_on_gui_startup=0
"""


class VimPluginYCM(VimPluginBase):
    PLUGIN_NAME = "Valloric/YouCompleteMe"
    COMMENT = "自动补全"
    PLUGIN_CONFIG = """
map gd :YcmCompleter GoToDefinitionElseDeclaration<CR>
" 输入两个字母即可进行语义补全
let g:ycm_semantic_triggers =  {
            \ 'c,cpp,python,java,go,erlang,perl': ['re!\w{2}'],
            \ 'cs,lua,javascript': ['re!\w{2}'],
            \ }
" 语义补全框配色
highlight PMenu ctermfg=0 ctermbg=242 guifg=black guibg=darkgrey
highlight PMenuSel ctermfg=242 ctermbg=8 guifg=darkgrey guibg=black

" 关闭函数原型预览框
set completeopt=menu,menuone
let g:ycm_add_preview_to_completeopt = 1
let g:ycm_autoclose_preview_window_after_completion=1
let g:ycm_python_binary_path = 'python'

" 关闭诊断信息
let g:ycm_show_diagnostics_ui = 0
"let g:ycm_global_ycm_extra_conf = '~/.vim/bundle/YouCompleteMe/.ycm_extra_conf.py'
let g:ycm_global_ycm_extra_conf = '~/.vim/bundle/YouCompleteMe/.ycm_cpp_conf.py'
let g:ycm_seed_identifiers_with_syntax = 1
set completeopt=longest,menu
let g:syntastic_ignore_files=[".*\.py$"]
"""
    CMD = "python3 ~/.vim/bundle/YouCompleteMe/install.py --all && mv .ycm_cpp_conf.py ~/.vim/bundle/YouCompleteMe/"
    OTHER_PKG = [
        "cmake",
        "make",
        "build-essential",
        "gcc",
        "g++",
        "gcc-c++",
        "python3-dev",
        "[yum|dnf]python3-devel",
        "python",
        "golang",
    ]


class VimPluginVimGo(VimPluginBase):
    PLUGIN_NAME = "fatih/vim-go"
    COMMENT = "golang"
    CMD = "vim +GoInstallBinaries +qall"
    PLUGIN_CONFIG = """
" format code for golang
autocmd FileType go nnoremap <buffer><Leader>cf :GoFmt<CR>
autocmd FileType go vnoremap <buffer><Leader>cf :GoFmt<CR>
"""


class VimPluginPolyglot(VimPluginBase):
    PLUGIN_NAME = "sheerun/vim-polyglot"
    COMMENT = "主题"


class VimPluginColorEdge(VimPluginBase):
    PLUGIN_NAME = "sainnhe/edge"
    COMMENT = "edge 主题"
    CMD = "cp -rf ~/.vim/bundle/edge/colors/ ~/.vim/"
    PLUGIN_CONFIG = """
" important!!
set termguicolors

" for dark version
set background=dark
" the configuration options should be placed before `colorscheme edge`
let g:edge_style = 'neon'
let g:edge_disable_italic_comment = 1

colorscheme edge    
"""


class VimPluginNerdCommenter(VimPluginBase):
    PLUGIN_NAME = "scrooloose/nerdcommenter"
    COMMENT = "注释"
    PLUGIN_CONFIG = """
" 注释的时候自动加个空格, 强迫症必配
" <leader>cc   加注释
" <leader>cu   解开注释
" 
" <leader>c<space>  加上/解开注释, 智能判断
" <leader>cy   先复制, 再注解(p可以进行黏贴)
let g:NERDSpaceDelims=1    
"""


class VimPluginNerdGit(VimPluginBase):
    PLUGIN_NAME = "Xuyuanp/nerdtree-git-plugin"
    COMMENT = "文件浏览git标识"


class VimPluginDevIcons(VimPluginBase):
    PLUGIN_NAME = "ryanoasis/vim-devicons"
    COMMENT = "文件浏览图标"
