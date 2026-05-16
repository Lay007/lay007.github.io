# Engineering Proof Assets

This page collects concrete proof assets across the portfolio.

## Portfolio proof matrix

| Proof asset | Repository | What it demonstrates |
|---|---|---|
| SDR experiment manifests | `zynq-sdr-course` | reproducible lab objectives, metadata and acceptance criteria |
| SDR measurement loop SVG | `zynq-sdr-course` | model-to-hardware-to-report engineering flow |
| Markdown asset CI | `zynq-sdr-course` | documentation quality and broken-link prevention |
| DSP test-vector strategy | `cpp-dsp-showcase` | deterministic validation direction |
| Benchmark baseline schema | `cpp-dsp-showcase` | reproducible performance reporting |
| Direct FIR vs overlap-save notes | `cpp-dsp-showcase` | algorithmic tradeoff explanation |
| SLA dashboard | `network-quality-assessment` | measurement-oriented report UX |
| Timestamp comparison manifest | `network-quality-assessment` | hardware vs software timing credibility |
| CDC comparison flow | `optical-demodulator` | optical DSP method comparison |
| IEEE-style paper outline | `optical-demodulator` | publication-oriented research structure |

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
| SDR education | `zynq-sdr-course` | MkDocs, labs, manifests, CI checks |
| C++ DSP | `cpp-dsp-showcase` | tests, benchmarks, vectors, tradeoff docs |
| Network measurement | `network-quality-assessment` | timestamping, SLA reports, dashboards |
| Optical DSP research | `optical-demodulator` | CDC, BER/EVM/SNR, paper scaffold |

## Next website improvements

- add visual project cards using these proof assets;
- add a downloadable CV;
- add Open Graph preview image;
- add a dedicated projects page;
- add a research page with optical DSP and SDR focus.
