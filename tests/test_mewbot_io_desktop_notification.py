# SPDX-FileCopyrightText: 2023 Mewbot Developers <mewbot@quicksilver.london>
#
# SPDX-License-Identifier: BSD-2-Clause

# -*- coding: utf-8 -*-

"""
Contains tests for mewbot-desktop-notification.
"""


class TestDesktopNotificationAPI:
    """
    Tests that we can import the expected things from the defined modules.

    Mostly tests we can import anything at all...
    Just in case the implicit namespace system is screwed up in some way.
    """

    @staticmethod
    def test_import_DesktopNotificationIO() -> None:
        """
        Tests we can import DesktopNotificationIO.

        :return:
        """
        from mewbot.io.desktop_notification import DesktopNotificationIO

        assert DesktopNotificationIO is not None
