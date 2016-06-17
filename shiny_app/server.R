
library(httr)
library(shiny)
library(dplyr)
library(ggplot2)
library(base64enc)

shinyServer(function(input, output, session) {

  observeEvent(input$score, {
    session$sendCustomMessage(type='saveimage', message='Scoring Image')
  })
  
  #For debugging
  output$results <- renderPrint({
    binary.image <- input$myimage
    
    img <- base64decode(binary.image)
    img
    str(img)
  })
  
  output$distPlot <- renderPlot({
    ggplot(mtcars, aes(x=mpg, y=hp, color=cyl)) +
      geom_point()
  })

})

