# import time
# from tqdm import tqdm
#
# from tqdm import trange
#
# class my_pbar:
#     def __init__(self, total, msg):
#         self.total = total
#         self.message = msg
#         self.pbar = tqdm(self.total)
#         # with tqdm(total=self.total) as pbar:
#         # pbar.update(1)
#
#     def pbar_update(self,num):
#         self.pbar.update(num)
#


from __future__ import print_function
import sys
import re


class ProgressBar(object):
    DEFAULT = 'Progress: %(bar)s %(percent)3d%%'
    FULL = '%(bar)s %(current)d/%(total)d (%(percent)3d%%) remaining:%(remaining)d %(msg)s '

    def __init__(self, total, width=40, fmt=DEFAULT, msg='file:', symbol='*',
                 output=sys.stderr):
        assert len(symbol) == 1

        self.total = total
        self.width = width
        self.msg = msg
        self.symbol = symbol
        self.output = output
        self.fmt = re.sub(r'(?P<name>%\(.+?\))d',
            r'\g<name>%dd' % len(str(total)), fmt)

        self.current = 0

    def __call__(self):
        percent = self.current / float(self.total)
        size = int(self.width * percent)
        remaining = self.total - self.current
        bar = '[' + self.symbol * size + ' ' * (self.width - size) + ']'

        args = {
            'total': self.total,
            'bar': bar,
            'current': self.current,
            'percent': percent * 100,
            'remaining': remaining,
            'msg': self.msg
        }
        print('\r' + self.fmt % args, file=self.output, end='')

    def done(self):
        self.current = self.total
        self()
        print('', file=self.output)