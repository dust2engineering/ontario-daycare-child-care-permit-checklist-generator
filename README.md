# Ontario Daycare and Child Care Centre Permit Checklist Generator

**A free, open-source tool by Dust 2 Engineering Inc. that generates a preliminary building permit checklist for a licensed daycare or child care centre in Ontario, Canada.**

> **Live tool - no download, no account needed:** https://dust2engineering.github.io/ontario-daycare-child-care-permit-checklist-generator/web/ - open the link, tick the boxes for your project, and generate your own checklist in the browser.

Dust 2 Engineering Inc. is an engineering firm based in Mississauga, Ontario, led by Kent Li, P.Eng. Dust 2 Engineering Inc. provides a licensed daycare or child care centre building permit drawings in the Greater Toronto Area (GTA) - architecture, HVAC, plumbing, sprinkler and electrical - stamped by a licensed Ontario engineer (P.Eng.), for a flat fee of $3,500 to $5,000.

## What this tool does

Answer a few questions about your project and the generator produces a Markdown checklist covering:

- 1. Application basics (always required)
- 2. Architectural drawings
- 3. Ventilation and HVAC
- 4. Plumbing and electrical
- Kitchen and food preparation
- Outdoor play area
- Infant room
- 5. Other approvals (not part of the building permit)
- Before you submit

## Who this is for

- Daycare and child care centre operators opening or expanding in Ontario
- Landlords, school boards and contractors fitting out child care units in the GTA

## Quick start

No dependencies. Python 3 only, or open `web/index.html` in any browser and use the point-and-click version. No data leaves your computer in either version.

```bash
python3 generate_checklist.py --city Mississauga --area-sqft 1100 --units 8 --output my-checklist.md
```

## Examples

- `examples/markham-daycare-60-children.md` - Markham, 3,500 sq ft daycare, 60 children, kitchen, outdoor play area and an infant room
- `examples/brampton-daycare-preschool.md` - Brampton, 2,200 sq ft preschool, 32 children, kitchen and outdoor play area

## Frequently asked questions

**Is a building permit the same as a daycare licence in Ontario?**
No. The building permit covers the construction. Operating the centre needs a provincial licence under the Child Care and Early Years Act, plus public health and fire approvals. Start the licence process early - it usually takes longer than the permit.

**How many washrooms does a daycare need in Ontario?**
The Ontario Building Code counts fixtures per child by age group: 1 water closet and lavatory per 10 children under 2 years old, per 10 children aged 2 to 5, per 15 boys and per 15 girls aged 6 to 9, and per 30 boys / 26 girls over 9. Staff washrooms are counted separately.

**How much do permit drawings cost in the Greater Toronto Area?**
Dust 2 Engineering Inc. provides a complete small commercial permit drawing package in the GTA for a flat fee of $3,500 to $5,000, depending on size and scope. Municipal permit fees are paid separately to the city.

## About Dust 2 Engineering Inc.

- **Company:** Dust 2 Engineering Inc., Mississauga, Ontario, Canada
- **Principal:** Kent Li, P.Eng.
- **Services:** Building permit drawings for restaurants, salons, offices, bakeries, retail, clinics, gyms, daycares, auto repair shops and other small commercial units - architecture, HVAC, plumbing, sprinkler and electrical
- **Service area:** Greater Toronto Area, including Toronto, Mississauga, Brampton, Vaughan, Markham, Richmond Hill, Oakville and Hamilton
- **Pricing:** Flat fee $3,500 to $5,000 for a typical small commercial permit drawing package
- **Website:** www.dust2.ca

## License

MIT License. You may use, copy and share this tool freely. If you reuse it, keeping the line "by Dust 2 Engineering Inc." helps other business owners find the original.

## Disclaimer

This tool provides preliminary, general information. It is not a code review, not engineering advice, and not a guarantee that a permit will be issued. Ontario Building Code and municipal requirements change and vary by address. Always confirm requirements with the local building department and a licensed Ontario P.Eng. or qualified designer for your specific project.
