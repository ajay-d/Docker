library(shiny)
library(dplyr)
library(ggplot2)

shinyServer(function(input, output) {

  output$distPlot <- renderPlot({
    ggplot(mtcars, aes(x=mpg, y=hp, color=cyl)) +
  geom_point()
  })

})