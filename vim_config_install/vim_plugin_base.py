# coding: utf-8
from .plugin_manager_base import PluginManagerBase


class VimPluginBase:
    """
    每个插件的配置
    """
    # 是否初始化安装
    ENABLE = True
    # 插件名称
    PLUGIN_NAME = ""
    # 其他依赖依赖的包
    OTHER_PKG = []
    # 针对插件的配置
    PLUGIN_CONFIG = ""
    # 注释插件
    COMMENT = ""
    # 文档地址
    DOC = ""
    # 其他需要执行的命令
    CMD = ""

    @property
    def enable(self):
        return self.ENABLE

    @property
    def plugin_name(self):
        return self.PLUGIN_NAME

    def __init__(self, plugin_manager: PluginManagerBase):
        self._plugin_manager = plugin_manager

    @property
    def plugin_install_config(self):
        return " ".join([self._plugin_manager.plugin_prefix, "'" + self.PLUGIN_NAME + "'"])

    @property
    def other_pkg(self):
        return self.OTHER_PKG

    @property
    def plugin_config(self):
        return self.PLUGIN_CONFIG

    @property
    def doc(self):
        return self.DOC if self.DOC else "https://github.com/" + self.plugin_name

    @property
    def cmd(self):
        return self.CMD

    @property
    def comment(self):
        return self.COMMENT
