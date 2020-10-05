# PYTHON script
import os
import meta
from meta import models
from meta import results
from meta import utils
from meta import windows
from meta import guitk
from meta import annotations

class Anno:
	
	def DeleteAnnotations():
		utils.MetaCommand('annotation del 1-100')
	
	def HideAnnotations():
		utils.MetaCommand('erase annotation 1-100')
		
	def ShowAnnotations():
		utils.MetaCommand('add annotation 1-100')
	
	def LHS(model_id,window_name,pointer_position):
		annotation_id = 1
		group_name = 'LHS_PANELS_ELSET'
		head, sep, tail = group_name.partition('_')
		
		text = 'Empty Annotation'
		a = annotations.CreateEmptyAnnotation(window_name, text, annotation_id)
		a = annotations.SetAnnotationPointerOnGroup(annotation_id, model_id, group_name, pointer_position)
			
		utils.MetaCommand('annotation position '+str(annotation_id)+' setxy 0.889752 0.637332')
		Anno.AnnoSettings(annotation_id,head,pointer_position)
		
		
		###Collect values from annotation
		HVal, SVal, TVal = str(a.text).split(',')[1].partition('=')
		return round(float(TVal),3)
		
	def RHS(model_id,window_name,pointer_position):
		annotation_id = 2
		group_name = 'RHS_PANELS_ELSET'
		head, sep, tail = group_name.partition('_')
		
		text = 'Empty Annotation'
		a = annotations.CreateEmptyAnnotation(window_name, text, annotation_id)
		a = annotations.SetAnnotationPointerOnGroup(annotation_id, model_id, group_name, pointer_position)
			
		utils.MetaCommand('annotation position '+str(annotation_id)+' setxy 0.457061 0.328128')
		Anno.AnnoSettings(annotation_id,head,pointer_position)
		
		###Collect values from annotation
		HVal, SVal, TVal = str(a.text).split(',')[1].partition('=')
		return round(float(TVal),3)
		
	def Rear(model_id,window_name,pointer_position):
		annotation_id = 3
		group_name = 'REAR_PANELS_ELSET'
		head, sep, tail = group_name.partition('_')
		
		text = 'Empty Annotation'
		a = annotations.CreateEmptyAnnotation(window_name, text, annotation_id)
		a = annotations.SetAnnotationPointerOnGroup(annotation_id, model_id, group_name, pointer_position)
			
		utils.MetaCommand('annotation position '+str(annotation_id)+' setxy 0.535357 0.402585')
		Anno.AnnoSettings(annotation_id,head,pointer_position)
		
		###Collect values from annotation
		HVal, SVal, TVal = str(a.text).split(',')[1].partition('=')
		return round(float(TVal),3)
		
	def Roof(model_id,window_name,pointer_position):
		annotation_id = 4
		group_name = 'ROOF_PANELS_ELSET'
		head, sep, tail = group_name.partition('_')
		
		text = 'Empty Annotation'
		a = annotations.CreateEmptyAnnotation(window_name, text, annotation_id)
		a = annotations.SetAnnotationPointerOnGroup(annotation_id, model_id, group_name, pointer_position)
			
		utils.MetaCommand('annotation position '+str(annotation_id)+' setxy 0.564890 0.914478')
		Anno.AnnoSettings(annotation_id,head,pointer_position)
		
		###Collect values from annotation
		HVal, SVal, TVal = str(a.text).split(',')[1].partition('=')
		return round(float(TVal),3)
		
	def Front(model_id,window_name,pointer_position):
		annotation_id = 5
		group_name = 'FRONT_PANELS_ELSET'
		head, sep, tail = group_name.partition('_')
		
		text = 'Empty Annotation'
		a = annotations.CreateEmptyAnnotation(window_name, text, annotation_id)
		a = annotations.SetAnnotationPointerOnGroup(annotation_id, model_id, group_name, pointer_position)
			
		utils.MetaCommand('annotation position '+str(annotation_id)+' setxy 0.325192 0.889658')
		Anno.AnnoSettings(annotation_id,head,pointer_position)
		
		###Collect values from annotation
		HVal, SVal, TVal = str(a.text).split(',')[1].partition('=')
		return round(float(TVal),3)
		
	def Bottom(model_id,window_name,pointer_position):
		annotation_id = 6
		group_name = 'BOTTOM_ELSET'
		head, sep, tail = group_name.partition('_')
		
		text = 'Empty Annotation'
		a = annotations.CreateEmptyAnnotation(window_name, text, annotation_id)
		a = annotations.SetAnnotationPointerOnGroup(annotation_id, model_id, group_name, pointer_position)
		
		utils.MetaCommand('annotation position '+str(annotation_id)+' setxy 0.493461 0.087177')
		Anno.AnnoSettings(annotation_id,head,pointer_position)
		
		###Collect values from annotation
		HVal, SVal, TVal = str(a.text).split(',')[1].partition('=')
		return round(float(TVal),3)
		
		
	
	def AnnoSettings(annotation_id,head,pointer_position):
		
		if pointer_position.startswith("disp"):
			utils.MetaCommand('annotation text '+str(annotation_id)+' text "'+head+'\\n\$funcName =\$fval\[3f\] m"')
		else:
			utils.MetaCommand('annotation text '+str(annotation_id)+' text "'+head+'\\nMax =\$fval\[3f\] "')
		
		
		utils.MetaCommand('annotation text '+str(annotation_id)+' color Black')
		utils.MetaCommand('annotation background '+str(annotation_id)+' color manual White')
		utils.MetaCommand('annotation border '+str(annotation_id)+' color Black')
		
		
	def PositionSettings():
		utils.MetaCommand('annotation arrange sorted 1-6 .8 .07 .10	')
		utils.MetaCommand('annotation line 1-6 color Black')
		utils.MetaCommand('annotation line 1-6 width 3')
		utils.MetaCommand('annotation pointer 1-6 style arrow')
	


