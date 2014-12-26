
team_ids = ['428','796','539','418','306','518','559','509','416','312','301','587','463','392']
year_ids = ['12020','11540','11220','10740','10440','10260']
BIG_Hist = []
MINN_Hist = []
BIG_CY = []
MINN_CY = []


def BIGH(a,b):
    for year in a:
        first = "http://stats.ncaa.org/team/roster/" + str(year) + "?org_id="
        for team in b:
            link = first + str(team)
            BIG_Hist.append(link)
def BIGCY(a,b):
    first = "http://stats.ncaa.org/team/roster/" + str(a[0]) + "?org_id="
    for team in b:
        link = first + str(team)
        BIG_CY.append(link)
def MINNH(a,b):
    for year in a:
        first = "http://stats.ncaa.org/team/roster/" + str(year) + "?org_id=" + str(b)
        MINN_Hist.append(first)
def MINNCY(a,b):
    first = "http://stats.ncaa.org/team/roster/" + str(a[0]) + "?org_id=" + str(b)
    MINN_CY.append(first)



BIGH(year_ids,team_ids)
BIGCY(year_ids,team_ids)
MINNH(year_ids,'428')
MINNCY(year_ids,'428')

print BIG_Hist
print BIG_CY
print MINN_Hist
print MINN_CY
