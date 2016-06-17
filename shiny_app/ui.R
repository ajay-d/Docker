library(shiny)

shinyUI(pageWithSidebar(
  headerPanel("MNIST Demonstration"),
  sidebarPanel(
    conditionalPanel(condition="input.conditionedPanels==1",
                     helpText("Model trained from MNIST"),
                     tags$a(href="http://yann.lecun.com/exdb/mnist/", "MNIST homepage")
                     
    ),
    conditionalPanel(condition="input.conditionedPanels==2",
                     helpText("Content Panel 2")
    ) 
  ),
  mainPanel(
    tabsetPanel(
      tabPanel(title="Main Image Scoring", value=1,
               
               tags$head(tags$style("#container { position: relative; }
                                     #imageView { border: 1px solid #000; }")),
               tags$head(tags$script(src = "image_save.js")),
               
               h5('Draw a number with the mouse'),
               tags$p("Release click to stop drawing"),
               tags$div(id="container",
                        tags$canvas(id="imageView", width="400", height="300"),
                        tags$br(),
                        tags$p("Reload to refresh canvas"),
                        tags$script(src='mouse_draw.js'),
                        actionButton("score", "Score Image")),
               # a shiny element to display unformatted text
               verbatimTextOutput("results"),
               plotOutput('distPlot')), 
      tabPanel(title="Supplemental Plots", value=2)
      , id = "conditionedPanels"
    )
  )
))

