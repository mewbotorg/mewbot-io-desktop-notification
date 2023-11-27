# SPDX-FileCopyrightText: 2023 Mewbot Developers <mewbot@quicksilver.london>
#
# SPDX-License-Identifier: BSD-2-Clause

# -*- coding: utf-8 -*-

"""
Contains tests for mewbot-desktop-notification.
"""

from mewbot.io.desktop_notification import (
    DesktopNotificationIO,
    DesktopNotificationOutput,
)


class TestDesktopNotificationAPI:
    """
    Tests that we can import the expected things from the defined modules.

    Mostly tests we can import anything at all...
    Just in case the implicit namespace system is screwed up in some way.
    """

    @staticmethod
    def test_import_desktop_notification_io() -> None:
        """
        Tests we can import DesktopNotificationIO.

        :return:
        """
        assert DesktopNotificationIO is not None

    @staticmethod
    def test_ioconfig_init() -> None:
        """
        Tests __init__ for the IOConfig.

        :return:
        """
        test_io_config = DesktopNotificationIO()
        assert test_io_config is not None

    @staticmethod
    def test_enable_and_disable() -> None:
        """
        Tests enabling and disabling the IOConfig.

        :return:
        """
        test_io_config = DesktopNotificationIO()
        test_io_config_outputs = test_io_config.get_outputs()
        assert len(test_io_config_outputs) == 1

        test_io_config_output = test_io_config_outputs[0]
        assert isinstance(test_io_config_output, DesktopNotificationOutput)
