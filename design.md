# Design – CR10

**Registration Number:** B23F0001SE028
**Change Request:** CR10
**Release:** R4
**Change:** Multi-crop price bands

## Proposed Design

The existing rate calculation routine will be examined before
modification. Its dependencies and current single-crop behaviour
will be documented. The routine will then be restructured carefully
so that crop-specific price bands can be introduced without changing
unrelated payment calculations.

The design will keep the existing single-crop calculation as the
default behaviour and apply the appropriate price band when a
farmer's delivery contains multiple crops.

## Test Plan

1. **Single-crop regression test:** Verify that existing single-crop
   payments remain unchanged after the modification.

2. **Multi-crop price-band test:** Verify that the correct price
   band is applied when a delivery contains multiple crops.

3. **Fractional-weight regression test:** Verify that calculations
   involving fractional weights still produce correct payment values.

4. **Multiple-delivery-slip regression test:** Verify that multiple
   delivery slips for the same farmer are processed correctly.

## Acceptance Criteria

- Existing single-crop payment calculations remain unchanged.
- Multi-crop deliveries use the correct price bands.
- Existing payment calculations do not regress.
- All planned tests pass before release.

## Design Risks

The rate routine is poorly structured and directly affects farmer
payments. Changes must be reviewed carefully, and regression tests
must be completed before deployment.
