================================
zfit: scalable, pythonic fitting
================================


|zfit_logo|

**How it works**: click on the links or the images to explore zfit.

What is zfit?
-------------

zfit is a (likelihood) model fitting library. Hereby, model refer to analytic distributions
such as a Normal, Poisson. It is enspired to be powerful and flexible enough to satisfy the
strong requirements in High Energy Physics, but is a general purpose library. It focuses strongly on two points,
namely:

- performance: it is built on top of the *low-level* components of TensorFlow. This is an
  mathematical library very similar to Numpy but with the native ability to compile
  parts and imply various optimizations, including GPU support and automatic gradients.
- customizability of models: While comparable libraries offer usually a limited set of
  model combinations or the possibility to implement custom models, zfit supports
  products, sums and muldidimensional distributions out-of-the-box.
  Furthermore, implementing a custom model is straightforward and allows for arbitrary
  complicated functions; if analytical methods for integration and sampling are not
  available, it falls back to numerical methods.

.. |zfit_logo| image:: website/images/zfit-fin-hires.png
   :target: https://github.com/zfit/zfit

.. |tutorial10| image:: website/images/gauss_fit.png
   :target: https://mybinder.org/v2/gh/zfit/zfit-tutorials/9fc3fb862f078d410288142a354c78edfa0d0b05?filepath=10%20-%20Introduction%20to%20zfit.ipynb
   :alt: zfit logo