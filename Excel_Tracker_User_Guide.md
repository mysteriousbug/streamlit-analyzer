# AI/LLM Security Learning Path - Excel Tracker User Guide

## Overview

This Excel workbook tracks the progress of all 16 Information & Cybersecurity team members through the AI/LLM security learning path. It has automated summary calculations and is designed for easy weekly updates.

**File Name:** `AI_Learning_Path_Team_Tracker.xlsx`  
**Sheets:** 1 (Team Progress)  
**Update Frequency:** Weekly (recommended)  
**Shared With:** All 16 team members + Mo (manager)

---

## Sheet Structure: "Team Progress"

The tracker is organized into **3 sections** corresponding to the learning path:

### SECTION 1: ENTRY-LEVEL TRAINING (Rows 4-24)
**Mandatory for all 16 team members | Weeks 1-2**

**Columns:**
- **A:** Team Member Name (pre-populated with "Team Member 1" - "Team Member 16")
- **B:** Overall Status → Options: "Not Started" | "In Progress" | "Completed"
- **C-G:** Individual training completion (OWASP Top 10, MITRE ATLAS, RAND Guide, NIST AI RMF, Google SAIF)
  - Values: "Pending" | "In Progress" | "Completed"
- **H:** Attestation Date (manual entry: date when all 5 trainings completed)
- **I:** Notes (optional: any blockers, questions, etc.)

**Automated Summary (Row 24):**
- "Total Completed": Counts how many team members have status = "Completed"
- "% Complete": Divides total completed by 16; displays as percentage

**How to Update:**
1. Each team member updates their own row (A-I) weekly
2. Change **Column B** status from "Not Started" → "In Progress" → "Completed"
3. Update individual training columns (C-G) as completed
4. Enter **Attestation Date (H)** when all 5 trainings done
5. Optional: Add notes in column I

**Example:**
```
Row 6: Team Member 1 | In Progress | Completed | Completed | Pending | In Progress | Pending | [blank] | Waiting for NIST login
```

**Success Criteria for Section 1:**
- All 16 team members with "Completed" status in Column B
- "% Complete" = 100%
- Attestation dates filled for all

---

### SECTION 2: HANDS-ON LABS (Rows 27-46)
**Mandatory for all 16 team members | Weeks 4-8**

**Columns:**
- **A:** Team Member Name
- **B:** Overall Status → Options: "Not Started" | "In Progress" | "Completed"
- **C-G:** Lab completion by group
  - Labs 1-3 (Prompt Injection) | Labs 4-6 (Model & Data Attacks) | Labs 7-9 (Supply Chain) | Labs 10-12 (Agent & Autonomy) | Labs 13-15 (Integration & Capstone)
  - Values: "Not Started" | "In Progress" | "Completed"
- **H:** Capstone Exercise → Options: "Pending" | "Submitted" | "Passed"
- **I:** CAISP Exam → Options: "Not Taken" | "In Progress" | "Passed"
- **J:** Certification Date (manual entry: date when CAISP exam passed)
- **K:** Notes

**Automated Summary (Row 46):**
- "Capstone Submitted": Counts how many have "Submitted" or "Passed" in Column H
- "CAISP Certified": Counts how many have "Passed" in Column I
- "% Certified": Certified count / 16; displays as percentage

**How to Update:**
1. Each team member updates their own row weekly
2. Update **Column B** as progress moves from "Not Started" → "In Progress" → "Completed"
3. Update individual lab group columns (C-G) as labs completed
4. Update **Capstone (H)**: "Pending" → "Submitted" → "Passed"
5. Update **CAISP Exam (I)**: "Not Taken" → "In Progress" → "Passed"
6. Enter **Cert Date (J)** when exam passed
7. Add notes (K) as needed

**Example:**
```
Row 7: Team Member 2 | In Progress | Completed | Completed | In Progress | Pending | Pending | Submitted | In Progress | [blank] | Completed labs 1-6, waiting on lab 7
```

**Success Criteria for Section 2:**
- All 16 team members with "Completed" status in Column B
- All 16 with "Passed" in Capstone (H)
- All 16 with "Passed" in CAISP Exam (I)
- "% Certified" = 100%

---

### SECTION 3: OPTIONAL CERTIFICATIONS (Rows 49-68)
**Optional | Timeline: Weeks 8-12 (post-labs)**

**Columns:**
- **A:** Team Member Name
- **B:** Pursuing? → Options: "Yes" | "No"
- **C:** Modern Security Cert Status → Options: "Not Started" | "In Progress" | "Completed"
- **D:** Certification Date (manual entry: date when cert earned)
- **E:** Notes

**Automated Summary (Row 68):**
- "Pursuing Modern Security Cert": Counts how many have "Yes" in Column B

**How to Update:**
1. Only team members pursuing optional cert update this section
2. Update **Column B**: "No" → "Yes"
3. Update **Column C** as progress: "Not Started" → "In Progress" → "Completed"
4. Enter **Cert Date (D)** when completed
5. Add notes (E)

**Example:**
```
Row 8: Team Member 3 | Yes | In Progress | [blank] | 40 hours completed, taking exam next week
Row 9: Team Member 4 | No | Not Started | [blank] | [blank]
```

**Note:** This section is informational; no mandatory targets.

---

## Color Coding

**Status Indicators:**
- **Red background** (Columns B only): "Not Started" = incomplete, needs action
- **Yellow background** (when applicable): "In Progress" = work ongoing, on track
- **Green text** (Summary rows): Automated counts and percentages

**Blue headers:** Column titles and section breaks

---

## Weekly Update Workflow (Recommended)

