# Constants for heat index calculation (from the NOAA formula)
T = 32  # Temperature in Celsius
H = 77  # Relative humidity in percent

# Using the approximation formula for Heat Index in Celsius
c1 = -8.78469475556
c2 = 1.61139411
c3 = 2.33854883889
c4 = -0.14611605
c5 = -0.012308094
c6 = -0.016424828
c7 = 0.002211732
c8 = 0.00072546
c9 = -0.000003582

# Heat index formula calculation
heat_index = c1 + (c2 * T) + (c3 * H) + (c4 * T * H) + (c5 * T**2) + (c6 * H**2) + (c7 * T**2 * H) + (c8 * T * H**2) + (c9 * T**2 * H**2)
heat_index
