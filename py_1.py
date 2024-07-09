# 1
PMAX_member = [ "anuwat sagulmontreechai",
                "rattanaporn changwong","jakarin akrin","phasit sritonchai","rattanaporn akkasri"
                "chayutra chantachote","nattaphong pannengpet","nattanon moontip","kitsakron sophawan","sangnapha akrin",
                "phakawat bootnampetch","kunlanat damang","chaowarin anusornprasert","chanachai baisaen"]
# print(PMAX_member)

# 2
PMAX_member_sort = sorted(PMAX_member)
PMAX_member_sort.reverse()
# print(PMAX_member_sort)

# 3
for member in PMAX_member_sort:
    name = member.split(' ')
    # print(name[0].title(),name[1][:1].title()+'.')

# 4
other_member = ["rattanasuda samart ","siritas suvadhanabhakdi"]
other_member.extend(PMAX_member_sort)
other_member.sort()
other_member.reverse()
# print(other_member)