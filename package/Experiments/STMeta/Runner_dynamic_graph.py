import os

#############################################
# BenchMark Bike
#############################################
########### Metro_Shanghai_IOFLOW ###########

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghaiDynamic.data.yml '
          '-p graph:Distance,MergeIndex:1,mark:D_Graph')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghaiDynamic.data.yml '
          '-p graph:static,MergeIndex:1,mark:static_Graph')
