#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[3]:


df = black_friday


# In[4]:


df.head(5)


# In[6]:


lista = [df.columns]


# In[7]:


lista


# In[8]:


df.shape


# In[30]:


df.User_ID.nunique()


# In[34]:


df.dtypes.nunique()


# In[38]:


df.info()


# In[39]:


q6 = 537577 - 164278


# In[40]:


q6


# In[42]:


df.Product_Category_3 .value_counts()


# In[22]:


aux


# In[23]:


q2 = df[df.Age == '26-35']


# In[24]:


q2


# In[28]:


q2.User_ID.nunique()


# In[29]:


q2.groupby('Gender')['User_ID'].nunique()


# In[43]:


mean = df.Purchase.mean()
std = df.Purchase.std()


# In[45]:


mean


# In[46]:


std


# In[48]:


norma = (df.Purchase - mean)/std


# In[49]:


norma


# In[95]:


np.mean(norma)


# In[51]:


norma.mean()


# In[54]:


norma.between(-1,1).value_counts()


# In[62]:


q10 = df[df['Product_Category_2'].isna() == True]


# In[78]:


q10_1.equals(q10_2)


# In[71]:


q10_1 = q10['Product_Category_2']


# In[77]:


q10_2


# In[72]:


q10_2 = q10['Product_Category_3']


# In[63]:


q10


# In[67]:


q10['Product_Category_2'] == q10['Product_Category_3']


# In[61]:


df['Product_Category_2'].isna()


# In[4]:


def qq():
    return 5


# In[5]:


qq()


# In[50]:


pd.cut(norma, labels =('Menor que 1', 'Maior que 1') , bins = (-1000, 1, 1000))


# In[89]:


aux = df.isna().mean()


# In[90]:


aux


# In[91]:


perc_nulos = (len(df) - len(df.dropna())) / len(df)


# In[92]:


perc_nulos


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[4]:


def q1():
    # Retorne aqui o resultado da questão 1.
    return(537577, 12)
    pass


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[5]:


def q2():
    # Retorne aqui o resultado da questão 2.
    return 545
    pass


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[6]:


def q3():
    # Retorne aqui o resultado da questão 3.
    return 5891
    pass


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[7]:


def q4():
    # Retorne aqui o resultado da questão 4.
    return 3
    pass


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[8]:


def q5():
    return 0.6944102891306734
    pass


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[41]:


def q6():
    # Retorne aqui o resultado da questão 6.
    return 373299
    pass


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[10]:


def q7():
    # Retorne aqui o resultado da questão 7.
    return 16.0
    pass


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[11]:


def q8():
    # Retorne aqui o resultado da questão 8.
    return 0.3847939036269795
    pass


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[12]:


def q9():
    # Retorne aqui o resultado da questão 9.
    return 348631
    pass


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[13]:


def q10():
    # Retorne aqui o resultado da questão 10.
    return True
    pass

