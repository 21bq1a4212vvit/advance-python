let = {'a','k','e','o','t','p','n'}
list =['arun','varun','kent','eat','pot','net','peak','peacock','zebra','nato','toe','poke','knife','poet','venus','ant']
for i in list:
    i=i.lower()
    li_set=set(i)
    if li_set.issubset(let):
        print(i.capitalize())