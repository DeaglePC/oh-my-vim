# coding: utf-8
import os

from .vim_plugin_base import VimPluginBase
from .plugin_manager_base import PluginManagerBase


class Installer:
    """
    插件安装
    """
    SPLIT_COMMENT = "\" ============================== {} =============================="
    SYS_REQUIREMENT = ["git"]

    def __init__(
            self,
            basic_cfg: str,
            sys_pkg: str,
            plugin_manager: PluginManagerBase,
            vim_plugins=None,
            output_file=None
    ):
        self._basic_config = basic_cfg
        self._plugin_manager = plugin_manager
        self._plugins = vim_plugins if vim_plugins else list()
        self._sys_pkg = sys_pkg  # 包管理工具，比如brew yum apt-get
        self._vimrc = ""
        self._output_file = os.path.join(os.path.expanduser('~'), ".vimrc") if not output_file else output_file

    def _append_vimrc(self, str_cfg_line):
        self._vimrc += str_cfg_line + "\n"

    def add_plugin(self, plugin: VimPluginBase):
        self._plugins.append(plugin)

    def install_sys_requirements(self):
        for item in self.SYS_REQUIREMENT:
            cmd = " install -y ".join(["sudo " + self._sys_pkg, item])
            print(cmd)
            os.system(cmd)

    def install_vim_plugin_manager(self):
        os.system(self._plugin_manager.install_cmd)

    def gen_vimrc(self):
        self._gen_vimrc_basic_config()
        self._gen_vimrc_plugin_config()

    def _gen_vimrc_basic_config(self):
        split_comment = self.SPLIT_COMMENT.format("基本配置")
        self._append_vimrc(split_comment)
        self._append_vimrc(self._basic_config)
        self._append_vimrc(split_comment)
        self._append_vimrc("\n")

    def _gen_vimrc_plugin_config(self):
        split_comment = self.SPLIT_COMMENT.format("插件配置")
        self._append_vimrc(split_comment)

        plugin_config = ""
        for plugin in self._plugins:
            cfg_str = ""
            cfg_str += '" ' + plugin.comment + "\n"
            cfg_str += plugin.plugin_install_config
            if not plugin.plugin_config:
                cfg_str += "\n"
            cfg_str += plugin.plugin_config
            cfg_str += self._plugin_manager.plugin_split_comment
            plugin_config += cfg_str

        self._append_vimrc(self._plugin_manager.plugin_config.format(plugin_config))

        self._append_vimrc(split_comment)

    def write_vimrc(self):
        if os.path.exists(self._output_file):
            while True:
                print("{} 文件已存在，确认做好备份，是否覆盖？（Y/N）".format(self._output_file))
                ic = input()
                if ic == "N" or ic == "n":
                    exit(-1)
                elif ic == "Y" or ic == "y":
                    break

        with open(self._output_file, "w") as f:
            f.write(self._vimrc)

    def install_plugins(self):
        cmd = self._plugin_manager.INSTALL_PLUGIN_CMD
        print(cmd)
        os.system(cmd)

    def exec_plugins_cmd(self):
        """
        某些特殊插件需要执行的东西比如YCM
        :return:
        """
        for plugin in self._plugins:
            if plugin.cmd:
                os.system(plugin.cmd)

    @staticmethod
    def _check_other_pkg(spkgm: str, pkg: str) -> str:
        if pkg[0] != '[':
            return pkg

        idx = pkg.find(']')
        if idx == -1:
            return ""

        tmp_sub_spkgm = pkg[:idx]
        if spkgm in tmp_sub_spkgm:
            return pkg[idx+1:]

        return ""

    def install_other_pkg(self):
        """
        安装其他依赖
        :return:
        """
        for plugin in self._plugins:
            if not plugin.other_pkg:
                continue
            for pkg in plugin.other_pkg:
                pkg = self._check_other_pkg(self._sys_pkg, pkg)
                if not pkg:
                    continue
                cmd = " install -y ".join(["sudo " + self._sys_pkg, pkg])
                print(cmd)
                os.system(cmd)

    @property
    def vimrc(self):
        return self._vimrc

    def install_all(self):
        self.display_msg()
        self.install_sys_requirements()
        self.install_vim_plugin_manager()
        self.gen_vimrc()
        self.write_vimrc()
        self.install_plugins()
        self.install_other_pkg()
        self.exec_plugins_cmd()

    def display_msg(self):
        print("将安装以下插件")
        for plugin in self._plugins:
            print("{}({})".format(plugin.plugin_name, plugin.comment))

        print("Y/y 继续安装，其他键退出安装")
        ic = input()
        if ic != "Y" and ic != "y":
            exit(-1)
