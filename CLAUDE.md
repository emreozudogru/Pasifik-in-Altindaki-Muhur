# CLAUDE.md — Agent Instructions for "The Seal Beneath the Pacific"

> **This file is the first thing any AI agent working on this project must read.**  
> After reading this file, you must read the entire novel before doing anything else.

---

## 🔴 MANDATORY FIRST STEP: Read the Novel

**Before writing a single word, making any edit, or answering any question — read the full novel.**

### Reading Order

1. **Read the original Turkish draft first** (canonical source):
   ```
   tr/metin/orijinal.txt
   ```

2. **Then read all 22 expanded chapters in order:**
   ```
   tr/metin/bolumler/01-prolog-dunyanin-ucu.md
   tr/metin/bolumler/02-ilk-savas.md
   tr/metin/bolumler/03-muhurculerin-toplanmasi.md
   tr/metin/bolumler/04-en-nakarin-yakalanmasi.md
   tr/metin/bolumler/05-yolculuk-1.md
   tr/metin/bolumler/06-yolculuk-2.md
   tr/metin/bolumler/07-yolculuk-3.md
   tr/metin/bolumler/08-kuroshima-ve-insa.md
   tr/metin/bolumler/09-muhurlerin-tartismasi.md
   tr/metin/bolumler/10-yedi-muhur.md
   tr/metin/bolumler/11-yuzyillar-boyu-unutma.md
   tr/metin/bolumler/12-1945-morita-genzo.md
   tr/metin/bolumler/13-1946-2010-enfeksiyonlar.md
   tr/metin/bolumler/14-arakawa-ve-ren.md
   tr/metin/bolumler/15-arsivin-olusumu.md
   tr/metin/bolumler/16-dijital-cag-ve-suphe.md
   tr/metin/bolumler/17-voss-ilk-karsilasma.md
   tr/metin/bolumler/18-arsiv-parcalanmasi.md
   tr/metin/bolumler/19-voss-cay-evi.md
   tr/metin/bolumler/20-yalniz-kalan-ren.md
   tr/metin/bolumler/21-son-yuzlesme.md
   tr/metin/bolumler/22-sekizinci-muhur-ve-kapanis.md
   ```

3. **Then read the plan docs relevant to your task:**
   - Turkish development: `docs/tr-implementation-plan.md`
   - Turkish design spec: `docs/tasarim-spec.md`

Do not skip this step. Do not summarize and move on. Read and retain.

---

## 📖 Project Overview

**Title (TR):** Pasifik'in Altındaki Mühür  
**Author:** Emre Ozudogru  
**Genre:** Literary historical fantasy  
**Language:** Turkish original (English translation planned)  
**Structure:** 22 chapters across 4 parts  
**License:** CC BY 4.0

### The Story in One Paragraph

217 BCE. A secret coalition of scholars — the **Sealers** (*Mühürcüler*) — capture an ancient entity called **En-Nakar** and imprison it beneath a volcanic island in what is now Japan (Kuroshima). They seal the prison with seven seals: stone, silver, lead, name, silence, forgetting, and blood/price. In 1945, the atomic bomb cracks the seal — because it was the first time humanity replicated the energy of the sun, something the ancient seals were never designed to withstand. En-Nakar emerges into the modern world, not to destroy, but to learn — and to operate through information systems, attention economies, and human psychology. In 2026, an archivist named **Sato Ren** traces the entity, loses her allies, and ultimately forges an eighth seal: not a wall, but a pause — the half-second between impulse and action.

---

## 🧑‍🤝‍🧑 Characters

### Ancient Era (217 BCE)

| Character | Role | Key Trait |
|---|---|---|
| **Eirene** | Greek healer from Kos; final Sealer | Most silent, most perceptive. She argues the seventh seal should be "bedel" (price/cost) not "kan" (blood). Her fingerprint — five fingers, thin, a healer's hand — is left on the threshold stone and echoes through millennia. |
| **Lu Shen** | Chinese court scribe | Pragmatist and recorder. Translates "bedel" as "kan" because concrete language persists. Writes what will survive, not what is true. |
| **En-Nakar** | The imprisoned entity | Not a monster. Not a devil. Something older — it shows humans their own darkness and says: *"This is you."* Cannot be killed; can only be separated from the world. Its prophecy: *"One day, man will bring the sun to earth."* |

### Modern Era (1999–2026)

| Character | Role | Key Trait |
|---|---|---|
| **Sato Ren** | Japanese archivist, protagonist | Introverted, obsessive, slow to trust. Not a hero — deliberately so. Her power is restraint. She inherits her teacher Arakawa's work after his suspicious death. |
| **Prof. Arakawa Naomi** | Ren's mentor, Tokyo University scholar | Studies obscure island beliefs. Dies before reaching Kuroshima. Last message: *"That thing didn't die — it just learned to be modern."* |
| **Kerem** | Turkish cybersecurity engineer, Archive member | Warm, emotionally driven. Finds the Istanbul notebook with Eirene's fingerprint. Disappears — officially flew to Baku, but his passport was still at home. Sends Ren a final encrypted video before vanishing. |
| **Dr. Elias Voss** | En-Nakar's modern incarnation/vessel | Not overtly evil. Believes himself to be honesty itself. Presents at AI ethics conferences. His warning to Ren: *"Don't be a hero — heroes open doors fastest."* |
| **Morita Genzo** | 1945 island guardian, age 70 | The last true Coastal Watcher. Knew none of the real history — only his grandfather's four rules. Does not run. Fires his rifle at the door. Is consumed. |

