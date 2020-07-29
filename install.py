# coding: utf-8
from vim_config_install.plugin_manager_vundle import VundlePluginManager
from vim_config_install.basic_config import BASIC_CONFIG
from vim_config_install.vim_config_installer import Installer
from vim_config_install.vim_plugins import get_plugins


def install():
    print("请输入包管理软件，如 yum/apt-get/brew/dnf")
    pkg_manager = input()

    manager = VundlePluginManager()
    plugins = get_plugins(manager)
    installer = Installer(BASIC_CONFIG, pkg_manager, manager, plugins)
    installer.install_all()

    print("all done!")


if __name__ == '__main__':
    install()
