library(shiny)
library(dplyr)
library(ggplot2)

shinyServer(function(input, output) {

  observeEvent(input$score, {
    #session$sendCustomMessage(type = 'testmessage',
      #message = 'Thank you for clicking')
  })
  
  output$distPlot <- renderPlot({
    ggplot(mtcars, aes(x=mpg, y=hp, color=cyl)) +
  geom_point()
  })

})

