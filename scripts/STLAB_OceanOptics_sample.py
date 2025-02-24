#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 10:40:13 2022

@author: jtm

Sample the spectral output of STLAB with its internal spectrometer and
optionally also with an external OceanOptics spectrometer.
"""

import os
import os.path as op
from time import perf_counter

import pandas as pd

from pyplr.stlabsampler import SpectraTuneLabSampler
from pyplr.oceanops import OceanOptics

SAVE_TO = "../data/STLAB/"
STLAB_PREFIX = "STLAB_1"
STLAB_ADDRESS = 1
if not op.exists(SAVE_TO):
    os.mkdir(SAVE_TO)

# Whether to also obtain samples with an external OceanOptics spectrometer
USE_OCEAN_OPTICS = True
if USE_OCEAN_OPTICS:
    EXTERNAL_PREFIX = f"{STLAB_PREFIX}_oo"
    CALIBRATED_WAVELENGTHS = pd.read_csv(
        "../data/jazcal/Ar_calibrated_wls.csv"
    ).squeeze()


try:
    # Connect to devices
    d = SpectraTuneLabSampler.from_config()
    d.default_address = STLAB_ADDRESS

    if USE_OCEAN_OPTICS:
        oo = OceanOptics.from_first_available()
        d.external = oo
        external_kwargs = {
            "correct_nonlinearity": True,
            "correct_dark_counts": False,
            "boxcar_width": 0,
            "scans_to_average": 1,
            "ignore_pixels": [960, 45, 624, 1493, 478, 1256, 1054, 676, 1517, 1467],
            "collect_dark_spectra": True
        }

    # Specify LEDs and intensities to be sampled. In this case, each
    # channel at its maximum setting. For a more complete profiling,
    # uncomment the lines below. This will sample each channel accross the
    # range of intensities in steps of 65.
    #leds = [0, 1, 2]#, 3, 4, 5, 6, 7, 8, 9]
    #intensities = [4095]

    leds = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    intensities = [i for i in range(65, 4096, 65)]

    start = perf_counter()
    # Sample
    d.sample(
        leds=leds, intensities=intensities, randomise=True, **external_kwargs
    )
    end = perf_counter()
    print(f"> Measurment sequence completed in {end-start:2f} s")

    # Save results to csv in current working directory
    d.make_dfs()
    d.ex_spectra.columns = CALIBRATED_WAVELENGTHS
    d.save_samples(
        stlab_prefix=op.join(SAVE_TO, STLAB_PREFIX),
        external_prefix=op.join(SAVE_TO, EXTERNAL_PREFIX),
    )


except KeyboardInterrupt:
    print("> Sampling interrupted by user. No data were saved.")

finally:
    if USE_OCEAN_OPTICS:
        oo.close()
        print("> Closed connection with OceanOptics spectrometer.")
    d.turn_off()
    d.logout()
    print("> Logging out of STLAB.")
