Changelog
=========


0.1 (unreleased)
----------------

- Add packaging-files like ``setup.py``, ``setup.cfg``, ``MANIFEST.in``
  [WouterVH]

- Fix thread-safety issues with the DescriptorManager.
  Fixes https://github.com/lameiro/cx_oracle_on_ctypes/issues/8
  [lameiro / K0Te]

- Fix ``StatementError: 'module' object has no attribute 'Binary'`` in SqlAlchemy.
  Fixes https://github.com/lameiro/cx_oracle_on_ctypes/issues/6
  [lameiro]

- Support ``kwargs`` for sid and service name. Fixes sqlalchemy ``create_engine``.
  Fixes https://github.com/lameiro/cx_oracle_on_ctypes/issues/5
  [lameiro / muxueqz]

- Compatibility with oracle 12.
  Fixes https://github.com/lameiro/cx_oracle_on_ctypes/issues/4
  [lameiro]

- Fix type in ``OCILobIsTemporary``-function-call.
  Fixes https://github.com/lameiro/cx_oracle_on_ctypes/issues/2
  [K0Te]

- Fix error on windows.
  Fixes https://github.com/lameiro/cx_oracle_on_ctypes/issues/2
  [lameiro]

- Initial implementation
  [lameiro]