# PYTHON script
import os
import meta
import time
from meta import models
from meta import results
from meta import utils
from meta import windows
from meta import guitk
import webbrowser



def selectfile():
	print('Select the file for reading')
	read_file_inp = utils.SelectOpenFile(0, 'inp (*.inp)')
	read_file_odb = read_file_inp[0].replace(".inp",".odb")
	read_file_path = "/".join(read_file_inp[0].split("/")[:-1])+"/"
	if not read_file_inp:
		print('No file was selected')
	else:
		print('The file selected is: ' + read_file_inp[0])
	return [read_file_inp[0],read_file_odb,read_file_path]



def delete_existing_model(M):
	model_id = M[0].id
	window_name = windows.ActiveWindow().name
	models.DeleteModel(model_id, window_name)


def reset_all():
	utils.MetaCommand('model active all')
	utils.MetaCommand('window enable all')
	utils.MetaCommand('color fringebar window "MetaPost" scalarset "StressTensor"')
	utils.MetaCommand('window active "MetaPost"')
	utils.MetaCommand('window position 0,0')
	utils.MetaCommand('window active "MetaPost"')
	utils.MetaCommand('window size 186,163')
	utils.MetaCommand('window active "MetaPost"')
	utils.MetaCommand('window maximize "MetaPost"')
	utils.MetaCommand('window size 186,163')
	utils.MetaCommand('window size 1503,974')
	utils.MetaCommand('window size 1520,974')
	utils.MetaCommand('write options outputsize workspace 1520,974')
	utils.MetaCommand('window clearcreate 3d keepses')
	utils.MetaCommand('window size 1520,974')
	utils.MetaCommand('report clear all')
	utils.MetaCommand('spreadsheet clearall')
	utils.MetaCommand('options var clearuservars')

class BCGUI:
	
	
	def Q_prompt():
		w = guitk.BCWindowCreate("CheckBox", guitk.constants.BCOnExitDestroy)
		
		#Create check box
		cbenable = guitk.BCCheckBoxCreate(w, "Modal Analysis: Result images (Powerpoint will be created in the .inp path location)")
		cbenable2 = guitk.BCCheckBoxCreate(w, "Modal Analysis: Result gifs (Folder and .gif for each mode will be created in the .inp path location)")
		
		#Set the initial state of checkbox 
		guitk.BCCheckBoxSetChecked(cbenable, True)
		guitk.BCCheckBoxSetChecked(cbenable2, False)
		
		#Set the function to be called when the Check Box is toggled
		guitk.BCCheckBoxSetToggledFunction(cbenable, BCGUI.CheckBoxEnableChangedState, None)
		guitk.BCCheckBoxSetToggledFunction(cbenable2, BCGUI.CheckBoxEnableChangedState,None)
		
		data = [cbenable,cbenable2]
		#PushButtons tend to occupy all available width
		
		#Set the Corrensponding behaviour for PushButton when the Check box change states
		dbb = guitk.BCDialogButtonBoxCreate(w)
		guitk.BCWindowSetAcceptFunction(w, BCGUI.acceptFunc, None)
		guitk.BCWindowSetRejectFunction(w, BCGUI.rejectFunc, None)
		
		guitk.BCShow(w)
		
		cb1 = guitk.BCCheckBoxIsChecked(data[0])
		cb2 = guitk.BCCheckBoxIsChecked(data[1])		
		return [cb1,cb2]
		
		
	def acceptFunc(w, data):
			print("Running")
			return 1	
			
	def rejectFunc(w, data):
			print("Exit")
			return 1		
	
	
	def CheckBoxEnableChangedState(cb, state, data):
		str_state = "Off"
		if guitk.BCCheckBoxIsChecked(cb): str_state = "On"
		print ("State of '", guitk.BCCheckBoxText(cb), "' checkBox is ", str_state)
		return 0
		
	def Q_States(st_list):
		window = guitk.BCWindowCreate("Example LineEdit", guitk.constants.BCOnExitDestroy)
		hl = guitk.BCBoxLayoutCreate(window, guitk.constants.BCHorizontal)
		guitk.BCLabelCreate(hl, "Amount of states: ")
		lineedit = guitk.BCLineEditCreate(hl, "")
		
		
		f = guitk.BCFrameCreate(window)
		l = guitk.BCBoxLayoutCreate(f, guitk.constants.BCHorizontal)
		listView = guitk.BCListViewCreate(window, 2, ['ID', 'State'], 1)
		BCGUI.appendPartListViewItems(listView,st_list)
		
		guitk.BCLineEditSetInfo(lineedit, "If you enter e.g. 5, you will obtain: (Base State + 5 states)")
		guitk.BCShow( window )
		
		output = guitk.BCLineEditGetText(lineedit)
		
		return output


	def appendPartListViewItems(listView,st_list):
		rn = [0,0]
		cols = guitk.BCListViewColumns(listView)
		guitk.BCListViewSaveSortStateAndDisableSorting(listView)
		
		cc = -1
		for stateI in st_list:
			cc += 1
			guitk.BCListViewAddItem(listView, cols, [str(cc),str(stateI)], rn)

		guitk.BCListViewRestoreSortState(listView)


