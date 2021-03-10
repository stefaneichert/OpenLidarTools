# -*- coding: utf-8 -*-
"""
/***************************************************************************
 OpenLidarTools
                                 A QGIS plugin
 Open Lidar Tools for Archaeology
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2021-03-10
        copyright            : (C) 2021 by Benjamin Štular, Ediza Lozić, Stefan Eichert
        email                : stefaneichert@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

__author__ = 'Benjamin Štular, Ediza Lozić, Stefan Eichert'
__date__ = '2021-03-10'
__copyright__ = '(C) 2021 by Benjamin Štular, Ediza Lozić, Stefan Eichert'


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load OpenLidarTools class from file OpenLidarTools.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .open_lidar_tools import OpenLidarToolsPlugin
    return OpenLidarToolsPlugin()
