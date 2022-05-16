import time
from datetime import datetime
from samplebase import SampleBase
from rgbmatrix import graphics
import requests
from protobuf_to_dict import protobuf_to_dict
from google.transit import gtfs_realtime_pb2
#from config import APIKey

#MTA API Key
APIKey=""

# set color variables
blue = graphics.Color(0, 57, 166)
orange = graphics.Color(255, 99, 25)
black = graphics.Color(0, 0, 0)
white = graphics.Color(255, 255, 255)
yellow = graphics.Color(252, 204, 10)
red = graphics.Color(238,53,46)
silver = graphics.Color(167,169,172)
green = graphics.Color(0,147,60)

# set font colors
whitefont = graphics.Color(255, 255, 255)
orangefont = graphics.Color(
# MTA Color Standards
#ACEblue = graphics.Color(0,57,166)
#BDFMorange = graphics.Color(255,99,25)
#Ggreen = graphics.Color(108,190,69)
#JZbrown = graphics.Color(153,102,51)
#Lsilver = graphics.Color(167,169,172)
#NQRyellow = graphics.Color(252,204,10)
#Sgrey = graphics.Color(128,129,131)
#OneTwoThreered = graphics.Color(238,53,46)
#FourFiveSixgreen = graphics.Color(0,147,60)
#Sevenpurple = graphics.Color(185,51,173)


# Subway Lines
BDFMfeed = 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-bdfm'  # B,D,F,M
ACEHfeed = 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-ace'  # A,C,E,H
OneTwoThreefeed = 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs'  # 1,2,3,4,5,6,7
Gfeed = 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-g'  # G
NQRWfeed = 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-nqrw'  # N,Q,R,W
JZfeed = 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-jz'  # J,Z
Lfeed = 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-l' # L
SIRfeed = 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-si' # SIR (Staten Island Railway)

#Add your feeds here
feedsToCheck = [OneTwoThreefeed, ACEHfeed]
feedScores = dict.fromkeys(feedsToCheck, 0)


class RunText(SampleBase):

    def __init__(self, *args, **kwargs):
        for key in kwargs:
            print(key, kwargs[key])
        for arg in args:
            print(arg)

        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

    def drawCircle(self, canvas, offset, color):
        graphics.DrawLine(canvas, 7, 0 + offset, 11, 0 + offset, color)
        graphics.DrawLine(canvas, 5, 1 + offset, 13, 1 + offset, color)
        graphics.DrawLine(canvas, 4, 2 + offset, 14, 2 + offset, color)
        graphics.DrawLine(canvas, 4, 3 + offset, 14, 3 + offset, color)
        graphics.DrawLine(canvas, 3, 4 + offset, 15, 4 + offset, color)
        graphics.DrawLine(canvas, 3, 5 + offset, 15, 5 + offset, color)
        graphics.DrawLine(canvas, 3, 6 + offset, 15, 6 + offset, color)
        graphics.DrawLine(canvas, 3, 7 + offset, 15, 7 + offset, color)
        graphics.DrawLine(canvas, 3, 8 + offset, 15, 8 + offset, color)
        graphics.DrawLine(canvas, 4, 9 + offset, 14, 9 + offset, color)
        graphics.DrawLine(canvas, 4, 10 + offset, 14, 10 + offset, color)
        graphics.DrawLine(canvas, 5, 11 + offset, 13, 11 + offset, color)
        graphics.DrawLine(canvas, 7, 12 + offset, 11, 12 + offset, color)

    def draw_a(self, location, canvas):
        if location == 'top':
            text_offset = 0
            circle_offset = 2
        else:
            text_offset = 16
            circle_offset = 18

        self.drawCircle(canvas, circle_offset, blue)

        graphics.DrawLine(canvas, 7, 7 + text_offset, 7, 11 + text_offset, white)
        graphics.DrawLine(canvas, 11, 7 + text_offset, 11, 11 + text_offset, white)
        graphics.DrawLine(canvas, 8, 6 + text_offset, 8, 6 + text_offset, white)
        graphics.DrawLine(canvas, 9, 5 + text_offset, 9, 5 + text_offset, white)
        graphics.DrawLine(canvas, 10, 6 + text_offset, 10, 6 + text_offset, white)
        graphics.DrawLine(canvas, 8, 9 + text_offset, 10, 9 + text_offset, white)

    def draw_c(self, location, canvas):
        if location == 'top':
            text_offset = 0
            circle_offset = 2
        else:
            text_offset = 16
            circle_offset = 18

        self.drawCircle(canvas, circle_offset, blue)

        graphics.DrawLine(canvas, 7, 6 + text_offset, 7, 10 + text_offset, white)
        graphics.DrawLine(canvas, 8, 5 + text_offset, 10, 5 + text_offset, white)
        graphics.DrawLine(canvas, 8, 11 + text_offset, 10, 11 + text_offset, white)
        graphics.DrawLine(canvas, 11, 6 + text_offset, 11, 6 + text_offset, white)
        graphics.DrawLine(canvas, 11, 10 + text_offset, 11, 10 + text_offset, white)

    def draw_e(self, location, canvas):
        if location == 'top':
            text_offset = 0
            circle_offset = 2
        else:
            text_offset = 16
            circle_offset = 18

        self.drawCircle(canvas, circle_offset, blue)

        graphics.DrawLine(canvas, 7, 5 + text_offset, 7, 11 + text_offset, white)
        graphics.DrawLine(canvas, 8, 5 + text_offset, 11, 5 + text_offset, white)
        graphics.DrawLine(canvas, 8, 8 + text_offset, 10, 8 + text_offset, white)
        graphics.DrawLine(canvas, 8, 11 + text_offset, 11, 11 + text_offset, white)
    
    def draw_b(self, location, canvas):
        if location == 'top':
            text_offset = 0
            circle_offset = 2
        else:
            text_offset = 16
            circle_ofset = 18
            
        self.drawCircle(canvas, circle_offset, orange)
        
        graphics.Drawline(canvas, 7, 5 + text_offset, 7, 11 + text_offset, white)
        graphics.Drawline(canvas, 8, 5 + text_offset, 10, 5 + text_offset, white)
        graphics.Drawline(canvas, 8, 8 + text_offset, 10, 8 + text_offset, white)
        graphics.Drawline(canvas, 8, 11 + text_offset, 11, 10 + text_offset, white)
        graphics.Drawline(canvas, 11, 6 + text_offset, 11, 7 + text_offset, white)
        graphics.Drawline(canvas, 11, 9 + text_offset, 11, 10 + text_offset, white)
    
    def draw_d(self, location, canvas):
        if location == 'top':
            text_offset = 0
            circle_offset = 2
        else:
            text_offset = 16
            circle_offset = 18

        self.drawCircle(canvas, circle_offset, orange)

        graphics.DrawLine(canvas, 7, 5 + text_offset, 7, 11 + text_offset, white)
        graphics.DrawLine(canvas, 8, 5 + text_offset, 10, 5 + text_offset, white)
        graphics.DrawLine(canvas, 8, 11 + text_offset, 10, 11 + text_offset, white)
        graphics.DrawLine(canvas, 11, 6 + text_offset, 11, 10 + text_offset, white)

    def draw_m(self, location, canvas):
        if location == 'top':
            text_offset = 0
            circle_offset = 2
        else:
            text_offset = 16
            circle_offset = 18

        self.drawCircle(canvas, circle_offset, orange)

        graphics.DrawLine(canvas, 6, 5 + text_offset, 6, 11 + text_offset, white)
        graphics.DrawLine(canvas, 12, 5 + text_offset, 12, 11 + text_offset, white)
        graphics.DrawLine(canvas, 7, 6 + text_offset, 7, 6 + text_offset, white)
        graphics.DrawLine(canvas, 8, 7 + text_offset, 8, 7 + text_offset, white)
        graphics.DrawLine(canvas, 9, 8 + text_offset, 9, 8 + text_offset, white)
        graphics.DrawLine(canvas, 10, 7 + text_offset, 10, 7 + text_offset, white)
        graphics.DrawLine(canvas, 11, 6 + text_offset, 11, 6 + text_offset, white)

    def draw_f(self, location, canvas):
        if location == 'top':
            text_offset = 0
            circle_offset = 2
        else:
            text_offset = 16
            circle_offset = 18

        self.drawCircle(canvas, circle_offset, orange)

        graphics.DrawLine(canvas, 7, 5 + text_offset, 11, 5 + text_offset, white)
        graphics.DrawLine(canvas, 7, 6 + text_offset, 7, 11 + text_offset, white)
        graphics.DrawLine(canvas, 8, 8 + text_offset, 9, 8 + text_offset, white)
        
    def draw_one(self, location, canvas):
        if location == 'top':
            text_offset = 0
            circle_offset = 2
        else:
            text_offset = 16
            circle_offset = 18

        self.drawCircle(canvas, circle_offset, red)

        graphics.DrawLine(canvas, 8, 6 + text_offset, 8, 6 + text_offset, white)
        graphics.DrawLine(canvas, 8, 11 + text_offset, 8, 11 + text_offset, white)
        graphics.DrawLine(canvas, 9, 5 + text_offset, 9, 11 + text_offset, white)
        graphics.DrawLine(canvas, 10, 11 + text_offset, 10, 11 + text_offset, white)
        
    def draw_two(self, location, canvas):
        if location == 'top':
            text_offset = 0
            circle_offset = 2
        else:
            text_offset = 16
            circle_offset = 18

        self.drawCircle(canvas, circle_offset, red)

        graphics.DrawLine(canvas, 7, 6 + text_offset, 7, 6 + text_offset, white)
        graphics.DrawLine(canvas, 7, 11 + text_offset, 11, 11 + text_offset, white)
        graphics.DrawLine(canvas, 8, 5 + text_offset, 10, 5 + text_offset, white)
        graphics.DrawLine(canvas, 8, 10 + text_offset, 8, 10 + text_offset, white)
        graphics.DrawLine(canvas, 9, 9 + text_offset, 9, 9 + text_offset, white)
        graphics.DrawLine(canvas, 10, 8 + text_offset, 10, 8 + text_offset, white)
        graphics.DrawLine(canvas, 11, 6 + text_offset, 11, 7 + text_offset, white)
    
    def draw_three(self, location, canvas):
        if location == 'top':
            text_offset = 0
            circle_offset = 2
        else:
            text_offset = 16
            circle_offset = 18

        self.drawCircle(canvas, circle_offset, red)

        graphics.DrawLine(canvas, 7, 5 + text_offset, 11, 5 + text_offset, white)
        graphics.DrawLine(canvas, 7, 10 + text_offset, 7, 10 + text_offset, white)
        graphics.DrawLine(canvas, 8, 11 + text_offset, 10, 11 + text_offset, white)
        graphics.DrawLine(canvas, 9, 8 + text_offset, 10, 8 + text_offset, white)
        graphics.DrawLine(canvas, 10, 7 + text_offset, 10, 7 + text_offset, white)
        graphics.DrawLine(canvas, 11, 6 + text_offset, 11, 6 + text_offset, white)
        graphics.DrawLine(canvas, 11, 9 + text_offset, 11, 10 + text_offset, white)
        
    def gettimes(self, feed, s1, s2):

        uptownTimes = []
        downtownTimes = []
        uptownTrainIDs = []
        downtownTrainIDs = []
        route_id = ""

        # Request parameters
        headers = {'x-api-key': APIKey}

        # Get the train data from the MTA
        try:
            response = requests.get(feed, headers=headers, timeout=30)
        except:
            return 'fail'
        # Parse the protocol buffer that is returned
        feed = gtfs_realtime_pb2.FeedMessage()
        try:
            feed.ParseFromString(response.content)
        except:
            return 'fail'
        # Get a list of all the train data
        subway_feed = protobuf_to_dict(feed)  # subway_feed is a dictionary
        realtime_data = subway_feed['entity']  # train_data is a list

        # Iterate over each train arrival
        for train in realtime_data:
            # If there is a trip update with a stop time update
            if train.get('trip_update'):
                if (train['trip_update'].get('stop_time_update')):
                    # get for each stop time update that is at our stop
                    for update in train['trip_update'].get('stop_time_update'):
                        stop_id = update['stop_id']

                        if (stop_id in [s1, s2]):

                            # Get the number of seconds from now to the arrival time
                            elapsed = update['arrival']['time'] - time.mktime(datetime.now().timetuple())

                            # If we alredy missed it, skip it
                            if (elapsed < 0):
                                continue

                            route_id = (train['trip_update']['trip']['route_id'])[0]

                            # Calculate minutes and seconds until arrival
                            mins = int(elapsed / 60)
                            secs = int(elapsed % 60)


                            # Round to nearest minute
                            if (secs > 30):
                                mins = mins + 1

                            # Skips zeros
                            if (mins == 0):
                                continue

                            if (stop_id == s1):
                                # Check for dupes and then append
                                if (mins not in uptownTimes):
                                    uptownTimes.append(mins)
                                    uptownTrainIDs.append(route_id)

                            if (stop_id == s2):
                                if (mins not in downtownTimes):
                                    downtownTimes.append(mins)
                                    downtownTrainIDs.append(route_id)

        # Sort the results
        if (len(uptownTimes) != 0):
            (uptownTimes, uptownTrainIDs) = tuple(zip(*sorted(zip(uptownTimes, uptownTrainIDs), key=lambda p: p[0])))

        if (len(downtownTimes) != 0):
            (downtownTimes, downtownTrainIDs) = tuple(zip(*sorted(zip(downtownTimes, downtownTrainIDs), key=lambda p: p[0])))

        # Return our results as a tuple
        return(uptownTrainIDs, uptownTimes, downtownTrainIDs, downtownTimes)

    def getTrainTimes(self, ourUptownStation, ourDowntownStation):
        global feedsToCheck
        global feedScores

        uptownTrainIDs = []
        uptownTimes = []
        downtownTrainIDs = []
        downtownTimes = []


        # Check each of the feeds in turn for trains arriving at our station until
        # we get some results
        for f in feedsToCheck:
            times = self.gettimes(f, ourUptownStation, ourDowntownStation)
            # If we found our station in the feed, then increment the feed's score and break out
            if times == 'fail':
                return 'fail'
            if (len(times[0]) != 0):
                # Found uptown
                feedScores[f] += 1
                uptownTrainIDs = times[0]
                uptownTimes = times[1]
                if (len(downtownTrainIDs) != 0):
                    # Found both
                    break
            if (len(times[2]) != 0):
                # Found downtown
                feedScores[f] += 1
                downtownTrainIDs = times[2]
                downtownTimes = times[3]
                if (len(uptownTrainIDs) != 0):
                    # Found both
                    break

        # Sort 'feedsToCheck' so that we are checking the most likely feeds first
        feedsToCheck = sorted(feedsToCheck, reverse=True, key=lambda p: feedScores[p])

        return (uptownTrainIDs, uptownTimes, downtownTrainIDs, downtownTimes)

    def run(self):
        loop = 0

        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont('fonts/5x8.bdf')
        
        while True:
            if loop == 0:
                desc_top = "Uptown"
                desc_bottom = "Downtown"
                loop += 1
            else:
                desc_top = "Bronx"
                desc_bottom = "Brooklyn"
                loop = 0

            offscreen_canvas.Clear()


            # grab 123 train times and first uptown and downtown line
            train_times = self.getTrainTimes("120N", "120S")
            if train_times == 'fail':
                loop = 0
                while train_times == 'fail':
                    train_times = self.getTrainTimes("120N", "120S")
                    loop += 1
                    print('Fail Loop Count: ' + loop)
                    if loop == 10:
                        top_line = 'B'
                        top_line_time = 99
                        bottom_line = 'B'
                        bottom_line_time = 99

                        break
            else:
                if train_times == 'fail':
                    top_line = 'X'
                    top_line_time = 99
                    bottom_line = 'X'
                    bottom_line_time = 99
                else:
                    top_line = train_times[0][0]
                    top_line_time = train_times[1][0]
                    bottom_line = train_times[2][0]
                    bottom_line_time = train_times[3][0]

            # grab the ACE trains and first uptown and downtown line
            train_times2 = self.getTrainTimes("A19N", "A19S")
            if train_times2 == 'fail':
                top_line2 = 'X'
                top_line_time2 = 99
                bottom_line2 = 'X'
                bottom_line_time2 = 99
            else:
                top_line2 = train_times2[0][0]
                top_line_time2 = train_times2[1][0]
                bottom_line2 = train_times2[2][0]
                bottom_line_time2 = train_times2[3][0]

            # if AE line will show up before  DFM

            if top_line_time2 < top_line_time:
                top_line_time = top_line_time2
                top_line = top_line2
            time_top = str(top_line_time) + 'min'

            if bottom_line_time2 < bottom_line_time:
                bottom_line_time = bottom_line_time2
                bottom_line = bottom_line2
            time_bottom = str(bottom_line_time) + 'min'

            print('Top Line: ' + top_line + ' - ' + 'Time: ' + time_top)
            print('Bottom Line: ' + bottom_line + ' - ' + 'Time: ' + time_bottom)
            print('---------------------------------------------------------')

            # top image print
            if top_line == 'A':
                self.draw_a('top', offscreen_canvas)
            elif top_line == 'C':
                self.draw_c('top', offscreen_canvas)
            elif top_line == 'E':
                self.draw_e('top', offscreen_canvas)
            elif top_line == 'B':
                self.draw_b('top', offscreen_canvas)
            elif top_line == 'D':
                self.draw_d('top', offscreen_canvas)
            elif top_line == 'F':
                self.draw_f('top', offscreen_canvas)
            elif top_line == 'M':
                self.draw_m('top', offscreen_canvas)
            elif top_line == '1':
                self.draw_one('top', offscreen_canvas)
            elif top_line == '2':
                self.draw_two('top', offscreen_canvas)
            elif top_line == '3':
                self.draw_three('top', offscreen_canvas)              
            elif top_line == '4':
                self.draw_four('top', offscreen_canvas)
            elif top_line == '5':
                self.draw_five('top', offscreen_canvas)
            elif top_line == '6':
                self.draw_six('top', offscreen_canvas)
            elif top_line == '7':
                self.draw_seven('top', offscreen_canvas)
            elif top_line == 'G':
                self.draw_g('top', offscreen_canvas)
            elif top_line == 'J':
                self.draw_j('top', offscreen_canvas)
            elif top_line == 'Z':
                self.draw_z('top', offscreen_canvas)
        
            # bottom image print
            if bottom_line == 'A':
                self.draw_a('bottom', offscreen_canvas)
            elif bottom_line == 'C':
                self.draw_c('bottom', offscreen_canvas)
            elif bottom_line == 'E':
                self.draw_e('bottom', offscreen_canvas)
            elif bottom_line == 'B':
                self.draw_b('bottom', offscreen_canvas)
            elif bottom_line == 'D':
                self.draw_d('bottom', offscreen_canvas)
            elif bottom_line == 'F':
                self.draw_f('bottom', offscreen_canvas)
            elif bottom_line == 'M':
                self.draw_m('bottom', offscreen_canvas)
            elif bottom_line == '1':
                self.draw_one('bottom', offscreen_canvas)
            elif bottom_line == '2':
                self.draw_two('bottom', offscreen_canvas)
            elif bottom_line == '3':
                self.draw_three('bottom', offscreen_canvas)              
            elif bottom_line == '4':
                self.draw_four('bottom', offscreen_canvas)
            elif bottom_line == '5':
                self.draw_five('bottom', offscreen_canvas)
            elif bottom_line == '6':
                self.draw_six('bottom', offscreen_canvas)
            elif bottom_line == '7':
                self.draw_seven('bottom', offscreen_canvas)
            elif bottom_line == 'G':
                self.draw_g('bottom', offscreen_canvas)
            elif bottom_line == 'J':
                self.draw_j('bottom', offscreen_canvas)
            elif bottom_line == 'Z':
                self.draw_z('bottom', offscreen_canvas)

            # shift time text left so it still lines up
            if len(time_top) == 5:
                top_offset = 0
            else:
                top_offset = 0
            if len(time_bottom) == 5:
                bottom_offset = 0
            else:
                bottom_offset = 0

            # draw descriptions for 32x64 Matrix
            graphics.DrawText(offscreen_canvas, font, 20, 8, white, desc_top)
            graphics.DrawText(offscreen_canvas, font, 20, 24, white, desc_bottom)
            graphics.DrawLine(offscreen_canvas, font, 0, 16, 64, 16, white)

            # draw time for 32x64 Matrix
            graphics.DrawText(offscreen_canvas, font, 20 + top_offset, 14, orangefont, time_top)
            graphics.DrawText(offscreen_canvas, font, 20 + bottom_offset, 30, orangefont, time_bottom)

            time.sleep(1)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

            # sleep for 30 seconds before running again
            time.sleep(30)
        
        # Add delay when subways are down for maintenance or else we spam API
        time.sleep(30)

if __name__ == '__main__':
    while True:
        run_text = RunText()
        if (not run_text.process()):
            run_text.print_help()

        time.sleep(5)
