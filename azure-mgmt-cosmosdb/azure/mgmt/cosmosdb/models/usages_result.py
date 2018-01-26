# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class UsagesResult(Model):
    """The response to a list usage request.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar value: The list of usages for the database. A usage is a point in
     time metric
    :vartype value: list[~azure.mgmt.cosmosdb.models.Usage]
    """

    _validation = {
        'value': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Usage]'},
    }

    def __init__(self):
        super(UsagesResult, self).__init__()
        self.value = None
