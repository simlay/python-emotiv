# -*- coding: utf-8 -*-
# vim:set et ts=4 sw=4:
#
## Copyright (C) 2012 Ozan Çağlayan <ocaglayan@gsu.edu.tr>
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

from bitstring import BitArray
from Crypto.Cipher import AES

def decryptionProcess(aes_key, endpoint, pipe):
    # Setup decryption cipher
    cipher = AES.new(aes_key)

    # Setup a 4 second buffer
    # Each second 128 packets are sent. After each second 1 packet
    # is sent to notify battery and quality information.
    _buffer = list(xrange(129))

    while 1:
        try:
            for i in xrange(129):
                _buffer[i] = BitArray(bytes=cipher.decrypt(endpoint.read(32)))
        except:
            pass
        else:
            # 1 second of EEG is acquired, pass it
            pipe.send(_buffer)
