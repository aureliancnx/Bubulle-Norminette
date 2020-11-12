#
# Copyright (c) 2020 aureliancnx
#
# MIT LICENSE
#
# This project is part of aureliancnx.
# See https://github.com/aureliancnx/Bubulle-Norminette for further info.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.#

import multiprocessing
import threading
import time

threads = []
thread_count = 1
sleeper = 0.05
s_id = 0


class BubulleWorker(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.w = []
        self.wk_end = False
        self.start()

    def run(self):
        while 1:
            if self.wk_end:
                return
            if len(self.w) != 0:
                try:
                    self.w[0]()
                except:
                    pass
                del self.w[0]
            time.sleep(sleeper)


def av_work(test):
    global s_id
    if s_id >= len(threads) - 1:
        s_id = 0
    else:
        s_id += 1
    threads[s_id].w.append(test)


def init_workers():
    thread_count = multiprocessing.cpu_count()
    for i in range(0, thread_count):
        threads.append(BubulleWorker("BubulleWorker-{0}".format(str(i))))


def wait():
    while 1:
        end = True
        for t in threads:
            if len(t.w) != 0:
                end = False
        if end:
            for t in threads:
                t.wk_end = True
            break
