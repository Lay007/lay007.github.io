# Engineering Proof Assets

This page collects concrete proof assets across the portfolio.

## Portfolio proof matrix

| Proof asset | Repository | What it demonstrates |
|---|---|---|
| Two-board QPSK RF link | `zynq-sdr-course` | in-fabric modem on Zynq-7020 + AD9361, payload BER ≈4×10⁻⁴ at 915 MHz |
| Reviewer path and evidence map | `zynq-sdr-course` | proven artifacts, gaps and reproduction commands |
| SDR experiment manifests | `zynq-sdr-course` | reproducible lab objectives, metadata and acceptance criteria |
| Markdown asset CI | `zynq-sdr-course` | documentation quality and broken-link prevention |
| MATLAB M1 acceptance report | `zynq-lora-phy-positioning` | 32 SF×CR modes, BER/PER, calibrated 2D TDoA Monte Carlo |
| HDL cosimulation and synthesis evidence | `zynq-lora-phy-positioning` | exact 8/8 ToA cosimulation, receiver synthesized for `xc7z020clg400-2` |
| DSP test-vector strategy | `cpp-dsp-showcase` | deterministic validation direction |
| Benchmark baseline schema | `cpp-dsp-showcase` | reproducible performance reporting |
| Direct FIR vs overlap-save notes | `cpp-dsp-showcase` | algorithmic tradeoff explanation |
| Synthetic SLA demo in CI | `network-quality-assessment` | reproducible report pipeline without hardware |
| Timestamp comparison manifest | `network-quality-assessment` | hardware vs software timing credibility |
| PowerShell quality gates | `script-toolbox` | AST syntax check, Markdown links, PSScriptAnalyzer |
| CDC comparison flow | `optical-demodulator` (private) | optical DSP method comparison |
| IEEE-style paper outline | `optical-demodulator` (private) | publication-oriented research structure |

## Engineering story

The repositories are connected by one method:

```text
model
-> implementation
-> fixed-point or hardware constraints
-> measurement
-> metrics
-> report
-> reproducibility
```

## Main domains

| Domain | Main repository | Key evidence |
|---|---|---|
| SDR education | `zynq-sdr-course` | MkDocs, labs, manifests, CI checks, RF link metrics |
| LoRa PHY and positioning | `zynq-lora-phy-positioning` | acceptance reports, HDL cosimulation, synthesis evidence |
| C++ DSP | `cpp-dsp-showcase` | tests, benchmarks, vectors, tradeoff docs |
| Network measurement | `network-quality-assessment` | timestamping, SLA reports, dashboards |
| Optical DSP research | `optical-demodulator` (private) | CDC, BER/EVM/SNR, paper scaffold |

## Website status

Done:

- project cards with evidence statements and "open first" links;
- 10-minute reviewer page linked from the main page, with evidence links, limits and Open Graph metadata;
- Open Graph preview image rendered from `tools/social-preview.html`;
- mobile version of the engineering pipeline diagram;
- static validator for links, anchors, metadata and sitemap, plus a weekly external link check.

Open:

- add a downloadable CV;
- add dates and organizations to the Background section;
- replace the "R&D" metric with concrete publication and patent counts;
- export higher-resolution project covers (1280×720);
- publish `optical-demodulator` and add it to the site, or keep it out of the public narrative;
- add dedicated projects/research HTML pages if these Markdown notes become public-facing.
