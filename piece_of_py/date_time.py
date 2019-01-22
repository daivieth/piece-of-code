# Copyright (c) 2018-present, Taatu Ltd.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
import datetime
import time
from datetime import timedelta

d = datetime.datetime.now() - timedelta(days=30) ; d = d.strftime('%Y%m%d')

d2 = datetime.datetime.now() ; d2 = d2.strftime("%d-%b-%Y")