class MetaCommands:

	def SetStates(state):
		utils.MetaCommand('0:option state '+str(state)+'')
		
	def DeleteAllStates():
		utils.MetaCommand('0:displ delete all')
		utils.MetaCommand('0:function delete all')
		
	def ScalarFringe():
		utils.MetaCommand('grstyle scalarfringe enable')
		
	def Create_Annotation():
		utils.MetaCommand('annotation add 1 "Empty Annotation"')
		utils.MetaCommand('annotation text 1 text " Mode = \$mode0 \\n Frequency = \$frequency0\[2f\] Hz"')
		
		utils.MetaCommand('annotation text 1 color Black')
		utils.MetaCommand('annotation text 1 font "MS Shell Dlg 2,24,-1,5,75,0,0,0,0,0"')
		utils.MetaCommand('annotation background 1 transp 0.990000')
		utils.MetaCommand('annotation background 1 color manual 175_199_255_255')		
		utils.MetaCommand('annotation position 1 setxy 0.177528 0.885521')
		
	def SetEntities():
		#Set all entities on or only shell + solid?
		utils.MetaCommand('era global all 0')
		utils.MetaCommand('add global shell 0')
		#utils.MetaCommand('add global solid 0')
	
	def deformation():
		#Set fringe options on deformation
		utils.MetaCommand('grstyle deform on')
		utils.MetaCommand('grstyle scalarfringe onnode')
		utils.MetaCommand('grstyle scalarfringe cplot')
		
		
	def Front_view():
		#FRONT VIEW
		utils.MetaCommand('view scale in 0.599588,0.528438')
		utils.MetaCommand('view set -1.07617,3.20851,0.124798,-15.4229,44.1412,-6.63185,-0.134783,0.115211,0.984154,-15.4229,44.1412,-6.63185,-22.6615,110.456,28,0')
		

	def Rear_view():		
		#REAR VIEW
		utils.MetaCommand('view scale in 0.579412,0.355739')
		utils.MetaCommand('view set 1.95099,2.44514,-0.171699,22.3481,-24.1667,-14.7986,0.204727,-0.346286,0.915518,22.3481,-24.1667,-14.7986,-2.92738,76.0896,28,0')

	def Right_view():
		utils.MetaCommand('view scale in 0.579412,0.355739')
		utils.MetaCommand('view set -1.87847,0.81362,-1.09925,23.3992,27.1376,-3.60151,0.0388997,0.0574733,0.997589,23.3992,27.1376,-3.60151,-2.92738,76.0896,28,0')
		
	def Left_view():		
		utils.MetaCommand('view scale out 0.646291,0.409514')
		utils.MetaCommand('view set 0.302619,3.63385,-0.440926,11.9623,40.2626,-21.639,0.363702,0.377157,0.851747,11.9623,40.2626,-21.639,-22.6615,110.456,28,0')
		
		
	def reportComposer(nbr_states,filename):
		
		
		#Set window size
		utils.MetaCommand('window size 1456,967')
		utils.MetaCommand('write options outputsize workspace 1456,967')
		
		#Create report
		utils.MetaCommand('report windows pptx active "Report Composer 1"')
		utils.MetaCommand('report windows pptx new "Report Composer 1"')
		

		utils.MetaCommand('srange window "MetaPost" auto enable')
		
		#Scale deformations
		utils.MetaCommand('disp scale multiplier 5.000000E+001')
		
		#Create annotation
		MetaCommands.Create_Annotation()
		
		######Extract modes from different states and save in PP
		for i in range(nbr_states+2):
			
			MetaCommands.SetStates(i)
			
			Set_slide = 'Slide '+str(i+1)
			
			utils.MetaCommand('0:options state variable gen "serial=5" 340.000000')
			utils.MetaCommand('report presentation nameaddslide "'+Set_slide+'"')
			

			MetaCommands.Front_view()
			utils.MetaCommand('clipboard copy image "MetaPost"')
			utils.MetaCommand('report presentation slide clipboard pasteimage "'+Set_slide+'"')
			utils.MetaCommand('report presentation slide element resize "'+Set_slide+'" "Image 1" 0.0512 0.1026 0.5098 0.4514')
			utils.MetaCommand('report presentation slide element move "'+Set_slide+'" "Image 1" 0.0008 -0.0037')
			
			
			MetaCommands.Rear_view()
			utils.MetaCommand('clipboard copy image "MetaPost"')
			utils.MetaCommand('report presentation slide clipboard pasteimage "'+Set_slide+'"')
			utils.MetaCommand('report presentation slide element resize "'+Set_slide+'" "Image 2" 0.0512 0.1026 0.5098 0.4514')
			utils.MetaCommand('report presentation slide element move "'+Set_slide+'" "Image 2" 0.4899 -0.0037')
			
			
			MetaCommands.Left_view()
			utils.MetaCommand('clipboard copy image "MetaPost"')
			utils.MetaCommand('report presentation slide clipboard pasteimage "'+Set_slide+'"')
			utils.MetaCommand('report presentation slide element resize "'+Set_slide+'" "Image 3" 0.0512 0.1026 0.5098 0.4514')
			utils.MetaCommand('report presentation slide element move "'+Set_slide+'" "Image 3" -0.0009 0.5394')
			
			
			MetaCommands.Right_view()
			utils.MetaCommand('clipboard copy image "MetaPost"')
			utils.MetaCommand('report presentation slide clipboard pasteimage "'+Set_slide+'"')
			utils.MetaCommand('report presentation slide element resize "'+Set_slide+'" "Image 4" 0.0512 0.1026 0.5098 0.4514')
			utils.MetaCommand('report presentation slide element move "'+Set_slide+'" "Image 4" 0.4887 0.5438')
			

		
		#SAVE Powerpoint
		
		head, sep, tail = str(os.path.basename(filename)).partition('.')
		
		utils.MetaCommand('report presentation options save textbox autofit shrinkwrap enable')
		utils.MetaCommand('report presentation options save variables values enable')
		utils.MetaCommand('report presentation saveas "'+str(os.path.dirname(filename))+'/'+'PP_'+head+'.pptx'+'"')

