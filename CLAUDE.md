# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

> **This file is the first thing any AI agent working on this project must read.**  
> After reading this file, you must read the entire novel before doing anything else.

> ℹ️ **This is a prose repository, not a software one.** The "code" here exists only to render the novel into audiobook (MP3) and eBook (EPUB) formats. The product is the Turkish text in `tr/metin/bolumler/`.

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
   - Turkish development: `docs/implementation-plan.md`
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
    bolumler/             ← 22 expanded chapters (active development — SOURCE OF TRUTH)
  sesli_kitap/
    metinler/             ← plain text for TTS per chapter (DERIVED from bolumler/)
    mp3/  aiff/           ← generated audio (gitignored)
    generate_audiobook.py ← edge-tts: reads metinler/, writes mp3/
    generate_audiobook_mac.sh ← macOS `say` fallback (writes aiff/)
    AUDIOBOOK_STATUS.md   ← which chapters have current audio
  ebook/
    generate_ebook.py     ← reads bolumler/ directly, writes pasifik_muhur.epub
    pasifik_muhur.epub    ← DERIVED, git-tracked binary

docs/
  implementation-plan.md
  tasarim-spec.md

mcps/                     ← AI tool schemas, do not touch
README.md  LICENSE        ← CC BY 4.0
```

---

## 🔧 Build Pipeline & Commands

The chapters in `tr/metin/bolumler/*.md` are the **single source of truth**. Two artifacts are *derived* from them and go stale whenever a chapter changes — both must be regenerated after edits, or the audiobook/eBook will reproduce pre-edit text (this has happened before).

```
tr/metin/bolumler/NN-*.md   ──┬──►  tr/sesli_kitap/metinler/bolum_NN.txt  ──►  mp3/bolum_NN.mp3
  (source of truth)           │      (TTS plain text, git-tracked)             (gitignored audio)
                              └──►  tr/ebook/pasifik_muhur.epub  (git-tracked binary)
```

**Markdown → plain-text transform** (applied identically by both the audiobook and eBook generators): drop lines starting with `#` or `---` or blank lines, strip the `🌑` emoji, collapse internal whitespace. The `**Pasifik'in Altındaki Mühür**` banner line is **kept**. The TTS `.txt` files have **no trailing newline** — match this exactly when regenerating, or every file shows a spurious diff.

```bash
# eBook (EPUB) — reads ../metin/bolumler directly, outputs pasifik_muhur.epub
cd tr/ebook && pip install ebooklib && python3 generate_ebook.py

# Audiobook (MP3) — needs edge-tts; reads metinler/, writes mp3/ + AUDIOBOOK_STATUS.md + playlist.m3u
cd tr/sesli_kitap && pip install -r requirements.txt && python3 generate_audiobook.py
# macOS native fallback (uses `say`, outputs .aiff): ./generate_audiobook_mac.sh

# Regenerate the TTS .txt sources after editing chapters (there is no script for this step —
# apply the transform above; only re-write files whose content actually changed).
```

- **Voice:** `generate_audiobook.py` uses `edge-tts` voice `tr-TR-EmelNeural` (female). Needs network for Azure TTS — **not runnable inside the Airlock sandbox**; flag MP3 regeneration to the user instead.
- `pip install ebooklib` succeeds through the gateway proxy; the EPUB *can* be rebuilt here.
- `mp3/` and `aiff/` are gitignored; `metinler/*.txt` and `pasifik_muhur.epub` **are** tracked — commit them when chapters change. `AUDIOBOOK_STATUS.md` tracks which chapters have current audio.

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
3. **Every agent (including any sub-agents or spawned agents) must perform a git commit after every meaningful change**, using descriptive commit messages (e.g. `feat: 13 - Enfeksiyon örnekleri era-specific ve non-Voss vessel'larla genişletildi; Voss 2026-only ayrımı netleştirildi`). The main coordinating agent (Grok) will also execute git commits for all coordinated/synthesized changes from sub-agents.
4. **Do not push to a branch** — work on `main`.
5. **If you are unsure whether a change preserves tone** — read the surrounding three paragraphs again before applying.
