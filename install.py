# coding: utf-8
import platform

from vim_config_install.plugin_manager_vundle import VundlePluginManager
from vim_config_install.vim_plugins import *
from vim_config_install.basic_config import BASIC_CONFIG
from vim_config_install.vim_config_installer import VimPluginInstaller


PKG_MANAGER_MAP = {
    "macOS": "brew",
    "Ubuntu": "apt",
    "centos": "yum",
}


def install():
    plat = platform.platform()
    pkg_manager = ""

    for ost in PKG_MANAGER_MAP:
        if ost in plat:
            pkg_manager = PKG_MANAGER_MAP[ost]
            break

    if not pkg_manager:
        print("请输入包管理软件，如yum")
        pkg_manager = input()

    manager = VundlePluginManager()
    plugins = [
        VimPluginAirline(manager),
        VimPluginClangFormat(manager),
        VimPluginOperatorUser(manager),
        VimPluginFlyGrep(manager),
        VimPluginAle(manager),
        VimPluginIndentLine(manager),
        VimPluginDelimitMate(manager),
        VimPluginCurtineIncSw(manager),
        VimPluginTagbar(manager),
        VimPluginNerdTree(manager),
        VimPluginYCM(manager),
    ]
    installer = VimPluginInstaller(BASIC_CONFIG, pkg_manager, manager, plugins)
    installer.install_all()

    print("all done!")


if __name__ == '__main__':
    install()
