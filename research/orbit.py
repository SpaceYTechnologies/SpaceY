"""Educational ideal circular Earth orbit estimator; not for operational navigation."""
import argparse
import math

EARTH_RADIUS_KM = 6378.137  # approximate equatorial radius
EARTH_MU = 398600.435507  # km^3/s^2; NASA/JPL https://ssd.jpl.nasa.gov/astro_par.html


def circular_orbit(altitude_km):
    if not math.isfinite(altitude_km) or altitude_km <= 0:
        raise ValueError("Altitude must be finite and positive")
    r = EARTH_RADIUS_KM + altitude_km
    return math.sqrt(EARTH_MU / r), 2 * math.pi * math.sqrt(r**3 / EARTH_MU) / 60


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--altitude-km', type=float, required=True)
    args = parser.parse_args()
    try:
        speed, period = circular_orbit(args.altitude_km)
    except ValueError as exc:
        parser.error(str(exc))
    print(f'Ideal circular speed: {speed:.4f} km/s')
    print(f'Ideal orbital period: {period:.2f} minutes')