### Archive Members (supporting)

- **Ana** (Brazil) — digital forensics expert; withdraws when her child is threatened
- **Marta** (Poland) — linguist; career sabotaged by fake emails
- **Daniel** (USA) — psychiatrist; patient confidentiality investigation opened against him

---

## 🔑 Key Themes and Motifs

### The Seven Seals
| Seal | Element | Meaning |
|---|---|---|
| 1 | Stone | Language ends |
| 2 | Silver | What is corrupted is reflected |
| 3 | Lead | Weight holds |
| 4 | Name | Do not name it — naming is the door |
| 5 | Silence | Do not feed it with attention |
| 6 | Forgetting | Not ignorance — not feeding |
| 7 | Blood / **Price** | Lu Shen wrote "blood"; Eirene carved "price" |

**The Eighth Seal (modern):** Not a physical structure. It is the half-second pause before reacting — the act of asking *"Is this really what I want, or is it my fear speaking?"*

### Recurring Lines
- **"İsim kapıdır"** — naming En-Nakar amplifies it
- **"Bedel her nesil sorar"** — Eirene's warning
- **"Başka çaren yok"** — En-Nakar's greatest lie
- **"Tanınan karanlık küçülür; tapılan karanlık büyür"** — Lu Shen's final note
- **"Kahraman olma. Kahramanlar kapıları en hızlı açanlardır."** — Voss to Ren

### Eirene's Fingerprint
The most important motif. Eirene presses her five fingers into stone at the threshold — not blood, not a name, just a mark. A question. This fingerprint appears in:
- Ch. 06: left on sandstone during the sea voyage
- Ch. 10: pressed into the threshold at Kuroshima
- Ch. 15: Kerem finds it in the Istanbul notebook (five fingers, thin, a woman's hand)
- Ch. 22: Ren realizes Eirene understood 2,000 years ago that fear cannot be cured — only recognized

---

## 🏗️ Repository Structure

```
tr/
  metin/
    orijinal.txt          ← NEVER MODIFY — canonical baseline
    bolumler/             ← 22 expanded chapters (active development)
  sesli_kitap/
    metinler/             ← plain text for TTS per chapter
    mp3/                  ← generated audio
    generate_audiobook.py ← reads from metinler/, writes to mp3/
    run_audiobook.bat

docs/
  tr-implementation-plan.md
  tasarim-spec.md

mcps/                     ← AI tool schemas, do not touch
```

---

## ✍️ Writing Rules (for any editing/generation task)

### Tone
- **Ancient sections (Ch. 1–11):** Epic, rhythmic, fragmented. Single-word paragraphs. Short declarative sentences. No irony.
- **Transition (Ch. 12):** Cinematic and heavy. Both registers.
- **Modern sections (Ch. 13–22):** Tense, compressed, contemporary. Lists work. Transitions should flow.

### What to Preserve
- En-Nakar is **never** purely evil. It shows truth — the darkest, most accurate truth. Voss must be philosophically credible.
- Ren is **not** a hero. She does small things. The victory is small, internal, fragile.
- The ending is **anti-climactic by design.** The door turns inward. The seal is a pause, not a wall.
- Every motif line must appear **at least once** in any major revision.

### What to Avoid
- Do not add action sequences or thriller beats.
- Do not make Voss/En-Nakar defeated. It is *slowed*, not stopped.
- Do not add romance subplots.
- Do not make Ren "realize everything" — she doesn't. She acts with uncertainty.

---

## 📋 Current Status (as of last update)

| Task | Status |
|---|---|
| Original Turkish draft | ✅ Complete |
| 22 expanded TR chapters | ✅ Complete — all reviewed and deduplicated |
| Critical revision (Jun 2026) | ✅ Done — Ch. 07/09/10/15/16/17 rewritten |
| Motif consistency pass | ✅ Done — fingerprint, "yedi parmak" fixed |
| TR audiobook (partial) | 🔄 In progress |
| TR final polish | 📋 Planned |

---

## ⚠️ Critical Rules

1. **Never modify `tr/metin/orijinal.txt`** — it is the unaltered baseline.
2. **Never name En-Nakar casually in prose** — every naming is intentional and weight-bearing.
3. **Commit after every meaningful change** with descriptive messages.
4. **Do not push to a branch** — work on `main`.
5. **If you are unsure whether a change preserves tone** — read the surrounding three paragraphs again before applying.
