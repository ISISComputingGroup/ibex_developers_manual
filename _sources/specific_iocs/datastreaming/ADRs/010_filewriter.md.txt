# 10 - File writer implementation

## Status

Accepted in a meeting 11/09/2026 with Tom W, Jack H, Freddie A, George R, Martyn G, Sudeepta C, Dan N, Dan K.

## Context

In the context of the data streaming project targeting HRPD-X, SANDALS2, WISH2, and other endeavour instruments,
we need to implement a filewriter for HRPD-X that listens to Kafka messages and writes a corresponding NeXus file in
the expected ISIS NeXus format.

Requirements were written and discussed with relevant consumers (including Mantid and GudRun developers), along with
MNeuData developers.

Three main implementation options were considered:
- Using the ESS filewriter as a technical baseline
- Using the SuperMuSR filewriter as a technical baseline
- A greenfield development

Documents describing what each implementation approach would look like are detailed [here](https://github.com/ISISComputingGroup/DataStreaming/tree/filewriter_evaluation/filewriter_evaluation). Feedback on these documents
was sought from both the SuperMuSR and ESS teams. The ESS option was discussed in detail with the ESS DMSC team on
9/9/2026.

## Decision

The decision is that we will implement a filewriter using the greenfield approach, documented [here](https://github.com/ISISComputingGroup/DataStreaming/blob/filewriter_evaluation/filewriter_evaluation/greenfield.md).

It is likely that the SuperMuSR team will collaborate with us on this filewriter, with the eventual aim of this becoming
the unified ISIS filewriter for both Neutron instruments and SuperMuSR.

We will stick with the proven high-level approach that the ESS filewriter uses: a pooled filewriter with a dynamic NeXus structure and 'writer modules' describing how to write a specific part of a NeXus file.

Where advantageous, we will re-use technical patterns and ideas from the ESS filewriter, the SuperMuSR filewriter, and the prototype Rust ESS filewriter.

## Alternatives rejected

- Using the SuperMuSR filewriter as the technical baseline was rejected because its current functionality was seen as
a relatively poor fit for our requirements on the Neutron side. Large refactors would have been needed in multiple areas.
It was generally seen as a more favourable route for the SuperMuSR team to collaborate with us on the greenfield option
rather than incrementally refactoring the existing SuperMuSR filewriter.
- Using the ESS filewriter as the technical baseline was rejected because:
  - It is already being considered 'legacy' code by the ESS, with a partial re-write already in progress, and low likelihood of still being in use in several years.
It is highly likely that we would be developing on a local fork, where the upstream may then be abandoned in favour of the ESS rewrite.
  - Significant refactoring would still be required (though substantially less than the SuperMuSR option)
  - Less standard technology fit (C++) than either the SuperMuSR or greenfield options (Rust)
  - Full cross-facility collaboration was seen to be risky on the timescales required for HRPD-X

Other options considered in less detail included:
- CLF filewriter: the [CLF schemas](https://github.com/CentralLaserFacility/epac-flatbuffer-formats/tree/bf1813b87126daa072cc7577152e22afe99b1d0c/schemas) and file formats are very different to the Neutron needs, to the point where it is unlikely that adopting a CLF filewriter would form a suitable technical baseline for our requirements.
- ESS Rust prototype filewriter: this is in a very early stage of development; too early to sensibly use it as a technical baseline. However, it may contain useful
technical ideas or patterns that we may re-use in our greenfield development.

## Consequences

- We will need to implement a filewriter from scratch, using the greenfield approach
- ISIS will remain in full control of the file writing code
- Assuming that, in time, SuperMuSR are able to migrate to this filewriter, ISIS as a facility will only need to maintain
one file writer.