def selectfile():
	print('Select the file for reading')
	read_file = utils.SelectOpenFile(0, 'odb (*.odb)')
	if not read_file:
		print('No file was selected')
	else:
		print('The file selected is: ' + read_file[0])
	return read_file[0]



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
	
	def Q_States(st_list):
		window = guitk.BCWindowCreate("Example LineEdit", guitk.constants.BCOnExitDestroy)
		hl = guitk.BCBoxLayoutCreate(window, guitk.constants.BCHorizontal)
		guitk.BCLabelCreate(hl, "Choose states: ")
		lineedit = guitk.BCLineEditCreate(hl, "")
		
		
		f = guitk.BCFrameCreate(window)
		l = guitk.BCBoxLayoutCreate(f, guitk.constants.BCHorizontal)
		listView = guitk.BCListViewCreate(window, 2, ['ID', 'State'], 1)
		BCGUI.appendPartListViewItems(listView,st_list)
		
		guitk.BCLineEditSetInfo(lineedit, "Necessary input, for state 1 and 4: '1,4' ")
		guitk.BCShow( window )
		
		output = guitk.BCLineEditGetText(lineedit)
		
		return output


	def appendPartListViewItems(listView,st_list):
		rn = [0,0]
		cols = guitk.BCListViewColumns(listView)
		guitk.BCListViewSaveSortStateAndDisableSorting(listView)
		
		cc = 0
		for stateI in st_list:
			cc += 1
			guitk.BCListViewAddItem(listView, cols, [str(cc),str(stateI)], rn)

		guitk.BCListViewRestoreSortState(listView)

################################################################################################
################################################################################################


