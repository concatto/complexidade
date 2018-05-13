
for (heap in c("binomial", "fibonacci")) {
  of_heap <- experiments[experiments$heap == heap,]
  X <- unique(of_heap$n)
  
  y_full <- colMeans(matrix(of_heap$full, nrow=30))
  y_last <- colMeans(matrix(of_heap$last, nrow=30))
  
  model_full <- lm(log(y_full)~log(X))
  model_last <- lm(log(y_last)~log(X))

  print(paste(heap, " full"))
  print(model_full)
  print(paste(heap, " last"))
  print(model_last)
  
  y_full_predicted <- exp(model_full$coefficients[1]) * X^model_full$coefficients[2]
  y_last_predicted <- exp(model_last$coefficients[1]) * X^model_last$coefficients[2]
  
  plot(X, y_last)
  lines(X, y_last_predicted, col="green")
  
  plot(X, y_full)
  lines(X, y_full_predicted, col="red")
}