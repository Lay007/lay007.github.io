# Projects

This page summarizes the main engineering repositories and their proof assets.

## zynq-sdr-course

**Role:** SDR education and hardware experimentation platform.

**Engineering proof:**

- MkDocs course site;
- bilingual RU/EN structure;
- SDR measurement loop diagram;
- experiment manifests;
- HDL smoke direction;
- CI checks for documentation assets.

**Engineering chain:**

```text
model -> fixed-point -> FPGA -> RF frontend -> RTL-SDR -> IQ capture -> analysis -> report
```

Repository: https://github.com/Lay007/zynq-sdr-course

---

## cpp-dsp-showcase

**Role:** compact production-style C++ DSP showcase.

**Engineering proof:**

- deterministic C++ kernels;
- benchmark methodology;
- test-vector strategy;
- FIR implementation tradeoff notes;
- downstream CMake usage direction.

**Engineering chain:**

```text
reference vector -> C++ kernel -> numerical comparison -> benchmark -> report
```

Repository: https://github.com/Lay007/cpp-dsp-showcase

---

## network-quality-assessment

**Role:** hardware-assisted network measurement and SLA analytics concept.

**Engineering proof:**

- hardware timestamp datapath diagram;
- SLA dashboard;
- software vs hardware timestamp manifest;
- measurement credibility notes;
- SLA report template.

**Engineering chain:**

```text
probe traffic -> timestamp -> metrics -> SLA dashboard -> report
```

Repository: https://github.com/Lay007/network-quality-assessment

---

## optical-demodulator

**Role:** coherent optical DSP research workspace.

**Engineering proof:**

- coherent receiver pipeline;
- CDC comparison flow;
- BER/EVM/SNR methodology;
- CDC comparison manifest;
- IEEE-style paper outline.

**Engineering chain:**

```text
IQ dataset -> CDC -> synchronization -> decisions -> BER/EVM/SNR -> paper-ready report
```

Repository: https://github.com/Lay007/optical-demodulator

---

## script-toolbox

**Role:** repeatable engineering workstation automation.

**Engineering proof:**

- practical setup scripts;
- Windows / SSH / Git / CMake workflow direction;
- reusable operational notes.

Repository: https://github.com/Lay007/script-toolbox
