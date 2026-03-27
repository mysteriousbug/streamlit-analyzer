# AI/LLM Security Learning Path - Slide-Ready Content
## SCB Group Internal Audit | Information & Cybersecurity Team

---

## SECTION 1: ENTRY-LEVEL AI SECURITY TRAINING (Mandatory for All - 16 Team Members)

**Duration:** 2-3 weeks  
**Time Commitment:** 12-15 hours per person  
**Completion Requirement:** Team attestation required (tracked in Excel)  
**Objective:** Build foundational understanding of AI/LLM risks and security fundamentals

### Mandatory Content (All Team Members MUST Complete)

**1.1 OWASP Top 10 for LLM Applications 2025**
- **Source:** LLMRisks Archive - OWASP Gen AI Security Project
- **URL:** https://genai.owasp.org/llm-top-10/
- **Duration:** 3-4 hours
- **Content Covered:**
  - LLM01: Prompt Injection (direct & indirect)
  - LLM02: Insecure Output Handling
  - LLM03: Supply Chain Vulnerabilities
  - LLM04: Training Data Poisoning
  - LLM05: Inadequate Data Sanitization
  - LLM06: Excessive Agency
  - LLM07: System Prompt Leakage
  - LLM08: Vector Database Poisoning
  - LLM09: Unbounded Consumption
  - LLM10: Misinformation & Hallucinations
- **Deliverable:** Completion attestation (self-signed)
- **Why This:** Foundational vulnerability knowledge; directly applicable to AI Factory audit

---

**1.2 MITRE ATLAS™ Framework**
- **Source:** Adversarial Threat Landscape for Artificial-Intelligence Systems
- **URL:** https://atlas.mitre.org/
- **Duration:** 2-3 hours
- **Content Covered:**
  - 14 core tactics (Reconnaissance, Resource Development, Initial Access, Execution, etc.)
  - 66+ techniques with real-world examples
  - Case studies of AI attacks in production
  - ATLAS Navigator tool walkthrough
- **Deliverable:** Completion attestation + personal tactic reference notes
- **Why This:** Threat modeling framework for AI systems; mirrors MITRE ATT&CK familiar to security teams

---

**1.3 RAND Corporation: AI Security Guide**
- **Source:** https://www.rand.org/pubs/tools/TLA4174-1/ai-security/guide.html
- **Duration:** 2-3 hours
- **Content Covered:**
  - Understanding AI model risks (data, model, deployment layers)
  - Prioritizing risk mitigation strategies
  - Practical solutions for risk reduction
  - Business case for AI security investment
- **Deliverable:** Completion attestation
- **Why This:** Risk prioritization lens for audit decision-making

---

**1.4 NIST AI Risk Management Framework (NIST AI RMF)**
- **Source:** AI Risk Management Playbook - AIRC
- **URL:** https://playbook.nist.gov/AI
- **Duration:** 2-3 hours (select core sections)
- **Content Covered:**
  - NIST AI RMF governance & risk management approach
  - Integration with existing audit frameworks
  - Control mapping to AI systems
- **Deliverable:** Completion attestation
- **Why This:** Bridges audit frameworks to AI governance; regulatory alignment
- **Note:** Focus on governance & control sections; detailed technical sections are optional for future reading

---

**1.5 Google Secure AI Framework (SAIF)**
- **Source:** https://saif.google/
- **Duration:** 1-2 hours (overview only)
- **Content Covered:**
  - Google's approach to responsible AI deployment
  - Best practices from industry leader
  - Security principles for AI systems
- **Deliverable:** Completion attestation
- **Why This:** Industry best practice reference; complements NIST/OWASP frameworks
- **Note:** Overview focus; detailed technical deep-dives optional

---

### Optional Entry-Level Content (For Future Self-Study)

**Optional:** Databricks AI Fundamentals & Security Framework
- **URL:** https://www.databricks.com/resources/learn/training/databricks-fundamentals
- **Timing:** Post-completion (Week 4+ or during hands-on labs phase)
- **Rationale:** Specific to AI Factory technology stack; valuable for specialists but not critical baseline

---

### Entry-Level Success Criteria

