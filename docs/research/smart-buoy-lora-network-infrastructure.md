# Smart Buoy LoRa Network Infrastructure

## Data path to a PHP/MySQL server

The recommended endpoint is:

```text
POST https://iot.philipmcgaw.com/data/
```

Telemetry should be sent in the request body rather than as a GET query string. This avoids URL length limits, proxy/server logging of telemetry and signatures, caching, and accidental replay.

A suitable request is:

```http
Content-Type: application/octet-stream
X-Device-ID: buoy-001
X-Sequence: 1842
X-Signature: <HMAC-SHA256 signature>
```

The body can contain a compact binary packet or a Base64URL-encoded packet where necessary. A packet should contain a version, device ID, sequence number, timestamp, payload, CRC, and cryptographic signature.

A CRC detects accidental corruption. An HMAC-SHA256 signature authenticates the device and detects deliberate modification. The signature should cover the device ID, sequence number, timestamp, and complete payload. The server should reject old sequence numbers or timestamps to prevent replay attacks.

The PHP endpoint should:

1. Receive the HTTPS POST.
2. Verify the device authentication and HMAC.
3. Verify the CRC.
4. Reject duplicate sequence numbers.
5. Decode the measurements.
6. Insert the raw packet and decoded measurements into MySQL/MariaDB using PDO prepared statements.
7. Return a short JSON acknowledgement.

```json
{
  "accepted": true,
  "device_id": "buoy-001",
  "sequence": 1842
}
```

Store both the original raw packet and the decoded values. This preserves evidence for troubleshooting and allows the decoder to be improved later.

Recommended read-only endpoints are:

```text
GET /data/latest.php
GET /data/history.php
GET /data/export.php?from=...&to=...
```

A telemetry table should include the device ID, sequence number, captured timestamp, server receipt timestamp, transport, radio metadata, raw payload, decoded measurements, and a unique constraint on `(device_id, sequence_number)`.

The overall path is:

```text
Buoy radio package
  → HTTPS POST
  → PHP ingestion endpoint
  → MySQL/MariaDB
  → PHP API, dashboard, or CSV export
```
