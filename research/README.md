# SpaceY Orbit Lab

For a circular orbit, speed is sqrt(mu/r) and period is 2*pi*sqrt(r^3/mu), with r the Earth-centred radius. This simple two-body model neglects drag, oblateness and all other perturbations. It does not assess whether an orbit is practically sustainable. It is for education, not mission operations.

References: [NASA orbital mechanics](https://science.nasa.gov/learn/basics-of-space-flight/chapter3-3/), [NASA/JPL astrodynamic parameters](https://ssd.jpl.nasa.gov/astro_par.html).

From repository root run `python3 research/orbit.py --altitude-km 400` and `python3 -m unittest discover -s tests -v`.
