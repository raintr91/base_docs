# #derived-data

SSOT (docs hub): [`product/shared/data-model/derived-data.md`](../../product/shared/data-model/derived-data.md)

Use when BE adds fields/tables not in FE spec for search, sort, compute, or snapshots.

Requirements: `backendOnly: true` · `sourceOfTruth` · `refresh` · `staleness` (if not realtime).  
Do not hide wrong relationship design with derived tables.

Grill: BE-only fields → ask member (add to contract / `#derived-data` / remove).
