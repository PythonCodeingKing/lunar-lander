import sys
import math
Gravity = -32.2
V=0
Q='n'
G=-32.2
LandTime=0

TInt=10
T=0
Fuel=22000
Ship=11000
Acc=-32.2
XY=52800
TotWt=0
ShipMass=0
FuelMass=0
TotMass=0
Burn=0
BurnMass=0
AvgMass=0
DistTrav=0
Flag=False
Crash=False
FuelOut=False
Thrust=0
TermV=0
TermTime=0

def Initialize():
	global G
	global V
	global Fuel
	global FuelMass
	global Ship
	global ShipMass
	global Acc
	global XY
	global TotWt
	global TotMass
	global T
	global Burn
	global BurnMass
	global Flag
	global Crash
	global FuelOut
	global Thrust
	global TermV
	global TermTime
	global LandTime
	G=-32.2
	print
	print
	print 'A positive velocity is towards the planet, a negative velocity is away from the planet'
	V = input('What velocity (MPH) do you want? ')
	print "velocity set to:",V
	V= (-V)
	Q = raw_input('Do you want to use Earth Gravity? Type y or n. ').lower()
	if Q == "n":
		G = input('earth gravity is 32.2. What do you want? ')
		if G <= 0: 
			while G<=0:
				print 'You have to enter a positive number.  Try again.'
				G = input('earth gravity is 32.2. What do you want? ')
		print'your gravity is set to:',G
		G=-G
	else:
		print 'you successfully set gravity to earth gravity.'
	
	V=V*1.467
	FuelMass=75000/32.2
	Fuel=FuelMass*-G
	ShipMass=11000/32.2
	Ship=ShipMass*-G
	Acc=G
	XY=52800
	TotWt=Fuel+Ship
	TotMass=FuelMass+ShipMass
	T=0
	Burn=0
	BurnMass=0
	Flag=False
	Crash=False
	FuelOut=False
	Thrust=0
	TermV=0
	TermTime=0
	LandTime=0
	Game()
	return;	

def PrintScr():
	global T
	global XY
	global V
	global FuelMass
	global G
	global Burn
	print 'Sec: ',T
	print'Miles + Ft: ',int(XY/5280),' Miles, ',int(XY-(5280*int(XY/5280))),' Feet'
	print'MPH: ',int(-V/1.467)
	print'LB Fuel: ', int(FuelMass*-G)
	print'Last Burn Rate: ',Burn
	print
	
	return;
	
def Game():
	global Flag
	global FuelOut
	global TermTime
	global TermV
	global T
	global TInt
	while Flag==False:
		PrintScr()
		AskFuel()
		Recalculate()
		T=T+TInt
		CheckFuel()
		if FuelOut==True: 
			print 'You Idiot!! You ran out of fuel!'
			TerminalVelocity()
			print 'You landed in ', TermTime,' sec'
			print 'Your final velocity was ',abs(TermV/1.467),' MPH'
			break
		CheckLand()
	CheckCrash()
	return;

def TerminalVelocity():
	global TermTime
	global V
	global G
	global XY
	global TermV
	TermTime=(-V+math.sqrt((V*V)-(4*G*XY)))/(G)
	if TermTime<0: TermTime=(-V-math.sqrt((V*V)-(4*G*XY)))/(G)
	TermV=V+(G*TermTime)
	V=TermV
	return;
	

def CheckFuel():
	global FuelMass
	global FuelOut
	if FuelMass<1:FuelOut=True 
	return;
	

def AskFuel():
	global Burn
	global TInt
	global Fuel
	print 'Max fuel to burn (lbs per sec) over ',TInt,' seconds interval is: ',(Fuel)/TInt
	Burn=input('How many pounds of fuel to burn (lbs per sec): ')
	print
	return;

def Recalculate():
	global Thrust
	global Burn
	global BurnMass
	global G
	global AvgMass
	global TotMass
	global Acc
	global FuelMass
	global TInt
	global Fuel
	global ShipMass
	global TotWt
	global Ship
	global DistTrav
	global V
	global XY
	global LandTime
	Thrust=230*Burn
	BurnMass=Burn/-G
	AvgMass=(TotMass+(TotMass-(BurnMass*TInt)))/2
	Acc=Thrust/AvgMass
	FuelMass=FuelMass-(BurnMass*TInt)
	TotMass=FuelMass+ShipMass
	Fuel=FuelMass*-G
	TotWt=Fuel+Ship
	DistTrav=(0.5*(Acc+G)*TInt*TInt)+(V*TInt)+XY
	if DistTrav < 0:
		LandTime=(-V+math.sqrt((V*V)+(4*(Acc+G)*XY)))/(Acc+G)
		if LandTime < 0:
			LandTime=(-V-math.sqrt((V*V)+(4*(Acc+G)*XY)))/(Acc+G)
		V=V+((Acc+G)*LandTime)
	else:
		V=V+((Acc+G)*TInt)
	XY=DistTrav
	return;

def CheckLand():
	global XY
	global Flag
	if XY <= 10: 
		Flag=True
	return;

def CheckCrash():
	global V
	global Crash
	if abs(V) > (50*1.467):
		Crash=True
		print 'You Crashed!!!  Oh No!'
		print 'Your Velocity at impact was ', int(-V/1.467)
		Ans=raw_input('Play Again?? y/n ').lower()
		if Ans=='n': sys.exit()
		if Ans=='y': Initialize()
	if abs(V) < (10*1.467): 
		print 'Nice job! You Landed Safely!'
		Ans=raw_input('Play Again?? y/n ').lower()
		if Ans=='n': sys.exit()
		if Ans=='y': Initialize()
	else:
		print 'You Landed.  A Little Bumpy - Try Harder Next Time.'
		Ans=raw_input('Play Again?? y/n ').lower()
		if Ans=='n': sys.exit()
		if Ans=='y': Initialize()
	return;
		
	
Initialize()

