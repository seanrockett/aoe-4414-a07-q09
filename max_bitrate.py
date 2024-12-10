#max_bitrate.py
#
# Usage: python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz
# Usage: max_bitrate.py
#
# Input:
#  tw_w: Transmitting power
#  tx_gain_db: Transmitting antenna gain
#  freq_hz: communication frequency
#  dist_km: communication distance 
#  r_gain_db: Receiving antenna gain
#  n0_j: Noise spectral density
#  bw_hz: Communication bandwidth
# Output:
#  Maximum achievable bitrate
#
# Written by Sean Rockett
# Other contributors: None

#modules
import sys
import math

#Constants
speed_of_light = 299792458 # m/s
antenna_line_loss = math.pow(10,-1/10)
atmo_loss = math.pow(10,0/10)

#if else statement w args
if len(sys.argv)==8:
    tx_w = float(sys.argv[1])
    tx_gain_db = float(sys.argv[2])
    freq_hz = float(sys.argv[3])
    dist_km = float(sys.argv[4])
    rx_gain_db = float(sys.argv[5])
    n0_j = float(sys.argv[6])
    bw_hz = float(sys.argv[7])
else:
    print(\
     'Usage: '\
     'max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz'\
    )
    exit()
    
# script starts here
wave_len=speed_of_light/freq_hz
C=tx_w * antenna_line_loss * tx_gain_db * (wave_len/(4*math.pi*dist_km*1000))**2  * atmo_loss * rx_gain_db
N=n0_j*bw_hz
rmax=bw_hz*math.log(1+C/N,2)

# print output
print(math.floor(rmax))