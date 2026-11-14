#!/usr/bin/env python3
"""Ontario Daycare and Child Care Centre Permit Checklist Generator - by Dust 2 Engineering Inc., Mississauga, Ontario.
Preliminary information only. Not engineering advice and not a code review.
Verify every item with your designer and the local building department.
"""
import argparse, pathlib
CONFIG = {'title': 'Ontario Daycare and Child Care Centre Permit Checklist Generator', 'tagline': 'Ontario Daycare and Child Care Centre Permit Checklist Generator by Dust 2 Engineering Inc.', 'unit_label': 'Licensed child capacity', 'flags': [{'arg': 'kitchen-food-prep', 'label': 'Kitchen / food preparation on site'}, {'arg': 'outdoor-play', 'label': 'Outdoor play area included in this project'}, {'arg': 'infant-room', 'label': 'Infant room (children under 18 months)'}], 'sections': [{'title': '1. Application basics (always required)', 'items': ['Municipal building permit application form, completed and signed by the owner or authorized agent', 'Schedule 1: Designer Information form for each qualified designer on the project', 'Owner authorization if the applicant is not the property owner, plus the lease for a tenant fit-out if the city asks for it']}, {'title': '2. Architectural drawings', 'items': ['Floor plan with a room for each age group, the licensed capacity of each room, washrooms, sleep areas and the secure entry', 'Zoning review first: child care centres are not permitted in every zone - confirm the use at this address before design starts', 'Barrier-free entrance, path of travel and barrier-free washroom where required', 'Fire separations from neighbouring units, exit signs and emergency lighting shown on plan', 'Child-height fixtures and finishes that can be washed and disinfected in play and washroom areas', 'Sign permit is separate from the building permit - apply for it separately']}, {'title': '3. Ventilation and HVAC', 'items': ['HVAC drawings: heating, cooling and ventilation for play rooms, sleep rooms and offices', 'Washroom exhaust shown with equipment schedules', 'Kitchen exhaust added if food is cooked on site (see the kitchen section)']}, {'title': '4. Plumbing and electrical', 'items': ['Washroom fixtures counted per child from the Ontario Building Code child care table: 1 water closet and lavatory per 10 children under 2, per 10 children aged 2 to 5, and per 15 children of each sex aged 6 to 9', 'Hot water tempered to prevent scalding at fixtures children use', 'Laundry sink and mop sink, backflow preventer where required', 'Electrical drawings: panels, lighting, receptacles with covers in child areas, emergency lighting']}, {'title': 'Kitchen and food preparation', 'when': 'kitchen-food-prep', 'items': ['Food premises layout: preparation area separated from play areas, handwash lavatory inside the preparation area', 'Three-compartment sink or commercial dishwasher, plus food storage shown on plan', 'Grease interceptor if cooking produces grease-laden waste', 'Public health food premises approval is separate from the building permit - notify public health before opening']}, {'title': 'Outdoor play area', 'when': 'outdoor-play', 'items': ['Fenced outdoor play area shown on the site plan, with self-closing gates and no direct exit to a parking lot or road', 'Play space sized per child under the provincial child care licensing rules', 'Play equipment is expected to meet CSA Z614 - keep the equipment certificates for the licensing visit']}, {'title': 'Infant room', 'when': 'infant-room', 'items': ['Separate infant sleep room shown on plan', 'Diaper change counter with an adjacent hand sink, away from food preparation', 'Bottle preparation sink and storage shown on plan']}, {'title': '5. Other approvals (not part of the building permit)', 'items': ['Provincial child care licence under the Child Care and Early Years Act (Ministry of Education) - separate from, and usually slower than, the building permit', 'Public health inspection of the centre before opening', 'Fire safety plan and fire department approval for the occupancy', 'Business licence from the city, after the permit is closed']}, {'title': 'Before you submit', 'items': ['One combined PDF set: architectural, mechanical, plumbing, electrical and structural (if any), all consistent with each other', 'All drawing sets use the same address, unit number, floor area and counts', 'Designs that require an engineer must be stamped by a licensed Ontario P.Eng.; BCIN designer information where applicable', 'Book a pre-consultation or zoning check with the city if the use or layout is not clearly permitted']}]}
def main():
    p = argparse.ArgumentParser(description=CONFIG["tagline"])
    p.add_argument("--city", default="Toronto")
    p.add_argument("--area-sqft", type=int, default=1200)
    p.add_argument("--units", type=int, default=0, help=CONFIG["unit_label"])
    for f in CONFIG["flags"]:
        p.add_argument("--" + f["arg"], action="store_true", help=f["label"])
    p.add_argument("--output", default="")
    a = p.parse_args()
    L = []
    L.append("# " + CONFIG["title"] + " - Ontario")
    L.append("")
    L.append("**City:** %s | **Area:** %d sq ft | **%s:** %d" % (a.city, a.area_sqft, CONFIG["unit_label"], a.units))
    L.append("")
    L.append("> Preliminary checklist generated with the free open-source " + CONFIG["title"] + " by Dust 2 Engineering Inc., Mississauga, Ontario. Verify every item with your designer and the local building department before submitting.")
    L.append("")
    for s in CONFIG["sections"]:
        if s.get("when") and not getattr(a, s["when"].replace("-", "_")):
            continue
        L.append("## " + s["title"])
        for it in s["items"]:
            L.append("- [ ] " + it)
        L.append("")
    L.append("---")
    L.append("Generated by the " + CONFIG["title"] + ", a free open-source tool by Dust 2 Engineering Inc. Dust 2 Engineering Inc. provides building permit drawings (architecture, HVAC, plumbing, sprinkler and electrical) stamped by an Ontario P.Eng. in the Greater Toronto Area, including Toronto, Mississauga, Brampton, Vaughan, Markham and Hamilton, for a flat fee of $3,500 to $5,000. This checklist is preliminary information only and is not engineering advice.")
    L.append("")
    out = "\n".join(L)
    if a.output:
        pathlib.Path(a.output).write_text(out, encoding="utf-8")
        print("Wrote " + a.output)
    else:
        print(out)
if __name__ == "__main__":
    main()