**All 16 Team Members Must:**
- [ ] Complete OWASP Top 10 for LLM Applications 2025 (self-attestation)
- [ ] Complete MITRE ATLAS Framework (self-attestation)
- [ ] Complete RAND AI Security Guide (self-attestation)
- [ ] Complete NIST AI RMF Playbook - core sections (self-attestation)
- [ ] Complete Google SAIF overview (self-attestation)
- [ ] **Sign attestation in Excel tracker by [DATE]**

**Attestation Method:**
- Team members electronically sign tracker (Excel) with completion date
- Mo receives automated summary (Excel formula) showing completion status
- Baseline assessment quiz (optional, self-validated) available in tracker

---

---

## SECTION 2: HANDS-ON LABS & PRACTICAL TRAINING

**Duration:** 6-8 weeks  
**Time Commitment:** 40-50 hours per person  
**Delivery:** Self-paced, online, browser-based labs  
**Completion Requirement:** Lab completion + capstone exercise documented in tracker  
**Objective:** Develop offensive & defensive AI security skills; hands-on vulnerability testing

### Recommended Platform: Practical DevSecOps - MITRE ATLAS + OWASP Hands-On Course

**Platform Details:**
- **Name:** Certified AI Security Professional (CAISP) Certification Program
- **URL:** https://www.practical-devsecops.com/mitre-atlas-framework-guide-securing-ai-systems/
- **Cost:** USD 1,099 per person (recommended for entire team: USD 17,584 for 16 people)
- **Format:** Self-paced, online, 100% browser-based labs
- **Delivery:** No instructor required; learn on your own schedule
- **Lab Access:** 60 days of lab environment access included
- **Certification:** Certified AI Security Professional (CAISP) upon completion

---

### Lab Curriculum (15 Progressive Labs)

**Week 1-2: Prompt Injection Mastery**
- Lab 1: Direct Prompt Injection (instruction override)
- Lab 2: Indirect Prompt Injection (RAG document poisoning)
- Lab 3: Multi-turn Crescendo attacks
- **Deliverable in Tracker:** Evidence (screenshots) + lab summary

**Week 3: Model & Data Attacks**
- Lab 4: Model extraction via API querying
- Lab 5: Training data poisoning detection
- Lab 6: Embedding inversion attacks
- **Deliverable in Tracker:** Attack scenarios + findings

**Week 4: Supply Chain & System-Level Risks**
- Lab 7: SBOM vulnerability scanning
- Lab 8: Plugin sandboxing bypass
- Lab 9: RAG database retrieval attacks
- **Deliverable in Tracker:** Risk assessment summary

**Week 5: Agent & Autonomous Systems**
- Lab 10: Agent goal hijacking
- Lab 11: Tool invocation privilege escalation
- Lab 12: Agent memory/context exfiltration
- **Deliverable in Tracker:** Test case documentation

**Week 6-8: Integration & Certification**
- Lab 13: End-to-end attack chains
- Lab 14: Defense implementation & validation
- Lab 15: Capstone exercise (simulated AI system audit)
- **Deliverable in Tracker:** Capstone project submission + CAISP certification

---

### Lab Completion Requirements

**Mandatory for All 16 Team Members:**
- [ ] Complete minimum 10 out of 15 labs (core labs: 1-7, 10-12)
- [ ] Document evidence for each lab (screenshots, test outputs)
- [ ] Submit capstone exercise (Lab 15)
- [ ] Pass CAISP certification exam (built into platform)
- [ ] Update tracker with lab completion status weekly

**Certification Outcome:**
- All 16 team members earn "Certified AI Security Professional (CAISP)" credential
- Certification valid for 3 years
- Professional credential for resume/LinkedIn

---

### Why Practical DevSecOps Platform?

✅ **Comprehensive Coverage:** OWASP Top 10 + MITRE ATLAS tactics in hands-on labs  
✅ **Browser-Based:** No installation required; works on any OS  
✅ **Self-Paced:** Flexibility to complete during work hours or personal time  
✅ **Certification Included:** CAISP credential with professional value  
✅ **Budget-Efficient:** USD 1,099 per person (all-in; no hidden costs)  
✅ **Aligned to Frameworks:** Direct mapping to audit requirements (OWASP + MITRE)  
✅ **Repeatability:** 60-day lab access allows multiple attempts & review

