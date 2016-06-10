#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Thu Jun  9 10:52:35 2016
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import osmosdr
import sip
import sys
import time


class top_block(gr.top_block):

    def __init__(self, command):
        gr.top_block.__init__(self, "Top Block")  

        # ##################################################
        # # Variables
        # ##################################################
        self.samp_rate = samp_rate = 5e6
        self.frequency = frequency = 49000000
        self.command = command

        # ##################################################
        # # Blocks
        # ###############################################
        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + "" )
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(frequency, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(0, 0)
        self.osmosdr_sink_0.set_if_gain(47, 0)
        self.osmosdr_sink_0.set_bb_gain(16, 0)
        self.osmosdr_sink_0.set_antenna("", 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)
          
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((6, ))
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, 
            "/home/cssummer2016/Desktop/" + self.command, True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.osmosdr_sink_0, 0))    
       
    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)

    def get_frequency(self):
        return self.frequency

    def set_frequency(self, frequency):
        self.frequency = frequency
        self.osmosdr_sink_0.set_center_freq(self.frequency, 0)

    def get_command(self):
        return self.command

    def set_command(self, command):
        self.command = command
        self.blocks_file_source_0.open("/home/cssummer2016/Desktop/" + command, False)


def sendCommand(command, top_block_cls=top_block, options=None): 
    tb = top_block_cls(command)
    tb.start()
    # time.sleep(delay) 
    # tb.stop()
    return tb

if __name__=='__main__':

    # tb = None

    # while True:
    #     command= str(raw_input('Command: '))
    #     if command == 'quit' or command == 'q':
    #         break
    #     else:
    #         if command != 'stop':
    #             tb = sendCommand(command)
    #         else:
    #             tb.stop()
    #             tb = None

    import pygame
    pygame.init()

    size = [800, 600]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption('RC Car Control')

    tb = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                # keys= pygame.key.get_pressed()
                # if keys[pygame.K_w]:
                #     tb= sendCommand('up')
                # if keys[pygame.K_a]:
                #     tb= sendCommand('left')
                # if keys[pygame.K_d]:
                #     tb= sendCommand('right')
                # if keys[pygame.K_s]:
                #     tb= sendCommand('down')
                # if keys[pygame.K_w] & keys[pygame.K_a]:
                #     tb= sendCommand('up')
                #     tb= sendCommand('left')
                # if keys[pygame.K_w] & keys[pygame.K_d]:
                #     tb= sendCommand('up')
                #     tb= sendCommand('right')
                # if keys[pygame.K_s] & keys[pygame.K_a]:
                #     tb= sendCommand('down')
                #     tb= sendCommand('left')
                # if keys[pygame.K_s] & keys[pygame.K_d]:
                #     tb= sendCommand('down')
                #     tb= sendCommand('right')

                if event.key == pygame.K_a:
                    tb = sendCommand('left')
                elif event.key == pygame.K_d:
                    tb = sendCommand('right')
                elif event.key == pygame.K_w:
                    tb = sendCommand('up')
                elif event.key == pygame.K_x:
                    tb = sendCommand('down')
                if event.key == pygame.K_q:
                    tb = sendCommand('upleft')
                elif event.key == pygame.K_e:
                    tb = sendCommand('upright')
                elif event.key == pygame.K_z:
                    tb = sendCommand('downleft')
                elif event.key == pygame.K_c:
                    tb = sendCommand('downright')
                elif event.key == pygame.K_ESCAPE:
                    sys.exit(0)
            elif event.type == pygame.KEYUP:
                try:
                    tb.stop()
                    tb = None
                except:
                    pass