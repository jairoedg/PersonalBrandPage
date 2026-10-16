# Design Language — Personal Brand Website

**Generated**: 2026-09-29  
**Gate**: B5-gate passed by Product Owner  
**Status**: In Review — Figma push pending

## Authority and Boundaries

`Enterprise` is the installed skill's taxonomy classification only. The approved Personal Brand Blueprint remains authoritative for the actual character: professional, corporate, approachable, reliable, collaborative, calm, transparent, structured, and empathetic.

This specification satisfies the installed Design Language workflow. Complete token coverage is separate from approved MVP usage. Reserved tokens are currently unassigned and do not create requirements, components, screens, forms, overlays, modal behavior, disabled states, animations, route transitions, disclosure mechanisms, dark mode, or other product behavior. No token assigns hierarchy based on OOUX Core/Supporting class, A3 prominence, or relationships. Deferred PRD/A10 decisions remain deferred.

## Tone

`[ASSUMPTION] Enterprise` — professional and evidence-led, while preserving the Blueprint's approachable, calm, people-first, transparent, structured, and empathetic character. Validation source: approved Personal Brand Blueprint and PRD/A10 audience and experience scope.

## Color Palette

### Primitives

| Family | 50 | 100 | 200 | 300 | 400 | 500 | 600 | 700 | 800 | 900 |
|---|---|---|---|---|---|---|---|---|---|---|
| Slate | `#F8FAFC` | `#F1F5F9` | `#E2E8F0` | `#CBD5E1` | `#94A3B8` | `#64748B` | `#475569` | `#334155` | `#1E293B` | `#0F172A` |
| Stone | `#FAFAF9` | `#F5F5F4` | `#E7E5E4` | `#D6D3D1` | `#A8A29E` | `#78716C` | `#57534E` | `#44403C` | `#292524` | `#1C1917` |
| Blue | `#EFF6FF` | `#DBEAFE` | `#BFDBFE` | `#93C5FD` | `#60A5FA` | `#3B82F6` | `#2563EB` | `#1D4ED8` | `#1E40AF` | `#1E3A8A` |
| Teal | `#F0FDFA` | `#CCFBF1` | `#99F6E4` | `#5EEAD4` | `#2DD4BF` | `#14B8A6` | `#0D9488` | `#0F766E` | `#115E59` | `#134E4A` |
| Emerald | `#ECFDF5` | `#D1FAE5` | `#A7F3D0` | `#6EE7B7` | `#34D399` | `#10B981` | `#059669` | `#047857` | `#065F46` | `#064E3B` |
| Amber | `#FFFBEB` | `#FEF3C7` | `#FDE68A` | `#FCD34D` | `#FBBF24` | `#F59E0B` | `#D97706` | `#B45309` | `#92400E` | `#78350F` |
| Rose | `#FFF1F2` | `#FFE4E6` | `#FECDD3` | `#FDA4AF` | `#FB7185` | `#F43F5E` | `#E11D48` | `#BE123C` | `#9F1239` | `#881337` |
| Sky | `#F0F9FF` | `#E0F2FE` | `#BAE6FD` | `#7DD3FC` | `#38BDF8` | `#0EA5E9` | `#0284C7` | `#0369A1` | `#075985` | `#0C4A6E` |

### Semantic Aliases

Aliases map directly to primitives. Reserved aliases are not MVP usage approvals.

| Token | Maps to | Usage |
|---|---|---|
| `color/action/primary` | `blue-700` | Candidate primary action |
| `color/action/hover` | `blue-800` | Reserved interaction token |
| `color/action/pressed` | `blue-900` | Reserved interaction token |
| `color/action/on-primary` | `stone-50` | Candidate foreground |
| `color/action/secondary` | `blue-800` | Reserved; no Contact ranking |
| `color/neutral/default` | `slate-700` | Neutral emphasis candidate |
| `color/neutral/subtle` | `slate-300` | Delineation candidate |
| `color/success/default` | `emerald-700` | Reserved status role |
| `color/success/surface` | `emerald-50` | Reserved status surface |
| `color/warning/default` | `amber-800` | A10 readiness/status candidate |
| `color/warning/surface` | `amber-50` | A10 readiness/status candidate |
| `color/error/default` | `rose-700` | A10 asset/reference fallback candidate |
| `color/error/surface` | `rose-50` | A10 fallback surface candidate |
| `color/info/default` | `sky-700` | Reserved informational role |
| `color/info/surface` | `sky-50` | Reserved informational surface |
| `color/surface/background` | `stone-100` | Page background candidate |
| `color/surface/card` | `stone-50` | Content surface candidate; not a component mandate |
| `color/surface/overlay` | `stone-50` | Reserved; no overlay authorization |
| `color/surface/scrim` | `slate-900` at 64% opacity | Reserved; no modal/sheet authorization |
| `color/text/default` | `slate-900` | Primary text candidate |
| `color/text/secondary` | `slate-700` | Supporting text candidate |
| `color/text/disabled` | `slate-600` | Reserved; no disabled control authorization |
| `color/text/on-dark` | `stone-50` | Reserved dark-surface text |
| `color/text/link` | `blue-700` | Link candidate |
| `color/border/default` | `slate-300` | Border candidate |
| `color/focus/visible` | `blue-700` | Visible-focus candidate |
| `color/accent/quiet` | `teal-700` | Reserved accent; not prominence or object hierarchy |

