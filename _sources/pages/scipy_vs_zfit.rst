.. _scipy-vs-zfit:

SciPy vs zfit
=============

zfit is a model fitting library with strong and flexible model building capabilities.
SciPy is a more general library with a lot broader functionality, that has also limited distributions
and minimization capabilities.

While the SciPy capabilities are good for simple fits, the library has a few shortcomings that zfit implements:



- extendability: while distributions can be added to scipy, only analytical integrable distributions can. zfit
  can deal with any function and applies numerical methods to it.
- compositions: zfit contains pdfs such as sums and products that build a new distribution out of others.
- speed: with TensorFlow as the backend, zfit can be a factor of 10-100 faster than comparable fits in scipy
- mulitple dimensions are handled consistently in zfit
- consistent design: the fitting workflow of zfit contains 5 elementary pieces - data, model, loss, minimizer, fitresult -
  which are all maximally decoupled and can be exchanged arbitrarily.

There are many more, smaller advantages such as parameters, different normalization ranges and more. There is
no disadvantage in using zfit compared to scipy to do a simple fit and it is straightforward to extend it to anything more
complicated due to the composite design of zfit structures.