class animation():
	
	
	def main_An(path,state,anim_state):
		
		print('main_An;State=',state)
		animation.Vis_Settings()
		Anim_path = animation.Create_Folder(path)
		
		animation.Create_Animation(Anim_path,state,anim_state)
		
		
	def anim_frontview():
		utils.MetaCommand('view set 1.21076,0.976504,1.19337,-11.258,32.3771,-15.2417,-0.086809,0.434696,0.896384,-11.258,32.3771,-15.2417,-19.2813,94.4233,28,0')
		return 'FrontView'
		
	def anim_rearview():	
		utils.MetaCommand('view set -2.1595,5.26514,1.37312,15.6079,-26.2717,-8.69316,0.128992,-0.234848,0.963435,15.6079,-26.2717,-8.69316,-19.2813,94.4233,28,0')
		return 'RearView'
	
	
		
	def Vis_Settings():
		utils.MetaCommand('era global gap 0')
		utils.MetaCommand('era global solsurf 0')
		
		#Set scaled deformations
		utils.MetaCommand('disp scale multiplier 5.000000E+001')
		
		#Gif settings
		utils.MetaCommand('record gif fps 12')
		
	def Create_Folder(path):
		path.strip()
		print('path+fig: ',path,'Figures/')
		try:
			os.mkdir(path+'Figures/')
			print("Directory " , path ,  " Created ")
		except FileExistsError:
			print("Directory " , path ,  " already exists")
		return path+'Figures/'
		
	def Create_Animation(Anim_path,state,anim_state):
		
		#Set state
		utils.MetaCommand('0:options state variable "serial='+str(state)+'"')
		
		
		#Front_view



		utils.MetaCommand('0:states winlock "MetaPost" -1')
		utils.MetaCommand('0:states winlock "MetaPost" '+str(anim_state)+'')
		
		utils.MetaCommand('animation autogen enable')
		utils.MetaCommand('animation for')
		time.sleep(2)
		utils.MetaCommand('animation off')
		utils.MetaCommand('0:opt winstate "MetaPost" '+str(anim_state)+'')
		
		view = animation.anim_frontview()
		utils.MetaCommand('record movie fab loop 1 gif "'+Anim_path+'Mode'+str(state)+view+'.gif'+'"')
		
		
		#Rear_view
		view = animation.anim_rearview()
		time.sleep(2)
		

		utils.MetaCommand('record movie fab loop 1 gif "'+Anim_path+'Mode'+str(state)+view+'.gif'+'"')
		
		