Spot-check ratios: neutral ink on page surface 16.36:1; action blue 6.14:1; readiness ink 6.79:1; asset-error ink 6.02:1. These are not a formal conformance claim.

## Typography Scale

Typeface: Inter for display/body roles; system `ui-monospace` for Code. Website font sourcing/hosting remains deferred. `1rem = 16px` is specification arithmetic only.

| Step | Typeface | Size | Weight | Line Height | Letter Spacing | Usage |
|---|---|---:|---:|---|---|---|
| Display | Inter | 48px / 3rem | 600 | 56px / 3.5rem | −0.025em | Reserved display role |
| H1 | Inter | 40px / 2.5rem | 600 | 48px / 3rem | −0.020em | Primary heading candidate |
| H2 | Inter | 32px / 2rem | 600 | 40px / 2.5rem | −0.015em | Section heading candidate |
| H3 | Inter | 28px / 1.75rem | 600 | 36px / 2.25rem | −0.010em | Subsection candidate |
| H4 | Inter | 24px / 1.5rem | 600 | 32px / 2rem | −0.005em | Reserved heading role |
| Body-L | Inter | 18px / 1.125rem | 400 | 28px / 1.75rem | 0em | Large reading candidate |
| Body-M | Inter | 16px / 1rem | 400 | 24px / 1.5rem | 0em | Default reading candidate |
| Body-S | Inter | 14px / 0.875rem | 400 | 20px / 1.25rem | 0em | Supporting reading candidate |
| Caption | Inter | 12px / 0.75rem | 400 | 16px / 1rem | +0.005em | Reserved caption role |
| Label | Inter | 14px / 0.875rem | 500 | 20px / 1.25rem | +0.005em | Label candidate |
| Code | ui-monospace | 13px / 0.8125rem | 400 | 20px / 1.25rem | 0em | Reserved code role |

## Spacing Scale

4px grid. Values are available for future approved layouts; they do not select a screen layout.

| Token | Value | Usage |
|---|---:|---|
| `space-1` | 4px | Base increment |
| `space-2` | 8px | Compact gap |
| `space-3` | 12px | Small gap |
| `space-4` | 16px | Standard gap |
| `space-5` | 20px | Medium gap |
| `space-6` | 24px | Content padding candidate |
| `space-7` | 28px | Reserved |
| `space-8` | 32px | Section gap candidate |
| `space-9` | 36px | Reserved |
| `space-10` | 40px | Reserved |
| `space-11` | 44px | Reserved |
| `space-12` | 48px | Large section gap candidate |
| `space-13` | 52px | Reserved |
| `space-14` | 56px | Reserved |
| `space-15` | 60px | Reserved |
| `space-16` | 64px | Large spacing candidate |

Generic component-token candidates: `padding-button-sm` = 8px/12px, `padding-button-md` = 12px/16px, `padding-card` = 24px, `gap-list` = 16px, `gap-form` = 16px. These do not authorize components, forms, or a form backend.

## Elevation

| Level | Shadow | Tint | Usage |
|---|---|---|---|
| `elevation/flat` | `none` | `stone-50`, 0% | Base candidate |
| `elevation/raised` | `0 2px 6px rgba(15, 23, 42, 0.08)` | `stone-50` + slate at 1% | Reserved |
| `elevation/floating` | `0 8px 24px rgba(15, 23, 42, 0.12)` | `stone-50` + slate at 2% | Reserved; no floating UI implied |
| `elevation/overlay` | `0 20px 48px rgba(15, 23, 42, 0.18)` | `stone-50` + slate at 3% | Reserved; no overlay UI implied |

## Motion

| Token | Value | Usage |
|---|---|---|
| `ease/enter` | `cubic-bezier(0, 0, 0.2, 1)` | Reserved |
| `ease/exit` | `cubic-bezier(0.4, 0, 1, 1)` | Reserved |
| `ease/standard` | `cubic-bezier(0.4, 0, 0.2, 1)` | Reserved |
| `ease/spring` | `cubic-bezier(0.34, 1.56, 0.64, 1)` | Reserved; no MVP use |
| `duration/instant` | 0ms | Reserved |
| `duration/fast` | 100ms | Reserved |
| `duration/normal` | 200ms | Reserved |
| `duration/slow` | 400ms | Reserved |
| `duration/deliberate` | 600ms | Reserved |

No animation, route transition, or disclosure mechanism is authorized by these tokens.

## Iconography

Outlined style, 24px grid, 1.75px stroke, rounded caps/joins. No library selected. If icons are later approved, they supplement descriptive labels and never carry essential meaning alone. No icon components are created here.

## B5 Approval and Preservation

B5 was explicitly approved by the Product Owner on 2026-09-29. Approval covers the complete token specification and allows Activity 9 Step 4 to write this artifact and push approved Variables/Styles. It does not authorize Activity 10, Part C, Explore Step 5, new screens, components, forms, overlays, modals, disabled states, animations, route transitions, disclosure mechanisms, dark mode, or resolution of deferred PRD/A10 decisions.
