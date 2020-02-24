#!/usr/bin/env python
# coding: utf-8

# # 作業一

# In[ ]:


def mean_squred_error(y, yp):
    '''
    y : 實際值
    yp : 預測值
    '''
    mse = MSE = sum((y-yp) ** 2) / len(y)
    return mse


# # 作業二

# In[ ]:


1. 能從這組資料中分析民眾訂房的趨勢，以及每組客人的組成、訂房的時間長短等資料，藉此給飯店業者進行參考
2. 從論文"Hotel booking demand datasets"下載下來
3. csv
4. 能從這組資料中分析並預測顧客訂房的情況，藉此讓飯店業者規劃因應的行銷策略


# # 作業三

# In[ ]:


1. 會影響業績的因素有'載客數量'、'距離長短'、'時間'，首先載客數量越多越好，雖然距離越長，該趟金額越多，但相對花費時間也較多，
   最後是時間，例如假日結束與平日的載客需求會有明顯差異，所以所需人力也不同
2. 所需的資料有在交通較繁忙的地區，例如車站，不同時間的人數分布，以及職業分布，需要靠問卷收集
3. CSV
4. 根據所收集到的資料，在車站等地點在不同的時間安排不同的人力，並觀察業績是否會上升
