

###Author = Yajas Dwivedi
    # This is a script that takes as an input a .txt file of the format 'time encoder potentiometer' where time, encoder and potentiometer
    # are floating point seconds,signed integer and unsigned integer respectively.
    # To run the file simply run the script in a terminal followed by giving an argument - which needs to be a .txt textfile of the format
    # specified above.







import sys
textfile = sys.argv[1]     #Takes in the textfile as an argument


print "reading file"

if textfile is not 0:    #If a valid textfile is entered,the program begins further execution.

    problemCheck = 0     #variable to determine if a file has problems
    potentiometer = []   #initializing list for potentiometer column
    # Start
    f = open(textfile, "r") # Textfile is opened and begins reading
    lines = f.readlines()   #all lines are read and saved in lines
    f.close()

    time = []         #initializing list for time column
    encoder = []      #initializing list for encoder column
    a = []           #general array to store the contents of the text file



    def calibrate():            #Function to calibrate and determine the initial offset as per potentiometer reading
        pot_offset = (potentiometer[0] + potentiometer[1] + potentiometer[2]+ potentiometer[3]+ potentiometer[4]+ potentiometer[5]+ potentiometer[6]+ potentiometer[7]+ potentiometer[8]+ potentiometer[9])/10
        return int (pot_offset) #Returns the average of the first 10 readings of the potentiometer

    def verification(encoder, time, pot, pot_offset):
            for i in range(0, len(time)):
                currentTime = time[i]
                if time[i] > 0.5: #Verification begins only after the first 0.5 seconds since
                    actual_Encoder = encoder[i];  #it's assumed the potentiometer and the encoder are functioning well during that time.
                    expected_Encoder = 30 * (2048/255) * (pot[i] - pot_offset); #Formula to compute the expected encoder theoretical value.
                    if (actual_Encoder > (expected_Encoder - (240*5)) and (     #A tolerance of 10 potentiometer readings or approximately +/- 7.5 degrees
                    actual_Encoder < (expected_Encoder + (240*5)))):            #is given
                        problemCheck = 0;
                        pass



                    else:
                        # pass;
                        problemCheck = 1;
                        print 'Problem at {0} seconds'.format(currentTime) #If an error is found,the time at which it's found is printed
            print "Analysis Complete!"
            if problemCheck == 0:
                print "No issues found!"
            else:
                print"Problems found!"
            return



    for x in lines:
        a = x.split()
        time.append(float(a[0]))               #Time column is taken as an input
        encoder.append(int(a[1]))              #Encoder column is taken as input
        potentiometer.append(int(a[2]))        #Potentiometer column is taken as input

    cal = calibrate()
    verification(encoder, time, potentiometer, cal)
else:
    print "No text file input"

