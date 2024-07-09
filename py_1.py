# 1
PMAX_member = ["jakarin akrin","phasit sritonchai","prakrapong pongpang","chayutra chantachote","nattaphong pannengpet",
"nattanon moontip","kitsakron sophawan","sangnapha akrin"]

PMAX_member.remove("prakrapong pongpang")
PMAX_member.insert(0,"anuwat sagulmontreechai")
PMAX_member.insert(1,"rattanaporn changwong")
PMAX_member.insert(4,"rattanaporn akkasri")

PMAX_new_member = ["phakawat bootnampetch","kunlanat damang","chaowarin anusornprasert","chanachai baisaen"]

PMAX_member = PMAX_member + PMAX_new_member

print(PMAX_member)

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