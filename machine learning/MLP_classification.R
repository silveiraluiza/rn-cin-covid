library(keras)
library(magrittr)
library(caret)
library(readr)


output_densenet_train <- read_csv("Downloads/output_densenet_train.csv")  ### reading training data
output_densenet_test <- read_csv("Downloads/output_densenet_train.csv")   ### reading test data
output_densenet_val <- read_csv("Downloads/output_densenet_train.csv")    ### reading validation data



data_train <- as.matrix(output_densenet_train[,-1])     ###processing data into matriz format
y_train <- as.matrix(output_densenet_train[,1])

data_val <- as.matrix(output_densenet_val[,-1])
y_val <- as.matrix(output_densenet_val[,1])

data_test <- as.matrix(output_densenet_test[,-1])
y_test <- as.matrix(output_densenet_test[,1])

model <- keras_model_sequential()   ###model building


model %>%
  layer_flatten(input_shape = 1024) %>%
  layer_dense(units = 512, activation = 'relu', kernel_regularizer = regularizer_l2(0.05)) %>%
  layer_dropout(rate = 0.15) %>%
  layer_dense(units = 256, activation = 'relu', kernel_regularizer = regularizer_l2(0.05)) %>%
  layer_dropout(rate = 0.15) %>%
  layer_dense(units = 1, activation = 'sigmoid')

model %>% compile(    ##model compilation
  optimizer = optimizer_sgd(
    lr = 0.001,
    momentum = 0.9), 
  loss = 'binary_crossentropy',
  metrics = c('accuracy')
)



history <- fit(model,      ##model training
               x = data_train,
               y = y_train,
               validation_data = list(data_val, y_val),
               epochs = 500,
               verbose = 1
)

test_predictions <- model %>% predict_classes(data_test)    ###prediction for test data



confusionMatrix(table(y_test, test_predictions), positive = '1')    ###confusion matrix and metrics

