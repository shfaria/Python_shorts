import pandas as pd

zoom = pd.read_csv("/Users/shfaria/Downloads/zoom.csv")
vsession = pd.read_csv("/Users/shfaria/Downloads/vsession.csv")

length_zoom = len(zoom.Name) 
length_public = len(vsession.Name) 

for i in range(length_zoom) :
    for j in range(length_public):
        if zoom.Name[i] == vsession.Name[j]:
            x = vsession.Type[j]
            zoom.Type[i] = x
            print(zoom.Type[i])

mergedata = zoom.merge(vsession, how = 'left', on='Name')

mergedata.to_csv("/Users/shfaria/Downloads/out.csv", index=False)

# length_band = len(zoom.Name) 
# length_avail = len(vsession.Name) 

# for i in range(length_band) :
#     for j in range(length_avail):
#         if zoom.Name[i] == vsession.Name[j]:
#             x = vsession.Type[j]
#             zoom.Type[i] = x
#             print(zoom.Type[i])

# mergedata = zoom.merge(vsession, how = 'outer', on='Name')
mergedata = vsession.merge(zoom, how = 'outer', on='Name')


mergedata.to_csv("C:/Users/faria/Documents/totalzoomout2.csv", index=False)
            
            

    

