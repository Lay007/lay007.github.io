# Projects

This page summarizes the main engineering repositories, their proof assets and current limits.
Only public repositories are linked from the website.

## zynq-sdr-course

**Role:** SDR education and hardware experimentation platform.

**Engineering proof:**

- bilingual RU/EN MkDocs course site;
- executable DSP and synchronization labs with CI smoke checks;
- HDL regressions for Block 5 and Block 8 CSS Verilog;
- IQ recording workflows, dataset manifests and Git LFS checksum checks;
- in-fabric QPSK modem on Zynq-7020 + AD9361 closed on a two-board 915 MHz RF link (payload BER ≈4×10⁻⁴).

**Engineering chain:**

```text
model -> fixed-point -> FPGA -> RF frontend -> RTL-SDR -> IQ capture -> analysis -> report
```

**Open first:** [reviewer path](https://github.com/Lay007/zynq-sdr-course/blob/main/docs/reviewer-path.md),
[flagship reviewer report](https://github.com/Lay007/zynq-sdr-course/blob/main/reports/flagship_reviewer_report.md),
[course evidence map](https://github.com/Lay007/zynq-sdr-course/blob/main/reports/course-evidence-map.md).

**Current limit:** the raw QPSK RF recording stays local; its checksum, manifest, plots and metrics are public.

Repository: https://github.com/Lay007/zynq-sdr-course

---

## zynq-lora-phy-positioning

**Role:** LoRa PHY, FPGA timestamping, and positioning research platform on ZynqSDR.

**Engineering proof:**

- MATLAB floating-point model with M1 acceptance across all 32 SF5…SF12 × CR 4/5…4/8 modes;
- streaming fixed-point Simulink model with MATLAB-aligned regressions (M2);
- generated Verilog with exact 8/8 HDL cosimulation for ToA and a synthesized SF7 IQ-to-AXI timestamp receiver (M3);
- LoRa PHY Inspector for synthetic, HDL-generated, and recorded SX1262 IQ evidence;
- fractional ToA and calibrated 2D TDoA Monte Carlo results.

**Engineering chain:**

```text
LoRa model -> fixed-point -> HDL -> ZynqSDR -> IQ/metadata -> ToA -> TDoA
```

**Open first:** [MATLAB M1 acceptance](https://github.com/Lay007/zynq-lora-phy-positioning/blob/main/docs/matlab-m1-acceptance.md),
[Simulink M2 acceptance](https://github.com/Lay007/zynq-lora-phy-positioning/blob/main/docs/simulink-m2-acceptance.md),
[roadmap](https://github.com/Lay007/zynq-lora-phy-positioning/blob/main/docs/roadmap.md).

**Current limit:** hardware LoRa reception and synchronized multi-receiver positioning (M4–M6) have not started.

Repository: https://github.com/Lay007/zynq-lora-phy-positioning

---

## cpp-dsp-showcase

**Role:** compact production-style C++ DSP showcase.

**Engineering proof:**

- C++17 kernels: windowed-sinc FIR, Goertzel tone detection, GCC-PHAT delay estimation, rational L/M resampling;
- deterministic unit tests and multi-platform CI;
- optional AVX2 hot paths and generated benchmark reports;
- FIR implementation tradeoff notes;
- installable CMake package for downstream projects.

**Engineering chain:**

```text
reference vector -> C++ kernel -> numerical comparison -> benchmark -> report
```

**Open first:** [reviewer quick check](https://github.com/Lay007/cpp-dsp-showcase/blob/main/docs/reviewer-quick-check.md),
[algorithm evidence matrix](https://github.com/Lay007/cpp-dsp-showcase/blob/main/docs/algorithm-evidence-matrix.md).

Repository: https://github.com/Lay007/cpp-dsp-showcase

---

## network-quality-assessment

**Role:** hardware-assisted network measurement and SLA analytics concept.

**Engineering proof:**

- hardware timestamp datapath diagram;
- hardware-free synthetic SLA demo checked in CI;
- committed sample result package and filled report example;
- software vs hardware timestamp manifest and measurement credibility notes;
- reviewer acceptance checklist separating synthetic demos from hardware measurements.

**Engineering chain:**

```text
probe traffic -> timestamp -> metrics -> SLA dashboard -> report
```

**Open first:** [synthetic SLA demo](https://github.com/Lay007/network-quality-assessment/blob/master/docs/synthetic-sla-demo.md),
[reviewer acceptance checklist](https://github.com/Lay007/network-quality-assessment/blob/master/docs/reviewer-acceptance-checklist.md).

Repository: https://github.com/Lay007/network-quality-assessment

---

## script-toolbox

**Role:** repeatable engineering workstation automation.

**Engineering proof:**

- toolkits for Windows OpenSSH key-only access, Git + SSH onboarding, CMake and Visual Studio Build Tools;
- CI quality gates: PowerShell AST syntax check, Markdown link check, PSScriptAnalyzer;
- engineering safety model and script release checklist.

**Open first:** [CI quality gates](https://github.com/Lay007/script-toolbox/blob/main/docs/ci-quality-gates.md),
[engineering safety model](https://github.com/Lay007/script-toolbox/blob/main/docs/engineering-safety-model.md).

Repository: https://github.com/Lay007/script-toolbox

---

## optical-demodulator

**Role:** coherent optical DSP research workspace.

**Engineering proof:**

- coherent receiver pipeline across MATLAB, C++17 and Verilog layers;
- public synthetic CDC demo with BER/EVM/SNR/runtime plots;
- BER/EVM/SNR methodology and fixed-point error budget;
- CDC comparison manifest;
- IEEE-style paper outline.

**Engineering chain:**

```text
IQ dataset -> CDC -> synchronization -> decisions -> BER/EVM/SNR -> paper-ready report
```

**Repository status:** private. It is not linked from the website until it is published.
