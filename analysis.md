# Analysis – CR10

**Registration Number:** B23F0001SE028
**Change Request:** CR10
**Release:** R4
**Effort:** 55 hours
**Category:** Perfective

## Reason for Change

The cooperative board requested multi-crop price bands (REQ-66).
The existing rate routine was too tangled to extend directly,
so it required internal cleanup before the new functionality
could be implemented.

## Components Likely to Be Affected

- Rate calculation routine
- Crop pricing and rate-band logic
- Farmer payment advice generation
- Regression-sensitive payment calculations

## Maintenance Approach

The existing rate routine should first be examined and its
dependencies understood. Its structure can then be improved
carefully before introducing multi-crop price-band functionality.

## Effort and Risk

The estimated effort is 55 hours, the highest among the
14 recorded change requests. The change carries significant
regression risk because the rate routine is critical to
payment calculations. A defect could affect farmer payments.

Regression testing should cover existing single-crop
calculations, multiple delivery slips, fractional weights,
and the new multi-crop price bands.

## Risk Assessment

Risk level: High

The rate routine is sensitive because it directly affects
farmer payment calculations. The system has no available
specification, and the previous rate-routine fix required
three weeks of testing before it was trusted (PROFILE F2, F6).
Therefore, the cleanup and new functionality should be
introduced cautiously, with regression testing before release.
