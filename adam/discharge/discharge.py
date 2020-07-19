from tkinter import *

from tkinter import ttk
from tkinter.ttk import *

import adamApp as adam

import math
import numpy
from scipy.special import erfc
import pylab
# from gnuradio import gr, digital

import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Best to choose powers of 10
N_BITS = 1e7
RAND_SEED = 42

class discharge(adam.adamApp):
    apps = {'Discharge':'discharge',
            'Setup':'setup',
            'Motor Test':'motorTest'}

    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.controller = controller

        self.showScreen('Discharge')

    def setup(self, p):
        label = Label(p, text="setup screen")
        label.pack(side=TOP, fill=BOTH)

        f = plt.Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)

        canvas = FigureCanvasTkAgg(f, self)
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])

        # EbN0_min = 0
        # EbN0_max = 15
        # EbN0_range = range(EbN0_min, EbN0_max+1)
        # ber_theory = [berawgn(x) for x in EbN0_range]
        # print("Simulating...")
        # ber_simu = [simulate_ber(x) for x in EbN0_range]
        #
        # f = pylab.figure()
        # s = f.add_subplot(1,1,1)
        # s.semilogy(EbN0_range, ber_theory, 'g-.', label="Theoretical")
        # s.semilogy(EbN0_range, ber_simu, 'b-o', label="Simulated")
        # s.set_title('BER Simulation')
        # s.set_xlabel('Eb/N0 (dB)')
        # s.set_ylabel('BER')
        # s.legend()
        # s.grid()
        # pylab.show()

    def motorTest(self, p):
        label = Label(p, text="motorTest screen")
        label.pack(side=TOP, fill=BOTH)
        return 1

#     def simulate_ber(EbN0):
#         """ All the work's done here: create flow graph, run, read out BER """
#         print("Eb/N0 = %d dB" % EbN0)
#         fg = BERAWGNSimu(EbN0)
#         fg.run()
#         return numpy.sum(fg.sink.data())
#
#     def berawgn(EbN0):
#         """ Calculates theoretical bit error rate in AWGN (for BPSK and given Eb/N0) """
#         return 0.5 * erfc(math.sqrt(10**(float(EbN0)/10)))
#
# class BitErrors(gr.hier_block2):
#     """ Two inputs: true and received bits. We compare them and
#     add up the number of incorrect bits. Because integrate_ff()
#     can only add up a certain number of values, the output is
#     not a scalar, but a sequence of values, the sum of which is
#     the BER. """
#     def __init__(self, bits_per_byte):
#         gr.hier_block2.__init__(self, "BitErrors",
#                 gr.io_signature(2, 2, gr.sizeof_char),
#                 gr.io_signature(1, 1, gr.sizeof_int))
#
#         # Bit comparison
#         comp = gr.xor_bb()
#         intdump_decim = 100000
#         if N_BITS < intdump_decim:
#             intdump_decim = int(N_BITS)
#         self.connect(self,
#                      comp,
#                      gr.unpack_k_bits_bb(bits_per_byte),
#                      gr.uchar_to_float(),
#                      gr.integrate_ff(intdump_decim),
#                      gr.multiply_const_ff(1.0/N_BITS),
#                      self)
#         self.connect((self, 1), (comp, 1))
#
# class BERAWGNSimu(gr.top_block):
#     " This contains the simulation flow graph "
#     def __init__(self, EbN0):
#         gr.top_block.__init__(self)
#         self.const = digital.qpsk_constellation()
#         # Source is N_BITS bits, non-repeated
#         data = map(int, numpy.random.randint(0, self.const.arity(), N_BITS/self.const.bits_per_symbol()))
#         src   = gr.vector_source_b(data, False)
#         mod   = gr.chunks_to_symbols_bc((self.const.points()), 1)
#         add   = gr.add_vcc()
#         noise = gr.noise_source_c(gr.GR_GAUSSIAN,
#                                   self.EbN0_to_noise_voltage(EbN0),
#                                   RAND_SEED)
#         demod = digital.constellation_decoder_cb(self.const.base())
#         ber   = BitErrors(self.const.bits_per_symbol())
#         self.sink  = gr.vector_sink_f()
#         self.connect(src, mod, add, demod, ber, self.sink)
#         self.connect(noise, (add, 1))
#         self.connect(src, (ber, 1))
#
#     def EbN0_to_noise_voltage(self, EbN0):
#         """ Converts Eb/N0 to a single-sided noise voltage (assuming unit symbol power) """
#         return 1.0 / math.sqrt(2.0 * self.const.bits_per_symbol() * 10**(float(EbN0)/10))
