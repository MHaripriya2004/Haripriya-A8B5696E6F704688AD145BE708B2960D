class player:
  def play (self):
   print ("the player is playing cricket.")
  #define the batsman class,derived from player
class batsman(player):
  def play (self):
   print("the batsman iso batting.")
      #define the bowler class,derived from player
class bowler (player):
  def play (self):
    print ("the bowler is bowling.")
    #create objects of batsman and bowler classes 
batsman=batsman ()
bowler=bowler()
#call the play ()method for each object 
batsman.play ()
bowler.play ()
    