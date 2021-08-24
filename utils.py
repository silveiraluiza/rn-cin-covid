#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import shutil
import pandas as pd

def remove_augmentation():
    
    #if len(os.listdir('/home/dell/Documentos/rn-cin-covid/data/tmp/')) > 0:
    #    raise Exception("Já há dados no diretório")
        
    train_labels_gauss = pd.read_csv("data/train_labels_gauss.txt", sep=" ",header=None)
    train_labels_gauss.columns = ['id', 'image', 'label', 'database']
    train_labels_gauss = train_labels_gauss[['image','label']]
    
    path = '/home/dell/Documentos/rn-cin-covid/'
    temp_dir_train = '/home/dell/Documentos/rn-cin-covid/data/tmp/train'
    temp_dir_val = '/home/dell/Documentos/rn-cin-covid/data/tmp/val'
       
    dir_train = '/home/dell/Documentos/rn-cin-covid/data/train'
    dir_val = '/home/dell/Documentos/rn-cin-covid/data/val'
    
    os.chdir(path)
    
    # Criando diretórios novos

    for path in [temp_dir_train, temp_dir_val]:
        for lb in ['positive', 'negative']:
            path_lb = os.path.join(path, lb)
            try:
                os.makedirs(path_lb)
            except OSError:
                print ("Creation of the directory %s failed" % path_lb)
            else:
                print ("Successfully created the directory %s" % path_lb)

    # Copiando as imagens
    
    for image in os.listdir('data/train/positive'):
        if image in train_labels_gauss['image'].tolist():
            shutil.move(os.path.join(dir_train,'positive',image), os.path.join(temp_dir_train, 'positive'))
            
    for image in os.listdir('data/train/negative'):
        if image in train_labels_gauss['image'].tolist():
            shutil.move(os.path.join(dir_train,'negative',image), os.path.join(temp_dir_train, 'negative'))
            
    for image in os.listdir('data/val/positive'):
        if image in train_labels_gauss['image'].tolist():
            shutil.move(os.path.join(dir_val,'positive',image), os.path.join(temp_dir_val, 'positive'))
    
    for image in os.listdir('data/val/negative'):
        if image in train_labels_gauss['image'].tolist():
            shutil.move(os.path.join(dir_val,'negative',image), os.path.join(temp_dir_val, 'negative'))
            
         
            
            
def add_back_augmentation():
    
    if len(os.listdir('/home/dell/Documentos/rn-cin-covid/data/tmp/')) < 1:
        raise Exception("Não há dados no diretório")
        
        
    train_labels_gauss = pd.read_csv("data/train_labels_gauss.txt", sep=" ",header=None)
    train_labels_gauss.columns = ['id', 'image', 'label', 'database']
    train_labels_gauss = train_labels_gauss[['image','label']]
    
    path = '/home/dell/Documentos/rn-cin-covid/'
    
    temp_dir_train = '/home/dell/Documentos/rn-cin-covid/data/tmp/train'
    temp_dir_val = '/home/dell/Documentos/rn-cin-covid/data/tmp/val'
    
    dir_train = '/home/dell/Documentos/rn-cin-covid/data/train'
    dir_val = '/home/dell/Documentos/rn-cin-covid/data/val'
    
    os.chdir(path)

    # Copiando as imagens
    
    for image in os.listdir('data/tmp/train/positive'):
        if image in train_labels_gauss['image'].tolist():
            shutil.move(os.path.join(temp_dir_train,'positive',image), os.path.join(dir_train, 'positive'))
            
    for image in os.listdir('data/tmp/train/negative'):
        if image in train_labels_gauss['image'].tolist():
            shutil.move(os.path.join(temp_dir_train,'negative',image), os.path.join(dir_train, 'negative'))
            
    for image in os.listdir('data/tmp/val/positive'):
        if image in train_labels_gauss['image'].tolist():
            shutil.move(os.path.join(temp_dir_val,'positive',image), os.path.join(tdir_val, 'positive'))
    
    for image in os.listdir('data/tmp/val/negative'):
        if image in train_labels_gauss['image'].tolist():
            shutil.move(os.path.join(temp_dir_val,'negative',image), os.path.join(dir_val, 'negative'))
            
            
    # Deletando diretórios
    
    shutil.rmtree(temp_dir_train)
    shutil.rmtree(temp_dir_val)
    


            

