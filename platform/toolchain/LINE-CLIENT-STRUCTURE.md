# Line client structure

> Đối xứng [portal ARCHITECTURE](~/workspace/portal/docs/operational/ARCHITECTURE.md)

## Layer map

| Portal | Line |
|--------|------|
| `app/components` | `Forms` / `Kiosk` |
| `hooks` | `ViewModels` |
| `services` | `Services` |
| `@portal/models` | `Line.Contracts` |
| `apiFetch` | `Line.Common.Http.ApiClientBase` |

## Envelope

Parse `{ success, data, message }` — khớp fast `api_response.py`.

## AutomationId

Đối xứng `data-testid`: `workforce-check-in-*`

## Pilot

Workforce check-in → `POST /api/workforce/check-in`
