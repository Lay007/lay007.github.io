# Research Focus

This portfolio is centered on reproducible engineering for communication and measurement systems.

## Main research directions

| Direction | Focus |
|---|---|
| Coherent optical DSP | chromatic-dispersion compensation, BER/EVM/SNR analysis, receiver architecture |
| SDR systems | model-to-RF experimentation, IQ recording, synchronization, measurement reports |
| Fixed-point DSP | implementation error, quantization, FPGA-ready architectures |
| C++ DSP | deterministic kernels, benchmarks, reusable libraries |
| Network measurement | timestamp credibility, jitter, one-way delay, SLA analytics |

## Optical DSP direction

The `optical-demodulator` repository is intended to support paper-style work around:

- coherent receiver chains;
- chromatic-dispersion compensation;
- MATLAB/C++/RTL alignment;
- BER, EVM and SNR methodology;
- implementation tradeoffs.

Key proof assets:

- CDC comparison flow;
- CDC comparison manifest;
- BER/EVM/SNR report template;
- IEEE-style paper outline.

## SDR direction

The `zynq-sdr-course` repository turns SDR learning into a reproducible engineering path:

```text
signal theory
-> modeling
-> fixed-point
-> HDL/FPGA
-> RF frontend
-> IQ recording
-> metrics
-> report
```

Key proof assets:

- MkDocs course site;
- SDR measurement loop diagram;
- experiment manifests;
- hardware bring-up checklist;
- CI asset checks.

## Measurement systems direction

The `network-quality-assessment` repository focuses on the gap between software-observed and datapath-observed timing.

Key proof assets:

- hardware timestamp datapath diagram;
- SLA dashboard;
- software vs hardware timestamp manifest;
- measurement credibility notes;
- SLA report template.

## Engineering principle

Every serious experiment should produce:

1. configuration;
2. reproducible data or manifest;
3. generated figure;
4. metric table;
5. engineering conclusion;
6. limitations and next step.
