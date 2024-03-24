#!/usr/bin/env python3
# Copyright (c) 2024 Egor
# SPDX-License-Identifier: GPL-2.0-or-later
def seedforsystem(sysno, galno=0, seed=(0x5a4a, 0x0248, 0xb753)):
    w0, w1, w2 = seed
    if galno & 4:
        w0 = w0<<4 & 0xf0f0 | w0>>4 & 0x0f0f
        w1 = w1<<4 & 0xf0f0 | w1>>4 & 0x0f0f
        w2 = w2<<4 & 0xf0f0 | w2>>4 & 0x0f0f
    if galno & 2:
        w0 = w0<<2 & 0xfcfc | w0>>6 & 0x0303
        w1 = w1<<2 & 0xfcfc | w1>>6 & 0x0303
        w2 = w2<<2 & 0xfcfc | w2>>6 & 0x0303
    if galno & 1:
        w0 = w0<<1 & 0xfefe | w0>>7 & 0x0101
        w1 = w1<<1 & 0xfefe | w1>>7 & 0x0101
        w2 = w2<<1 & 0xfefe | w2>>7 & 0x0101
    sysno *= 4
    while sysno >= 32:
        w0, w1, w2 = (
            (w0*0x4f91 + w1*0xf710 + w2*0xe4c0)&0xffff,
            (w0*0xe4c0 + w1*0x3451 + w2*0xdbd0)&0xffff,
            (w0*0xdbd0 + w1*0xc090 + w2*0x1021)&0xffff)
        sysno -= 32
    while sysno >= 1:
        w0, w1, w2 = w1, w2, (w0+w1+w2)&0xffff
        sysno -= 1
    return w0, w1, w2
def systemname(seed):
    w0, w1, w2 = seed
    pairs = 'ALLEXEGEZACEBISOUSESARMAINDIREA?ERATENBERALAVETIEDORQUANTEISRION'
    maxpairs = 4 if w0&1<<6 else 3
    s = ''
    while maxpairs > 0:
        if w2 & 0x1F00:
            s += pairs[w2>>7 & 0x3E:][:2]
            if s[-1] == '?':
                s = s[:-1]
        w0, w1, w2 = w1, w2, (w0+w1+w2)&0xFFFF
        maxpairs -= 1
    return s
def systempos(seed):
    return seed[1]>>8, seed[0]>>8
def systemecogovtech(seed):
    eco = seed[0]>>8 & 7
    gov = seed[1]>>3 & 7
    if gov < 2:
        eco |= 2
    tech = (eco^7) + (seed[1]&3) + (gov+1)//2
    return eco, gov, tech

mysqrt = []
for i in range(256):
    mysqrt += [i]*((i+1)*(i+1)-i*i)
def dist(p1, p2):
    return mysqrt[abs(p2[0]-p1[0])**2 + (abs(p2[1]-p1[1])//2)**2]*4

if __name__ == '__main__':
    rich = []
    poor = []
    for i in range(256):
        s = seedforsystem(i)
        pos = systempos(s)
        eco, gov, tech = systemecogovtech(s)
        if eco in (0, 6, 7) and gov >= 6:
            print(i, systemname(s), eco, gov, tech)
            if eco == 0:
                rich.append(i)
            else:
                poor.append(i)

    for i in rich:
        s = seedforsystem(i)
        p = systempos(s)
        for j in poor:
            t = seedforsystem(j)
            q = systempos(t)
            d = dist(p, q)
            if d <= 70:
                print(systemname(s), p, systemecogovtech(s), systemname(t), q, systemecogovtech(t), d)

