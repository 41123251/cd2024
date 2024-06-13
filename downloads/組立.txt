# NX 1872
# Journal created by Admin on Thu Jun 13 15:29:13 2024 台北標準時間

#
import math
import NXOpen
import NXOpen.Annotations
import NXOpen.Assemblies
import NXOpen.Assemblies.ProductInterface
import NXOpen.PDM
import NXOpen.Positioning
import NXOpen.Preferences
def main() : 

    theSession  = NXOpen.Session.GetSession()
    # ----------------------------------------------
    #   功能表：檔案(F)->新建(N)...
    # ----------------------------------------------
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    fileNew1 = theSession.Parts.FileNew()
    
    theSession.SetUndoMarkName(markId1, "新建 對話方塊")
    
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "新建")
    
    theSession.DeleteUndoMark(markId2, None)
    
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "新建")
    
    fileNew1.TemplateFileName = "assembly-mm-template.prt"
    
    fileNew1.UseBlankTemplate = False
    
    fileNew1.ApplicationName = "AssemblyTemplate"
    
    fileNew1.Units = NXOpen.Part.Units.Millimeters
    
    fileNew1.RelationType = ""
    
    fileNew1.UsesMasterModel = "No"
    
    fileNew1.TemplateType = NXOpen.FileNewTemplateType.Item
    
    fileNew1.TemplatePresentationName = "組立件"
    
    fileNew1.ItemType = ""
    
    fileNew1.Specialization = ""
    
    fileNew1.SetCanCreateAltrep(False)
    
    fileNew1.NewFileName = "C:\\Users\\Admin\\Desktop\\assembly1.prt"
    
    fileNew1.MasterFileName = ""
    
    fileNew1.MakeDisplayedPart = True
    
    fileNew1.DisplayPartOption = NXOpen.DisplayPartOption.AllowAdditional
    
    # User Function call - UF_PART_ask_part_name
    
    nXObject1 = fileNew1.Commit()
    
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    theSession.DeleteUndoMark(markId3, None)
    
    fileNew1.Destroy()
    
    theSession.ApplicationSwitchImmediate("UG_APP_MODELING")
    
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    addComponentBuilder1 = workPart.AssemblyManager.CreateAddComponentBuilder()
    
    componentPositioner1 = workPart.ComponentAssembly.Positioner
    
    componentPositioner1.ClearNetwork()
    
    componentPositioner1.BeginAssemblyConstraints()
    
    allowInterpartPositioning1 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression1 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    unit1 = workPart.UnitCollection.FindObject("MilliMeter")
    expression2 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression3 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    unit2 = workPart.UnitCollection.FindObject("Degrees")
    expression4 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression5 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression6 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression7 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression8 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network1 = componentPositioner1.EstablishNetwork()
    
    componentNetwork1 = network1
    componentNetwork1.MoveObjectsState = True
    
    componentNetwork1.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    theSession.SetUndoMarkName(markId4, "新增元件 對話方塊")
    
    componentNetwork1.MoveObjectsState = True
    
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "組立約束更新")
    
    addComponentBuilder1.SetComponentAnchor(NXOpen.Assemblies.ProductInterface.InterfaceObject.Null)
    
    addComponentBuilder1.SetInitialLocationType(NXOpen.Assemblies.AddComponentBuilder.LocationType.Snap)
    
    addComponentBuilder1.SetCount(4)
    
    addComponentBuilder1.SetScatterOption(True)
    
    addComponentBuilder1.ReferenceSet = "未知"
    
    addComponentBuilder1.Layer = -1
    
    # ----------------------------------------------
    #   對話開始 新增元件
    # ----------------------------------------------
    addComponentBuilder1.SetCount(3)
    
    addComponentBuilder1.SetCount(2)
    
    addComponentBuilder1.SetCount(1)
    
    basePart1, partLoadStatus1 = theSession.Parts.OpenBase("C:\\Users\\Admin\\Desktop\\model1.prt")
    
    partLoadStatus1.Dispose()
    addComponentBuilder1.ReferenceSet = "Use Model"
    
    addComponentBuilder1.Layer = -1
    
    partstouse1 = [NXOpen.BasePart.Null] * 1 
    part1 = basePart1
    partstouse1[0] = part1
    addComponentBuilder1.SetPartsToAdd(partstouse1)
    
    productinterfaceobjects1 = addComponentBuilder1.GetAllProductInterfaceObjects()
    
    arrangement1 = workPart.ComponentAssembly.Arrangements.FindObject("Arrangement 1")
    componentPositioner1.PrimaryArrangement = arrangement1
    
    coordinates1 = NXOpen.Point3d(8.871059071003355, 16.067604132464673, 0.0)
    point1 = workPart.Points.CreatePoint(coordinates1)
    
    coordinates2 = NXOpen.Point3d(8.871059071003355, 16.067604132464673, 0.0)
    point2 = workPart.Points.CreatePoint(coordinates2)
    
    origin1 = NXOpen.Point3d(8.871059071003355, 16.067604132464673, 0.0)
    vector1 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    direction1 = workPart.Directions.CreateDirection(origin1, vector1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    origin2 = NXOpen.Point3d(8.871059071003355, 16.067604132464673, 0.0)
    vector2 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    direction2 = workPart.Directions.CreateDirection(origin2, vector2, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    origin3 = NXOpen.Point3d(8.871059071003355, 16.067604132464673, 0.0)
    matrix1 = NXOpen.Matrix3x3()
    
    matrix1.Xx = 1.0
    matrix1.Xy = 0.0
    matrix1.Xz = 0.0
    matrix1.Yx = 0.0
    matrix1.Yy = 1.0
    matrix1.Yz = 0.0
    matrix1.Zx = 0.0
    matrix1.Zy = 0.0
    matrix1.Zz = 1.0
    plane1 = workPart.Planes.CreateFixedTypePlane(origin3, matrix1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    xform1 = workPart.Xforms.CreateXformByPlaneXDirPoint(plane1, direction2, point2, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem1 = workPart.CoordinateSystems.CreateCoordinateSystem(xform1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point3 = NXOpen.Point3d(8.871059071003355, 16.067604132464673, 0.0)
    orientation1 = NXOpen.Matrix3x3()
    
    orientation1.Xx = 1.0
    orientation1.Xy = 0.0
    orientation1.Xz = 0.0
    orientation1.Yx = 0.0
    orientation1.Yy = 1.0
    orientation1.Yz = 0.0
    orientation1.Zx = 0.0
    orientation1.Zy = 0.0
    orientation1.Zz = 1.0
    addComponentBuilder1.SetInitialLocationAndOrientation(point3, orientation1)
    
    movableObjects1 = [NXOpen.NXObject.Null] * 1 
    component1 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT model1 1")
    movableObjects1[0] = component1
    componentNetwork1.SetMovingGroup(movableObjects1)
    
    markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "新增元件")
    
    markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "AddComponent on_apply")
    
    componentNetwork1.Solve()
    
    componentPositioner1.ClearNetwork()
    
    nErrs1 = theSession.UpdateManager.AddToDeleteList(componentNetwork1)
    
    nErrs2 = theSession.UpdateManager.DoUpdate(markId5)
    
    componentPositioner1.EndAssemblyConstraints()
    
    logicalobjects1 = addComponentBuilder1.GetLogicalObjectsHavingUnassignedRequiredAttributes()
    
    addComponentBuilder1.ComponentName = "MODEL1"
    
    nXObject2 = addComponentBuilder1.Commit()
    
    errorList1 = addComponentBuilder1.GetOperationFailures()
    
    errorList1.Dispose()
    markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "ComponentOperationUtilities CreateFixConstraint")
    
    componentPositioner2 = workPart.ComponentAssembly.Positioner
    
    componentPositioner2.ClearNetwork()
    
    network2 = componentPositioner2.EstablishNetwork()
    
    componentNetwork2 = network2
    componentNetwork2.MoveObjectsState = True
    
    componentNetwork2.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork2.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    constraint1 = componentPositioner2.CreateConstraint(True)
    
    componentConstraint1 = constraint1
    componentConstraint1.ConstraintType = NXOpen.Positioning.Constraint.Type.Fix
    
    component2 = nXObject2
    constraintReference1 = componentConstraint1.CreateConstraintReference(component2, component2, False, False, False)
    
    componentNetwork2.Solve()
    
    componentPositioner2.ClearNetwork()
    
    nErrs3 = theSession.UpdateManager.AddToDeleteList(componentNetwork2)
    
    nErrs4 = theSession.UpdateManager.DoUpdate(markId4)
    
    theSession.DeleteUndoMark(markId6, None)
    
    theSession.SetUndoMarkName(markId4, "新增元件")
    
    addComponentBuilder1.Destroy()
    
    workPart.Points.DeletePoint(point1)
    
    componentPositioner2.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    theSession.DeleteUndoMark(markId5, None)
    
    markId9 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    addComponentBuilder2 = workPart.AssemblyManager.CreateAddComponentBuilder()
    
    componentPositioner3 = workPart.ComponentAssembly.Positioner
    
    componentPositioner3.ClearNetwork()
    
    componentPositioner3.PrimaryArrangement = arrangement1
    
    componentPositioner3.BeginAssemblyConstraints()
    
    allowInterpartPositioning2 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression9 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression10 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression11 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression12 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression13 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression14 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression15 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression16 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network3 = componentPositioner3.EstablishNetwork()
    
    componentNetwork3 = network3
    componentNetwork3.MoveObjectsState = True
    
    componentNetwork3.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    theSession.SetUndoMarkName(markId9, "新增元件 對話方塊")
    
    componentNetwork3.MoveObjectsState = True
    
    markId10 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "組立約束更新")
    
    addComponentBuilder2.SetComponentAnchor(NXOpen.Assemblies.ProductInterface.InterfaceObject.Null)
    
    addComponentBuilder2.SetInitialLocationType(NXOpen.Assemblies.AddComponentBuilder.LocationType.Snap)
    
    addComponentBuilder2.SetCount(1)
    
    addComponentBuilder2.SetScatterOption(True)
    
    addComponentBuilder2.ReferenceSet = "未知"
    
    addComponentBuilder2.Layer = -1
    
    # ----------------------------------------------
    #   對話開始 新增元件
    # ----------------------------------------------
    basePart2, partLoadStatus2 = theSession.Parts.OpenBase("C:\\Users\\Admin\\Desktop\\model2.prt")
    
    partLoadStatus2.Dispose()
    addComponentBuilder2.ReferenceSet = "Use Model"
    
    addComponentBuilder2.Layer = -1
    
    partstouse2 = [NXOpen.BasePart.Null] * 1 
    part2 = basePart2
    partstouse2[0] = part2
    addComponentBuilder2.SetPartsToAdd(partstouse2)
    
    productinterfaceobjects2 = addComponentBuilder2.GetAllProductInterfaceObjects()
    
    coordinates3 = NXOpen.Point3d(21.803865692141173, -62.345868398316675, 0.0)
    point4 = workPart.Points.CreatePoint(coordinates3)
    
    coordinates4 = NXOpen.Point3d(21.803865692141173, -62.345868398316675, 0.0)
    point5 = workPart.Points.CreatePoint(coordinates4)
    
    origin4 = NXOpen.Point3d(21.803865692141173, -62.345868398316675, 0.0)
    vector3 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    direction3 = workPart.Directions.CreateDirection(origin4, vector3, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    origin5 = NXOpen.Point3d(21.803865692141173, -62.345868398316675, 0.0)
    vector4 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    direction4 = workPart.Directions.CreateDirection(origin5, vector4, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    origin6 = NXOpen.Point3d(21.803865692141173, -62.345868398316675, 0.0)
    matrix2 = NXOpen.Matrix3x3()
    
    matrix2.Xx = 1.0
    matrix2.Xy = 0.0
    matrix2.Xz = 0.0
    matrix2.Yx = 0.0
    matrix2.Yy = 1.0
    matrix2.Yz = 0.0
    matrix2.Zx = 0.0
    matrix2.Zy = 0.0
    matrix2.Zz = 1.0
    plane2 = workPart.Planes.CreateFixedTypePlane(origin6, matrix2, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    xform2 = workPart.Xforms.CreateXformByPlaneXDirPoint(plane2, direction4, point5, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem2 = workPart.CoordinateSystems.CreateCoordinateSystem(xform2, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point6 = NXOpen.Point3d(21.803865692141173, -62.345868398316675, 0.0)
    orientation2 = NXOpen.Matrix3x3()
    
    orientation2.Xx = 1.0
    orientation2.Xy = 0.0
    orientation2.Xz = 0.0
    orientation2.Yx = 0.0
    orientation2.Yy = 1.0
    orientation2.Yz = 0.0
    orientation2.Zx = 0.0
    orientation2.Zy = 0.0
    orientation2.Zz = 1.0
    addComponentBuilder2.SetInitialLocationAndOrientation(point6, orientation2)
    
    movableObjects2 = [NXOpen.NXObject.Null] * 1 
    component3 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT model2 1")
    movableObjects2[0] = component3
    componentNetwork3.SetMovingGroup(movableObjects2)
    
    markId11 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "新增元件")
    
    theSession.DeleteUndoMark(markId11, None)
    
    markId12 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "新增元件")
    
    markId13 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "AddComponent on_apply")
    
    componentNetwork3.Solve()
    
    componentPositioner3.ClearNetwork()
    
    nErrs5 = theSession.UpdateManager.AddToDeleteList(componentNetwork3)
    
    nErrs6 = theSession.UpdateManager.DoUpdate(markId10)
    
    componentPositioner3.EndAssemblyConstraints()
    
    logicalobjects2 = addComponentBuilder2.GetLogicalObjectsHavingUnassignedRequiredAttributes()
    
    addComponentBuilder2.ComponentName = "MODEL2"
    
    nXObject3 = addComponentBuilder2.Commit()
    
    errorList2 = addComponentBuilder2.GetOperationFailures()
    
    errorList2.Dispose()
    theSession.DeleteUndoMark(markId12, None)
    
    theSession.SetUndoMarkName(markId9, "新增元件")
    
    addComponentBuilder2.Destroy()
    
    workPart.Points.DeletePoint(point4)
    
    componentPositioner3.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    theSession.DeleteUndoMark(markId10, None)
    
    # ----------------------------------------------
    #   功能表：編輯(E)->複製(C)
    # ----------------------------------------------
    workPart.PmiManager.RestoreUnpastedObjects()
    
    # ----------------------------------------------
    #   功能表：編輯(E)->貼上(P)
    # ----------------------------------------------
    markId14 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Component")
    
    option1 = theSession.Parts.LoadOptions.UsePartialLoading
    
    theSession.Parts.LoadOptions.UsePartialLoading = False
    
    componentsToOpen1 = [NXOpen.Assemblies.Component.Null] * 1 
    component4 = nXObject3
    componentsToOpen1[0] = component4
    partLoadStatus3, openStatus1 = workPart.ComponentAssembly.OpenComponents(NXOpen.Assemblies.ComponentAssembly.OpenOption.ComponentOnly, componentsToOpen1)
    
    theSession.Parts.LoadOptions.UsePartialLoading = True
    
    partLoadStatus3.Dispose()
    theSession.DeleteUndoMark(markId14, None)
    
    # ----------------------------------------------
    #   功能表：組立件(A)->元件(C)->新增元件(A)...
    # ----------------------------------------------
    markId15 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    addComponentBuilder3 = workPart.AssemblyManager.CreateAddComponentBuilder()
    
    componentPositioner4 = workPart.ComponentAssembly.Positioner
    
    componentPositioner4.ClearNetwork()
    
    componentPositioner4.PrimaryArrangement = arrangement1
    
    componentPositioner4.BeginAssemblyConstraints()
    
    allowInterpartPositioning3 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression17 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression18 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression19 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression20 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression21 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression22 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression23 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression24 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network4 = componentPositioner4.EstablishNetwork()
    
    componentNetwork4 = network4
    componentNetwork4.MoveObjectsState = True
    
    componentNetwork4.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    theSession.SetUndoMarkName(markId15, "新增元件 對話方塊")
    
    componentNetwork4.MoveObjectsState = True
    
    markId16 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "組立約束更新")
    
    addComponentBuilder3.SetComponentAnchor(NXOpen.Assemblies.ProductInterface.InterfaceObject.Null)
    
    addComponentBuilder3.SetInitialLocationType(NXOpen.Assemblies.AddComponentBuilder.LocationType.Snap)
    
    addComponentBuilder3.SetCount(1)
    
    addComponentBuilder3.SetScatterOption(True)
    
    addComponentBuilder3.ReferenceSet = "未知"
    
    addComponentBuilder3.Layer = -1
    
    addComponentBuilder3.ReferenceSet = "Use Model"
    
    addComponentBuilder3.Layer = -1
    
    partstouse3 = [NXOpen.BasePart.Null] * 1 
    partstouse3[0] = part2
    addComponentBuilder3.SetPartsToAdd(partstouse3)
    
    productinterfaceobjects3 = addComponentBuilder3.GetAllProductInterfaceObjects()
    
    coordinates5 = NXOpen.Point3d(-3.2478396113814583, -56.956316289965557, 0.0)
    point7 = workPart.Points.CreatePoint(coordinates5)
    
    coordinates6 = NXOpen.Point3d(-3.2478396113814583, -56.956316289965557, 0.0)
    point8 = workPart.Points.CreatePoint(coordinates6)
    
    origin7 = NXOpen.Point3d(-3.2478396113814583, -56.956316289965557, 0.0)
    vector5 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    direction5 = workPart.Directions.CreateDirection(origin7, vector5, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    origin8 = NXOpen.Point3d(-3.2478396113814583, -56.956316289965557, 0.0)
    vector6 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    direction6 = workPart.Directions.CreateDirection(origin8, vector6, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    origin9 = NXOpen.Point3d(-3.2478396113814583, -56.956316289965557, 0.0)
    matrix3 = NXOpen.Matrix3x3()
    
    matrix3.Xx = 1.0
    matrix3.Xy = 0.0
    matrix3.Xz = 0.0
    matrix3.Yx = 0.0
    matrix3.Yy = 1.0
    matrix3.Yz = 0.0
    matrix3.Zx = 0.0
    matrix3.Zy = 0.0
    matrix3.Zz = 1.0
    plane3 = workPart.Planes.CreateFixedTypePlane(origin9, matrix3, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    xform3 = workPart.Xforms.CreateXformByPlaneXDirPoint(plane3, direction6, point8, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem3 = workPart.CoordinateSystems.CreateCoordinateSystem(xform3, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point9 = NXOpen.Point3d(-3.2478396113814583, -56.956316289965557, 0.0)
    orientation3 = NXOpen.Matrix3x3()
    
    orientation3.Xx = 1.0
    orientation3.Xy = 0.0
    orientation3.Xz = 0.0
    orientation3.Yx = 0.0
    orientation3.Yy = 1.0
    orientation3.Yz = 0.0
    orientation3.Zx = 0.0
    orientation3.Zy = 0.0
    orientation3.Zz = 1.0
    addComponentBuilder3.SetInitialLocationAndOrientation(point9, orientation3)
    
    movableObjects3 = [NXOpen.NXObject.Null] * 1 
    component5 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT model2 1")
    movableObjects3[0] = component5
    componentNetwork4.SetMovingGroup(movableObjects3)
    
    markId17 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "新增元件")
    
    markId18 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "AddComponent on_apply")
    
    componentNetwork4.Solve()
    
    componentPositioner4.ClearNetwork()
    
    nErrs7 = theSession.UpdateManager.AddToDeleteList(componentNetwork4)
    
    nErrs8 = theSession.UpdateManager.DoUpdate(markId16)
    
    componentPositioner4.EndAssemblyConstraints()
    
    logicalobjects3 = addComponentBuilder3.GetLogicalObjectsHavingUnassignedRequiredAttributes()
    
    addComponentBuilder3.ComponentName = "MODEL2"
    
    nXObject4 = addComponentBuilder3.Commit()
    
    errorList3 = addComponentBuilder3.GetOperationFailures()
    
    errorList3.Dispose()
    theSession.DeleteUndoMark(markId17, None)
    
    theSession.SetUndoMarkName(markId15, "新增元件")
    
    addComponentBuilder3.Destroy()
    
    workPart.Points.DeletePoint(point7)
    
    componentPositioner4.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    theSession.DeleteUndoMark(markId16, None)
    
    markId19 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    addComponentBuilder4 = workPart.AssemblyManager.CreateAddComponentBuilder()
    
    componentPositioner5 = workPart.ComponentAssembly.Positioner
    
    componentPositioner5.ClearNetwork()
    
    componentPositioner5.PrimaryArrangement = arrangement1
    
    componentPositioner5.BeginAssemblyConstraints()
    
    allowInterpartPositioning4 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression25 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression26 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression27 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression28 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression29 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression30 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression31 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression32 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network5 = componentPositioner5.EstablishNetwork()
    
    componentNetwork5 = network5
    componentNetwork5.MoveObjectsState = True
    
    componentNetwork5.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    theSession.SetUndoMarkName(markId19, "新增元件 對話方塊")
    
    componentNetwork5.MoveObjectsState = True
    
    markId20 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "組立約束更新")
    
    addComponentBuilder4.SetComponentAnchor(NXOpen.Assemblies.ProductInterface.InterfaceObject.Null)
    
    addComponentBuilder4.SetInitialLocationType(NXOpen.Assemblies.AddComponentBuilder.LocationType.Snap)
    
    addComponentBuilder4.SetCount(1)
    
    addComponentBuilder4.SetScatterOption(True)
    
    addComponentBuilder4.ReferenceSet = "未知"
    
    addComponentBuilder4.Layer = -1
    
    # ----------------------------------------------
    #   對話開始 新增元件
    # ----------------------------------------------
    addComponentBuilder4.ReferenceSet = "Use Model"
    
    addComponentBuilder4.Layer = -1
    
    partstouse4 = [NXOpen.BasePart.Null] * 1 
    partstouse4[0] = part2
    addComponentBuilder4.SetPartsToAdd(partstouse4)
    
    productinterfaceobjects4 = addComponentBuilder4.GetAllProductInterfaceObjects()
    
    coordinates7 = NXOpen.Point3d(2.2149549037162366, -37.325527787706264, 0.0)
    point10 = workPart.Points.CreatePoint(coordinates7)
    
    coordinates8 = NXOpen.Point3d(2.2149549037162366, -37.325527787706264, 0.0)
    point11 = workPart.Points.CreatePoint(coordinates8)
    
    origin10 = NXOpen.Point3d(2.2149549037162366, -37.325527787706264, 0.0)
    vector7 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    direction7 = workPart.Directions.CreateDirection(origin10, vector7, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    origin11 = NXOpen.Point3d(2.2149549037162366, -37.325527787706264, 0.0)
    vector8 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    direction8 = workPart.Directions.CreateDirection(origin11, vector8, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    origin12 = NXOpen.Point3d(2.2149549037162366, -37.325527787706264, 0.0)
    matrix4 = NXOpen.Matrix3x3()
    
    matrix4.Xx = 1.0
    matrix4.Xy = 0.0
    matrix4.Xz = 0.0
    matrix4.Yx = 0.0
    matrix4.Yy = 1.0
    matrix4.Yz = 0.0
    matrix4.Zx = 0.0
    matrix4.Zy = 0.0
    matrix4.Zz = 1.0
    plane4 = workPart.Planes.CreateFixedTypePlane(origin12, matrix4, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    xform4 = workPart.Xforms.CreateXformByPlaneXDirPoint(plane4, direction8, point11, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem4 = workPart.CoordinateSystems.CreateCoordinateSystem(xform4, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point12 = NXOpen.Point3d(2.2149549037162366, -37.325527787706264, 0.0)
    orientation4 = NXOpen.Matrix3x3()
    
    orientation4.Xx = 1.0
    orientation4.Xy = 0.0
    orientation4.Xz = 0.0
    orientation4.Yx = 0.0
    orientation4.Yy = 1.0
    orientation4.Yz = 0.0
    orientation4.Zx = 0.0
    orientation4.Zy = 0.0
    orientation4.Zz = 1.0
    addComponentBuilder4.SetInitialLocationAndOrientation(point12, orientation4)
    
    movableObjects4 = [NXOpen.NXObject.Null] * 1 
    component6 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT model2 1")
    movableObjects4[0] = component6
    componentNetwork5.SetMovingGroup(movableObjects4)
    
    markId21 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "新增元件")
    
    markId22 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "AddComponent on_apply")
    
    componentNetwork5.Solve()
    
    componentPositioner5.ClearNetwork()
    
    nErrs9 = theSession.UpdateManager.AddToDeleteList(componentNetwork5)
    
    nErrs10 = theSession.UpdateManager.DoUpdate(markId20)
    
    componentPositioner5.EndAssemblyConstraints()
    
    logicalobjects4 = addComponentBuilder4.GetLogicalObjectsHavingUnassignedRequiredAttributes()
    
    addComponentBuilder4.ComponentName = "MODEL2"
    
    nXObject5 = addComponentBuilder4.Commit()
    
    errorList4 = addComponentBuilder4.GetOperationFailures()
    
    errorList4.Dispose()
    theSession.DeleteUndoMark(markId21, None)
    
    theSession.SetUndoMarkName(markId19, "新增元件")
    
    addComponentBuilder4.Destroy()
    
    workPart.Points.DeletePoint(point10)
    
    componentPositioner5.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    theSession.DeleteUndoMark(markId20, None)
    
    markId23 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    addComponentBuilder5 = workPart.AssemblyManager.CreateAddComponentBuilder()
    
    componentPositioner6 = workPart.ComponentAssembly.Positioner
    
    componentPositioner6.ClearNetwork()
    
    componentPositioner6.PrimaryArrangement = arrangement1
    
    componentPositioner6.BeginAssemblyConstraints()
    
    allowInterpartPositioning5 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression33 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression34 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression35 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression36 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression37 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression38 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression39 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression40 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network6 = componentPositioner6.EstablishNetwork()
    
    componentNetwork6 = network6
    componentNetwork6.MoveObjectsState = True
    
    componentNetwork6.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    theSession.SetUndoMarkName(markId23, "新增元件 對話方塊")
    
    componentNetwork6.MoveObjectsState = True
    
    markId24 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "組立約束更新")
    
    addComponentBuilder5.SetComponentAnchor(NXOpen.Assemblies.ProductInterface.InterfaceObject.Null)
    
    addComponentBuilder5.SetInitialLocationType(NXOpen.Assemblies.AddComponentBuilder.LocationType.Snap)
    
    addComponentBuilder5.SetCount(1)
    
    addComponentBuilder5.SetScatterOption(True)
    
    addComponentBuilder5.ReferenceSet = "未知"
    
    addComponentBuilder5.Layer = -1
    
    # ----------------------------------------------
    #   對話開始 新增元件
    # ----------------------------------------------
    addComponentBuilder5.ReferenceSet = "Use Model"
    
    addComponentBuilder5.Layer = -1
    
    partstouse5 = [NXOpen.BasePart.Null] * 1 
    partstouse5[0] = part2
    addComponentBuilder5.SetPartsToAdd(partstouse5)
    
    productinterfaceobjects5 = addComponentBuilder5.GetAllProductInterfaceObjects()
    
    coordinates9 = NXOpen.Point3d(45.484615582884487, -50.042324233402162, 0.0)
    point13 = workPart.Points.CreatePoint(coordinates9)
    
    coordinates10 = NXOpen.Point3d(45.484615582884487, -50.042324233402162, 0.0)
    point14 = workPart.Points.CreatePoint(coordinates10)
    
    origin13 = NXOpen.Point3d(45.484615582884487, -50.042324233402162, 0.0)
    vector9 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    direction9 = workPart.Directions.CreateDirection(origin13, vector9, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    origin14 = NXOpen.Point3d(45.484615582884487, -50.042324233402162, 0.0)
    vector10 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    direction10 = workPart.Directions.CreateDirection(origin14, vector10, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    origin15 = NXOpen.Point3d(45.484615582884487, -50.042324233402162, 0.0)
    matrix5 = NXOpen.Matrix3x3()
    
    matrix5.Xx = 1.0
    matrix5.Xy = 0.0
    matrix5.Xz = 0.0
    matrix5.Yx = 0.0
    matrix5.Yy = 1.0
    matrix5.Yz = 0.0
    matrix5.Zx = 0.0
    matrix5.Zy = 0.0
    matrix5.Zz = 1.0
    plane5 = workPart.Planes.CreateFixedTypePlane(origin15, matrix5, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    xform5 = workPart.Xforms.CreateXformByPlaneXDirPoint(plane5, direction10, point14, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem5 = workPart.CoordinateSystems.CreateCoordinateSystem(xform5, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point15 = NXOpen.Point3d(45.484615582884487, -50.042324233402162, 0.0)
    orientation5 = NXOpen.Matrix3x3()
    
    orientation5.Xx = 1.0
    orientation5.Xy = 0.0
    orientation5.Xz = 0.0
    orientation5.Yx = 0.0
    orientation5.Yy = 1.0
    orientation5.Yz = 0.0
    orientation5.Zx = 0.0
    orientation5.Zy = 0.0
    orientation5.Zz = 1.0
    addComponentBuilder5.SetInitialLocationAndOrientation(point15, orientation5)
    
    movableObjects5 = [NXOpen.NXObject.Null] * 1 
    component7 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT model2 1")
    movableObjects5[0] = component7
    componentNetwork6.SetMovingGroup(movableObjects5)
    
    markId25 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "新增元件")
    
    markId26 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "AddComponent on_apply")
    
    componentNetwork6.Solve()
    
    componentPositioner6.ClearNetwork()
    
    nErrs11 = theSession.UpdateManager.AddToDeleteList(componentNetwork6)
    
    nErrs12 = theSession.UpdateManager.DoUpdate(markId24)
    
    componentPositioner6.EndAssemblyConstraints()
    
    logicalobjects5 = addComponentBuilder5.GetLogicalObjectsHavingUnassignedRequiredAttributes()
    
    addComponentBuilder5.ComponentName = "MODEL2"
    
    nXObject6 = addComponentBuilder5.Commit()
    
    errorList5 = addComponentBuilder5.GetOperationFailures()
    
    errorList5.Dispose()
    theSession.DeleteUndoMark(markId25, None)
    
    theSession.SetUndoMarkName(markId23, "新增元件")
    
    addComponentBuilder5.Destroy()
    
    workPart.Points.DeletePoint(point13)
    
    componentPositioner6.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    theSession.DeleteUndoMark(markId24, None)
    
    markId27 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    addComponentBuilder6 = workPart.AssemblyManager.CreateAddComponentBuilder()
    
    componentPositioner7 = workPart.ComponentAssembly.Positioner
    
    componentPositioner7.ClearNetwork()
    
    componentPositioner7.PrimaryArrangement = arrangement1
    
    componentPositioner7.BeginAssemblyConstraints()
    
    allowInterpartPositioning6 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression41 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression42 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression43 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression44 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression45 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression46 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression47 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression48 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network7 = componentPositioner7.EstablishNetwork()
    
    componentNetwork7 = network7
    componentNetwork7.MoveObjectsState = True
    
    componentNetwork7.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    theSession.SetUndoMarkName(markId27, "新增元件 對話方塊")
    
    componentNetwork7.MoveObjectsState = True
    
    markId28 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "組立約束更新")
    
    addComponentBuilder6.SetComponentAnchor(NXOpen.Assemblies.ProductInterface.InterfaceObject.Null)
    
    addComponentBuilder6.SetInitialLocationType(NXOpen.Assemblies.AddComponentBuilder.LocationType.Snap)
    
    addComponentBuilder6.SetCount(1)
    
    addComponentBuilder6.SetScatterOption(True)
    
    addComponentBuilder6.ReferenceSet = "未知"
    
    addComponentBuilder6.Layer = -1
    
    # ----------------------------------------------
    #   對話開始 新增元件
    # ----------------------------------------------
    componentPositioner7.ClearNetwork()
    
    addComponentBuilder6.RemoveAddedComponents()
    
    addComponentBuilder6.Destroy()
    
    componentPositioner7.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner7.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId28, None)
    
    theSession.UndoToMark(markId27, None)
    
    theSession.DeleteUndoMark(markId27, None)
    
    # ----------------------------------------------
    #   功能表：組立件(A)->元件位置(P)->組立約束(N)...
    # ----------------------------------------------
    markId29 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "通過定位任務建立約束")
    
    markId30 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    componentPositioner8 = workPart.ComponentAssembly.Positioner
    
    componentPositioner8.ClearNetwork()
    
    componentPositioner8.PrimaryArrangement = arrangement1
    
    componentPositioner8.BeginAssemblyConstraints()
    
    allowInterpartPositioning7 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression49 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression50 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression51 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression52 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression53 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression54 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression55 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression56 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network8 = componentPositioner8.EstablishNetwork()
    
    componentNetwork8 = network8
    componentNetwork8.MoveObjectsState = True
    
    componentNetwork8.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork8.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId30, "組立約束 對話方塊")
    
    componentNetwork8.MoveObjectsState = True
    
    componentNetwork8.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId31 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    scaleAboutPoint1 = NXOpen.Point3d(-20.816862219069261, -13.469734377044796, 0.0)
    viewCenter1 = NXOpen.Point3d(20.816862219069261, 13.469734377044796, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint1, viewCenter1)
    
    scaleAboutPoint2 = NXOpen.Point3d(-11.26559602443748, -11.755404547239102, 0.0)
    viewCenter2 = NXOpen.Point3d(11.26559602443748, 11.755404547239102, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint2, viewCenter2)
    
    scaleAboutPoint3 = NXOpen.Point3d(-8.8165534104293251, -9.4043236377912809, 0.0)
    viewCenter3 = NXOpen.Point3d(8.8165534104293251, 9.4043236377912809, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint3, viewCenter3)
    
    scaleAboutPoint4 = NXOpen.Point3d(-7.0532427283434487, -7.5234589102330265, 0.0)
    viewCenter4 = NXOpen.Point3d(7.053242728343462, 7.5234589102330265, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint4, viewCenter4)
    
    component8 = nXObject5
    face1 = component8.FindObject("PROTO#.Features|EXTRUDE(2)|FACE 150 {(0,-2.5,-1) EXTRUDE(2)}")
    line1 = workPart.Lines.CreateFaceAxis(face1, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    objects1 = [NXOpen.TaggedObject.Null] * 1 
    objects1[0] = line1
    nErrs13 = theSession.UpdateManager.AddObjectsToDeleteList(objects1)
    
    face2 = component2.FindObject("PROTO#.Features|EXTRUDE(6)|FACE 170 {(-26,-8.5,-1) EXTRUDE(2)}")
    line2 = workPart.Lines.CreateFaceAxis(face2, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    markId32 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint2 = componentPositioner8.CreateConstraint(True)
    
    componentConstraint2 = constraint2
    componentConstraint2.ConstraintType = NXOpen.Positioning.Constraint.Type.Concentric
    
    edge1 = component8.FindObject("PROTO#.Features|EXTRUDE(2)|EDGE * 130 * 150 {(-0.5,-5,0.8660254037844)(1,-5,-0)(-0.5,-5,-0.8660254037844) EXTRUDE(2)}")
    constraintReference2 = componentConstraint2.CreateConstraintReference(component8, edge1, False, False, False)
    
    helpPoint1 = NXOpen.Point3d(1.2198164996087846, -42.325527787706264, 0.098486327327569942)
    constraintReference2.HelpPoint = helpPoint1
    
    edge2 = component2.FindObject("PROTO#.Features|EXTRUDE(6)|EDGE * 150 * 170 {(-26.5,-11,-0.8660254037844)(-25,-11,0)(-26.5,-11,0.8660254037844) EXTRUDE(2)}")
    constraintReference3 = componentConstraint2.CreateConstraintReference(component2, edge2, False, False, False)
    
    helpPoint2 = NXOpen.Point3d(-16.753198017639846, 5.0676041324646741, 0.9267239419401645)
    constraintReference3.HelpPoint = helpPoint2
    
    constraintReference3.SetFixHint(True)
    
    objects2 = [NXOpen.TaggedObject.Null] * 1 
    objects2[0] = line2
    nErrs14 = theSession.UpdateManager.AddObjectsToDeleteList(objects2)
    
    componentNetwork8.Solve()
    
    component9 = nXObject6
    face3 = component9.FindObject("PROTO#.Features|EXTRUDE(2)|FACE 150 {(0,-2.5,-1) EXTRUDE(2)}")
    line3 = workPart.Lines.CreateFaceAxis(face3, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    objects3 = [NXOpen.TaggedObject.Null] * 1 
    objects3[0] = line3
    nErrs15 = theSession.UpdateManager.AddObjectsToDeleteList(objects3)
    
    markId33 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "組立約束")
    
    nErrs16 = theSession.UpdateManager.DoUpdate(markId31)
    
    componentNetwork8.Solve()
    
    componentPositioner8.ClearNetwork()
    
    nErrs17 = theSession.UpdateManager.AddToDeleteList(componentNetwork8)
    
    componentPositioner8.DeleteNonPersistentConstraints()
    
    nErrs18 = theSession.UpdateManager.DoUpdate(markId31)
    
    theSession.DeleteUndoMark(markId33, None)
    
    theSession.SetUndoMarkName(markId30, "組立約束")
    
    componentPositioner8.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner8.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId31, None)
    
    theSession.DeleteUndoMark(markId32, None)
    
    markId34 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner9 = workPart.ComponentAssembly.Positioner
    
    componentPositioner9.ClearNetwork()
    
    componentPositioner9.PrimaryArrangement = arrangement1
    
    componentPositioner9.BeginAssemblyConstraints()
    
    allowInterpartPositioning8 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression57 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression58 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression59 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression60 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression61 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression62 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression63 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression64 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network9 = componentPositioner9.EstablishNetwork()
    
    componentNetwork9 = network9
    componentNetwork9.MoveObjectsState = True
    
    componentNetwork9.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork9.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId34, "組立約束 對話方塊")
    
    componentNetwork9.MoveObjectsState = True
    
    componentNetwork9.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId35 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    # ----------------------------------------------
    #   對話開始 組立約束
    # ----------------------------------------------
    line4 = workPart.Lines.CreateFaceAxis(face3, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    objects4 = [NXOpen.TaggedObject.Null] * 1 
    objects4[0] = line4
    nErrs19 = theSession.UpdateManager.AddObjectsToDeleteList(objects4)
    
    markId36 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint3 = componentPositioner9.CreateConstraint(True)
    
    componentConstraint3 = constraint3
    componentConstraint3.ConstraintType = NXOpen.Positioning.Constraint.Type.Concentric
    
    edge3 = component9.FindObject("PROTO#.Features|EXTRUDE(2)|EDGE * 130 * 150 {(-0.5,-5,0.8660254037844)(1,-5,-0)(-0.5,-5,-0.8660254037844) EXTRUDE(2)}")
    constraintReference4 = componentConstraint3.CreateConstraintReference(component9, edge3, False, False, False)
    
    helpPoint3 = NXOpen.Point3d(44.972561524329862, -55.042324233402162, 0.858953224056896)
    constraintReference4.HelpPoint = helpPoint3
    
    edge4 = component2.FindObject("PROTO#.Features|EXTRUDE(6)|EDGE * 130 * 160 {(3.5,-11,-0.8660254037844)(5,-11,0)(3.5,-11,0.8660254037844) EXTRUDE(2)}")
    constraintReference5 = componentConstraint3.CreateConstraintReference(component2, edge4, False, False, False)
    
    helpPoint4 = NXOpen.Point3d(12.38511165699591, 5.0676041324646741, 0.87398804958619292)
    constraintReference5.HelpPoint = helpPoint4
    
    constraintReference5.SetFixHint(True)
    
    componentNetwork9.Solve()
    
    markId37 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "組立約束")
    
    nErrs20 = theSession.UpdateManager.DoUpdate(markId35)
    
    componentNetwork9.Solve()
    
    componentPositioner9.ClearNetwork()
    
    nErrs21 = theSession.UpdateManager.AddToDeleteList(componentNetwork9)
    
    componentPositioner9.DeleteNonPersistentConstraints()
    
    nErrs22 = theSession.UpdateManager.DoUpdate(markId35)
    
    theSession.DeleteUndoMark(markId37, None)
    
    theSession.SetUndoMarkName(markId34, "組立約束")
    
    componentPositioner9.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner9.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId35, None)
    
    theSession.DeleteUndoMark(markId36, None)
    
    markId38 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner10 = workPart.ComponentAssembly.Positioner
    
    componentPositioner10.ClearNetwork()
    
    componentPositioner10.PrimaryArrangement = arrangement1
    
    componentPositioner10.BeginAssemblyConstraints()
    
    allowInterpartPositioning9 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression65 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression66 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression67 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression68 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression69 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression70 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression71 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression72 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network10 = componentPositioner10.EstablishNetwork()
    
    componentNetwork10 = network10
    componentNetwork10.MoveObjectsState = True
    
    componentNetwork10.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork10.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId38, "組立約束 對話方塊")
    
    componentNetwork10.MoveObjectsState = True
    
    componentNetwork10.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId39 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    # ----------------------------------------------
    #   對話開始 組立約束
    # ----------------------------------------------
    rotMatrix1 = NXOpen.Matrix3x3()
    
    rotMatrix1.Xx = -0.38826398341216001
    rotMatrix1.Xy = 0.81085409042923007
    rotMatrix1.Xz = -0.43791177561137651
    rotMatrix1.Yx = -0.61200247897563043
    rotMatrix1.Yy = 0.12839768911087329
    rotMatrix1.Yz = 0.78036337635659858
    rotMatrix1.Zx = 0.68898769576285279
    rotMatrix1.Zy = 0.57099008525995798
    rotMatrix1.Zz = 0.44639251519511486
    translation1 = NXOpen.Point3d(17.008446705993961, 10.700744971979525, 0.83749692355669669)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix1, translation1, 2.1100666846744698)
    
    scaleAboutPoint5 = NXOpen.Point3d(19.310211202931423, -19.435602184768644, 0.0)
    viewCenter5 = NXOpen.Point3d(-19.310211202931423, 19.435602184768644, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint5, viewCenter5)
    
    scaleAboutPoint6 = NXOpen.Point3d(23.172253443517722, -0.60187671281864208, 0.0)
    viewCenter6 = NXOpen.Point3d(-23.172253443517722, 0.60187671281864208, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint6, viewCenter6)
    
    scaleAboutPoint7 = NXOpen.Point3d(28.965316804397148, -0.75234589102331317, 0.0)
    viewCenter7 = NXOpen.Point3d(-28.965316804397148, 0.75234589102330252, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint7, viewCenter7)
    
    component10 = nXObject4
    face4 = component10.FindObject("PROTO#.Features|EXTRUDE(2)|FACE 140 {(0,-2.5,-3.3991878676582) EXTRUDE(2)}")
    line5 = workPart.Lines.CreateFaceAxis(face4, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    face5 = component10.FindObject("PROTO#.Features|BLEND(3)|FACE 1 {(0,-0.2928932188135,3.1062946488448) EXTRUDE(2)}")
    line6 = workPart.Lines.CreateFaceAxis(face5, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    face6 = component10.FindObject("PROTO#.Features|EXTRUDE(2)|FACE 150 {(0,-2.5,-1) EXTRUDE(2)}")
    line7 = workPart.Lines.CreateFaceAxis(face6, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    objects5 = [NXOpen.TaggedObject.Null] * 1 
    objects5[0] = line5
    nErrs23 = theSession.UpdateManager.AddObjectsToDeleteList(objects5)
    
    objects6 = [NXOpen.TaggedObject.Null] * 1 
    objects6[0] = line7
    nErrs24 = theSession.UpdateManager.AddObjectsToDeleteList(objects6)
    
    objects7 = [NXOpen.TaggedObject.Null] * 1 
    objects7[0] = line6
    nErrs25 = theSession.UpdateManager.AddObjectsToDeleteList(objects7)
    
    markId40 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint4 = componentPositioner10.CreateConstraint(True)
    
    componentConstraint4 = constraint4
    componentConstraint4.ConstraintType = NXOpen.Positioning.Constraint.Type.Concentric
    
    edge5 = component10.FindObject("PROTO#.Features|EXTRUDE(2)|EDGE * 120 * 150 {(-0.5,0,0.8660254037844)(1,0,-0)(-0.5,0,-0.8660254037844) EXTRUDE(2)}")
    constraintReference6 = componentConstraint4.CreateConstraintReference(component10, edge5, False, False, False)
    
    helpPoint5 = NXOpen.Point3d(-3.1161607699504916, -56.956316289965557, 0.99129243047619331)
    constraintReference6.HelpPoint = helpPoint5
    
    edge6 = component2.FindObject("PROTO#.Features|EXTRUDE(8)|EDGE * 130 * 160 {(-25.5,49,-0.8660254037844)(-27,49,0)(-25.5,49,0.8660254037844) EXTRUDE(2)}")
    constraintReference7 = componentConstraint4.CreateConstraintReference(component2, edge6, False, False, False)
    
    helpPoint6 = NXOpen.Point3d(-17.941626418598872, 65.067604132464666, 0.58270257849953044)
    constraintReference7.HelpPoint = helpPoint6
    
    constraintReference7.SetFixHint(True)
    
    componentNetwork10.Solve()
    
    markId41 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "組立約束")
    
    nErrs26 = theSession.UpdateManager.DoUpdate(markId39)
    
    componentNetwork10.Solve()
    
    componentPositioner10.ClearNetwork()
    
    nErrs27 = theSession.UpdateManager.AddToDeleteList(componentNetwork10)
    
    componentPositioner10.DeleteNonPersistentConstraints()
    
    nErrs28 = theSession.UpdateManager.DoUpdate(markId39)
    
    theSession.DeleteUndoMark(markId41, None)
    
    theSession.SetUndoMarkName(markId38, "組立約束")
    
    componentPositioner10.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner10.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId39, None)
    
    theSession.DeleteUndoMark(markId40, None)
    
    markId42 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner11 = workPart.ComponentAssembly.Positioner
    
    componentPositioner11.ClearNetwork()
    
    componentPositioner11.PrimaryArrangement = arrangement1
    
    componentPositioner11.BeginAssemblyConstraints()
    
    allowInterpartPositioning10 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression73 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression74 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression75 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression76 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression77 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression78 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression79 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression80 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network11 = componentPositioner11.EstablishNetwork()
    
    componentNetwork11 = network11
    componentNetwork11.MoveObjectsState = True
    
    componentNetwork11.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork11.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId42, "組立約束 對話方塊")
    
    componentNetwork11.MoveObjectsState = True
    
    componentNetwork11.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId43 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    # ----------------------------------------------
    #   對話開始 組立約束
    # ----------------------------------------------
    face7 = component4.FindObject("PROTO#.Features|EXTRUDE(2)|FACE 150 {(0,-2.5,-1) EXTRUDE(2)}")
    line8 = workPart.Lines.CreateFaceAxis(face7, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    objects8 = [NXOpen.TaggedObject.Null] * 1 
    objects8[0] = line8
    nErrs29 = theSession.UpdateManager.AddObjectsToDeleteList(objects8)
    
    markId44 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint5 = componentPositioner11.CreateConstraint(True)
    
    componentConstraint5 = constraint5
    componentConstraint5.ConstraintType = NXOpen.Positioning.Constraint.Type.Concentric
    
    edge7 = component4.FindObject("PROTO#.Features|EXTRUDE(2)|EDGE * 120 * 150 {(-0.5,0,0.8660254037844)(1,0,-0)(-0.5,0,-0.8660254037844) EXTRUDE(2)}")
    constraintReference8 = componentConstraint5.CreateConstraintReference(component4, edge7, False, False, False)
    
    helpPoint7 = NXOpen.Point3d(20.803866395104897, -62.345868398316675, -0.0011857179061987245)
    constraintReference8.HelpPoint = helpPoint7
    
    edge8 = component2.FindObject("PROTO#.Features|EXTRUDE(8)|EDGE * 150 * 170 {(4.5,49,-0.8660254037844)(3,49,0)(4.5,49,0.8660254037844) EXTRUDE(2)}")
    constraintReference9 = componentConstraint5.CreateConstraintReference(component2, edge8, False, False, False)
    
    helpPoint8 = NXOpen.Point3d(12.037032066018703, 65.067604132464666, 0.55172362189445123)
    constraintReference9.HelpPoint = helpPoint8
    
    constraintReference9.SetFixHint(True)
    
    componentNetwork11.Solve()
    
    markId45 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "組立約束")
    
    nErrs30 = theSession.UpdateManager.DoUpdate(markId43)
    
    componentNetwork11.Solve()
    
    componentPositioner11.ClearNetwork()
    
    nErrs31 = theSession.UpdateManager.AddToDeleteList(componentNetwork11)
    
    componentPositioner11.DeleteNonPersistentConstraints()
    
    nErrs32 = theSession.UpdateManager.DoUpdate(markId43)
    
    theSession.DeleteUndoMark(markId45, None)
    
    theSession.SetUndoMarkName(markId42, "組立約束")
    
    componentPositioner11.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner11.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId43, None)
    
    theSession.DeleteUndoMark(markId44, None)
    
    markId46 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner12 = workPart.ComponentAssembly.Positioner
    
    componentPositioner12.ClearNetwork()
    
    componentPositioner12.PrimaryArrangement = arrangement1
    
    componentPositioner12.BeginAssemblyConstraints()
    
    allowInterpartPositioning11 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression81 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression82 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression83 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression84 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression85 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression86 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression87 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression88 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network12 = componentPositioner12.EstablishNetwork()
    
    componentNetwork12 = network12
    componentNetwork12.MoveObjectsState = True
    
    componentNetwork12.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork12.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId46, "組立約束 對話方塊")
    
    componentNetwork12.MoveObjectsState = True
    
    componentNetwork12.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId47 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    # ----------------------------------------------
    #   對話開始 組立約束
    # ----------------------------------------------
    componentPositioner12.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner12.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId47, None)
    
    theSession.UndoToMark(markId46, None)
    
    theSession.DeleteUndoMark(markId46, None)
    
    theSession.DeleteUndoMark(markId29, None)
    
    # ----------------------------------------------
    #   功能表：工具(T)->動作記錄(J)->停止錄製(S)
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()