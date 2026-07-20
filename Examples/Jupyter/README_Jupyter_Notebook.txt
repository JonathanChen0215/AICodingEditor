AICodingEditor V0.1.34 Jupyter Notebook Example

Open SinCos_Live_Notebook.ipynb in AICodingEditor. It opens in cell-text mode.
Choose Jupyter Run or Run Current to execute all code cells.
This sample uses only Python standard library math and prints AICE_VAR telemetry.


V0.1.35 nbformat repair test
--------------------------------
Notebook headers must use JSON integers:
  "nbformat": 4
  "nbformat_minor": 4
not decimals such as 4.0. When a notebook uses an integral decimal header,
AICodingEditor repairs the header before nbconvert runs and creates a timestamped
.aicodingeditor-backup-*.ipynb file in the notebook folder.
