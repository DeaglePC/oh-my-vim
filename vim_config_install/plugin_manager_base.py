# coding: utf-8


class PluginManagerBase:
    """
    插件管理
    """
    # 每个插件之间的分隔符
    PLUGIN_SPLIT_COMMENT = ""
    # 插件管理程序
    PLUGIN_MANAGER = ""
    # 配置文件中安装插件时的前缀
    PLUGIN_MANAGER_PREFIX = ""
    # 插件管理器的配置
    PLUGIN_REQUIRE_CONFIG = ""
    # 安装插件管理器的命令
    INSTALL = ""
    # 安装插件的命令
    INSTALL_PLUGIN_CMD = ""

    @property
    def plugin_manager(self):
        return self.PLUGIN_MANAGER

    @property
    def plugin_prefix(self):
        return self.PLUGIN_MANAGER_PREFIX

    @property
    def plugin_split_comment(self):
        return self.PLUGIN_SPLIT_COMMENT

    @property
    def plugin_config(self):
        return self.PLUGIN_REQUIRE_CONFIG

    @property
    def install_cmd(self):
        return self.INSTALL

    @property
    def plugin_install_cmd(self):
        return self.INSTALL_PLUGIN_CMD
