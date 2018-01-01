# usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by koretsunobuyasu on 2018/01/01
import configparser


def main():
    cfg = configparser.ConfigParser()
    print(cfg.read('settings.cfg'))
    print(cfg)
    print(cfg['french'])
    print(cfg['french']['greeting'])
    print(cfg['files']['bin'])

    return 0


if __name__ == '__main__':
    main()