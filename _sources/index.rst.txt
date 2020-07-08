

================================
zfit: scalable, pythonic fitting
================================


|zfit_logo|

**How it works**: click on the links or the images to explore zfit.

What is zfit?
-------------

zfit is a (likelihood) model fitting library. Hereby, model refers to analytic distributions
such as a Normal, Poisson. (`This is similar to SciPy distributions and fitting, why zfit? <scipy_vs_zfit>`_)

|tutorial10|

It is built to be powerful and flexible enough to satisfy the
strong requirements of High Energy Physics, but is a general purpose library. It focuses strongly on two points,
namely:

- performance: it is built on top of the *low-level* components of TensorFlow. This is an
  mathematical library very similar to Numpy but with the native ability to compile
  parts and imply various optimizations, including GPU support and automatic gradients.
- customizability of models: While comparable libraries offer usually a limited set of
  model combinations or the possibility to implement custom models, zfit supports `a variety of
  composed and multidimensional distributions <https://mybinder.org/v2/gh/zfit/zfit-tutorials/9fc3fb862f078d4
  10288142a354c78edfa0d0b05?filepath=20%20-%20Composite%20Models.ipynb>`_, such as
  products and sums, out-of-the-box.
  Implementing a custom model with your own function
  (`you can try your own shape  <https://mybinder.org/v2/gh/zfit/zfit-tutorials/9fc3fb862f078d410288142a354c78edfa0d0b05?filepath=60%20-%20Custom%20PDF.ipynb>`_)
  is straightforward and allows for arbitrary
  complicated functions - even functions reaching thousands of lines of code;
  if analytical methods for integration and sampling are not
  available, it automatically falls back to numerical methods. No further care needs to
  be taken by the user therefore.

.. |zfit_logo| image:: images/zfit-fin_400x168.png
   :target: https://github.com/zfit/zfit

.. |tutorial10| image:: images/gauss_fit.png
   :target: https://mybinder.org/v2/gh/zfit/zfit-tutorials/9fc3fb862f078d410288142a354c78edfa0d0b05?filepath=10%20-%20Introduction%20to%20zfit.ipynb
   :alt: zfit logo