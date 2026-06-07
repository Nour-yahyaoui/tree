# treepy

Errors are reported once and do not stop the walk.

## Notes

The JSON document carries a version so consumers can check it.
The exit code is one when anything failed.
Colour is decided in a single place so the rest stays testable.
Keeping this small makes the behaviour easy to reason about.
