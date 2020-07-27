# coding: utf-8
from .plugin_manager_base import PluginManagerBase


class VundlePluginManager(PluginManagerBase):
    PLUGIN_SPLIT_COMMENT = "\n\n"

    PLUGIN_MANAGER = "VundleVim/Vundle.vim"

    PLUGIN_MANAGER_PREFIX = "Plugin"

    PLUGIN_REQUIRE_CONFIG = """
    " set the runtime path to include Vundle and initialize
    set rtp+=~/.vim/bundle/Vundle.vim
    call vundle#begin()
    " alternatively, pass a path where Vundle should install plugins
    "call vundle#begin('~/some/path/here')

    " let Vundle manage Vundle, required
    Plugin 'VundleVim/Vundle.vim'


    {}
    " All of your Plugins must be added before the following line
    call vundle#end()            " required
    filetype plugin indent on    " required
    " To ignore plugin indent changes, instead use:
    "filetype plugin on
    "
    " Brief help
    " :PluginList       - lists configured plugins
    " :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
    " :PluginSearch foo - searches for foo; append `!` to refresh local cache
    " :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
    "
    " see :h vundle for more details or wiki for FAQ
    " Put your non-Plugin stuff after this line

    """

    INSTALL = "git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim"

    INSTALL_PLUGIN_CMD = "vim +PluginInstall +qall"
