# -*- coding: utf-8 -*-
# This file is part of Shuup Mailchimp Addon.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.


class PostIsNotAllowed(Exception):
    pass


def raise_on_request(url, **kwargs):
    class MockedResponse:
        def __init__(self, url, **kwargs):
            self.url = url
            self.data = kwargs.get("json")
            assert self.data is not None
            self.status_code = 500

        def json(self):
            raise PostIsNotAllowed("Post is not allowed!")
    return MockedResponse(url, **kwargs)


def success_response(url, **kwargs):
    class MockedResponse:
        def __init__(self, url, **kwargs):
            self.url = url

        def json(self):
            return {"id": "some_list_id", "stats": {"member_count": 0}}
    return MockedResponse(url, **kwargs)
