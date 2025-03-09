import turtle
import tkinter
import tkinter.colorchooser
import tkinter.filedialog
import tkinter.messagebox
import xml.dom.minidom
import math
import sys

class PlotApplication(tkinter.Frame):
    currentFile = None # used for the reload feature
    def __init__(self, master=None, datafile=None):
        super().__init__(master)
        self.datafile = datafile
        self.pack()
        self.buildWindow()


    def buildWindow(self):

        self.master.title("Plot")

        bar = tkinter.Menu(self.master)
        fileMenu = tkinter.Menu(bar,tearoff=0)
        open_button = None


        def loadFile(filename=None):

            if filename == None:
                filename = tkinter.filedialog.askopenfilename(title="Select a Plot File", filetypes=[("Extensible Markup Language", ".xml")])

            if filename == None or filename == '':
                return
                
            if open_button: open_button.destroy()
                
            self.currentFile = filename

            try:

                theTurtle.clear()
                theTurtle.penup()
                theTurtle.goto(0,0)
                theTurtle.pendown()
                screen.update()
                theTurtle.color("black")

                xmldoc = xml.dom.minidom.parse(filename)

                plotElement = xmldoc.getElementsByTagName("Plot")[0]

                attr = plotElement.attributes
                self.master.title(attr["title"].value)

                axesElement = plotElement.getElementsByTagName("Axes")[0]

                xAxisElement = axesElement.getElementsByTagName("XAxis")[0]
                xAxisLabel = xAxisElement.firstChild.data.strip()

                yAxisElement = axesElement.getElementsByTagName("YAxis")[0]
                yAxisLabel = yAxisElement.firstChild.data.strip()

                xAttr = xAxisElement.attributes
                yAttr = yAxisElement.attributes

                minX = float(xAttr["min"].value)
                maxX = float(xAttr["max"].value)
                minY = float(yAttr["min"].value)
                maxY = float(yAttr["max"].value)

                xSize = maxX - minX
                ySize = maxY - minY
                xCenter = xSize / 2.0 + minX

                xPlaces = max(4-round(math.log(xSize,10)),0)
                yPlaces = max(4-round(math.log(ySize,10)),0)

                labelYVal = maxY - 0.10 * ySize

                screen.setworldcoordinates(minX-0.20 * xSize,minY - 0.20 * ySize, \
                    maxX + 0.20 * xSize,maxY + 0.20 * ySize)

                theTurtle.ht()

                theTurtle.penup()
                theTurtle.goto(minX,minY)
                theTurtle.pendown()
                theTurtle.goto(maxX,minY)
                theTurtle.penup()
                theTurtle.goto(minX,minY)
                theTurtle.pendown()
                theTurtle.goto(minX,maxY)
                theTurtle.penup()

                theTurtle.goto(xCenter, minY - ySize * 0.10)
                theTurtle.write(xAxisLabel,align="center",font=("Arial",14,"bold"))

                theTurtle.goto(minX, maxY + 0.05 * ySize)
                theTurtle.write(yAxisLabel,align="center",font=("Arial",14,"bold"))

                for i in range(0,101,10):
                    x = minX + xSize * i / 100.0
                    y = minY + ySize * i / 100.0

                    theTurtle.penup()
                    theTurtle.goto(x,minY+ySize * 0.025)
                    theTurtle.pendown()
                    theTurtle.goto(x,minY-ySize * 0.025)
                    theTurtle.penup()
                    theTurtle.goto(x,minY-ySize * 0.05)

                    theTurtle.write(("%1."+str(xPlaces)+"f")%x,align="center", \
                        font=("Arial",12,"normal"))

                    theTurtle.penup()
                    theTurtle.goto(minX+xSize * 0.025, y)
                    theTurtle.pendown()
                    theTurtle.goto(minX-xSize * 0.025, y)
                    theTurtle.goto(minX-xSize * 0.001, y)
                    theTurtle.write(("%1."+str(yPlaces)+"f")%y,align="right", \
                        font=("Arial",12,"normal"))


                sequences = plotElement.getElementsByTagName("Sequence")

                for sequence in sequences:
                    attr = sequence.attributes

                    label = attr["title"].value.strip()
                    color = attr["color"].value
                    theTurtle.color(color)
                    theTurtle.penup()
                    theTurtle.goto(xCenter,labelYVal)
                    labelYVal -= 0.10 * ySize
                    theTurtle.write(label,align="center",font=("Arial",14,"bold"))

                    dataPoints = sequence.getElementsByTagName("DataPoint")

                    first = dataPoints[0]
                    attr = first.attributes
                    x = float(attr["x"].value)
                    y = float(attr["y"].value)
                    theTurtle.goto(x,y)
                    theTurtle.dot()
                    theTurtle.pendown()

                    for dataPoint in dataPoints:
                        attr = dataPoint.attributes
                        x = float(attr["x"].value)
                        y = float(attr["y"].value)
                        theTurtle.goto(x,y)
                        theTurtle.dot()

                    screen.update()
            except Exception as ex:
                tkinter.messagebox.showerror('Error Reading File', 'There was an error reading the XML plot data:\n' + str(ex))
                print("The error from reading the plot data.")
                print(repr(ex))
                
        def reloadFile():
            if self.currentFile != None: loadFile(self.currentFile)

        open_button = tkinter.Button(self.master, text='Load Plot Data', width=20,
             height=5, bd='10', command=loadFile)
        open_button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        fileMenu.add_command(label="Load Plot Data...",command=loadFile)
        
        fileMenu.add_command(label="Reload Plot Data...",command=reloadFile)

        fileMenu.add_command(label="Exit",command=self.master.quit)

        bar.add_cascade(label="File",menu=fileMenu)

        self.master.config(menu=bar)

        canvas = tkinter.Canvas(self,width=1000,height=800)
        canvas.pack(side=tkinter.LEFT)

        theTurtle = turtle.RawTurtle(canvas)

        screen = theTurtle.getscreen()

        screen.tracer(0)

        if self.datafile != None:
            loadFile(self.datafile.strip())

def main():
    root = tkinter.Tk()
    datafile = None
    if len(sys.argv) > 1:
        datafile = sys.argv[1]
    plotApp = PlotApplication(root, datafile)

    plotApp.mainloop()
    print("Program Execution Completed.")

if __name__ == "__main__":
    main()