class MC:

	def SetStates(state):
		utils.MetaCommand('0:options state variable "serial=' +state+'"') 

	def DeleteAllStates():
		utils.MetaCommand('0:displ delete all')
		utils.MetaCommand('0:function delete all')

	def SetFringebarRange(lowerV,upperV):
		utils.MetaCommand('srange window "MetaPost" set .'+str(lowerV)+','+str(upperV)+'.')

	def SetFringebarAutoRange():
		#Fringebar auto range
		utils.MetaCommand('srange window "MetaPost" auto enable')
		
	def ScalarFringe():
		utils.MetaCommand('grstyle scalarfringe enable')
		
		
	def SetEntities():
		#Set all entities on or only shell + solid?
		utils.MetaCommand('era global all 0')
		utils.MetaCommand('add global shell 0')
		#utils.MetaCommand('add global solid 0')
	
	def deformation():
		utils.MetaCommand('grstyle deform on')
		utils.MetaCommand('grstyle scalarfringe dnode')
		utils.MetaCommand('grstyle scalarfringe onelement')
		
		
	def Front_view():
		#FRONT VIEW
		utils.MetaCommand('view scale in 0.649265,0.528438')
		utils.MetaCommand('view set -2.55766,3.31977,0.990071,-27.8347,25.4403,15.4792,0.376434,-0.166765,0.91131,-27.8347,25.4403,15.4792,-2.92738,76.0896,28,0')
		MC.toggleLight(False)
		
	def Rear_view():
		#REAR VIEW		
		utils.MetaCommand('view scale in 0.579412,0.355739')
		utils.MetaCommand('view set 1.95099,2.44514,-0.171699,22.3481,-24.1667,-14.7986,0.204727,-0.346286,0.915518,22.3481,-24.1667,-14.7986,-2.92738,76.0896,28,0')
		MC.toggleLight(False)
		
	def Front_Set_view():
		utils.MetaCommand('view scale in 0.649265,0.528438')
		utils.MetaCommand('view set -0.176974,-0.53984,0.146601,-9.92512,33.8397,-7.67643,-0.00385922,0.220835,0.975304,-9.92512,33.8397,-7.67643,-22.6204,95.7827,28,0	')
		MC.toggleLight(False)
		
	def Rear_Set_view():
		utils.MetaCommand('view scale in 0.541896,0.514995')
		utils.MetaCommand('view set 1.8507,-0.931685,-0.694971,16.3033,-33.9347,-7.02783,0.0828045,-0.152709,0.984796,16.3033,-33.9347,-7.02783,0.397224,76.0896,28,0')	
		utils.MetaCommand('options light global lightambient 47')
		MC.toggleLight(True)
	
	def toggleLight(switch):
		
		if switch:
			utils.MetaCommand('options light global lightambient 35')
		else:
			utils.MetaCommand('options light global lightambient 0')
		
	def addSlide():
		global slide_counter
		slide_counter += 1
		utils.MetaCommand('report presentation nameaddslide "Slide '+str(slide_counter)+'"')	
		
	def TableGen(states, st_list, ls_vals1, ls_vals2, ls_vals3):
		
		###Export selected states!
		
		St1_h, St1_s, St1_t = st_list[int(states.split(',')[0])-1][0].partition('        ')
		St2_h, St2_s, St2_t = st_list[int(states.split(',')[1])-1][0].partition('        ')
		
		
		
		###Textbox 1
		utils.MetaCommand('report presentation slide addtextbox "Slide 13" "Textbox 1" ""')
		utils.MetaCommand('report presentation slide textbox line color "Slide 13" "Textbox 1" 0,0,0')
		utils.MetaCommand('report presentation slide textbox line width "Slide 13" "Textbox 1" 0.75')		
		utils.MetaCommand('report presentation slide element resize "Slide 13" "Textbox 1" 0.0744 0.1915 0.6759 0.3803')
		
		
		
		utils.MetaCommand('report presentation slide edittextbox "Slide 13" "Textbox 1" "<body style=&quot; font-family: font-size:20pt; font-weight:400; font-style:normal;&quot;><table border=&quot;0&quot; style=&quot;-qt-table-type: root; margin-top:4.91339px; margin-bottom:4.91339px; margin-left:9.44882px; margin-right:9.44882px;&quot;><tr><td style=&quot;border: none;&quot;><p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;><span style=&quot; font-size:16pt;&quot;>State: '+St1_t+'</span></p><p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;><span style=&quot; font-size:12pt; font-weight:600;&quot;>FRP Panel Deflection [m]</span></p><p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;><span style=&quot; font-size:12pt; font-weight:600;&quot;>Disp Tot Max</span></p><p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;&quot;><br /></p><p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;><span style=&quot; font-size:12pt;&quot;>Bottom: '+str(ls_vals1[5])+'</span></p><p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;><span style=&quot; font-size:12pt;&quot;>Rear: '+str(ls_vals1[2])+'</span></p><p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;><span style=&quot; font-size:12pt;&quot;>LHS: '+str(ls_vals1[0])+'</span></p><p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;><span style=&quot; font-size:12pt;&quot;>RHS: '+str(ls_vals1[1])+'</span></p><p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;><span style=&quot; font-size:12pt;&quot;>Roof: '+str(ls_vals1[3])+'</span></p></td></tr></table></body>"')
		
		utils.MetaCommand('report presentation slide element move "Slide 13" "Textbox 1" 0.0356 0.0363')	
		
		###Textbox 2
		
		utils.MetaCommand('report presentation slide addtextbox "Slide 13" "Textbox 2" ""')
		utils.MetaCommand('report presentation slide textbox line color "Slide 13" "Textbox 2" 0,0,0')
		utils.MetaCommand('report presentation slide textbox line width "Slide 13" "Textbox 2" 0.75')		
		utils.MetaCommand('report presentation slide element resize "Slide 13" "Textbox 2" 0.0744 0.1915 0.6759 0.3803')
		
		
		
		utils.MetaCommand('report presentation slide edittextbox "Slide 13" "Textbox 2" "<body style=&quot; font-family: font-size:20pt; font-weight:400; font-style:normal;&quot;><table border=&quot;0&quot; style=&quot;-qt-table-type: root; margin-top:4.91339px; margin-bottom:4.91339px; margin-left:9.44882px; margin-right:9.44882px;&quot;><tr><td style=&quot;border: none;&quot;><p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;><span style=&quot; font-size:16pt;&quot;>State: '+St2_t+'</span></p><p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;><span style=&quot; font-size:12pt; font-weight:600;&quot;>FRP Panel Deflection [m]</span></p><p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;><span style=&quot; font-size:12pt; font-weight:600;&quot;>Disp Tot Max</span></p><p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;&quot;><br /></p><p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;><span style=&quot; font-size:12pt;&quot;>Bottom: '+str(ls_vals2[5])+'</span></p><p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;><span style=&quot; font-size:12pt;&quot;>Rear: '+str(ls_vals2[2])+'</span></p><p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;><span style=&quot; font-size:12pt;&quot;>LHS: '+str(ls_vals2[0])+'</span></p><p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;><span style=&quot; font-size:12pt;&quot;>RHS: '+str(ls_vals2[1])+'</span></p><p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;><span style=&quot; font-size:12pt;&quot;>Roof: '+str(ls_vals2[3])+'</span></p></td></tr></table></body>"')
		
		utils.MetaCommand('report presentation slide element move "Slide 13" "Textbox 2" 0.0356 0.3573')	
		
		
		###Textbox 3
		
		utils.MetaCommand('report presentation slide addtextbox "Slide 13" "Textbox 3" ""')				
		utils.MetaCommand('report presentation slide textbox line color "Slide 13" "Textbox 3" 0,0,0')
		utils.MetaCommand('report presentation slide textbox line width "Slide 13" "Textbox 3" 0.75')		
		utils.MetaCommand('report presentation slide element resize "Slide 13" "Textbox 3" 0.0744 0.1915 0.6759 0.3803')
		
		
		
		
		utils.MetaCommand('report presentation slide edittextbox "Slide 13" "Textbox 3" "<body style=&quot; font-family: font-size:20pt; font-weight:400; font-style:normal;&quot;><table border=&quot;0&quot; style=&quot;-qt-table-type: root; margin-top:4.91339px; margin-bottom:4.91339px; margin-left:9.44882px; margin-right:9.44882px;&quot;><tr><td style=&quot;border: none;&quot;><p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;><span style=&quot; font-size:16pt;&quot;>State: '+St2_t+'</span></p><p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;><span style=&quot; font-size:12pt; font-weight:600;&quot;>FRP Strain Capacity</span></p><p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;&quot;><br /></p><p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;><span style=&quot; font-size:12pt;&quot;>Bottom: '+str(ls_vals3[5])+'</span></p><p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;><span style=&quot; font-size:12pt;&quot;>Rear: '+str(ls_vals3[2])+'</span></p><p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;><span style=&quot; font-size:12pt;&quot;>LHS: '+str(ls_vals3[0])+'</span></p><p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;><span style=&quot; font-size:12pt;&quot;>RHS: '+str(ls_vals3[1])+'</span></p><p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;><span style=&quot; font-size:12pt;&quot;>Roof: '+str(ls_vals3[3])+'</span></p></td></tr></table></body>"')
		
		utils.MetaCommand('report presentation slide element move "Slide 13" "Textbox 3" 0.0349 0.6665')
		
		
	def reportComposer(filename,model_id,window_name,states,st_list):
		
		#Set window size
		utils.MetaCommand('window size 1456,967')
		utils.MetaCommand('write options outputsize workspace 1456,967')
		
		#Create report
		utils.MetaCommand('report windows pptx active "Report Composer 1"')
		utils.MetaCommand('report windows pptx new "Report Composer 1"')
		
		MC.SetFringebarAutoRange()
		
		#Scale deformations
		utils.MetaCommand('disp scale multiplier 1.000000E+000')
		
		#Set a slide counter
		global slide_counter
		slide_counter = 0
		##############################################################
		#																Displacement
		##############################################################
		
		####################################
		MC.SetStates('1')
		Anno.DeleteAnnotations()
		###
		MC.addSlide()
		MC.Front_view()
		utils.MetaCommand('clipboard copy image "MetaPost"')
		utils.MetaCommand('report presentation slide clipboard pasteimage "Slide '+str(slide_counter)+'"')
		
		###
		MC.addSlide()
		MC.Rear_view()
		utils.MetaCommand('clipboard copy image "MetaPost"')
		utils.MetaCommand('report presentation slide clipboard pasteimage "Slide '+str(slide_counter)+'"')
		
		
		########SETS
		MC.addSlide()
		MC.Front_Set_view()
		
		
		pointer_position = 'disptotmax'
		LHSval_disp1 = Anno.LHS(model_id,window_name,pointer_position)
		RHSval_disp1 = Anno.RHS(model_id,window_name,pointer_position)
		Rearval_disp1 = Anno.Rear(model_id,window_name,pointer_position)
		Roofval_disp1 = Anno.Roof(model_id,window_name,pointer_position)
		Frontval_disp1 = Anno.Front(model_id,window_name,pointer_position)
		Bottomval_disp1 = Anno.Bottom(model_id,window_name,pointer_position)
		ls_vals1 = [LHSval_disp1, RHSval_disp1, Rearval_disp1, Roofval_disp1, Frontval_disp1, Bottomval_disp1]
		Anno.PositionSettings()
		
		utils.MetaCommand('clipboard copy image "MetaPost"')
		utils.MetaCommand('report presentation slide clipboard pasteimage "Slide '+str(slide_counter)+'"')
		
		MC.addSlide()		
		MC.Rear_Set_view()
		utils.MetaCommand('clipboard copy image "MetaPost"')
		utils.MetaCommand('report presentation slide clipboard pasteimage "Slide '+str(slide_counter)+'"')		
		
		
		Anno.DeleteAnnotations()
		
		
		####################################
		MC.SetStates('2')
		MC.SetFringebarAutoRange()
		###
		MC.addSlide()
		MC.Front_view()
		utils.MetaCommand('clipboard copy image "MetaPost"')
		utils.MetaCommand('report presentation slide clipboard pasteimage "Slide '+str(slide_counter)+'"')
		
		
		
		###
		MC.addSlide()
		MC.Rear_view()
		utils.MetaCommand('clipboard copy image "MetaPost"')
		utils.MetaCommand('report presentation slide clipboard pasteimage "Slide '+str(slide_counter)+'"')	
		
		
		
		########SETS
		MC.addSlide()
		MC.Front_Set_view()		
		
		pointer_position = 'disptotmax'
		LHSval_disp2 = Anno.LHS(model_id,window_name,pointer_position)
		RHSval_disp2 = Anno.RHS(model_id,window_name,pointer_position)
		Rearval_disp2 = Anno.Rear(model_id,window_name,pointer_position)
		Roofval_disp2 = Anno.Roof(model_id,window_name,pointer_position)
		Frontval_disp2 = Anno.Front(model_id,window_name,pointer_position)
		Bottomval_disp2 = Anno.Bottom(model_id,window_name,pointer_position)
		ls_vals2 = [LHSval_disp2, RHSval_disp2, Rearval_disp2, Roofval_disp2, Frontval_disp2, Bottomval_disp2]
		Anno.PositionSettings()
		
		
		utils.MetaCommand('clipboard copy image "MetaPost"')
		utils.MetaCommand('report presentation slide clipboard pasteimage "Slide '+str(slide_counter)+'"')
		
		MC.addSlide()		
		MC.Rear_Set_view()
		utils.MetaCommand('clipboard copy image "MetaPost"')
		utils.MetaCommand('report presentation slide clipboard pasteimage "Slide '+str(slide_counter)+'"')		
		
		
		#Anno.HideAnnotations()
		Anno.DeleteAnnotations()
		
		##############################################################
		#																STRAIN
		##############################################################
		MC.DeleteAllStates()
		utils.MetaCommand('read dis Abaqus '+str(filename)+' '+states.split(',')[1]+' Displacements')
		utils.MetaCommand('read onlyfun Abaqus  '+str(filename)+' '+states.split(',')[1]+' Maximumstraintheoryfailuremeasure,MaxofInOut/AllLayers,IntPnt')		

		
		MC.SetStates('1')
		
		utils.MetaCommand('srange window "MetaPost" set .0,.505')
		utils.MetaCommand('srange window "MetaPost" auto disable')
		utils.MetaCommand('grstyle scalarfringe elemdata')
		
		utils.MetaCommand('read options excludesingularity enable')
		utils.MetaCommand('read options excluderigid enable')
		
		
		###
		MC.addSlide()
		MC.Front_view()
		utils.MetaCommand('clipboard copy image "MetaPost"')
		utils.MetaCommand('report presentation slide clipboard pasteimage "Slide '+str(slide_counter)+'"')		
		
		###		
		MC.addSlide()
		MC.Rear_view()
		utils.MetaCommand('clipboard copy image "MetaPost"')
		utils.MetaCommand('report presentation slide clipboard pasteimage "Slide '+str(slide_counter)+'"')
		
		########SETS
		MC.addSlide()
		MC.Front_Set_view()
		
		
		pointer_position = 'elemmax'
		LHSval_strain = Anno.LHS(model_id,window_name,pointer_position)
		RHSval_strain = Anno.RHS(model_id,window_name,pointer_position)
		Rearval_strain = Anno.Rear(model_id,window_name,pointer_position)
		Roofval_strain = Anno.Roof(model_id,window_name,pointer_position)
		Frontval_strain = Anno.Front(model_id,window_name,pointer_position)
		Bottomval_strain = Anno.Bottom(model_id,window_name,pointer_position)
		ls_vals3 = [LHSval_strain, RHSval_strain, Rearval_strain, Roofval_strain, Frontval_strain, Bottomval_strain]
		Anno.PositionSettings()
		
		utils.MetaCommand('clipboard copy image "MetaPost"')
		utils.MetaCommand('report presentation slide clipboard pasteimage "Slide '+str(slide_counter)+'"')		
		
		MC.addSlide()		
		MC.Rear_Set_view()
		utils.MetaCommand('clipboard copy image "MetaPost"')
		utils.MetaCommand('report presentation slide clipboard pasteimage "Slide '+str(slide_counter)+'"')
				
		##############################################################
		#															#Excel
		##############################################################
		MC.TableGen(states,st_list, ls_vals1, ls_vals2, ls_vals3)
		
		
		
		##############################################################
		#															#SAVE Powerpoint
		##############################################################
		head, sep, tail = str(os.path.basename(filename)).partition('.')
		
		utils.MetaCommand('report presentation options save textbox autofit shrinkwrap enable')
		utils.MetaCommand('report presentation options save variables values enable')
		utils.MetaCommand('report presentation saveas "'+str(os.path.dirname(filename))+'/'+'PP_'+head+'.pptx'+'"')
		
		
