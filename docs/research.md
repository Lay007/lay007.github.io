# Research and Engineering Focus

This portfolio is centered on reproducible engineering for communication and measurement systems.

## Main directions

| Direction | Focus | Repository |
|---|---|---|
| SDR systems | model-to-RF experimentation, IQ recording, synchronization, measurement reports | [zynq-sdr-course](https://github.com/Lay007/zynq-sdr-course) |
| LoRa PHY and positioning | CSS/LoRa receiver chain, fractional ToA, calibrated TDoA, FPGA timestamping | [zynq-lora-phy-positioning](https://github.com/Lay007/zynq-lora-phy-positioning) |
| Fixed-point DSP and FPGA | quantization, streaming RTL architectures, HDL cosimulation | `zynq-sdr-course`, `zynq-lora-phy-positioning` |
| C++ DSP | deterministic kernels, benchmarks, reusable libraries | [cpp-dsp-showcase](https://github.com/Lay007/cpp-dsp-showcase) |
| Network measurement | timestamp credibility, jitter, one-way delay, SLA analytics | [network-quality-assessment](https://github.com/Lay007/network-quality-assessment) |
| Coherent optical DSP | chromatic-dispersion compensation, BER/EVM/SNR analysis, receiver architecture | `optical-demodulator` (private) |

## Engineering methodology

```text
model
-> implementation
-> fixed-point
-> FPGA
-> measurement
-> report
-> reproducibility
```

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
- experiment and dataset manifests;
- hardware bring-up checklist;
- CI smoke checks for labs and HDL;
- in-fabric QPSK modem on a two-board 915 MHz RF link with payload BER ≈4×10⁻⁴.

## LoRa PHY and positioning direction

The `zynq-lora-phy-positioning` repository exposes the complete LoRa PHY chain and its timing measurements:

```text
MATLAB float model
-> streaming fixed-point Simulink
-> generated Verilog
-> ZynqSDR
-> ToA
-> TDoA
```

Key proof assets:

- MATLAB M1 acceptance across all 32 SF×CR modes, with BER/PER and calibrated 2D TDoA Monte Carlo results;
- Simulink M2 acceptance with MATLAB-aligned regressions;
- exact 8/8 HDL cosimulation for ToA and a synthesized SF7 IQ-to-AXI timestamp receiver.

Current limit: hardware reception and synchronized positioning have not started.

## Measurement systems direction

The `network-quality-assessment` repository focuses on the gap between software-observed and datapath-observed timing.

Key proof assets:

- hardware timestamp datapath diagram;
- synthetic SLA demo checked in CI;
- software vs hardware timestamp manifest;
- measurement credibility notes;
- SLA report template and filled example.

## Optical DSP direction

The `optical-demodulator` repository is currently private, so it is not linked from the public site.
It is intended to support paper-style work around:

- coherent receiver chains;
- chromatic-dispersion compensation;
- MATLAB/C++/RTL alignment;
- BER, EVM and SNR methodology;
- implementation tradeoffs.

## Engineering principles

- reproducible experiments;
- explicit metrics;
- shared datasets and test vectors;
- deterministic validation;
- publication-oriented visualization.

Every serious experiment should produce:

1. configuration;
2. reproducible data or manifest;
3. generated figure;
4. metric table;
5. engineering conclusion;
6. limitations and next step.
