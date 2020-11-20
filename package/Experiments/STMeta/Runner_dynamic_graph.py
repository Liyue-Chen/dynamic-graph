import os

#############################################
# BenchMark Bike
#############################################
########### Metro_Shanghai_IOFLOW ###########

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghaiDynamic.data.yml '
#           '-p graph:Distance-Correlation-Line,MergeIndex:1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghaiDynamic.data.yml '
#           '-p graph:Distance-Correlation-Line,MergeIndex:3')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghaiDynamic.data.yml '
#           '-p graph:Distance-Correlation-Line,MergeIndex:6')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghaiDynamic.data.yml '
          '-p graph:Distance-Line,MergeIndex:12')