---

---

## SECTION 3: ADVANCED CERTIFICATIONS (Optional - Self-Interest)

**Timeline:** Concurrent with hands-on labs (weeks 4-12) or post-completion  
**Recommendations:** Based on manager feedback; focuses on security-specific, audit-applicable certifications

---

### Option 1: Certified AI Security Professional (CAISP) - Practical DevSecOps
**Status:** ✅ **RECOMMENDED - Include in Primary Path**  
**Coverage:** Already included in Hands-On Labs section (Section 2)  
**No Additional Content Needed Here**

---

### Option 2: Modern Security AI Security Certification
**Status:** ✅ **RECOMMENDED - Alternative/Complementary**

**Certification Details:**
- **Provider:** Modern Security (https://www.modernsecurity.io/)
- **Format:** Self-paced, online
- **Duration:** 40-50 hours
- **Cost:** USD 800-1,200
- **Delivery Method:** Video tutorials + hands-on labs + capstone projects
- **Certification Valid For:** 3 years

**Curriculum Highlights:**
- Introduction to AI Security fundamentals
- LLM attacks & defense mechanisms
- OWASP Top 10 for LLMs deep-dive
- Threat modeling AI systems
- AI supply chain security
- Emerging threats & governance
- 15+ hands-on exercises
- 4 capstone projects

**Best For:**
- Team members interested in **offensive security focus** (not just audit governance)
- Hands-on lab preference (more practical, less theoretical)
- Flexible learning pace

**Recommendation:**
- **Optional for interested team members** (2-5 people)
- Can be pursued after CAISP completion (weeks 8+)
- Complements CAISP with additional depth on AI threat modeling & security architecture

---

### ~~Option 3: ISACA Advanced in AI Audit (AAIA)~~
**Status:** ❌ **NOT RECOMMENDED (Per Manager Feedback)**
**Reason:** "Fluffy, high-level stuff" - governance-focused, limited practical security depth
**Alternative:** Use NIST AI RMF (already in Entry-Level) for governance framework

---

### ~~Option 4: Certified AI Auditor (CAA) by NLL.ai~~
**Status:** ❌ **NOT RECOMMENDED (Per Manager Feedback)**
**Reason:** "Not cyber/security specific" - focuses on algorithm fairness & bias, not security vulnerabilities
**Alternative:** CAISP + Modern Security certifications provide better cybersecurity focus

---

### Certification Recommendation Summary

| Certification | Recommended | Audience | Timeline |
|---------------|-------------|----------|----------|
| CAISP (Practical DevSecOps) | ✅ **YES - Mandatory** | All 16 team members | Weeks 4-8 (with labs) |
| Modern Security AI Security | ✅ **OPTIONAL** | 2-5 interested members | Weeks 8-12 (post-CAISP) |
| ISACA AAIA | ❌ NO | - | - |
| NLL.ai CAA | ❌ NO | - | - |

---

---

## SECTION 4: IMPLEMENTATION TIMELINE (12 WEEKS)

### Week 1-2: Entry-Level Training Phase
- **Deliverable:** Team attestation of all 5 mandatory trainings completed
- **Tracker Update:** Excel signed completion dates

### Week 3-4: Lab Platform Access & Onboarding
- Enroll all 16 team members in Practical DevSecOps platform
- Distribute lab access credentials
- Kickoff Lab Week 1 (Prompt Injection focus)

### Week 4-8: Hands-On Labs Phase
- Labs 1-15 progressive completion
- Weekly tracker updates (lab completion %)
- Peer learning encouraged (team channel discussions)

### Week 8-12: Capstone & Certification
- Lab 15 capstone submission (simulated AI system audit)
- CAISP certification exam completion
- Final tracker update with certification status

### Optional: Week 8+ (Modern Security Certification)
- For interested 2-5 team members
- Self-paced, can continue beyond week 12

---

---

## SECTION 5: SUCCESS METRICS & ACCOUNTABILITY

### Tracked in Excel Tracker (Shared with All Team Members)

**Entry-Level Phase (Week 1-2):**
- OWASP Top 10 completion: YES/NO + date
- MITRE ATLAS completion: YES/NO + date
- RAND Guide completion: YES/NO + date
- NIST AI RMF completion: YES/NO + date
- Google SAIF completion: YES/NO + date
- **Overall Entry-Level Status:** Completed/In Progress/Not Started

**Hands-On Labs Phase (Weeks 4-8):**
- Lab 1-15 completion status (completed Y/N + date)
- Lab evidence submitted (Y/N)
- Capstone exercise submitted (Y/N + date)
- CAISP exam passed (Y/N + date)
- **Overall Lab Status:** Completed/In Progress/Not Started

**Certifications Phase (Weeks 8-12):**
- CAISP certification awarded (Y/N + date)
- Modern Security cert (if pursuing): In Progress/Completed/Not Pursuing
- **Overall Cert Status:** Completed/In Progress/Not Started

**Team-Level Rollup:**
- % of team completed entry-level (auto-calc: 16/16, etc.)
- % of team completed labs (auto-calc)
- % of team completed CAISP cert (auto-calc)
- % of team pursuing Modern Security cert (info only)

---

### Attestation Method

**Self-Attestation with Mo Verification:**
1. Team members mark completion in Excel (self-signed, with date)
2. Honor system: Self-accountability
3. Mo reviews tracker weekly
4. Escalation if <80% of team on pace (week 2, week 6, week 10)

---

---

## SECTION 6: BUDGET SUMMARY

| Item | Unit Cost | Qty (16 members) | Total | Notes |
|------|-----------|-----------------|-------|-------|
| Practical DevSecOps (CAISP) | USD 1,099 | 16 | **USD 17,584** | Mandatory; includes 60-day lab access + certification |
| Modern Security AI Security Cert | USD 900 | 3-5 | **USD 2,700-4,500** | Optional; for interested specialists |
| **TOTAL MANDATORY** | | | **USD 17,584** | Entry-level trainings are FREE (online resources) |
| **TOTAL WITH OPTIONAL** | | | **USD 20,284-22,084** | If 3-5 pursue Modern Security cert |

**Budget Efficiency:**
- Entry-level: 0 cost (free online resources)
- Labs + Certification: USD 1,099 per person (all-in)
- Advanced cert: USD 900 per person (optional, selective)

---

---

## SECTION 7: ROLES & RESPONSIBILITIES

### Team Members (All 16)
- Complete entry-level trainings by Week 2
- Enroll in Practical DevSecOps labs by Week 3
- Update Excel tracker weekly (self-attestation)
- Attend optional team lab Q&A sessions (async channel)

### Mo (Manager, Information & Cybersecurity)
- Approve training plan & budget (done)
- Monitor Excel tracker for compliance (weekly review)
- Escalate blockers (lab access issues, time constraints)
- Sign-off on team readiness for AI Factory audit (Week 12)

### Learning Coordinator (TBD - Optional)
- Distribute lab access credentials (Week 3)
- Monitor platform announcements & updates
- Facilitate peer learning (team channel)
- Consolidate completion reports for Mo (weekly)

---

---

## CONCLUSION

This streamlined 12-week program equips your 16-person Information & Cybersecurity team with:

✅ **Foundational Knowledge:** OWASP Top 10 + MITRE ATLAS frameworks (Entry-Level)  
✅ **Hands-On Skills:** 15 labs + CAISP certification (Practical DevSecOps)  
✅ **Professional Credentials:** 16 CAISP-certified AI security professionals  
✅ **Optional Specialization:** Modern Security cert for 2-5 interested team members  
✅ **Audit Readiness:** Complete capability for AI Factory security assessment  
✅ **Accountability:** Excel tracker with team-wide visibility & completion attestation  

**Total Investment:** USD 17,584 (mandatory) | USD 20,284-22,084 (with optional certs)  
**ROI:** Team capability for autonomous AI system auditing; repeatable methodology for future engagements

---

**End of Slide-Ready Content**

*Use this content to paste directly into your presentation slides.*