################################################################################################
	
def main():
	window_name = 'MetaPost'

	filename = selectfile()

	deck = 'ABAQUS'
	r = models.LoadModel(window_name, filename, deck)
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
	
	MC.DeleteAllStates()
	
	###
	
	
	selected_states = BCGUI.Q_States(st_list)
	states = selected_states.split(',')[0]+','+selected_states.split(',')[1]
	print ('Selected states: ' + str(states))
	
	
	data = 'Displacements,Translational'
	new_resultsets = results.LoadDeformations(model_id, filename, deck, states, data)
	data = 'Displacements,Magnitude'
	new_resultsets = results.LoadScalar(model_id, filename, deck, states, data)
	for res in new_resultsets:
		print(res.name, res.nodal_data_name, res.function_data_name, res.state)

	fringe_name = 'StressTensor'
	fringe_type = 'scalar'
	windows.ActivateFringe(window_name, fringe_name, fringe_type)
	
	
	MC.ScalarFringe()
	MC.SetEntities()
	

	utils.MetaCommand('options fringebar format enabled fixed')
	utils.MetaCommand('options fringebar format enabled digits 3')
	utils.MetaCommand('options fringebar font enabled values "MS Shell Dlg 2,20,-1,5,75,0,0,0,0,0"')
	
	MC.deformation()
	
	MC.reportComposer(filename,model_id,window_name,states,st_list)
	
	
	
	

if __name__ == '__main__':
	reset_all()
	utils.ClearMonitor()
	M = models.ActiveModels()
	if M:
		delete_existing_model(M)
	main()



