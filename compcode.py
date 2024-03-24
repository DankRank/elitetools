#!/usr/bin/env python3
# Copyright (c) 2024 Egor
# SPDX-License-Identifier: GPL-2.0-or-later
def showinfo(code):
    k0 = code>>24
    k1 = code>>16 & 0xFF
    k2 = code>>8 & 0xFF
    k3 = code & 0xFF
    k3 ^= k1 ^ 0x5A
    k1 ^= k2
    k2 ^= k0
    flags = ['Manual mis-jump', 'Casette', 'Disk (bugged)/SP6502', 'Electron', 'Bit 4', 'Disk (fixed)', 'Bit 6', 'Tampered']
    rank = '<no rank> ' if k3 < 1 else 'Competent' if k3 < 2 else 'Dangerous' if k3 < 10 else 'Deadly' if k3 < 25 else 'Elite'
    s = ', '.join(s for s in [flags[i] if k2&1<<i else '' for i in range(8)] if s != '')
    print(f'Flags: {s}')
    print(f'Cash: at least {k1*256} Cr')
    print(f'Kills: {k3*256}-{k3*256+255} - {rank}')

if __name__ == '__main__':
	showinfo(int(input()))
