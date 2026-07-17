# Integration structure

> Đối xứng [fast FAST-API-STRUCTURE](./FAST-API-STRUCTURE.md)

## Layer map

| Fast | Integration |
|------|-------------|
| router | Endpoints (Minimal API) |
| services | Application |
| clients (outbound) | — |
| presenters | Presenters |
| — | Infrastructure (MES/OPC) |

## Envelope

`Integration.Common.ApiResponse<T>` — `{ success, data, message }`

## Pilot

`GET /plants/{plantId}/downtime` → keys `plant_id`, `items[].machine_id`
