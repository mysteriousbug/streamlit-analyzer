# PAM Audit — Additional DA Use Cases

**Audit:** Privileged Access Management (2026-GT-XAXXX)  
**Prepared by:** Ananya Aithal | **Date:** 02 Apr 2026  
**Status:** Proposed — for discussion with Mo & Haidi

---

| # | Priority | Use Case | Scope Area | Data Source(s) | Key Fields / Logic | Expected Output |
|---|----------|----------|------------|----------------|--------------------|-----------------|
| 7 | 🔴 High | **EID Withdrawal Pattern Analysis** — Flag EID withdrawals used for BAU/routine work rather than genuine emergencies. Identify teams over-reliant on EIDs. | Release | EID Report | `REASON`, `SHORT DESCRIPTION`, `PRIORITY` (e.g. "4 – Low" on an EID = red flag), `ASSIGNMENT_GROUP` | Heatmap of EID misuse by team; list of low-priority tickets using emergency IDs |
| 9 | 🔴 High | **Session Recording Review Gap** — Calculate % of OV sessions actually reviewed, average review lag, and sessions never reviewed. | Release | OV_Logs | `Reviewed` (blank = unreviewed), `Reviewed Date` vs `Session End` delta | Review coverage %, lag distribution, unreviewed session listing |
| 5 | 🔴 High | **Unvaulted PID Aging Analysis** — Identify PIDs that remain unvaulted across consecutive monthly snapshots. Assess whether Catalyst vs Non-Catalyst tiering drives vaulting priority. | Identification & Vaulting | Consolidated_Unvaulted_Output (monthly) | `Status` = "PID Exception – Low Privilege", `Catalyst` flag, month-over-month delta | Aging report of persistently unvaulted PIDs; Catalyst vs Non-Catalyst breakdown |
| 8 | 🔴 High | **EID-to-Ticket Validation** — Verify every EID withdrawal maps to a valid SNOW ticket. Flag orphan withdrawals with missing/invalid references. | Release | EID Report | `TICKET NUMBER`, `Relationship INC/TAS` — check for nulls, invalid formats | List of unaccounted EID withdrawals with no valid ticket |
| 12 | 🟠 Medium | **Dormant PID Detection** — Cross-reference PID inventory against retrieval/session activity. Flag PIDs with zero usage over 6–12 months. | Recertification | PID_Retrieval_Report, OV_Logs, Managed Account Listing | Join on account/system; filter for zero retrievals in lookback window | Dormant PID listing with last-use date and owner |
| 10 | 🟠 Medium | **Protocol & File-Size Anomaly Detection** — Flag sessions with abnormal duration-to-file-size ratios (potential data exfiltration). | Release | OV_Logs | `Protocol`, `Duration`, `File Size`, `Session Start/End` | Anomaly-scored session list ranked by exfiltration risk |
| 13 | 🟠 Medium | **EID Withdrawal Trend & KRI Benchmarking** — Build time-series of EID volumes and compare against defined KRIs. Assess whether risk posture is improving from the historic baseline. | Risk Management | EID Report | `RETRIEVE DATE-UKT` aggregated weekly/monthly; compare to KRI thresholds | Trend chart + KRI compliance summary for Mo |
| 6 | 🟡 Low | **Vaulting Platform Consistency** — Check whether OneVault vs HashiCorp Vault assignment follows a policy-driven pattern by platform (Oracle, MSSQL, Mongo, etc.). | Identification & Vaulting | Consolidated_Unvaulted_Output | `Status` (Vaulted in OneVault / HCV), `CI_Type`, `CI_Sub_Type` | Platform-to-vault mapping matrix; fragmentation exceptions |
| 11 | 🟡 Low | **Splunk Detection Coverage vs PID Inventory** — Map Splunk correlation rules to PID categories. Identify high-risk PIDs (Catalyst, Oracle/MSSQL) with no monitoring rule. | Reconciliation | Active_Use_Cases, Consolidated_Unvaulted_Output | `action.correlationsearch.label` mapped against `CI_Type` + `Catalyst` | Monitoring gap matrix; unmonitored Catalyst PID count |

---

**Recommendation:** Prioritise Use Cases 7, 9, 5, and 8 for immediate development — they directly address the core risk themes (EID misuse, session accountability, vaulting completeness) and the data is readily available. Use Cases 12, 10, and 13 can follow as stretch targets depending on data quality and timeline.