### Monday-Wednesday (Self-Update):
Each team member spends 2-5 minutes:
1. Open tracker
2. Update their row(s) with current progress
3. Add notes if any blockers
4. Save file

### Thursday or Friday (Mo's Review):
Mo (manager) spends 10 minutes:
1. Open tracker
2. Review **Summary rows**:
   - Entry-Level % Complete (Row 24)
   - Capstone Submitted % (Row 46)
   - CAISP Certified % (Row 46)
3. Check for blockers or slow progress (marked in Notes columns)
4. Optional: Send team Slack update with progress snapshot

### Escalation Triggers (For Mo):
- **Week 2:** Entry-Level % Complete < 50% → Nudge team
- **Week 6:** Lab Capstone Submitted < 30% → Check for platform access issues
- **Week 10:** CAISP Certified < 80% → Monitor exam prep

---

## How to Interpret Key Metrics

### Entry-Level % Complete (Row 24, Column D)
- **Target:** 100% by end of Week 2
- **< 50%:** Team members not starting; may need access troubleshooting
- **50-99%:** Normal progression; some members behind schedule
- **100%:** Complete; team ready for labs phase

### CAISP Certification % (Row 46, Column F)
- **Target:** 100% by end of Week 8
- **0-25%:** Early labs phase; expected
- **25-50%:** Mid-labs phase; ensure no access issues
- **50-100%:** Labs complete; exams underway
- **100%:** All certified; ready for capstone exercise review

### Optional Cert Pursuit Count (Row 68, Column B)
- **Expected:** 3-5 team members (optional)
- **> 5:** Good adoption; specialization interest high
- **0-2:** Normal; specialized interest varies

---

## Common Questions

### Q: Can team members edit other people's rows?
**A:** Yes, by design. It's a shared tracker. However, recommend:
- Honor system: only update your own row
- Mo can audit tracker for accuracy if needed
- Use Notes column if concerns about self-reporting

### Q: What if someone is sick/on leave?
**A:** Mark their row with note "On leave until [DATE]"
- Exclude from weekly count metrics during leave
- Update Row 24 formula if needed to adjust denominator

### Q: Can we add more columns for additional tracking?
**A:** Yes. Insert columns after Section 3 (after Row K) without affecting formulas.
- Example: Add "Lab Partner" or "Blocker Status" columns
- Do NOT modify formulas in summary rows (24, 46, 68)

### Q: What date format should we use?
**A:** Recommendation: DD-MMM-YYYY (e.g., "27-Mar-2026")
- Consistent across all date columns (H, J, D)
- Easier to read and sort

### Q: How often should we backup this file?
**A:** Recommend weekly:
- Save as versioned backup: `AI_Learning_Path_Team_Tracker_Week01.xlsx`, `Week02.xlsx`, etc.
- Keeps history in case of accidental deletion
- Easy to compare week-to-week progress

---

## Excel Formula Reference (For Mo or IT Support)

**If formulas need repair/modification, here are the current formulas:**

### Summary Formulas (Used in Automated Counts)

**Row 24 - Entry-Level Summary:**
- B24: `=COUNTIF(B6:B21,"Completed")` → Count of "Completed" statuses
- D24: `=B24/16` → Percentage complete

**Row 46 - Labs Summary:**
- B46: `=COUNTIF(H29:H44,"Yes")` → Count capstone submissions
- D46: `=COUNTIF(I29:I44,"Yes")` → Count CAISP certifications
- F46: `=D46/16` → Percentage certified

**Row 68 - Optional Cert Summary:**
- B68: `=COUNTIF(B51:B66,"Yes")` → Count pursuing optional certs

**Note:** All formulas use exact row ranges. If rows are inserted/deleted, formulas must be updated manually.

---

## Troubleshooting

### Issue: Summary numbers not updating
**Solution:** 
1. Ensure cells are formatted as text values (not links or formulas)
2. Manually edit a cell in the tracked range (e.g., change "In Progress" to "In Progress")
3. Press Enter; formulas should recalculate
4. If still not working: Click formula cell (e.g., B24) → Press F2 → Press Enter

### Issue: File is slow to open
**Solution:**
1. Ensure file is saved locally (not on slow network drive)
2. Close all other Excel files
3. If persistent: Save as new file with `Save As` → `Excel Workbook (.xlsx)`

### Issue: Teammate can't see latest updates
**Solution:**
1. Close and reopen file
2. Ensure all teammates have saved their changes
3. Consider using shared drive with consistent naming (e.g., shared OneDrive folder)
4. Email new version to all teammates after major updates

---

## Tips for Success

1. **Set Reminder:** Assign someone (e.g., a team member on rotation) to send weekly Slack reminder: "Update tracker by Friday EOD"

2. **Public Recognition:** Celebrate milestones in team channel:
   - "🎉 Entry-Level Training 100% Complete!"
   - "🔐 First 5 team members earned CAISP certification!"
   - "✅ All 16 team members passed CAISP exam!"

3. **Peer Accountability:** Share summary snapshot in team standup:
   - Show bar chart of % complete per section
   - Recognize top performers

4. **Bottleneck Early Detection:** Review Notes column weekly for repeated issues:
   - Lab platform access problems
   - Exam scheduling conflicts
   - Learning pace challenges

5. **Keep It Simple:** Don't over-complicate tracker. Stick to the 3 sections; resist adding too many custom columns.

---

## Contact & Support

**Tracker Owner:** Mo (Manager, Information & Cybersecurity, GIA)  
**Technical Questions:** [IT Support or Learning Coordinator]  
**Platform Issues:** Practical DevSecOps support (for Hands-On Labs section)  

---

**End of User Guide**

*Print this guide and share link with all 16 team members in Week 1.*