################################################################################################
################################################################################################	
	
def main(ls_alt):
	global path
	if ls_alt[0]:
		window_name = 'MetaPost'
	
		filename_lst = selectfile()
		print('filename',filename_lst)
		filename_inp = filename_lst[0]
		filename = filename_lst[1]
		path =filename_lst[2]
		deck = 'ABAQUS'
		r = models.LoadModel(window_name, filename_inp, deck)
		model_id = r.id
		
		
		### Reads in all available states and print it in info window for user, then deletes them. 
		
		#"AllStates" variable is set to read: Base State + 99 States
		AllStates = '1-100'
		
		data_tmp = 'Displacements'
		temp_resultsets = results.LoadDeformations(model_id, filename, deck, AllStates, data_tmp)
		
		st_list =[]
		print('Available states:')
		for res in temp_resultsets:
			print(res.name, res.nodal_data_name, res.function_data_name, res.state)
			tmp_list = [res.name, res.nodal_data_name, res.function_data_name, res.state]
			st_list.append(tmp_list)
				
		MetaCommands.DeleteAllStates()
		
		###
		
		
		nbr_states = int(BCGUI.Q_States(st_list))
		states = '1-'+str(nbr_states+1)
		print ('Selected states: ' +  '1-'+str(nbr_states))
		
		data = 'Displacements'
		new_resultsets = results.LoadDeformations(model_id, filename, deck, states, data)
		data = 'Displacements,Magnitude'
		new_resultsets = results.LoadScalar(model_id, filename, deck, states, data)
		
		
		print('Selected states:')
		for res in new_resultsets:
			print(res.name, res.nodal_data_name, res.function_data_name, res.state)
	
		fringe_name = 'StressTensor'
		fringe_type = 'scalar'
		windows.ActivateFringe(window_name, fringe_name, fringe_type)
		
		
		
		MetaCommands.ScalarFringe()
		MetaCommands.SetEntities()
		utils.MetaCommand('options fringebar off')
	
	
		MetaCommands.deformation()
		MetaCommands.reportComposer(nbr_states,filename)
	
	
	if ls_alt[1]:
		if ls_alt[0]:
			### Animation stage
			anim_state = 1
			for i in range(nbr_states+1):
				print('sdada',i)
				if i > 0 and i < 6:
					anim_state += 18
				elif i == 6:
					anim_state = 92
				elif i > 6:
					anim_state += 1
				print('anim_state',anim_state)
				animation.main_An(path,i,anim_state)
		else:
			print('\n',80*'*','\n',80*'*','\n',80*'*','\n','\n','Please check box: Modal Analysis: Result images, to generate animations','\n','\n',80*'*','\n',80*'*','\n',80*'*')		


class html():
	
	def Gen():
		# write-html.py
		print('path',path)
		f = open(path+'\Figures\Results_Overview.html','w')
		
		message = """<html>
		<head></head>
		<body>
		<h1>Figures and Animations</h1>
		<p>Click for large version</p>
		<hr>
		<h2>Modal Analysis (First 4 modes displayed)</h2>
		<a href="Mode1FrontView.gif"> <img width=40% src="Mode1FrontView.gif"> </a>
		<a href="Mode1RearView.gif"> <img width=40% src="Mode1RearView.gif"> </a>
		
		<a href="Mode2FrontView.gif"> <img width=40% src="Mode2FrontView.gif"> </a>
		<a href="Mode2RearView.gif"> <img width=40% src="Mode2RearView.gif"> </a>
		
		<a href="Mode3FrontView.gif"> <img width=40% src="Mode3FrontView.gif"> </a>
		<a href="Mode3RearView.gif"> <img width=40% src="Mode3RearView.gif"> </a>
		
		<a href="Mode4FrontView.gif"> <img width=40% src="Mode4FrontView.gif"> </a>
		<a href="Mode4RearView.gif"> <img width=40% src="Mode4RearView.gif"> </a>
		<hr>
		
		
		</body>
		</html>"""
		
		f.write(message)
		f.close()
		webbrowser.open_new_tab(path+'\Figures\Results_Overview.html')
	
			
if __name__ == '__main__':
	reset_all()
	utils.ClearMonitor()
	M = models.ActiveModels()
	if M:
		delete_existing_model(M)
		
	[alt1,alt2] = BCGUI.Q_prompt()
	
	main([alt1,alt2])
	
	html.Gen()	
			
	




